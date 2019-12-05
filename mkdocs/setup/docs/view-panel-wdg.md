# View Panel

![image](media/1_view_panel_overview.png)

**Description**

The View Panel is a composite widget which binds together a Table Layout
Widget and a Search Widget. The Search Widget is a searching mechanism
that retrieves items and transfers them to a Table Layout Widget to
draw. The View Panel Widget is used in most of TACTIC’s predefined
views.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>View Panel</p></td>
</tr>
<tr class="even">
<td><p><strong>Class</strong></p></td>
<td><p>ViewPanelWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>2.5.0<br />
</p></td>
</tr>
<tr class="even">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>

**Implementation**

The View Panel widget makes use of the TableLayoutWdg capabilities. The
views available to the View Panel are identical to that of the Table
Layout Widget.

**Options**

<table>
<colgroup>
<col width="31%" />
<col width="68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>search_type</strong></th>
<th>Define The sType that this View panel displays with.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>view</strong></p></td>
<td><p>The TACTIC name for the view. e.g. admin.test_asset_tracking</p></td>
</tr>
<tr class="even">
<td><p><strong>insert_view</strong></p></td>
<td><p>Specify the path to a custom insert view.</p></td>
</tr>
<tr class="odd">
<td><p><strong>edit_view</strong></p></td>
<td><p>Specify the path to a custom edit view.</p></td>
</tr>
<tr class="even">
<td><p><strong>ingest_custom_view</strong></p></td>
<td><p>Specify a custom layout view that Ingest Files menu option opens in a new tab.</p></td>
</tr>
<tr class="odd">
<td><p><strong>ingest_data_view</strong></p></td>
<td><p>Specify a view similar to edit view that defines any data to be saved with each ingested sobject.</p></td>
</tr>
<tr class="even">
<td><p><strong>expression</strong></p></td>
<td><p>Use an expression for the search. The expression must return items. e.g. @SEARCH(sthpw/note) or @SOBJECT(sthpw/note)</p></td>
</tr>
<tr class="odd">
<td><p><strong>filter</strong></p></td>
<td><p>JSON data structure representing the settings for SearchWdg</p></td>
</tr>
<tr class="even">
<td><p><strong>parent_key</strong></p></td>
<td><p>Provide a parent item to filter in the search.</p></td>
</tr>
<tr class="odd">
<td><p><strong>search_key</strong></p></td>
<td><p>Provide the starting search key.</p></td>
</tr>
<tr class="even">
<td><p><strong>search_view</strong></p></td>
<td><p>(INTERNAL) View for custom searches.</p></td>
</tr>
<tr class="odd">
<td><p><strong>layout</strong></p></td>
<td><p>Different layout available - default, tile, fast_table, raw_table, old_table, static_table, collection, browser, card, tool, aggregate, custom_item, custom</p></td>
</tr>
<tr class="even">
<td><p><strong>show_gear</strong></p></td>
<td><p>Determine whether to show the gear menu - true, false.</p></td>
</tr>
<tr class="odd">
<td><p><strong>show_search</strong></p></td>
<td><p>Determine whether to show the search box - true, false.</p></td>
</tr>
<tr class="even">
<td><p><strong>show_search_limit</strong></p></td>
<td><p>Determine whether to show the search limit - true, false.</p></td>
</tr>
<tr class="odd">
<td><p><strong>show_insert</strong></p></td>
<td><p>Determine whether to show the insert button - true, false.</p></td>
</tr>
<tr class="even">
<td><p><strong>show_refresh</strong></p></td>
<td><p>Display the refresh button on the shelf - true, false.</p></td>
</tr>
<tr class="odd">
<td><p><strong>show_keyword_search</strong></p></td>
<td><p>Determine whether to show the Keyword search input - true, false.</p></td>
</tr>
<tr class="even">
<td><p><strong>show_select</strong></p></td>
<td><p>Determine whether to show row_selection - true, false.</p></td>
</tr>
<tr class="odd">
<td><p><strong>show_shelf</strong></p></td>
<td><p>Determine whether to show the action shelf - true, false.</p></td>
</tr>
<tr class="even">
<td><p><strong>show_layout_switcher</strong></p></td>
<td><p>Determine whether to show the layout switcher - true, false.</p></td>
</tr>
<tr class="odd">
<td><p><strong>show_column_manager</strong></p></td>
<td><p>Determine whether to show the column manager - true, false.</p></td>
</tr>
<tr class="even">
<td><p><strong>show_collection_tool</strong></p></td>
<td><p>Determine whether to show the collection button - true, false.</p></td>
</tr>
<tr class="odd">
<td><p><strong>show_context_menu</strong></p></td>
<td><p>Determine whether to show the context menu - true, false.</p></td>
</tr>
<tr class="even">
<td><p><strong>show_expand</strong></p></td>
<td><p>Determine whether to show the expand button - true, false.</p></td>
</tr>
<tr class="odd">
<td><p><strong>show_help</strong></p></td>
<td><p>Determine whether to show the help button - true, false.</p></td>
</tr>
<tr class="even">
<td><p><strong>show_border</strong></p></td>
<td><p>Determine whether to show the table border - true, false.</p></td>
</tr>
<tr class="odd">
<td><p><strong>popup</strong></p></td>
<td><p>Pop the view up in a pop-up window.</p></td>
</tr>
<tr class="even">
<td><p><strong>do_initial_search</strong></p></td>
<td><p>Run the search on loading of the view.</p></td>
</tr>
<tr class="odd">
<td><p><strong>init_load_num</strong></p></td>
<td><p>Set the number of rows to laod initially. If set to -1, it will not load in chunks</p></td>
</tr>
<tr class="even">
<td><p><strong>no_results_msg</strong></p></td>
<td><p>The message displayed when the search returns no item</p></td>
</tr>
<tr class="odd">
<td><p><strong>no_results_mode</strong></p></td>
<td><p>The display modes for no results</p></td>
</tr>
<tr class="even">
<td><p><strong>custom_filter_view</strong></p></td>
<td><p>View for custom filters. Defaults to &quot;custom_filter&quot;.</p></td>
</tr>
<tr class="odd">
<td><p><strong>process</strong></p></td>
<td><p>The process which is applicable in the UI when load view is used.</p></td>
</tr>
<tr class="even">
<td><p><strong>checkin_context</strong></p></td>
<td><p>Override the checkin context for Check-in New File - publish (default).</p></td>
</tr>
<tr class="odd">
<td><p><strong>checkin_type</strong></p></td>
<td><p>Override the checkin type for Check-in New File - auto, strict.</p></td>
</tr>
<tr class="even">
<td><p><strong>mode</strong></p></td>
<td><p>Mode to pass into the layout engine - widget, raw.</p></td>
</tr>
<tr class="odd">
<td><p><strong>element_names</strong></p></td>
<td><p>Provide a list of column names (ie. &quot;preview,name,description&quot;) for the view.</p></td>
</tr>
<tr class="even">
<td><p><strong>group_elements</strong></p></td>
<td><p>Provide a list of grouping column names. e.g. sort_order,category</p></td>
</tr>
<tr class="odd">
<td><p><strong>schema_default_view</strong></p></td>
<td><p>(INTERNAL) flag to show whether this is generated straight from the schema.</p></td>
</tr>
<tr class="even">
<td><p><strong>order_by</strong></p></td>
<td><p>The column name to order ascending by. multiple columns are to be comma separated.</p></td>
</tr>
<tr class="odd">
<td><p><strong>search_limit</strong></p></td>
<td><p>The number of items to show on each page. e.g. 20 A value &lt; 0 means no limit affecting the search.</p></td>
</tr>
<tr class="even">
<td><p><strong>search_limit_mode</strong></p></td>
<td><p>Determine if it displays top, bottom or both search limit - bottom, top, both</p></td>
</tr>
<tr class="odd">
<td><p><strong>simple_search_mode</strong></p></td>
<td><p>Display mode of simple search bar - inline, hidden.</p></td>
</tr>
<tr class="even">
<td><p><strong>simple_search_view</strong></p></td>
<td><p>View for defining a simple search.</p></td>
</tr>
<tr class="odd">
<td><p><strong>simple_search_config</strong></p></td>
<td><p>Xml config as opposed to a view for defining a simple search.</p></td>
</tr>
<tr class="even">
<td><p><strong>simple_search_columns</strong></p></td>
<td><p>Number of columns in the simple search bar - 2, 3 or 4.</p></td>
</tr>
<tr class="odd">
<td><p><strong>simple_search_visible_rows</strong></p></td>
<td><p>Number of visible rows in the simple search bar.</p></td>
</tr>
<tr class="even">
<td><p><strong>width</strong></p></td>
<td><p>Set the default width of the table</p></td>
</tr>
<tr class="odd">
<td><p><strong>gallery_align</strong></p></td>
<td><p>Gallery vertical alignment. It is used when a Preview icon is clicked to open in gallery mode - top, bottom.</p></td>
</tr>
</tbody>
</table>

**Advanced**

Often, the ViewPanelWdg is defined from a side bar link. It can be
defined by XML as follows

    <element name='summary'>
      <display class='tactic.ui.panel.ViewPanelWdg'>
        <search_type>sthpw/task</search_type>
        <view>task_summary</view>
      </display>
    </element>
