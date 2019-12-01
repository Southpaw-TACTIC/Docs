# Custom URL Configuration

TACTIC’s Custom Layout Editor provides users with the ability to
completely customize the end user inteface. The HTML, Python, Styles,
and Behaviours tabs offer the flexibility to dictate the appearance,
functionality and actions of generated views. However, there are times
where the appearance, functionality and actions need to be dynamic,
changing depending on different events or conditions.

Custom URL Configuration encompasses these possibilities by offering the
availability of variable options. Views can be modified by options that
are set statically by the user and change dynamically with the system.
These options can be inserted into code developed to define a view to
perform a desired behaviour.

The Custom URL can be configured through Project Essentials under Custom
URL. Entries can be added into the table with a specified URL path,
pointing to a Custom Layout view to be modified, for example, and the
associated HTML code under the Widget column to define the view.

![image](media/Custom%20URL.png)

A list of options are available to the user to set within the HTML that
defines a view from the Widget column. These options and associated
descriptions and values are provided below. The first three options
refer to the visibility and usability of the respective user interface
element (sidebar, index and admin) when the Custom Layout component is
drawn. The palette option establishes the overall color of these
respective user interface elements.

<table>
<colgroup>
<col width="15%" />
<col width="64%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option</strong></th>
<th><strong>Description</strong></th>
<th><strong>Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>sidebar</p></td>
<td><p>Determines whether the sidebar, as seen in the administrative layer, is available in the view.</p></td>
<td><p>true/false</p></td>
</tr>
<tr class="even">
<td><p>index</p></td>
<td><p>Determines whether the element will be displayed with the theming and configuration set up from the index URL. If set to &quot;true&quot;, it will only work if there is an entry with a URL as &quot;/index&quot; in the Custom URL table.</p></td>
<td><p>true/false</p></td>
</tr>
<tr class="odd">
<td><p>admin</p></td>
<td><p>Determines whether the element will be displayed with the theming and configuration of the administrative layer.</p></td>
<td><p>true/false</p></td>
</tr>
<tr class="even">
<td><p>palette</p></td>
<td><p>Determines the overall color theme of all of the tables and associated menus in the view.</p></td>
<td><p>aqua/aviator/bon noche/bright/dark/ silver/origami</p></td>
</tr>
</tbody>
</table>

Two examples are shown to demonstrate how to statically set these
options to configure a URL, as well as how to specify a view as the home
or landing page of a TACTIC project.

*Example 1: HTML Element Options*

The example below is taking a specific view for a job established by the
URL /job/JOB002 and setting the admin, sidebar and palette options
inline with the definition of the element tag. Notice that the URL
defined is only a portion of a full URL. The full URL would follow a
format of *[http://&lt;IP&gt;/tactic/jobs/job/JOB002](http://<IP>/tactic/jobs/job/JOB002)*. Only the latter portion
of the URL is required.

*URL Column*

    /job/JOB002

*Widget Column*

    <?xml version="1.0"?> <element admin='true' sidebar='false'
    palette='bright'> <display class='tactic.ui.panel.CustomLayoutWdg'>
    <search_type>my_project/my_sType</search_type> <view>my_view</view>
    </display> </element>

*Example 2: Setting Home Page through URL*

The user can set a custom view created in the Custom Layout Editor as
the home or landing page when the user and all other users sign in. The
HTML set in the Widget column can point to a specific view in the Custom
Layout Editor to set as the home page. In this case, the display class
would need to be defined as a Custom Layout Widget to accommodate for
the use of a Custom Layout view.

Notice how the URL is set as "/index", which differs from the Custom
Layout view in the HTML. The URL must be set as "/index" in order to
have this view set as the home page.

*URL Column*

    /index

*Widget Column*

    <element name='index'> <display class='tactic.ui.panel.CustomLayoutWdg'>
    <view>custom_layout_folder/my_custom_view</view> </display> </element>

**Dynamically Setting Options**

The following examples will demonstrate how to dynamically set options.
The first example will demonstrate how to configure multiple views using
a dynamic URL following from Example 1 in the Statically Setting Options
section. The second example will follow from the second example under
the Statically Setting Options section. The Custom Layout view set as
the home page will actually utilize mako with HTML in order to set the
value of a variable to be used in the HTML. This variable is used to set
the display class of the element.

*Example 1: Configuring Multiple Views through a Dynamic URL*

In Example 1 from the Statically Setting Options section, the view being
modified was for a specific job. In this example, you can see that the
same modifications can be applied to the views for all jobs. The \\{…​}
syntax allows for a variable value. In this case, the "code" variable
can change. The job "code" defines the jobs in the project through an
alphanumeric sequence, such as "JOB002". This variable syntax allows the
URL to keep changing for all the jobs present in the project. This means
that different jobs can appear in the same view as it will have the same
HTML definition.

Notice how the display class is changed to a Table Layout as opposed to
a Custom Layout Widget. This is just to demonstrate the different
display classes available to the user as well.

*URL Column*

    /job/\{code}

*Widget Column*

    <?xml version="1.0"?> <element admin='true' sidebar='false'
    palette='bright'> <display class='tactic.ui.panel.TableLayoutWdg'>
    <search_type>my_project/my_sType</search_type> <view>my_view</view>
    </display> </element>

*Example 2: Custom Layout Editor - Setting Element Display Class in HTML
with Changing Mako Variable Value*

The focus on this example will be the utilization of Mako and HTML in
the Custom Layout Editor for the view defined in Example 1 of the
Statically Setting Options section. The code from Example 1 of the
Statically Setting Options section is shown again here for reference.

The Mako code is set up to determine whether a search key is existent in
TACTIC. What this means is TACTIC is aware if an entry with a specific
ID already exists in the sType table. This code is utilizing that
ability and checking whether that entry does already exist. The entry’s
existence determines what the display\_widget variable will be set to.

In the HTML for the "last\_name" element, the display class is variable
as indicative of the syntax "$\\{…​}", which wraps the variable
display\_widget. Based on the existence of the search key, the display
class of the "last\_name" element will be either a text input widget or a
lookahead text input widget.

*URL Column*

    /index

*Widget Column*

    <element name='index'> <display class='tactic.ui.panel.CustomLayoutWdg'>
    <view>custom_layout_folder/my_custom_view</view> </display> </element>

*HTML Tab in Custom Layout Editor for
custom\_layout\_folder/my\_custom\_view View*

    <div>
        <div>
        <%
            sType2_key = kwargs.get("search_key") or ""
            if sType2_key:
                display_widget = "tactic.ui.input.TextInputWdg"
            else:
                display_widget = "tactic.ui.input.LookAheadTextInputWdg"
        %>
        </div>
    <table>
      <tr>
         <td>Last Name</td>
         <td class="spt_element">
           <element name="last_name">
             <display class="$\{display_widget}">
             <search_type>my_project/my_sType</search_type>
             <column>my_view2</column>
             <search_key>$\{sType2_key}</search_key>
             <filter_search_type>my_project/my_sType</filter_search_type>
             <value_column>id</value_column>
             <current_value_column>id</current_value_column>
             </display>
           </element>
         </td>
        </tr>
    </div>
