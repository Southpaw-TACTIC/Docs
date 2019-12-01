# Pipeline Process Options

Each node has a number of properties that can be set. These properties
may be used by TACTIC to derive useful information. These properties
are:

<table>
<colgroup>
<col width="16%" />
<col width="83%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Task Status Pipeline</strong></p></td>
<td><p>Selects from a list of 'Task Status Pipelines' to connect the selected process to. This accommodates a separate set of statuses for the specific process. These pipelines are defined the same way other pipelines are. The only difference is that these pipelines are assigned to the sthpw/task sType. This property represents the &quot;code&quot; property of the task pipeline.</p></td>
</tr>
<tr class="even">
<td><p><strong>Assign Login Group</strong></p></td>
<td><p>Specifies the process to a particular group of artists.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Supervisor Login Group</strong></p></td>
<td><p>Specifies the process to a particular group of supervisors.</p></td>
</tr>
<tr class="even">
<td><p><strong>Default Duration</strong></p></td>
<td><p>Set the a duration schedule (in days) of the process.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Color</strong></p></td>
<td><p>The color to represent the process in the GUI. For example the Task Status Widget can be setup to display the color of the process.</p></td>
</tr>
<tr class="even">
<td><p><strong>Label</strong></p></td>
<td><p>Add a label for the process.</p></td>
</tr>
</tbody>
</table>

To open the **Edit Properties** pop-up, select a node and then click on
the **Properties** button on the tools shelf:

Further process options can be found by right clicking on the node in
the:

**Pipeline Editor → Show Processes**

![image](media/2_pipeline_process-options_show_processes.png)

The **Processes** tab will appear in the panel at the bottom:

![image](media/3_pipeline_process-options_process_tab.png)

<table>
<colgroup>
<col width="16%" />
<col width="83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Pipeline Code</strong></th>
<th>eg. project/asset</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Process</strong></p></td>
<td><p>eg. design, rough, finale, delivery, etc.</p></td>
</tr>
<tr class="even">
<td><p><strong>Search Type</strong></p></td>
<td><p>eg. project/asset</p></td>
</tr>
<tr class="odd">
<td><p><strong>Checkin Mode</strong></p></td>
<td><p>File</p></td>
</tr>
<tr class="even">
<td><p>Directory</p></td>
<td><p>Sequence</p></td>
</tr>
<tr class="odd">
<td><p>Multiple Files</p></td>
<td><p><strong>Checkin Validate Script Path</strong></p></td>
</tr>
<tr class="even">
<td><p>Path to a script which is run upon checkin for validation.</p></td>
<td><p><strong>Checkin Options View</strong></p></td>
</tr>
<tr class="odd">
<td><p>Advanced custom layout to be used for checkin view.</p></td>
<td><p><strong>Subcontext</strong></p></td>
</tr>
</tbody>
</table>


