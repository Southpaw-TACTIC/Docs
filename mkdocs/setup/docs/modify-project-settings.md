# Modify Project Settings

Use the Project Settings tab to control the various options that exist
within TACTIC. Most project settings are defined to work with the
widgets that use them and when defined, the "Type" property specifies
how the "Value" property is delivered to the widget. The different types
of settings are outlined below.

-   String - A single string argument, this may be a true/false to define
    how a widget is displayed (i.e. hide a specific aspect)

-   Sequence - A sequence of items to choose from for entry (i.e. review|revise|complete)

-   Map - A map is a sequence in which each item has a label and name assignment. This accommodates a separation between what is shown in a
    drop-down \[name\] vs what is entered into the database \[label\] (i.e. rvw:Review|rev:Revise|com:Complete)

> **Note**
>
> The overall items in the sequence or map are separated with a pipe '|'
> character and the value:label are separated with a Colin ':' character

Most settings are types of "sequences" that appear in TACTIC as a
drop-down. For example, the notes\_dailies\_context setting defines the
different kinds of context you can use in entering notes for dailies.

To insert a project setting, click the insert button in the view.

![image](media/project-settings-view.png)

The properties for the project setting search type are listed below:

<table>
<colgroup>
<col width="23%" />
<col width="76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Description</strong></th>
<th>A description of the purpose of the project settings</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Key</strong></p></td>
<td><p>This property serves as the 'code' identifier of the setting</p></td>
</tr>
<tr class="even">
<td><p><strong>Value</strong></p></td>
<td><p>The Values for the setting.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Type</strong></p></td>
<td><p>The 'type' of data definition of the value data. This tells the widget begin delivered the value how the data should be displayed.</p></td>
</tr>
<tr class="even">
<td><p><strong>Search Type</strong></p></td>
<td><p>A search type to associate the project setting to, this help further filter the settings.</p></td>
</tr>
</tbody>
</table>

Any widgets that make use of a new project setting not yet defined in
TACTIC will prompt the user to insert data for a new project setting.

**Commonly Project Setting Examples**

This table lists the some commonly used project settings in TACTIC.

<table>
<colgroup>
<col width="34%" />
<col width="32%" />
<col width="16%" />
<col width="16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>key</strong></th>
<th>Description</th>
<th>Default Value</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>flash_output_format</strong></p></td>
<td><p>Output format for a Flash project, swf OR mov</p></td>
<td><p>swf</p></td>
<td><p>string</p></td>
</tr>
<tr class="even">
<td><p><strong>fps</strong></p></td>
<td><p>Frames per second</p></td>
<td><p>24</p></td>
<td><p>string</p></td>
</tr>
<tr class="odd">
<td><p><strong>handle_texture_dependency</strong></p></td>
<td><p>Handle texture dependencies when performing a checkin in a 3D application. Accepted values are 'true', 'false', 'optional'.</p></td>
<td><p>true</p></td>
<td><p>string</p></td>
</tr>
<tr class="even">
<td><p><strong>notes_dailies_context</strong></p></td>
<td><p>Notes context used in the Dailies tab</p></td>
<td><p>anim|effects|model</p></td>
<td><p>sequence</p></td>
</tr>
<tr class="odd">
<td><p><strong>shot_hierarchy</strong></p></td>
<td><p>Shot hierarchy structure. Accepted values are 'episode_sequence' or 'sequence'.</p></td>
<td><p>sequence</p></td>
<td><p>string</p></td>
</tr>
<tr class="even">
<td><p><strong>bin_label</strong></p></td>
<td><p>Label for a Bin</p></td>
<td><p>n/a</p></td>
<td><p>string</p></td>
</tr>
<tr class="odd">
<td><p><strong>bin_type</strong></p></td>
<td><p>Type of Bin</p></td>
<td><p>n/a</p></td>
<td><p>string</p></td>
</tr>
<tr class="even">
<td><p><strong>web_file_size</strong></p></td>
<td><p>dimension of the web type file size, e.g. 640x480</p></td>
<td><p>640x480</p></td>
<td><p>string</p></td>
</tr>
<tr class="odd">
<td><p><strong>thumbnail_protocol</strong></p></td>
<td><p>The protocol through which the link of a thumbnail is opened. Accepted values are 'file', 'http'.</p></td>
<td><p>http</p></td>
<td><p>string</p></td>
</tr>
<tr class="even">
<td><p><strong>versionless_mode</strong></p></td>
<td><p>The global setting for copy or symlink for versionless check-ins</p></td>
<td><p>copy</p></td>
<td><p>string</p></td>
</tr>
</tbody>
</table>


