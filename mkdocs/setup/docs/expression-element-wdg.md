# Expression

**Expression**

![image](media/expression-element-wdg_dynamic.png)

**Description**

The ExpressionElementWdg allows you to use the TACTIC expression
language to determine the value displayed in the table cell. The
expression is caclulated from a starting sobject which represents the
sobject in the particular row in the table. The expression is evaluated
for each sobject on every row. When an expression is evaluated, the
value is added to a dynamic attribute of the sobject and can be used in
future expressions in this widget. Please refer to the expression
language reference for more information on the expression language.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>ExpressionElementWdg</p></td>
</tr>
<tr class="even">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.table.ExpressionElementWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>Category</strong></p></td>
<td><p>Common Columns</p></td>
</tr>
<tr class="even">
<td><p><strong>Supported Interfaces</strong></p></td>
<td><p>TableLayoutWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>2.5.0<br />
</p></td>
</tr>
<tr class="even">
<td><p><strong>Required database columns</strong></p></td>
<td><p>depends on expression</p></td>
</tr>
</tbody>
</table>

**Implementation**

Display the total cost of an item by multiplying the total\_number column
with the unit\_cost column When an expression is evaluated by the
ExpressionElementWdg, a new attribute with the name of the element is
dynamically added to the sobject (in this cost) which can be used in the
"bottom" directive.

    <element name='cost'>
      <display class='tactic.ui.table.ExpressionElementWdg'>
        <expression>@GET(.total_number) * @GET(.unit_cost)</expression>
        <bottom>@SUM(.cost)</bottom>
      </display>
    </element>

**Options**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>expression</strong></th>
<th>Expression to evaluate the widget</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>display_format</strong></p></td>
<td><p>Display format string like DATETIME, DATE, -$1,234 applicable for various Formatted Element can be used here.</p></td>
</tr>
<tr class="even">
<td><p><strong>inline_styles</strong></p></td>
<td><p>Styles to add to the DIV generated that contains the result of the expression</p></td>
</tr>
<tr class="odd">
<td><p><strong>return</strong></p></td>
<td><p>single</p></td>
</tr>
<tr class="even">
<td><p>list - Determines what the expression return type should be</p></td>
<td><p><strong>bottom</strong></p></td>
</tr>
<tr class="odd">
<td><p>Expression to calculate the bottom row of the table</p></td>
<td><p><strong>group_bottom</strong></p></td>
</tr>
<tr class="even">
<td><p>Expression to calculate the group bottom row of the table</p></td>
<td><p><strong>mode</strong></p></td>
</tr>
<tr class="odd">
<td><p>value</p></td>
<td><p>boolean</p></td>
</tr>
<tr class="even">
<td><p>check</p></td>
<td><p>icon - Display mode for this widget</p></td>
</tr>
<tr class="odd">
<td><p><strong>expression_mode</strong></p></td>
<td><p>default</p></td>
</tr>
<tr class="even">
<td><p>absolute - If absolute mode is selected, it does not relate to the current SObject</p></td>
<td><p><strong>calc_mode</strong></p></td>
</tr>
<tr class="odd">
<td><p>fast</p></td>
<td><p>slow - fast uses new calculation mode. Only @SUM, @COUNT, @SOBJECT and @GET are current supported</p></td>
</tr>
<tr class="even">
<td><p><strong>enable_eval_listener</strong></p></td>
<td><p>Currently javascript expression evaluation is not fully baked, so only use the client side evaluation listener when needed and NOT by default</p></td>
</tr>
<tr class="odd">
<td><p><strong>icon_expr</strong></p></td>
<td><p>Expression to evaluate which icon to use when mode = 'icon'</p></td>
</tr>
<tr class="even">
<td><p><strong>order_by</strong></p></td>
<td><p>provide a simple string to order by e.g. code or by an attribute in a related sType in the same database, e.g. prod/sequence.dsecription</p></td>
</tr>
<tr class="odd">
<td><p><strong>group_by</strong></p></td>
<td><p>true</p></td>
</tr>
<tr class="even">
<td><p>false - Turn on group by in context menu if set to true</p></td>
<td><p><strong>group_by_time</strong></p></td>
</tr>
<tr class="odd">
<td><p>true</p></td>
<td><p>false - Turn on group by time options in context menu if set to true</p></td>
</tr>
<tr class="even">
<td><p><strong>justify</strong></p></td>
<td><p>default</p></td>
</tr>
<tr class="odd">
<td><p>left</p></td>
<td><p>right</p></td>
</tr>
</tbody>
</table>

**Examples**

Display the number of tasks for a given sobject and then display the
total number at the bottom.

    <element name='num_tasks'>
      <display class='tactic.ui.table.ExpressionElementWdg'>
        <expression>@COUNT(sthpw/task)</expression>
        <bottom>@SUM(.num_tasks)</bottom>
      </display>
    </element>

Mode "boolean" displays a green dot for every sobject that has an
expression that evalutes to True. In this case, a green dot is display
on every row where the number of tasks is greater than zero.

    <element name='has_tasks'>
      <display class='tactic.ui.table.ExpressionElementWdg'>
        <expression>@COUNT(sthpw/task) > 0</expression>
        <mode>boolean</mode>
      </display>
    </element>

Another example of a mode which displays a checkbox instead of red/green
dots. The checkbox appears for any result greater than zero

    <element name='has_tasks'>
      <display class='tactic.ui.table.ExpressionElementWdg'>
        <expression>@COUNT(sthpw/task) > 0</expression>
        <mode>check</mode>
      </display>
    </element>

The expression language has the ability to get values from other related
tables. The following example illustrates an expression to find the
description of the parent sequence of a shot.

    <element name='sequence_description'>
      <display class='tactic.ui.table.ExpressionElementWdg'>
        <expression>@GET(prod/sequence.description)</expression>
      </display>
    </element>

The expression language has the ability to get values from other related
tables and format it using the DATETIME project setting which can be
customized per project

    <element name='task_due_date'>
      <display class='tactic.ui.table.ExpressionElementWdg'>
        <expression>@GET(sthpw/task.bid_end_date)</expression>
        <display_format>DATETIME</display_format>
      </display>
    </element>

Ultimately, the ExpressionElementWdg can make use of any expression in
the TACTIC Expression Lanaguage.

When using mode = 'icon', it is possible to set up an expression using
icon\_expr to determine what that icon should be. A special variable
$VALUE is used to determine the value of the expressions

    <element name="is_synced" title='Synced' edit='false'>
      <display class='tactic.ui.table.ExpressionElementWdg'>
        <expression>@GET(.is_synced) == True</expression>
        <mode>icon</mode>
        <icon_expr>@IF( '$VALUE' == True, 'CHECK', 'CROSS' )</icon_expr>
      </display>
    </element>
