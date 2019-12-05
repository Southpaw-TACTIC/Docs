# Custom Checkin Pipeline

**Partial override**

There are four points in the current Application check-in process that
the developer can insert handlers to perform custom actions. These
events are called checkin/pre\_export, checkin/create, checkin/process,
checkin/dependency.

Here is a plain pipeline:

    <pipeline>
        <process name="model/>
        <process name="texture"/>
        <process name="shader"/>
        <process name="rig"/>
        <connect to="texture" from="model" context="model"/>
        <connect to="shader" from="texture" context="texture"/>
       <connect to="shot/layout" from="rig" context="rig"/>
        <connect to="rig" from="texture" context="texture"/>
        <connect to="shot/lighting" from="shader"/>
    </pipeline>

If we want to intercept the model process checkin with before exporting
occurs and the texture process before and after the export of the node
occurs, we will have a pipeline like this:

    <pipeline>
        <process name="model">
             <action event="checkin/pre_export" scope="client"
     class="pyasm.application.common.interpreter.MayaModelCheckinPreexport"/>
        </process>
         <process name="texture">
               <action event="checkin/pre_export" scope="client"
    class="pyasm.application.common.interpreter.MayaTextureCheckinPreexport"/>
               <action event="checkin/process" scope="client"
    class="pyasm.application.common.interpreter.MayaTextureCheckinProcess"/>
          </process>
        <process name="shader"/>
        <process name="rig"/>
        <connect to="texture" from="model" context="model"/>
        <connect to="shader" from="texture" context="texture"/>
        <connect to="shot/layout" from="rig" context="rig"/>
        <connect to="rig" from="texture" context="texture"/>
        <connect to="shot/lighting" from="shader"/>
    </pipeline>

The class attribute can point to a custom python path, usually
accessible on the network where the client computer is on. This python
class can do something as simple as adding a cube and parent it to the
to-be-exported node, the scene file is free from user-created junk
nodes, or making sure a certain special node exists in the scene file.
Please to the full override section for some python class examples. The
main method required is just execute(). And presumably you will import
the application’s python module to do the manipulation desired. For
Maya, you would run this to create a cube:

    import maya as cmaya
    cmaya.cmds.polyCube()

**Full override**

> **Warning**
>
> This method requires more set-up on the developer’s end as it
> does not leverage the exisiting application checkin functionalities.
> This section describes how to customize the checkin pipeline, which is a
> series of processes, each with an action handler defined.

Normally TACTIC handles many of the details for checking in files.
However, this process can be completely taken over and customized.

An example checkin pipeline might look like the following:

    <pipeline>
      <process name="validation">
        <action class="pyasm.application.common.interpreter.MayaModelValidate"/>
      </process>
      <process name="extractor">
        <action class="pyasm.application.common.interpreter.MayaModelCheckin"/>
      </process>
      <connect from="validation" to="extractor"/>
    </pipeline>

This structure is the same for all pipelines defined in TACTIC. It
describes a series of processes with actions. The actions have an
attribute "class" that handles a particular part of the checkin process.
TACTIC delivers a defined pipeline to a pipeline interpreter, which then
executes the handlers in order. Handlers make use of the Client API to
interact with TACTIC.

> **Note**
>
> For information on the Client API, refer to the [**Client
> API Documentation**](#clientAPI)

**Process Handlers**

A process handler is a function or subroutine that contains commands
that are executed in response to an event. In TACTIC, all handlers are
derived from the Handler class. This class defines a simple interface
which has some basic functions which can be overridden:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>execute()</strong></th>
<th>The commands to be performed by the handler.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>undo()</strong></p></td>
<td><p>The method called when an exception occurs. TACTIC calls the <em>undo()</em> method for each handler in the pipeline in the reverse order that they were executed.</p></td>
</tr>
</tbody>
</table>

There are several helper methods you can use to set and retrieve
information using handlers. Any particular handler has two sources of
information:

1.  **Package:** this data is global to all of the nodes. It is the
    dictionary data structure that TACTIC delivers to the client machine and
    includes such settings as status information and user interface selections. This data should be considered read-only.

    You can retrieve package information using the method:

    `get_package_value(my, key)`

    where *key* is the name of the dictionary key for the data. The exact
    list of the keys delivered will depend on the user interface settings.

2.  **Input:** this data is received from the previous process handler.
    The handler itself determines which input it receives.

    You can retrieve input information using the method:

    `get_input_value(my, key)`

    Handlers can deliver these values to future nodes with output values,
    which become the input values for the next node. You can set output
    information using the method:

    `set_output_value(my, key)`

**Example**

The following sample is simple validation handler code that checks a
Maya session for the existence of a particular node through its search
key.

    import maya.cmds as cmds

    from pyasm.application.common.interpreter import Handler

    class MayaModelValidate(Handler):
        def execute(my):
            # get the search key from the delivered package
            search_key = my.get_package_value("search_key")

            # get the sobject from the server
            sobject = my.server.get_by_search_key(search_key)
            if not sobject:
                raise Exception("SObject with search key [%s] does not exist" % \
                    search_key)

            # code and verify in maya that the node is in session
            code = sobject.get('code')
            if not cmds.ls(code):
                raise Exception("Cannot checkin: [%s] does not exist" % code)

            my.set_output_value('sobject', sobject)

This code example, although simple, illustrates a number of handler
interaction requirements.

`import maya.cmds as cmds`

This first line imports the standard Maya command libraries to allow the
handler to interact with Maya.

`search_key = my.get_package_value("search_key")`

This line requires user input from a field in the interface on the
search key (unique identifier) for a particular SObject.

`sobject = my.server.get_by_search_key(search_key)`

Using the search key obtained from the interface, this line uses the
client API to retrieve data about the specific SObject. Handlers can
access the server stub code by using the `my.server` prefix. All methods
defined in the Client API are accessible through this type of reference.
(See the Client API documentation for more information.)

The data structure returned is a dictionary of values that can be
accessed as follows:

    code = sobject.get('code')
    if not cmds.ls(code):
        raise Exception("Cannot checkin: [%s] does not exist" % code)

The code then checks the Maya session to verify that a node exists with
the same name as defined in the SObject. If not, an exception is created
that halts the checkin process and informs the user with the appropriate
error message that the checkin failed.
