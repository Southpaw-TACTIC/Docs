# Simple Table Element

![image](media/1_simple_table_element_overview.png)

**Description**

This widget displays the value in the database "as is", in its raw
unformatted form. This is the default display widget.

> **Note**
>
> The Simple Table Element widget is the same as the Raw Data widget.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Simple Table Element</p></td>
</tr>
<tr class="even">
<td><p><strong>Class</strong></p></td>
<td><p>raw_data</p></td>
</tr>
<tr class="odd">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>3.0.0 \+</p></td>
</tr>
<tr class="even">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>

**Implementation**

Use this widget to display the value in the database "as is", without
any pre-formatting. This widget is the default display widget.

**Options**

<table>
<colgroup>
<col width="30%" />
<col width="69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>type</strong></p></td>
<td><p>The database type: string, text, int, float, boolean, timestamp</p></td>
</tr>
</tbody>
</table>

**Example**

For example, to display the keywords field, as is, from the Edit Column
Definition→View Mode: Select **Widget → Raw Data → text**.

**Advanced**

Below is the XML for the above example.

    <element name="keywords" title="test" edit="true" color="false">
      <display widget="raw_data">
        <type>text</type>
      </display>
    </element>
