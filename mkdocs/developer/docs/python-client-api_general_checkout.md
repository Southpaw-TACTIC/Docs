# checkout

**checkout(search\_key, context, version=-1, file\_type='main', dir='', level\_key=None, to\_sandbox\_dir=False, mode='copy')**

Check out files defined in a snapshot from the repository. This
will copy files to a particular directory so that a user can work
on them.

**param:**

**search\_key** - a unique identifier key representing an sobject

**context** - context of the snapshot

**keyparam:**

**version** - version of the snapshot

**file\_type** - file type defaults to 'main'. If set to '\*', all paths are checked out

**level\_key** - the unique identifier of the level in the form of a search key

**to\_dir** - destination directory defaults to '.'

**to\_sandbox\_dir** - (True|False) destination directory defaults to

sandbox\_dir (overrides "to\_dir" arg)

**mode - (copy|download)** - determines the protocol that will be used

to copy the files to the destination location

**return:**

**list** - a list of paths that were checked out
