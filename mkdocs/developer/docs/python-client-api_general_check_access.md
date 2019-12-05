# check\_access

**check\_access(access\_group, key, access, value, is\_match, default="edit")**

check the access for a specified access\_group name like search\_type, sobject, project, or builtin.
It can also be custom-defined.

**param:**

**access\_group** - it can be custom-defined or predefined like search\_type, sobject, project, or builtin

**key** - usually in a dictionary or list of dictionary that maps to the parameters in the xml access rule

**access** - allow, delete, retire, insert, edit, view, deny

**keyparam:**

**value** - an extra modifier to the key. Rarely used.

**is\_match** - boolean to specify whether you want to match exactly the access string as defined in access\_rules.

The default is to return True if the specified access is equal or lower than the one defined.

**default** - default access like allow or view can be specified. The default access is "edit"

**return:**

**boolean** - True or False

**example:**

# check if one is allowed to view the project called workflow1

server.check\_access('project', \[{'code','workflow1'},{'code','\*}\], 'allow')

# check if one has retire\_delete access

access\_key1 = {

'key': 'retire\_delete',

'project': project\_code

}

access\_key2 = {

'key': 'retire\_delete'

}

access\_keys = \[access\_key1, access\_key2\]

server.check\_access('builtin', access\_keys, 'allow')
