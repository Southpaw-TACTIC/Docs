# Project Schema

The project schema is used to create structure or a "data model" of a
project. The Schema view defines the type of items managed by using a
visual graphical node editor. The Schema Editor displays the layout of
the created sTypes and the connections between them.

![image](media/project-schema-full-view.png)

The Project Schema Editor is available through the Getting Started link
in the side bar which is available after creating a project, or under
the Admin Views under Project Admin → Project Schema in the side bar.

The Project Schema editor is an essential tool used for the creation of
new project templates. This editor is used to layout the various types
of objects (files, assets) that will be managed and produced on a
project. These types (sTypes) are searchable within TACTIC. Node based
layout and work-flow, allows for simple manipulation and creation of
these various sTypes and their relationships to each other.

**Editor Button Shelf**

![image](media/project-schema-buttons.png)

**Main Editor Buttons**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Add</strong></p></td>
<td><p>Add a new node to the canvas. This represents an unregistered sType</p></td>
</tr>
<tr class="even">
<td><p><strong>Delete</strong></p></td>
<td><p>Delete the selected nodes or connections from the canvas</p></td>
</tr>
<tr class="odd">
<td><p><strong>Save</strong></p></td>
<td><p>Save all changes to the schema</p></td>
</tr>
</tbody>
</table>

**Editor Zoom Controls**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Zoom In</strong></p></td>
<td><p>Zoom the canvas in</p></td>
</tr>
<tr class="even">
<td><p><strong>Zoom Out</strong></p></td>
<td><p>Zoom the canvas out</p></td>
</tr>
<tr class="odd">
<td><p><strong>Zoom Options</strong></p></td>
<td><p>Allow for choosing the zoom level.</p></td>
</tr>
</tbody>
</table>

**Node Options (Applies to the selected nodes or connections)**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Register sType</strong></p></td>
<td><p>Registers the selected nodes as new Searchable Types using the registration wizard. If more than one node is selected, the sTypes will be registered in batch.</p></td>
</tr>
<tr class="even">
<td><p><strong>Edit Connection</strong></p></td>
<td><p>Load the connection editor pop-up.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Edit Pipelines</strong></p></td>
<td><p>Load the Project Work-flow (pipeline) editor.</p></td>
</tr>
</tbody>
</table>

**Laying out the sTypes**

![image](media/project-schema-layout.png)

To create a new Searchable Type (sType) in the schema, add a new node to
the canvas using the \[+\] button in the editor. It’s also possible to
create a new node from an existing node by simply dragging a connection
line from the output handle of the existing node.

![image](media/new-node.png)

Once the type has been created on the canvas, it can be renamed by right
clicking on the node or using a "CTRL-click" on the node.

![image](media/new-node-rename.png)

> **Note**
>
> It is important to note that during this initial process, you are
> creating a "blueprint" for your project. The next steps are to
> **register** the sTypes. Each sType in TACTIC is represented as a table in
> the project database, this table is required to go through a
> registration process. This process will generate the table as well as
> provide the opportunity to add columns (properties), a pipeline, default
> views for the sidebar and more.

**Workflow (Pipelines)**

Where applicable, you can add the pipeline attribute to a search type to
allow for association of the sObjects to a particular pipeline. Having a
pipeline assigned allows an sObject to travel through a set number of
processes. For each of these processes, a task can be created and
assigned to a user, files can be checked in, notes can be submitted and
work hours can be logged.

By choosing "Has Pipeline" on creation, an extra "pipeline\_code"
property will be added to store pipeline associations and a Pipeline
will be created and registered for the new sType.

> **Note**
>
> To edit the pipeline, you can click the pipeline link in the top of the
> editor or, in the sidebar navigate to Project Admin → Project Workflow.

**Node Options**

Once registered, each node provides options for further configuration of
sType related project setup and configuration, which can be executed
through the main shelf buttons or by right-clicking on a node:

![image](media/node-menu-register-stype.png)

**Editor Actions**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Add to Current Group</strong></p></td>
<td><p>Adds the selected node(s) to the current group (pipeline)</p></td>
</tr>
<tr class="even">
<td><p><strong>Rename Node</strong></p></td>
<td><p>Rename the node (sType)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Remove Node</strong></p></td>
<td><p>Remove the node (sType)</p></td>
</tr>
<tr class="even">
<td><p><strong>Remove Group</strong></p></td>
<td><p>Removes the group (pipeline)</p></td>
</tr>
</tbody>
</table>

**Node Actions**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Register sType</strong></p></td>
<td><p>Loads the sType registration wizard</p></td>
</tr>
</tbody>
</table>

**Node Options**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Table Manager</strong></p></td>
<td><p>Load the Database table manager for the selected type <em>(see &quot;Table Manager&quot; below)</em></p></td>
</tr>
<tr class="even">
<td><p><strong>View Manager</strong></p></td>
<td><p>Loads the view manager for the selected sType <em>(see &quot;View Manager&quot; below)</em></p></td>
</tr>
<tr class="odd">
<td><p><strong>Show Raw Data</strong></p></td>
<td><p>Loads the Raw database data in a table for the selected sType <em>(see &quot;Raw Data&quot; below)</em></p></td>
</tr>
<tr class="even">
<td><p><strong>Edit Pipeline</strong></p></td>
<td><p>Loads the Workflow Editor allowing access to edit the pipelines related to the selected sType.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Show File Naming</strong></p></td>
<td><p>Loads the file naming table for the selected sType <em>(see &quot;File Naming&quot; below)</em></p></td>
</tr>
</tbody>
</table>

**Table Manager**

![image](media/node-options-table-data.png)

**View Manager**

![image](media/node-options-view-manager-crop.png)

**Raw Data**

![image](media/node-options-raw-data.png)

**File Naming**

![image](media/node-options-show-naming.png)
