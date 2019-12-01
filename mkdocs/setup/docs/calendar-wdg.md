# Calendar Input Widget

**Calendar Input Widget**

![image](media/1_calendar_overview.png)

**Description**

The CalendarInputWdg displays a navigable calendar where dates can be
selected. It is an input widget that conforms to the BaseInputWdg
interface and is used for inline editing or as one of the items in the
EditWdg layout.

![image](media/2_calendar_closeup.png)

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Calendar Input</p></td>
</tr>
<tr class="even">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.widget.CalendarInputWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>Category</strong></p></td>
<td><p>Input widget</p></td>
</tr>
<tr class="even">
<td><p><strong>Supported Interfaces</strong></p></td>
<td><p>EditWdg, TableLayoutWdg (edit view)</p></td>
</tr>
<tr class="odd">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>2.5.0<br />
</p></td>
</tr>
<tr class="even">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none unless editing a specific date column</p></td>
</tr>
</tbody>
</table>

**Implementation**

The simple implementation does not require any options. It displays a
non-editable text box with a value that represents a date. Clicking on
the cell opens up the calendar widget.

**Options**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>first_day_of_week</strong></p></td>
<td><p>Integer representing first day of the week (0=Sunday, 6=Saturday)</p></td>
</tr>
<tr class="even">
<td><p><strong>read_only</strong></p></td>
<td><p>Sets the widget to be read only. In read-only mode, clicking on the cell does not bring up the calendar for input. Only a text box with the date value is displayed.</p></td>
</tr>
</tbody>
</table>

**Advanced**

The simplest and most common usage is the default implementation.

    <element name='start_date'>
      <display class='tactic.ui.widget.CalendarInputWdg'/>
    </element>

To set the work week to start on a different day than Sunday, change the
first\_day\_of\_week . This option is an integer which represents the days
of the week where 0=Sunday and 6=Saturday.

    <element name='start_date'>
      <display class='tactic.ui.widget.CalendarInputWdg'>
        <first_day_of_week>6</first_day_of_week>
      </display>
    </element>
