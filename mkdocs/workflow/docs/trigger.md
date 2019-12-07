# Triggers

Triggers are callbacks that are named based on certain events. TACTIC
provides three types of triggers which allow you to add to existing
functionality.

-   **Event-based triggers**: triggers based on specific events that occur
    within TACTIC. During the execution of a command in TACTIC, various
    named events may be called. Any one of these events may trigger other
    actions, if a custom trigger is registered to that event.

-   **Server-side pipeline triggers**: triggers defined in a server-side pipeline. They are called as a result of events that occur in the
    pipeline itself

-   **Client-side pipeline triggers**: triggers defined in a client-side pipeline. They are defined in the client API.

As TACTIC runs through its code, it will periodically call named events.
These named events provide a mechanism for attaching custom trigger
handlers.

There are two styles of named event triggers supported by TACTIC.

The first style of event-based trigger makes use of the client API. The
functionality in the client API can be accessed by the server code and
is often preferable for third parties to use because it uses a
well-defined interface much easier to program in than the complex server
code. To create your own custom trigger, create a new class derived from
the Handler class and override the execute function:

    from tactic_client_lib import TacticServerStub
    from tactic_client_lib.interpreter import Handler

    class CustomTrigger(Handler):
        def execute(my):
            # get a handle to the server stub
            server = TacticServerStub.get()
            server.start("Starting server transaction")
            try:
                # at this point, you have full access to the server using the client API
                ret_val = server.ping()

                # get values from the inputs
                search_key = my.get_input_value("search_key")
                sobject = server.get_by_search_key(search_key)
                if sobject.get('asset_library') != 'character':
                    return

                # check to see that the status has changed
                update_data = my.get_input_value("update_data")
                if update_data.get('status'):
                    do_something_interesting(sobject)

            except:
                server.abort()
            else:
                server.finish()

A reference to the TacticServerStub can be accessed through the static
method get(). Once a reference to the server stub is obtained, it is
possible to make use of the client API functionality. The main
difference is that this code is being run inside the TACTIC server
process, so the overhead of XMLRPC is not present. Thus triggers running
on the server side will run much faster that those running using the
XMLRPC protocol.

It is also possible in the trigger to access another TACTIC server by
using the TacticServerStub and explicitly setting the three settings
required to connect to another server. For example, here is some code to
synchronize the asset list:

        server = TacticServerStub()
        server.set_server("tactic2.com")
        server.set_ticket(ticket)
        server.set_project(project)
        server.start("Synchonizing data")
        try:
            search_key = my.get_input_value("search_key")
            update_data = my.get_input_value("update_data")
            server.update(search_key, update_data)
        except:
            server.abort()
        else:
            server.finish()

Synchronization of data between two TACTIC servers is possible once
authentication is set up. (Note that some priviledged knowledge about
the remote server is required in order to authenticate.)

The second style of event-based trigger is driven from the class
pyasm.command:

    from pyasm.command import Trigger
    class CustomTrigger(Trigger):
        def execute(my):
             print "executing custom trigger"

This trigger style makes use of server-side code and is much more
complex to use. It is most often used internally and should generally
not be used unless required due to a limitation in the client API.

As TACTIC server code is executed, triggers will be called periodically.
TACTIC will call named events, which will then trigger registered
handles that are listening to those events.

To better understand the event system, please review the **TACTIC Setup→
Project Automation → TACTIC Event System Introduction** documentation

Each of the handlers for the events listed above get an "input package"
delivered to them. This input package contains information that is
useful to the handler as determined by the command that called the
trigger.

<table>
<caption>Insert / Edit Input Values</caption>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>param</th>
<th>description</th>
<th>type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>is_insert</p></td>
<td><p>specifies whether a particular trigger was an insert or an edit</p></td>
<td><p>Boolean</p></td>
</tr>
<tr class="even">
<td><p>search_key</p></td>
<td><p>the search_key of the SObject operated on by the insert/edit</p></td>
<td><p>String</p></td>
</tr>
<tr class="odd">
<td><p>prev_data</p></td>
<td><p>a dictionary of previous values of attributes that were changed</p></td>
<td><p>Dictionary</p></td>
</tr>
<tr class="even">
<td><p>update_data</p></td>
<td><p>a dictionary of updated values of attributes that were changed</p></td>
<td><p>Dictionary</p></td>
</tr>
</tbody>
</table>

In order for a trigger to listen to an event, it must be registered in
the trigger search type.

In the TACTIC admin site: [http://&lt;server\_name&gt;/admin](http://<server_name>/admin), click on the
**triggers** view. This view defines a list of triggers and the events
they are registered to.

When you insert a new trigger, you specify the full class path of your
new trigger, along with a description and the event that the trigger
should listen for.

Time-based triggers allow you to execute custom code on the server at
either specific intervals or at a specific time of the day. These are
very useful triggers that allow you to handle any number of different
actions.

-   Backup (although this may be better done with a dedicated backup system)

-   Cleanup

-   Autobuilding of files

-   Statistics gathering

-   Data synchronization

In this example, the function get\_execute\_interval(), used to determine
the intervals during which this trigger will be run, is overridden to
3600. This trigger will be run every hour (60\*60) seconds. (The shortest
hard coded interval is every 60 seconds. If you set a smaller number it
will still execute once every 60 seconds.)

    class SampleTimedTrigger(TimedTrigger):
        def get_execute_interval(my):
            '''return number of seconds between execution'''
            return 3600

        def execute(my):
            print "doing a bunch of stuff"
            print "sleeping"
            time.sleep(15)
            print ".... done"

In order for TACTIC to recognize this trigger, it has to be registered
in the list of triggers in the Admin site. All timed triggers listen to
the "timed" event.
