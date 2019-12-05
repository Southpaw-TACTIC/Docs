# Checkin History

![image](media/1_sobject_checkin_history_overview.png)

**Description**

The Checkin History Widget is a toggle that opens a hidden row that
displays all the snapshots (snapshots are checkins at a particular
moment in time for a context) for an item.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Checkin History Widget</p></td>
</tr>
<tr class="even">
<td><p><strong>Common Title</strong></p></td>
<td><p>History</p></td>
</tr>
<tr class="odd">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.widget.SObjectCheckinHistoryWdg</p></td>
</tr>
<tr class="even">
<td><p><strong>Category</strong></p></td>
<td><p>Common</p></td>
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

**Usage**

The following details are displayed by the Checkin History Widget for a
task:

-   **preview** of the snapshot

-   whether checkout of the snapshot is **locked**

-   toggle to open a hidden row to list the **files** in the snapshot

-   link to **checkout** this particular snapshot

-   **context** of the snapshot

-   **version** of the snapshot

-   **revision** of the snapshot

-   **login** who checked in the snapshot

-   **timestamp** of the checkin

-   **description** written by the user at the time of the snapshot

-   indicator whether the snapshot is the **current** version for that
    context

-   toggle to open the notes using the **Note Sheet** Widget

**Implementation**

The Checkin History Widget can be found as a common column that can be
added using the Column Manager.

**Options**

There are no options provided for the Checkin History Widget.

**Advanced**

    <element name="history" edit="false">
        <display class="HiddenRowToggleWdg">
            <icon>HISTORY</icon>
            <dynamic_class>tactic.ui.widget.SObjectCheckinHistoryWdg</dynamic_class>
        </display>
    </element>
