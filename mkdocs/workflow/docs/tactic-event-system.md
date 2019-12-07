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


