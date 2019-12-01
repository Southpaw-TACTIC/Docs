SObjectChartWdg

**Description**

The SObjectChartWdg is a tool to chart data related to sObjects.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>SObjectChartWdg</p></td>
</tr>
<tr class="even">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.chart.SObjectChartWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>4.4.0+</p></td>
</tr>
<tr class="even">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>

![image](media/sobject_chart_wdg.png)

**Implementation**

The SObjectChartWdg is driven by input sObjects and y-axis elements, where
the y-axis elements are expressions or columns that each input sObject will
evaluated against.

The input sObjects can be specified with the options "expression", "search\_type", or
"search\_keys". Expression will override search\_type, and search\_type will override
search\_keys.

For example,

    expression = "@SOBJECT(sthpw/login['login', 'NEQ', 'admin'])"
    search_type = "sthpw/login"
    search_keys = ['sthpw/login?code=brad']

A single y-axis can be specified with option "y\_axis", or multiple elements can be specified
with option "elements" as a "|" separated list. Individual y-axis elements can be a TACTIC
expression enclosed in "{" and "}" or a predefined column for the search\_type.

For example,

    y_axis = "{@COUNT(sthpw/task['status', 'Assignment'])}"
    elements = "num_assignment|num_pending|num_completed"

The y-axis elements will be displayed side by side for each sObject, and x-axis
label is specified through the option "x\_axis".

**Options**

<table>
<colgroup>
<col width="31%" />
<col width="68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>chart_type</strong></p></td>
<td><p>Defines the type of chart that will be displayed for all y-axis elements. Can be 'line', 'bar', or 'area'. Defaults to 'bar'.</p></td>
</tr>
<tr class="even">
<td><p><strong>chart_types</strong></p></td>
<td><p>Defines the type of chart that will be displayed corresponding to each y-axis element.</p></td>
</tr>
<tr class="odd">
<td><p><strong>title</strong></p></td>
<td><p>Title to display in chart. Note: The legend will cover the title.</p></td>
</tr>
<tr class="even">
<td><p><strong>width</strong></p></td>
<td><p>The pixel width of the chart. Defaults to 800.</p></td>
</tr>
<tr class="odd">
<td><p><strong>height</strong></p></td>
<td><p>The pixel height of the chart. Defaults to 500.</p></td>
</tr>
<tr class="even">
<td><p><strong>x_axis</strong></p></td>
<td><p>The x-axis element label. This should be a column of the inputs sObjects. Defaults to 'code'.</p></td>
</tr>
<tr class="odd">
<td><p><strong>y_axis</strong></p></td>
<td><p>The y-axis element. This should be a column or expression of the input sObjects.</p></td>
</tr>
<tr class="even">
<td><p><strong>elements</strong></p></td>
<td><p>y-axis elements separated by a &quot;|&quot;.</p></td>
</tr>
<tr class="odd">
<td><p><strong>expression</strong></p></td>
<td><p>TACTIC expression which specifies sObjects for charting.</p></td>
</tr>
<tr class="even">
<td><p><strong>search_type</strong></p></td>
<td><p>Search type which specifies sObjects for charting.</p></td>
</tr>
<tr class="odd">
<td><p><strong>search_keys</strong></p></td>
<td><p>Search keys of sObjects for charting.</p></td>
</tr>
</tbody>
</table>


