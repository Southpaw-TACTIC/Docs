# add\_config\_element

**add\_config\_element(search\_type, view, name, class\_name=None, display\_options={}, action\_class\_name=None, action\_options={}, element\_attrs={},login=None, unique=True, auto\_unique\_name=False, auto\_unique\_view=False)**

This method adds an element into a config. It is used by various
UI components to add new widget element to a particular view.

**param:**

**search\_type** - the search type that this config belongs to

**view** - the specific view of the search type

**name** - the name of the element

**keyparam:**

**class\_name** - the fully qualified class of the display

**action\_class\_name** - the fully qualified class of the action

**display\_options** - keyward options in a dictionary to construct the specific display

**action\_options** - keyward options in a dictionary to construct the specific action

**element\_attrs** - element attributes in a dictionary

**login** - login name if it is for a specific user

**unique** - add an unique element if True. update the element if False.

**auto\_unique\_name** - auto generate a unique element and display view name

**auto\_unique\_view** - auto generate a unique display view name

**return:**

**boolean** - True

**example:**

This will add a new element to the "character" view for a 3D asset

            search_type = 'prod/asset'

            view = 'characters'

            class_name = 'tactic.ui.common.SimpleElementWdg'

            server.add_config_element(search_type, view, class_name)

This will add a new element named "user" to the "definition" view. It contains detailed display and action nodes

            data_dict = {} # some data here

            search_type = 'prod/asset'

            server.add_config_element(search_type, 'definition', 'user',  class_name = data_dict['class_name'], display_options=data_dict['display_options'], element_attrs=data_dict['element_attrs'], unique=True, action_class_name=data_dict['action_class_name'], action_options=data_dict['action_options'])
