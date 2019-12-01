# SimpleUploadWdg

![image](media/simple-checkin_menu.png)

**Description**

The Simple Upload Widget is used for uploading files in-line in tables
and also in edit windows. It is the simplest form of Tactic checkin as
is allows for uploading of a single file and uses only a single hard
coded (configured) checkin context.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Simple Upload Widget</p></td>
</tr>
<tr class="even">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.widget.SimpleUploadWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>Category</strong></p></td>
<td><p>Edit Widgets</p></td>
</tr>
<tr class="even">
<td><p><strong>Supported Interfaces</strong></p></td>
<td><p>TableWdg, EditWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>2.5.0 \+</p></td>
</tr>
<tr class="even">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>

**Implementation**

This widget is available as part of the "preview" common column. It is
also used when right-clicking on an item and choosing "Change preview"
or "Checkin File"

**Options**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Common Name(s)/Title</strong></p></td>
<td><p>Preview, Snapshot, Files</p></td>
</tr>
<tr class="even">
<td><p><strong>Context</strong></p></td>
<td><p>TableWdg, EditWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>Show Preview?</strong></p></td>
<td><p>2.5.0 \+</p></td>
</tr>
</tbody>
</table>

**Advanced**

    <element name='preview'>
      <display class='tactic.ui.widget.SimpleUploadWdg'>
        <context>icon</context>
      </display>
    </element>
