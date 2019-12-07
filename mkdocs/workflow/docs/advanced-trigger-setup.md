# Advanced Trigger Setup

Here are the examples of how to set up a Client Side Trigger.

Different types of database events cause the client trigger to be fired.

These include the following events: accept, update, lookahead.

**Example 1: Simple Javascript Alert**

1.  Open the Client Trigger view under: Admin Views → Project
    Essentials → \*Client\*Triggers

2.  Add the following new entry:

    <table>
    <colgroup>
    <col width="28%" />
    <col width="71%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><strong>Event</strong></th>
    <th>accept|my_project/my_sType</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Callback</strong></p></td>
    <td><p>my_script_folder/my_client_side_script</p></td>
    </tr>
    </tbody>
    </table>

3.  Open the Script Editor (keyboard short-cut is "9") and create the
    following entry:

    <table>
    <colgroup>
    <col width="28%" />
    <col width="71%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><strong>Script Path</strong></th>
    <th>my_script_folder/my_client_side_script</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><em>script type</em></p></td>
    <td><p>javascript</p></td>
    </tr>
    <tr class="even">
    <td><p><em>code</em></p></td>
    <td><p>log.critical(input)</p></td>
    </tr>
    </tbody>
    </table>

4.  Go to the view of the sType my\_project/my\_sType.

5.  Refresh the tab if the view is stale.

6.  Modify an entry and click off the field. The changed cell should
    turn green.

    Notice in the web browser Javascript console output, the contents of the
    input object is displayed. You can access useful information in there
    like search key by specifying "input.search\_key".

**Example 2: Refresh the row after it is saved**

1.  Open the Client Trigger view under: Admin Views → Project
    Essentials → \*Client\*Triggers

2.  Add the following new entry:

    <table>
    <colgroup>
    <col width="28%" />
    <col width="71%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><strong>Event</strong></th>
    <th>update|my_project/my_sType2</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Callback</strong></p></td>
    <td><p>my_script_folder/my_client_side_script2</p></td>
    </tr>
    </tbody>
    </table>

3.  Open the Script Editor (keyboard short-cut is "9") and create the
    following entry:

    <table>
    <colgroup>
    <col width="28%" />
    <col width="71%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><strong>Script Path</strong></th>
    <th>my_script_folder/my_client_side_script2</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><em>script type</em></p></td>
    <td><p>javascript</p></td>
    </tr>
    <tr class="even">
    <td><p><em>code</em></p></td>
    <td><p>(see code below)</p></td>
    </tr>
    </tbody>
    </table>

        log.critical(input);
        if (input.kwargs) {
            var search_key =
            input.kwargs.search_keys[0];
            var update_data = input.kwargs.update_data;
            var update_dict = eval(input.kwargs.update_data);
            var prev_description = update_dict[0]["description"];
            var server = TacticServerStub.get();
            //Append the word 'Hello' to the description.
            var data = {'description': prev_description + ' Hello'};
            server.update(search_key, data);
        }

4.  Go to the view of the sType my\_project/my\_sType2.

5.  Refresh the tab if the view is stale.

6.  Modify an entry’s description field. Try typing in "This is test"
    and save.

    Notice that after the entry is saved, and when you refresh the view, the
    description has the word "Hello" appended to it.

**Example 3: Automatically Put all Field Text into CAPS after Editing
(When Row Turns Green)**

1.  Open the Client Trigger view under: Admin Views → Project
    Essentials → \*Client\*Triggers

2.  Add the following new entry:

    <table>
    <colgroup>
    <col width="28%" />
    <col width="71%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><strong>Event</strong></th>
    <th>accept|my_project/my_sType3</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><strong>Callback</strong></p></td>
    <td><p>my_script_folder/my_client_side_script3</p></td>
    </tr>
    </tbody>
    </table>

3.  Open the Script Editor (keyboard short-cut is "9") and create the
    following entry:

    <table>
    <colgroup>
    <col width="28%" />
    <col width="71%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><strong>Script Path</strong></th>
    <th>my_script_folder/my_client_side_script3</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><em>script type</em></p></td>
    <td><p>javascript</p></td>
    </tr>
    <tr class="even">
    <td><p><em>code</em></p></td>
    <td><p>(see code below)</p></td>
    </tr>
    </tbody>
    </table>

        // Applies caps to Name column in my_sType3 sType
        try {
            var server = TacticServerStub.get();
            var column_name = input.element_name;
            // only affect Name column
            if (column_name == "name")
            { var column_data = input.new_value;
            column_data = column_data.toUpperCase();
            input.cell.setAttribute('spt_input_value', column_data);
            spt.table.set_display(input.cell, column_data, 'text'); }
        } catch( e ) {
            spt.alert(spt.exception.handler( e ));
        }

4.  Go to the view of the sType my\_project/my\_sType3.

5.  Refresh the tab if the view is stale.

6.  From the code example provided, modify an entry’s name field. Change
    the text in the name field to "Tester" and the row should turn green. Be
    sure to save the change.

    Notice that after the entry is saved, the text in the name field will
    now appear as "TESTER".

**Example 4: Look at Name Values in Table through a Lookahead and Pop Up
a Form with Details**

1.  Open the Client Trigger view under: Admin Views → Project
    Essentials → \*Client\*Triggers

2.  Add the following new entry:

    <table>
    <colgroup>
    <col width="28%" />
    <col width="71%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><strong>Event</strong></th>
    <th>lookahead</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p>my_project/my_sType4</p></td>
    <td><p><strong>Callback</strong></p></td>
    </tr>
    </tbody>
    </table>

3.  Open the Script Editor (keyboard short-cut is "9") and create the
    following entry:

    <table>
    <colgroup>
    <col width="28%" />
    <col width="71%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th><strong>Script Path</strong></th>
    <th>my_script_folder/my_client_side_script4</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><p><em>script type</em></p></td>
    <td><p>javascript</p></td>
    </tr>
    <tr class="even">
    <td><p><em>code</em></p></td>
    <td><p>(see code below)</p></td>
    </tr>
    </tbody>
    </table>

    > **Note**
    >
    > The code below is an example written to look for names of people
    > in an sType table and pop up a form with details about the person. The
    > details form would be created in the Custom Layout Editor. In the
    > example, the view is called my\_project.name\_detail.popup. Ensure that
    > all values that should be displayed as part of the details in the form
    > are also pulled from the sType table i.e. age.

        try{
            server = TacticServerStub.get();
            var class_name = 'tactic.ui.panel.CustomLayoutWdg';
            var search_type = 'my_project/my_sType4';
            var name = input.display;
            var name_id =input.value;
            if (!name) input.value = null;
            var form_table = input.firing_element.getParent(".spt_form_table");
            var last_input_name = form_table.getElement('.spt_last_input_name');
            var last_names = last_input_name.value.split('||');
            // Check if the current name input is what was typed in last
            var reused_name = false;
            // Check if the current name is unknown in my_sType4 table
            var unknown_name = false;
            if (last_names.length == 2)
            {
                reused_name = last_names[0] == name;
                unknown_name = (last_names[1] == name_id ) && (last_names[0] != name);
            }
            if (!name || name_id == '' || name_id === null || reused_name || unknown_name)
            { }
            else {
                var kwargs = { 'view': 'my_project.name_detail.popup',
                'name_id': name_id };
                // Load the popup
                var pop = spt.panel.load_popup("Name Details", class_name, kwargs);
                last_input_name.value = name + '||' + name_id;
                pop.activator = form_table;
            }
        }
        catch( e )  {
            spt.alert(spt.exception.handler( e ));
        }

4.  In order to have a lookahead that will look at the my\_sType4 table,
    a lookahead must be built within a custom view i.e.
    my\_views/lookahead\_form in the Custom Layout Editor (this will be a
    different view from the aforementioned name details form). An example of
    the code required to create this view is shown below.

    *HTML Tab in Custom Layout Editor for New View*

        <div>
        <div>
        <% name_key = kwargs.get("search_key") or "" %>
        </div> <table> <tr> <td>Name</td> <td>
        <element name="name">
            <display class="tactic.ui.input.LookAheadTextInputWdg">
                <search_type>my_project/my_sType4</search_type> <column>name</column>
                <search_key>${name_key}</search_key>
                <filter_search_type>metadata/Title</filter_search_type>
                <value_column>id</value_column>
                <current_value_column>id</current_value_column>
            </display>
        </element>
        </td> </tr>
        </table>
        </div>

5.  Go to the my\_views/lookahead\_form in Custom Layout Editor and click
    on the "Test" button to test the fucntionality of the view. The view can
    also be added to the sidebar.

6.  In the view, begin typing a name. A list of different name values
    from the my\_sType4 table should appear in a drop down from the lookahead.

7.  Clicking on one of the values in the drop down of the lookahead will
    then pop up the my\_project.name\_detail.popup with all of the values from
    the external system.


