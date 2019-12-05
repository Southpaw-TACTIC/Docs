# TACTIC Event System Introduction

The TACTIC Event System is built into the base transactional system in
Tactic’s core. Every transaction which occurs in Tactic can fire an
event which in turn, can be used to execute a trigger or notification.

These events can be incorporated to automate specific processes that are
often repetitive. At the simplest level, there are interfaces that help
prepare and configure these aspects but, it is good to understand how
they work. Overall, there are 2 levels that these events can be
configured. The first is using the predefined event options provided in
the Project Workflow or Project Schema interfaces and the second in the
low level database events.

**Predefined Events**

The following list of events are the events provided in the Project
Workflow interface. For more information in setting up Notifications and
Triggers with this interface, please refer to **Project Automation -
Triggers** and **Project Automation - Notifications**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>A task Status is Changed</strong></p></td>
<td><p>When the status of a task is changed. Further options are provided allowing for selection.</p></td>
</tr>
<tr class="even">
<td><p><strong>A new note is added</strong></p></td>
<td><p>When a new note (sthpw/note) is added to the project.</p></td>
</tr>
<tr class="odd">
<td><p><strong>A task is assigned</strong></p></td>
<td><p>When a task is assigned to a user.</p></td>
</tr>
<tr class="even">
<td><p><strong>Files are checked in</strong></p></td>
<td><p>When files are checked in to an SObject.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Files are checked out</strong></p></td>
<td><p>When files are checked out from an SObject.</p></td>
</tr>
<tr class="even">
<td><p><strong>Custom event</strong></p></td>
<td><p>Allows for calling of an event using the raw Database Events.</p></td>
</tr>
</tbody>
</table>

**Raw Database Events**

Below is the list of the database level events. These events are run
regardless of how they are called (interface, api, external integration
etc)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>done</strong></th>
<th>Executed each time a transaction completes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>insert</strong></p></td>
<td><p>Executed each time a Search Object has been inserted.</p></td>
</tr>
<tr class="even">
<td><p><strong>update</strong></p></td>
<td><p>Executed each time a Search Object has been updated.</p></td>
</tr>
<tr class="odd">
<td><p><strong>change</strong></p></td>
<td><p>Executed each time a Search Object has changed. This combines the events insert, update and delete.</p></td>
</tr>
<tr class="even">
<td><p><strong>retire</strong></p></td>
<td><p>Executed each time a Search Object has been retired.</p></td>
</tr>
<tr class="odd">
<td><p><strong>delete</strong></p></td>
<td><p>Executed each time a Search Object has been deleted.</p></td>
</tr>
<tr class="even">
<td><p><strong>checkin</strong></p></td>
<td><p>Executed each time a checkin occurs for a Search Object</p></td>
</tr>
<tr class="odd">
<td><p><strong>checkout</strong></p></td>
<td><p>Executed each time a checkout occurs for a Search Object</p></td>
</tr>
<tr class="even">
<td><p><strong>timed</strong></p></td>
<td><p>Executed on a timed interval. This is only supported for triggers.</p></td>
</tr>
</tbody>
</table>

For example, in a transaction where the status of a task is being
changed, an association to this event can be made with the following
notation:

    update|sthpw/task|assigned

The notation can consist of 3 sections although only the event is
required.

    <Event>|<SType>|<Column>

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Event</strong></p></td>
<td><p>The raw database event.</p></td>
</tr>
<tr class="even">
<td><p><strong>SType</strong></p></td>
<td><p>The Searchable Type (SType) the event is occurring for.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Column</strong></p></td>
<td><p>The Column that was changed in the SType.</p></td>
</tr>
</tbody>
</table>


