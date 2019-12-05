# Text Area

![image](media/1_textarea_overview.png)

**Description**

The TextAreaWdg is a simple text widget which is used for editing
full-text. The widget supports using the ENTER key for adding new lines
(the ENTER key is often not supported on text entry widgets where
CTRL+ENTER is used.) This widget can also be configured to display a
larger canvas to work on.

**Info**

<table>
<colgroup>
<col width="30%" />
<col width="69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th>TextAreaWdg</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Class</strong></p></td>
<td><p>pyasm.widget.TextAreaWdg</p></td>
</tr>
<tr class="even">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>2.5.0<br />
</p></td>
</tr>
<tr class="odd">
<td><p><strong>Required database columns</strong></p></td>
<td><p>requires a database column for storing the text data.</p></td>
</tr>
</tbody>
</table>

**Implementation**

The TextAreaWdg is used in Edit scenarios where full text input is
required. There is control for the columns (characters across) and rows
(characters down).

**Options**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>cols</strong></p></td>
<td><p>The number of character columns in the TextArea</p></td>
</tr>
<tr class="even">
<td><p><strong>rows</strong></p></td>
<td><p>The number of character rows in the TextArea</p></td>
</tr>
</tbody>
</table>

**Advanced**

The following example is a default implementation. The default number of
cols is **50** and the default number of rows is **3**.

    <element name="subject">
      <display class="TextAreaWdg"/>
    </element>

The following example creates a large text area which could be used for
writing large amounts of full-text.

    <element name="summary">
      <display class="TextAreaWdg">
        <cols>100</cols>
        <rows>30</rows>
      </display>
    </element>
