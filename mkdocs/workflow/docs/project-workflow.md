# Workflow Editor

![image](media/1_workflow_editor_overview.png)

**Introduction**

The Workflow Editor is a graphical tool in TACTIC used to interactively
create pipelines (workflows). It is a node-based tool which creates
processes in a pipeline and connects them. The Workflow Editor makes it
easier to create large complex pipelines to filter and process
information and file system flow.

The Workflow Editor is simple to use and similar to node base utilities
commonly found in other applications. Nodes can be created in the canvas
and connected together. Each node represents a process (with attributes
associated to it) and each connection represents information being
delivered from one process to the other. Together, the Workflow Editor
helps you create a definition of the pipeline document and drive much of
the information flow in TACTIC.

**Access the Workflow Editor**

Access the Workflow Editor by going to:

**Admin Views → Project Admin → Project Workflow**

When the option for "Has Pipeline" is selected during the registration
of the sType, this defines a default pipeline for that sType. This
pipeline can be found defined in the Workflow Editor in the sidebar
under **Project Pipelines**. To add a new pipeline manually, the select
the \[+\] icon in bottom panel of the Workflow Editor.

![image](media/2_workflow_editor_pipelines_panel.png)

**Interface Walk Through**

The buttons at the top of the Workflow Editor allow various operations
on the canvas:

![image](media/pipeline_tools.png)

-   **Create:** Creates a new node on the canvas.

-   **Delete:** Deletes the selected node.

-   **Save:** Saves the current state of the pipeline to the database.

-   **Clear:** Clears the canvas.

-   **Properties:** Opens the Node Properties panel.

**Edit Properties of a Pipeline**

To edit the properties of a pipeline, first select a node in the
pipeline and then click on the **Edit Properties** button on the tool
shelf.

> **Note**
>
> For more information regarding the Process Options, refer to the section
> Project Workflow → Pipeline Process Options

![image](media/7_workflow_editor_properties.png)

**Lay Out a Pipeline**

When you click the green plus button,
\*Create\*![image](media/add_button.png), a new node will appear on the
canvas.

![image](media/pipeline_node_insert.png)

Rename the node: Select the new node and press CTRL-LMB to rename the
node. Alternatively, right click and select **Rename Node** from the
context menu.

![image](media/pipeline_node_naming.png)

Type in the new name for the node ("Model," in this example), and press
**Enter**.

![image](media/pipeline_node.png)

Create another new node (called "Texture" in this example).

![image](media/pipeline_nodes.png)

To create a connection between the two nodes, click on the handle on the
right side of the "Model" node. This will create a connector which will
follow the cursor.

![image](media/pipeline_node_connector.png)

Click on the left handle of the "Texture" node to complete the
connection. Now, the 2 nodes are connected together. Once 2 nodes are
connected, they will stay connected unless the connector is selected and
deleted.

![image](media/pipeline_node_connection.png)

It is also possible to have one node connect to more than one node. In
the following example, the "Model" process delivers to both the
"Texture" process and a "Rig" process:

![image](media/Pipeline_node_tree.png)

**Pipeline Workflow Automation**

Repetition and daily components that make up a user’s workflow can be
made easier through automation of notifications, file/directory naming
and triggering custom logic. Automations such as these can vary from
simply sending an email or automatically setting upstream and downstream
task statuses to running custom Python scripts and tools to encode
files, submit renders, generate previews, deliver files to clients, etc.

On the Workflow Editor’s canvas, right-clicking on a node will bring up
the context menu where the automation interfaces can be loaded into the
lower half of the interface. These options include:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Show Properties</strong></th>
<th>Loads the Node Properties window.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Show Triggers/Notifications</strong></p></td>
<td><p>Loads the Triggers and Notifications setup Interface</p></td>
</tr>
<tr class="even">
<td><p><strong>Show File Naming</strong></p></td>
<td><p>Loads the Directory and File naming convention setup Interface</p></td>
</tr>
</tbody>
</table>

> **Note**
>
> Each of the menu options are explained in the "Project Automation"
> section of the documentation.

**Mouse and Keyboard Shortcuts**

When the cursor is over the canvas in the pipeline editor, the following
mouse and keyboard shortcuts are available:

<table>
<colgroup>
<col width="51%" />
<col width="48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>LMB</strong> on a node</th>
<th>Select the node</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>LMB</strong> on the empty canvas space</p></td>
<td><p>Clears selection</p></td>
</tr>
<tr class="even">
<td><p><strong>LMB + Ctrl</strong> click on a node</p></td>
<td><p>Edits the name of the node</p></td>
</tr>
<tr class="odd">
<td><p><strong>LMB + Shift</strong> click on a node</p></td>
<td><p>Add node to selection</p></td>
</tr>
<tr class="even">
<td><p><strong>LMB + drag</strong> on a node</p></td>
<td><p>Drags the node around the canvas</p></td>
</tr>
<tr class="odd">
<td><p><strong>LMB + drag</strong> on the empty canvas space</p></td>
<td><p>Pans around the canvas</p></td>
</tr>
<tr class="even">
<td><p><strong>LMB + Shift + drag</strong> to form a selection box</p></td>
<td><p>Forms a selection box</p></td>
</tr>
<tr class="odd">
<td><p><strong>LMB + Ctrl + drag</strong> to the left or the right</p></td>
<td><p>Zooms in or out on the canvas</p></td>
</tr>
<tr class="even">
<td><p><strong>DELETE</strong></p></td>
<td><p>Deletes the selected node(s)</p></td>
</tr>
</tbody>
</table>

**To Change Node Color**

To change the node color, go to the **Workflow Editor → sidebar**

right click on the pipeline and select **Edit Pipeline Data**

![image](media/3_workflow_editor_edit_pipeline_data.png)

Next, click on the color input field. A color swatch will pop-up. Select
the new color for this pipeline from the color swatch.

![image](media/4_workflow_editor_change_node_color.png)

Another way to change the color is in the **Workflow Editor → Pipelines
tab (panel at the bottom)** click on the **color** column and pick the
color from the color swatch.

![image](media/5_workflow_editor_change_node_color_method_two.png)

**Pipeline Node Context Menu Options**

Right click on the pipeline node will display the following menu
options:

![image](media/6_workflow_editor_node_context_menu.png)

<table>
<colgroup>
<col width="51%" />
<col width="48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Add To Current Group</strong></th>
<th>Add the selected node to the current group</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Rename Node</strong></p></td>
<td><p>Rename the current selected node</p></td>
</tr>
<tr class="even">
<td><p><strong>Delete Node</strong></p></td>
<td><p>Delete the current selected node</p></td>
</tr>
<tr class="odd">
<td><p><strong>Delete Group</strong></p></td>
<td><p>Delete the group for the current selected node</p></td>
</tr>
<tr class="even">
<td><p><strong>Edit Properties</strong></p></td>
<td><p>Edit the properties for the current selected node</p></td>
</tr>
<tr class="odd">
<td><p><strong>Show Triggers/Notifications</strong></p></td>
<td><p>Display the triggers and notifications view in the bottom panel</p></td>
</tr>
<tr class="even">
<td><p><strong>Show Processes</strong></p></td>
<td><p>Display the processes in the bottom panel</p></td>
</tr>
<tr class="odd">
<td><p><strong>Customize Task Status</strong></p></td>
<td><p>Create a custom task status pipeline for the process (refresh the Workflow Editor to see it added to the sidebar)</p></td>
</tr>
</tbody>
</table>

**Task Status Pipelines**

Task Status Pipelines are created in almost the same way as regular
Pipelines. except that in the new pipeline dialog, Task should be selected
for Search Type. Nodes are created and joined together in the same way.
Each task has a pipeline\_code attribute and by default it uses the built-in "task"
task status pipeline. When you specify a custom task status pipeline, the task’s
statuses will change accordingly.

**Types of Node**

There are five different types of nodes with different shapes:
manual, action, condition, approval, and hierarchy nodes. Each of the
different nodes can enhance the effectiveness of the pipelines and be
used to fit the environment and behaviors of specific workflows.

![image](media/type_of_nodes.png)

<table>
<colgroup>
<col width="34%" />
<col width="32%" />
<col width="32%" />
</colgroup>
<thead>
<tr class="header">
<th>Type of Node</th>
<th>Representation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Manual Node</p></td>
<td><p><img src="media/manual_node.png" alt="image" /></p></td>
<td><p>Manual nodes are the default nodes that represent tasks within a pipeline, users assigned to a Manual node are expected to complete the task. Manual nodes usually involve work that needs to be done, such as asset ingestion, or a submission of assets being worked on.</p></td>
</tr>
<tr class="even">
<td><p>Action Node</p></td>
<td><p><img src="media/action_node.png" alt="image" /></p></td>
<td><p>Action nodes can automatically execute an action based on a script once the preceding task is completed. For example, if its preceding Approval Node is 'Approved', or a Manual Node is set to 'Complete', the action node will be set off right away, and changes its following node will be set to 'Pending'.</p></td>
</tr>
<tr class="odd">
<td><p>Conditional Node</p></td>
<td><p><img src="media/conditional_node.png" alt="image" /></p></td>
<td><p>Condition nodes are used when the path of a process needs to be determined by checking specified conditions using a script. It can also automatically change statuses of other nodes. The condition check should either return True or False, or a list of the output streams. For example, if the conditional checks return &quot;False&quot;, it will set the status of the previous node to 'Revise'.</p></td>
</tr>
<tr class="even">
<td><p>Approval Node</p></td>
<td><p><img src="media/approval_node.png" alt="image" /></p></td>
<td><p>Approval nodes allow assignment to user groups that are required to approve the process. If the status of an Approval node is changed to 'Rejected', the preceding task status will be changed from 'Complete' to 'Revise' automatically. Similar to other nodes, if the status is changed to 'Approved', the following node will be in Pending status.</p></td>
</tr>
<tr class="odd">
<td><p>Hierarchy Node</p></td>
<td><p><img src="media/hierarchy_node.png" alt="image" /></p></td>
<td><p>Hierarchy nodes are currently on the development roadmap.</p></td>
</tr>
</tbody>
</table>

**Triggers**

To open the Trigger and Notification editor, begin by selecting a manual
node. On the right side of the window there will be a Process
Configuration view. If this view is empty, simply save the pipeline and
click the node one more time.

From this view, the Trigger and Notification editor can be displayed by
clicking the View button beside Triggers or Notifications. This will
bring up a popup giving information about existing Triggers and
Notifications. To add a new one, press the plus button in the popup
window.

From here, add a name and description of the trigger, and choose the
event and action. The list of events includes common operations
performed on nodes (or tasks). For example, the checking in of a file,
the assigning of a task or the changing of a status can all cause an
event.

Actions are what happens when an event is triggered. Many Actions have
the ability to affect other tasks, and others have the ability to send
out notifications.

![image](media/trigger_setup.png)

Here are some examples of common Event - Action relationships:

-   Changing a task status to Complete causes the next task’s status to change to In Progress

-   In the case of a Design task followed by a Review task: changing the
    Design task’s status to Complete changes the Review task’s status to
    Need Review

-   Changing a Review task’s status to Rejected changes the previous
    task’s status to Revise

-   Assigning a task to a user sends a notification to that user

-   Adding a note to a task sends a notification to a user group

Building on top of user-created pipelines, this trigger system allows
users to make use of powerful automation to make their projects run
smoother.

**Notifications**

Notifications are created in the same way as triggers. It’s simply a
matter of selecting Send a notification under the Action section. From
here a user can choose to send the default message and type in mail
destinations and cc’s. These two boxes can contain email addresses,
login codes and group codes.

![image](media/notification_setup.png)

The message can be customized also. To do so, uncheck Use Default
Message and fill in the Subject and Message text areas. A text-based
message can be entered, including variables related to the modified
item. Below is a table of common variables:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Login of user that made the change</p></td>
<td><p>\{@GET(.login)}</p></td>
</tr>
<tr class="even">
<td><p>If a note is added, the note content</p></td>
<td><p>\{@GET(.note)}</p></td>
</tr>
<tr class="odd">
<td><p>Name / Code of modified item</p></td>
<td><p>\{@GET(.name)} / \{@GET(.code)}</p></td>
</tr>
<tr class="even">
<td><p>If a note is assigned, the assignee</p></td>
<td><p>\{@GET(.assigned)}</p></td>
</tr>
<tr class="odd">
<td><p>Status of the given task</p></td>
<td><p>\{@GET(.status)}</p></td>
</tr>
<tr class="even">
<td><p>If a task is changed, name / code of its parent</p></td>
<td><p>\{@GET(parent.name)}</p>
<p>\{@GET(parent.code)}</p></td>
</tr>
<tr class="odd">
<td><p>Process of modified task</p></td>
<td><p>\{@GET(.process)}</p></td>
</tr>
<tr class="even">
<td><p>Any column of modified item</p></td>
<td><p>\{@GET(.&lt;column_code&gt;)}</p></td>
</tr>
</tbody>
</table>

For mail\_to and mail\_cc, you can use an email address or expression that
optionally makes use of the current sobject. Let’s say the sobject is a task,
the 'sobject' below is the environment variable.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>assignee of the task</p></td>
<td><p>@GET(sobject.assigned)</p></td>
</tr>
<tr class="even">
<td><p>supervisor of the task</p></td>
<td><p>@GET(sobject.supervisor)</p></td>
</tr>
<tr class="odd">
<td><p>Email to ben and cindy regardless of the current task</p></td>
<td><p>@GET(sthpw/login[\'login\',\'in\',\'ben|cindy'].login)</p></td>
</tr>
<tr class="even">
<td><p>Email to ben and cindy regardless of the current task</p></td>
<td><p>@SOBJECT(sthpw/login[\'login\',\'in\',\'ben|cindy'])</p></td>
</tr>
</tbody>
</table>

In order for notifications to be operational, two conditions have to be
met. First, the user that triggers an action that causes a notification
must have their email entered into their user profile. It is highly
encouraged that each user have their email entered upon their creation.
Secondly, the mail server of TACTIC | Workflow must be configured, which
is discussed in Section 8.3.

Note: If the user does not have an email entered into their user
profile, the notification will not be sent, but the action still goes
through.

**Advanced**

Behind the scenes, the pipeline is an XML text document. This document
is how TACTIC stores its representation of the pipeline structure of
nodes and connections.

Although it is rare to need to manually edit the pipeline XML structure,
it is available at the bottom of the Workflow Editor in the pipelines
table in the **Data** column.

Below is an example of the pipeline XML for the **Model → Rig / Texture**
pipeline:

    <?xml version='1.0' encoding='UTF-8'?>
    <pipeline scale='100'>
      <process name='model' ypos='-95' xpos='-138'/>
      <process name='rig' color='blue' xpos='38' completion='80' task_pipeline='task' ypos='-165'/>
      <process name='texture' ypos='-51' xpos='42'/>
      <connect to='rig' from='model'/>
      <connect to='texture' from='model'/>
    </pipeline>
