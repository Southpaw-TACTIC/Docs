# add\_dependency\_by\_code

**add\_dependency\_by\_code(to\_snapshot\_code, from\_snapshot\_code, type='ref')**

Append a dependency reference to an existing checkin. This dependency
is used to connect various checkins together creating a separate
dependency tree for each checkin.

**param:**

to\_snapshot\_code: the snapshot code which the dependency will be

connected to

from\_snapshot\_code: the snapshot code which the dependency will be

connected from

**type** - type of dependency. Values include 'ref' and 'input\_ref'

ref = hierarchical reference: ie A contains B

**input\_ref** - input reference: ie: A was used to create B

**tag** - a tagged keyword can be added to a dependency to categorize

the different dependencies that exist in a snapshot

**return:**

**dictionary** - the resulting snapshot
