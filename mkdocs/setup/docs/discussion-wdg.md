# Note (discussion)

**Note (discussion)**

**Description**

The Notes Widget allows users to write notes for a particular item
(sObject). This widget allows team members to exchange comments for a
process by writing them in the Notes Widget. The notes are displayed
chronologically with latest one appearing at the top. The complete
history is displayed by default. It’s one of the common columns which
can be added in any view for an sType. A similar note entry widget
called the Note Sheet Widget, focuses more on the speed of entry rather
than the display of the conversation.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th>Notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.widget.DiscussionWdg</p></td>
</tr>
<tr class="even">
<td><p><strong>Category</strong></p></td>
<td><p>Table Element Widget</p></td>
</tr>
<tr class="odd">
<td><p><strong>Supported Interfaces</strong></p></td>
<td><p>TableLayoutWdg</p></td>
</tr>
<tr class="even">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>2.5<br />
</p></td>
</tr>
<tr class="odd">
<td><p><strong>Required database columns</strong></p></td>
<td><p>This widget interacts with the built in sthpw/note table</p></td>
</tr>
</tbody>
</table>

**Usage**

To create a new note, select the New Note button.

This will switch the DiscussionWdg into insert mode where notes and
context of the notes can be entered.

In most cases, the grouping for the notes is derived through selecting a
'context'. This context is often chosen in relation to the context of a
given 'task' or 'snapshot' (Checkin) for the same parent sObject. This
then associates all tasks, notes and snapshots under a specific Search
Object. This allows users to retrieve historical data for a Search
Object through a context. This answers the question "What’s the history
of this Asset from the design department?"

To navigate the history of the notes, click on a particular note and it
will expand and display the full note.

> **Note**
>
> Depending on the configuration, the grouping (context) items will be
> grouped and separated by a group label represented as &lt;&lt; *label*&gt;&gt;. In
> that case, selecting the group label will trigger a warning pop-up.
>
> To unset a value, you can usually select the empty value with the label
> '-- Select --'.

**Implementation**

The Notes widget is a common column which can be added using the Column
Manager. The item name is "notes". A "default" context is used in this
simple implementation.

**Options**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>context</strong></th>
<th>a global context can be specified</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>append_context</strong></p></td>
<td><p>a context can be appended to the current list (deprecated)</p></td>
</tr>
<tr class="even">
<td><p><strong>setting</strong></p></td>
<td><p>A project setting can be used to drive the contexts. This provides the key of the project setting.</p></td>
</tr>
<tr class="odd">
<td><p><strong>append_setting</strong></p></td>
<td><p>This serves the same purpose as setting but would append the contexts at the end</p></td>
</tr>
<tr class="even">
<td><p><strong>include_submission</strong></p></td>
<td><p>If set to true, it would include the notes for the submission (a child) of the current sObject.</p></td>
</tr>
</tbody>
</table>

**Advanced**

    <element name="discussion" edit="false">
            <display class="pyasm.widget.DiscussionWdg">
                <context>default</context>
            </display>
    </element>
