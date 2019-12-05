# Validation Set-up

To limit what a user can enter in a field, you can set up validation for
the column. It is particularly useful when the user is required to type
in a text field instead of a selection list. This works on the client
side so it activates before you click on the save button.

Example 1: Ensure the field description of prod/shot starts with the
word "Client"

In the edit view of prod/shot, make sure there is an element for
description defined with these display options:

        <element name='description'>
           <display class='TextWdg'>
               <validation_js>return value.test(/^Client/)</validation_js>
               <validation_warning>It needs to start with Client</validation_warning>
           </display>
        </element>

If the person types in something, press Enter and it fails the
validation, the text field will turn red. You can view the warning
message when the mouse pointer is over the text field. The variable
'value' is assumed to be value the user types in.

Example 2: Ensure the field description of prod/shot contains the code
in the same row. The assumption is that the user would pick a show code
in the previous column before typing in a description.

In the edit view prod/shot, make sure there is an element for
description defined with these display options:

        <element name='description'>
           <display class='TextWdg'>
               <validation_script>validate_desc</validation_script>
               <validation_warning>It needs to contain the shot code</validation_warning>
           </display>
        </element>

The script it refers to is a javacript saved in the Script Editor. It
has a code equal to 'validate\_desc'.

            // value, display_target_el, and bvr are assumed variables
            var row = display_target_el.getParent('.spt_table_tr');
            var td = row.getElement('td[spt_element_name=shot_code]');
            var shot_code = td.getAttribute('spt_input_value');
            var exp = new RegExp(shot_code);
            if (!shot_code) {
                return false;
            }
            if (value.test(exp)) {
                return true;
            }
            else {
                return false;
            }

Like 'value', 'display\_target\_el' and 'bvr' are assumed variables.. The
former represents the html element holding the value whereas the latter
is the behavior object.
