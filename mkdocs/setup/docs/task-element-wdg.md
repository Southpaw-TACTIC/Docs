# Task Status Edit

**Description**

The Task Status Edit column is used to display the status of all tasks
for the item. It also provides conveniences such as changing the status
of the task and the assigned user.

![image](media/task_status_edit.png)

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Task Element Widget</p></td>
</tr>
<tr class="even">
<td><p><strong>Common Title</strong></p></td>
<td><p>Task Status Edit</p></td>
</tr>
<tr class="odd">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.table.TaskElementWdg</p></td>
</tr>
<tr class="even">
<td><p><strong>Category</strong></p></td>
<td><p>Common Columns</p></td>
</tr>
<tr class="odd">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>3.0.0<br />
</p></td>
</tr>
<tr class="even">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>

**Usage**

Once this column is added into the view, the drop down list can be used
to change the status. In addition, this column also displays the
process, schedule and the assigned user.

**Implementation**

This widget can be added using the Column Manager and can be found under
the common columns as **Task Status Edit**.

**Color**

TACTIC provides the ability to assign each status its own color. Setting
colors is handles from the Project Workflow (Pipeline) editor. Each
process in a regular pipeline or a status pipeline can be assigned a
color which will be used in this widget.

![image](media/status_color.png)

<table>
<colgroup>
<col width="30%" />
<col width="69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Bg Color</strong></p></td>
<td><p><strong>status</strong> and <strong>process</strong>. Set what controls the background color of the task. <strong>Status</strong> sets the task color to be the same as the status color. <strong>Process</strong> mode sets the task color to be the same color of the process as set in the Workflow Editor.</p></td>
</tr>
<tr class="even">
<td><p><strong>Status Color</strong></p></td>
<td><p><strong>status</strong> and <strong>process</strong>. Set what controls the background color of the status drop down. <strong>Status</strong> sets the status drop down color to be the same as the status color. <strong>Process</strong> mode sets the status drop down color to be the same color of the process as set in the Workflow Editor.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Context Color</strong></p></td>
<td><p><strong>status</strong> and <strong>process</strong>. Set what controls the background color of the context grid. <strong>Status</strong> sets the context grid color to be the same as the status color. <strong>Process</strong> mode sets the context grid color to be the same color of the process as set in the Workflow Editor.</p></td>
</tr>
<tr class="even">
<td><p><strong>Text Color</strong></p></td>
<td><p>Specifies the color of the task text using a color swatch.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Show Process</strong></p></td>
<td><p><strong>True</strong> or <strong>false</strong>. Displays the process of the task within the column.</p></td>
</tr>
<tr class="even">
<td><p><strong>Show Context</strong></p></td>
<td><p><strong>True</strong> or <strong>false</strong>. Displays the context of the task within the column.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Show Dates</strong></p></td>
<td><p><strong>True</strong> or <strong>false</strong>. Displays the time frame for the task. The schedule will display the start and end date.</p></td>
</tr>
<tr class="even">
<td><p><strong>Show Assigned</strong></p></td>
<td><p><strong>True</strong> or <strong>false</strong>. Displays the assigned user to the task.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Show Track</strong></p></td>
<td><p><strong>True</strong> or <strong>false</strong>.. Displays a button on each task which displays the last status and the user who changed it.</p></td>
</tr>
<tr class="even">
<td><p><strong>Show Labels</strong></p></td>
<td><p><strong>True</strong> or <strong>false</strong>. Displays the label of the pipeline’s process.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Show Border</strong></p></td>
<td><p><strong>all</strong>, <strong>one-sided</strong>, <strong>none</strong>. <strong>All</strong> displays a border around each task. <strong>One-sided</strong> displays a border around one one side of the task. <strong>None</strong> hides the border.</p></td>
</tr>
<tr class="even">
<td><p><strong>Show Current Pipeline Only</strong></p></td>
<td><p><strong>True</strong> or <strong>false</strong>. Displays tasks for the current pipeline only.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Show Task Edit</strong></p></td>
<td><p><strong>True</strong> or <strong>false</strong>. Displays a button which pops-up a window to edit the task info.</p></td>
</tr>
<tr class="even">
<td><p><strong>Task Edit view</strong></p></td>
<td><p>Specify the Task view by which to edit the task information.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Task Filter</strong></p></td>
<td><p><strong>panel</strong>, <strong>vertical</strong>, <strong>horizontal</strong>: Layout orientation to display the list of tasks.</p></td>
</tr>
<tr class="even">
<td><p><strong>Layout</strong></p></td>
<td><p><strong>context only</strong> or <strong>process only</strong>: Displays only tasks for either the context or the process.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Edit Status</strong></p></td>
<td><p><strong>True</strong> or <strong>false</strong>. Allows the user to open the status drop down selection box for the status to change it.</p></td>
</tr>
<tr class="even">
<td><p><strong>Edit Assigned</strong></p></td>
<td><p><strong>True</strong> or <strong>false</strong>. Allows the user to open the status drop down selection box for the assigned user to change it.</p></td>
</tr>
</tbody>
</table>

**Advanced**

    <element name='task_status_edit'>
      <display class='tactic.ui.table.TaskElementWdg'>
        <show_context>true</show_context>
        <show_assigned>true</show_assigned>
        <show_dates>true</show_dates>
        <edit>true</edit>
      </display>
      <action class='tactic.ui.table.TaskElementCbk'/>
    </element>
