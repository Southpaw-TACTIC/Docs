# group\_checkin

**group\_checkin(search\_key, context, file\_path, file\_range, snapshot\_type="sequence", description="", file\_type='main', metadata={}, mode=None, is\_revision=False, info={} )**

Check in a range of files. A range of file is defined as any group
of files that have some sequence of numbers grouping them together.
An example of this includes a range frames that are rendered.

Although it is possible to add each frame in a range using add\_file,
adding them as as sequence is lightweight, often significantly reducing
the number of database entries required. Also, it is understood that
test files form a range of related files, so that other optimizations
and manipulations can be operated on these files accordingly.

**param:**

**search\_key** - a unique identifier key representing an sobject

**file\_path** - expression for file range: ./blah.*\#*\#.jpg

**file\_type** - the typ of file this is checked in as. Default = 'main'

**file\_range** - string describing range of frames in the form '1-5/1'

**keyparam:**

**snapshot\_type** - type of snapshot this checkin will have

**description** - description related to this checkin

**file\_type** - the type of file that will be associated with this group

**metadata** - add metadata to snapshot

**mode** - determines whether the files passed in should be copied, moved

or uploaded. By default, this is a manual process (for backwards

compatibility)

**is\_revision** - flag to set this as a revision instead of a version

**info** - dict of info to pass to the ApiClientCmd

**return:**

**dictionary** - snapshot
