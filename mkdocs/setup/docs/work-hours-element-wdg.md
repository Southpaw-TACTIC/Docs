# Work Hours List

![image](media/1_work_hours_overview.png)

**Description**

The Work Hours widget provides an interface to record the number of work
hours spent for each task. The break down of the work hours by task
allows the analysis to be broken down at the lowest level of detail.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Work Hours List</p></td>
</tr>
<tr class="even">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.table.WorkHoursElementWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>2.5.0<br />
</p></td>
</tr>
<tr class="even">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>

**Implementation**

The Work Hours List Element is a common column that can be added to any
task view using the Column Manager.

**Options**

There are no options available for this widget.

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>view</strong></p></td>
<td><p>The view to retrieve from the Widget Config. This is not required if the HTML option is supplied.</p></td>
</tr>
<tr class="even">
<td><p><strong>html</strong></p></td>
<td><p>This option is where the HTML code is embedded.</p></td>
</tr>
<tr class="odd">
<td><p><strong>search_type</strong></p></td>
<td><p>The Search Type the CustomLayoutWdg applies to (if applicable)</p></td>
</tr>
</tbody>
</table>

**Examples**

We can record 4 hours of work on Wednesday and 3 hours on Thursday for a
task. The total for that week will also be displayed as a convenience.

![image](media/2_work_hours_eg.png)
