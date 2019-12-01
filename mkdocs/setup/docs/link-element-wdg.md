# Link Element

![image](media/1_link_element_overview.png)

**Description**

The Link Element Widget facilitates creation of a hyperlink. Clicking on
the link button opens the hyperlink in a new tab in the web browser.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Link Element</p></td>
</tr>
<tr class="even">
<td><p><strong>Common Title</strong></p></td>
<td><p>Link</p></td>
</tr>
<tr class="odd">
<td><p><strong>Class</strong></p></td>
<td><p>Link</p></td>
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

Go into edit mode for the Link column. Specify the full URL to a
hyperlink, such as: <http://support.southpawtech.com>.

Save the data and refresh the view.

Click on the link icon and the link to the web page will be opened in a
new tab.

**Implementation**

The Link Element Widget can be created using the Create New Column and
specifying: Display → Widget → **Link**.

**Options**

The ability to specify a customize icon to appears in the row.

**Advanced**

    <element name="link" title="link" edit="true" color="false">
      <display widget="link"/>
    </element>
