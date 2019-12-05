# get\_widget

**get\_widget(class\_name, args={}, values={})**

Get a defined widget

**params:**

**class\_name** - the fully qualified class name of the widget

**keyparams:**

**args** - keyword arguments required to create a specific widget

**values** - form values that are passed in from the interface

**return:**

**string** - html form of the widget

**example:**

class\_name = 'tactic.ui.panel.TableLayoutWdg'

args = {

'view': 'task\_list',

'search\_type': 'sthpw/task',

}

filter = \[{"prefix":"main\_body","main\_body\_enabled":"on","main\_body\_column":"project\_code","main\_body\_relation":"is","main\_body\_value":"{$PROJECT}"}, {"prefix":"main\_body","main\_body\_enabled":"on","main\_body\_column":"search\_type","main\_body\_relation":"is not","main\_body\_value":"sthpw/project"}\]

from simplejson import dumps

values = {'json': dumps(filter)}

widget\_html = server.get\_widget(class\_name, args, values)
