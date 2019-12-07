# TACTIC Event System Introduction

The TACTIC Event System is built into the base transactional system in
Tactic’s core. Every transaction which occurs in Tactic can fire an
event which in turn, can be used to execute a trigger or notification.


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


~
~
