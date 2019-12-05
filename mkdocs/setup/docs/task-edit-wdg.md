# Task Edit

![image](media/1_setup_task_edit_overview.png)

**Description**

The Task Edit Widget is a toggle that opens a hidden row that displays
all the tasks for an item. If there are multiple processes for an item,
the tasks for those processes will be displayed.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Task Edit</p></td>
</tr>
<tr class="even">
<td><p><strong>Common Title</strong></p></td>
<td><p>Tasks</p></td>
</tr>
<tr class="odd">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.panel.TableLayoutWdg</p></td>
</tr>
<tr class="even">
<td><p><strong>Category</strong></p></td>
<td><p>Table Layout Widget</p></td>
</tr>
<tr class="odd">
<td><p><strong>Supported Interfaces</strong></p></td>
<td><p>TableLayoutWdg</p></td>
</tr>
<tr class="even">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>3.0.0<br />
</p></td>
</tr>
<tr class="odd">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>

**Usage**

The following details are displayed by the Task Edit Widget for a task:

-   a link to the task’s Work Area (where the Checkin and Checkout tools
    can be found)

-   the task’s description

-   status for that process

-   the user assigned to the process

-   the supervisor of that process

-   the priority

-   start and end date for the process in the form of a Gantt chart

**Implementation**

The Task Edit Widget is a common column that can be added using the
Column Manager.

**Options**

There are no options provided for the Task Edit Widget.

**Advanced**

    <element name="task_edit" title="Tasks" edit="false">
        <display class="HiddenRowToggleWdg">
            <dynamic_class>tactic.ui.panel.TableLayoutWdg</dynamic_class>
        </display>
    </element>
