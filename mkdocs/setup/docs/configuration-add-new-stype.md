# Add new sType

**Add new sType**

Registering a new sType or "Searchable Type" in TACTIC provides
opportunity to track separate list of items. From a technical
standpoint, a new sType is a separate table in the project’s database.
This allows for the following configuration aspects:

-   Views

-   Custom Columns (properties)

-   Workflows processes and status

-   Notifications

-   Triggers

-   Tools

-   Security

-   …​and more

To register a new sType, click the \[+\] button in the top-left of the
configuration page. The **Register a new sType** wizard will appear:

![image](media/register_stype_definition.png)

**Information**

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Project Specific</strong></p></td>
<td><p><em>(available when creating a new sType for a project that is based on a template)</em></p></td>
</tr>
<tr class="even">
<td><p><strong>Title</strong></p></td>
<td><p>The title for the sType is used in the UI for display purposes.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Searchable Type</strong></p></td>
<td><p>Refers to the database name for the sType. in a &quot;&lt;project&gt;/&lt;name&gt;&quot; format. If no project is defined (i.e.. &quot;art/&quot;) than the current project namespace will be used.</p></td>
</tr>
<tr class="even">
<td><p><strong>Description</strong> <em>(optional)</em></p></td>
<td><p>An optional description of the sType.</p></td>
</tr>
</tbody>
</table>

Once the fields are completed, press "Next" or press "Register" to
complete the registration process. Note: It is recommended to go through
the series of steps outlined in the "Register a new sType" wizard, as
this allows for quick and easy configuration of the new sType that is
outside of the TACTIC defaults.

**Workflow**

![image](media/register_stype_pipeline.png)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Items have a Pipeline?</strong></p></td>
<td><p>When selected, sets up an association for a pipeline workflow for the sObjects in that sType. <em>The section below describes this relationship in more detail</em></p></td>
</tr>
<tr class="even">
<td><p><strong>Process</strong> <em>(optional)</em></p></td>
<td><p>Stages in the process. <em>eg. processes for an asset sType: design, model, texture, rigging eg. processes for a shot sType: layout, animation/fx, lighting, render, comp</em></p></td>
</tr>
</tbody>
</table>

**Preview Image**

![image](media/register_stype_preview_image.png)

<table>
<colgroup>
<col width="51%" />
<col width="48%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Preview Image</strong> <em>(optional)</em></p></td>
<td><p>Browse to select a preview image for the new sType.</p></td>
</tr>
</tbody>
</table>

**Columns**

![image](media/register_stype_columns.png)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Include Preview Image?</strong></p></td>
<td><p>Preview image for each item (sObject) of that sType.</p></td>
</tr>
<tr class="even">
<td><p><strong>Add Columns to sType</strong> <em>(optional)</em></p></td>
<td><p>During the registration process, default columns are added to the new sType table. You can also add additional columns during this process. Note - columns can be added after this process using the Table Manager</p></td>
</tr>
</tbody>
</table>

**Finish**

![image](media/register_stype_finish.png)

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Finish</strong></p></td>
<td><p>To complete the registration process, press &quot;Register&quot;. A this point, the option is provided to go back and change any information by clicking on the &quot;Back&quot; button.</p></td>
</tr>
</tbody>
</table>


