# add\_dependency

**add\_dependency(snapshot\_code, file\_path, type='ref')**

Append a dependency referent to an existing check-in.
All files are uniquely containe by a particular snapshot. Presently,
this method does a reverse lookup by file name. This assumes that
the filename is unique within the system, so it is not recommended
unless it is known that naming conventions will produce unique
file names for every this particular file. If this is not the
case, it is recommended that add\_dependency\_by\_code() is used.

**param:**

**snapshot\_code** - the unique code identifier of a snapshot

**file\_path** - the path of the dependent file. This function is able

reverse map the file\_path to the appropriate snapshot

**keyparam:**

**type** - type of dependency. Values include 'ref' and 'input\_ref'

ref = hierarchical reference: ie A contains B

input\_ref = input reference: ie: A was used to create B

**tag** - a tagged keyword can be added to a dependency to categorize

the different dependencies that exist in a snapshot

**return:**

**dictionary** - the resulting snapshot
