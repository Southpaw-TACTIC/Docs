# Task Status History

![image](media/1_task_status_history_overview.png)

**Description**

The Task Status History is a toggle that opens a hidden row that
displays all the status changes for an item. If there are multiple
processes for an item, the status updates for those processes will be
displayed.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Task Status History</p></td>
</tr>
<tr class="even">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.panel.TableLayoutWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>Category</strong></p></td>
<td><p>Common Columns</p></td>
</tr>
<tr class="even">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>3.0+</p></td>
</tr>
<tr class="odd">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>

**Implementation**

The Task Edit Widget is a common column that can be added using the
Column Manager.

**Options**

There are no options provided for the Task Edit Widget.

**Advanced**

    <element name="task_status_history">
      <display class="HiddenRowToggleWdg">
        <dynamic_class>tactic.ui.panel.TableLayoutWdg</dynamic_class>
        <search_type>sthpw/status_log</search_type>
        <view>table</view>
        <expression>@SOBJECT(sthpw/task.sthpw/status_log)</expression>
        <mode>simple</mode>
      </display>
    </element>
