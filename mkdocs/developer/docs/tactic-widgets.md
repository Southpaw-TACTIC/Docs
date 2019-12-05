# Widget Architecture

**What are Widgets?**

Widgets are drawable entities. They have the ability to draw themselves
and also have the ability to contain other widgets and call on their
drawing.

**Widget Architecture?**

The TACTIC interface is entirely built on top of widget architecture. A
widget has a drawing mechanism which displays the widget. Widgets can
contain any number of other widgets and pass information to them.

Certain widgets also make use of configuration xml documents in order to
configure how they should be drawn. These configs are useful because
they allow very quick and readable configuration of complex widgets.
This document can also be stored in the database as a way of remembering
the state of how to redraw a particular widget. This is widely used in
TACTIC to store various parts of the interface in the database.

Every widget has a display method which completely controls how a widget
is displayed. This display is recursive as each widget will call all of
it’s children’s display method. In this manner, the entire interface is
build up.

Widgets derive data to draw from sobjects. Generally a search is
performed to retrieve sobjects which are then used to draw the widget.
The widget itself can perform the search or it can recieve sobjects from
some external source.

**Widget Config**

Numerous widgets use configuration xml documents to help them draw their
display. These widgets are considered to be "layout" widgets in that
they generally use the configurations to determine what the child
widgets are and how and where they are drawn within the parent layout
widget. The widget config is an xml document which describes the child
elements and how they should be display. The format is defined as
follows.

    <config>
      <VIEW>
        <element name='NAME'  OPTION='VALUE'>
          <display class='CLASS_PATH'>
            <KWARG>VALUE</KWARG>
            <KWARG>VALUE</KWARG>
          </dispaly>
        </element>
        <element name='NAME' OPTION='VALUE'>
          <display class='CLASS_PATH'>
            <KWARG>VALUE</KWARG>
            <KWARG>VALUE</KWARG>
          </dispaly>
        </element>
      </VIEW>
    </config>

Where capitalized words represent variable entries.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>VIEW</p></td>
<td><p>The name of a view which encompases a particular configuration. There can be any number of views in a configuration documentation</p></td>
</tr>
<tr class="even">
<td><p>OPTION</p></td>
<td><p>An option defining a state or setting of this element. This information does not get passed to the element widget</p></td>
</tr>
<tr class="odd">
<td><p>VALUE</p></td>
<td><p>A value or a particular argument or options</p></td>
</tr>
<tr class="even">
<td><p>CLASS_PATH</p></td>
<td><p>The fully qualified python path of the widget class</p></td>
</tr>
<tr class="odd">
<td><p>KWARG</p></td>
<td><p>A kwarg that is passed to the class on construction</p></td>
</tr>
</tbody>
</table>

A simple example of a configuration is as follows:

    <config>
    <simple>
      <element name='email'>
        <display class='custom.MyCustomWdg'>
          <title>My Widget</title>
        </display>
      </element>
    </simple>
    </config>

In this case, the "simple" view defines a single element called "email".
This element

The configuration document can contain any number of "views". Each
"view" can contain any number of elements. Inside each element, there
are xml snippets which represents an xml serialization of a widget. In
the example above:

    <display class='custom.MyCustomWdg'>
      <title>My Widget</title>
    </display>

translates into python server code as follows:

    from custom import MyCustomWdg
    widget = MyCustomWdg(title='My Widget')

TACTIC uses this format extensively to serialize widgets to the
database. Although any source can be used, the config is most often
defined in the widget config table of a particular project.

There are a couple of layout classes that make heavy use of the widget
config.

**SideBarWdg:**

**TableLayoutWdg:** this class is the used to display most tabular data in
TACTIC. It contains many features to make the display of tabular data
dynamic and flexible. Views can be customized and saved. It is probably
the most used layout class in TACTIC. It makes heavy use of the widget
config for its display. It’s importance is sufficient to warrent a
section on its own below.

**CustomLayoutWdg:** this class makes use of a special version of the
config. It defines elements, but they are defined within an html tag,
allowing for precise layout of elements using HTML. This allows for very
flexible layouts while still being able make use of TACTIC widgets.

**SideBarWdg**

The SideBarWdg defines the look of the side bar on the left of the
TACTIC interface. The SideBarWdg makes heavy use of the widget config to
determine the contents of the side bar. There are 3 main types of
widgets that would be defined as elements in the SideBarWdg:

-   LinkWdg

-   FolderWdg (Currently SectionWdg)

-   SeparatorWdg

The top level view for the project views can be found in the widget
config table with the criteria:

-   search\_type = 'SideBarWdg'

-   view = 'project\_view'

This will defined a list of elements that appear in the top level of the
"Project View". An example would look like the following:

    <config>
      <project_view>
        <element name='summary'/>
        <element name='modeling'/>
      </project_view>
    </config>

Although, you could defined the display section here, there are are
hierarchical definitions to the elements. If a definition is not found
inline, TACTIC will look at the the database for the specially named
"definition" view.

-   search\_type = 'SideBarWdg'

-   view = 'definition'

<!-- -->

    <config>
      <definition>
        <element name='summary' title='Asset Summary'>
          <display class='LinkWdg'>
            <class_name>tactic.ui.panel.ViewPanelWdg</class_name>
            <search_type>prod/asset</search_type>
            <view>summary</view>
          </display>
        </element>
        <element name='modeling' title='Modelling'>
          <display class='FolderWdg'>
            <view>modeling</view>
          </display>
        </element>
      </definition>
    </config>

Both the summary and modeling elements are defined in this special
"definition" view"

Since all of the folders at all levels cascade to look at the
"definition" view, it is useful to always define defintions of elements
in the "definiton" view. This will allow a consistent definition for all
of the "views" in the project view.

The "summary" view is defined as a LinkWdg. This widget takes the
information defined in the options and then displays that class in the
main body of the TACTIC interface.

    widget = ViewPanelWdg( search_type='prod/asset', view='summary' )

As stated ealier, the ViewPanelWdg, combines a SearchWdg with a
TableLayoutWdg.

The second element defines a "modeling" folder. Whe a folder is click,
it will open up and display another list that is derived from the
"modeling" view.

**TableLayoutWdg**

This widget is the primary class used in TACTIC to lay out tabular data.
It makes heavy use of widget config to define what to display.

To display the rows and columns of the tabular layout, this widget makes
use of the following:

\\a) rows which are sobjects

\\b) columns which are widgets derived from BaseTableElementWdg.

The table layout widget is able to perform a search base on input
criteria. It is also able to receive sobjects through its set\_objects()
method.

This widget iterates through each of the sobjects per row.

For each column, the table draws the list of widgets provided by the
config. This config is typically defined in in the database in the
widget config table.

Two parameters are typcially used to find a particular widget config.

\\a) Search Type

\\b) View

**BaseTableElementWdg**

BaseTableElementWdg are extensively used in the UI. Each column in a
table you see in TACTIC derives from it. For examples of how to create
your own, please refer to the Widget Development section.
