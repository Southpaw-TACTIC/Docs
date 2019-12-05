# directory\_checkin

**directory\_checkin(search\_key, context, dir, snapshot\_type="directory", description="No description", file\_type='main', is\_current=True, level\_key=None, metadata={}, mode="copy", is\_revision=False, checkin\_type="strict")**

Check in a directory of files. This informs TACTIC to treat the
entire directory as single entity without regard to the structure
of the contents. TACTIC will not know about the individual files
and the directory hierarchy within the base directory and it it left
up to the and external program to intepret and understand this.

This is often used when logic on the exact file structure exists in
some external source outside of TACTIC and it is deemed too complicated
to map this into TACTIC’s snapshot definition.

**param:**

**search\_key** - a unique identifier key representing an sobject

**dir** - the directory that needs to be checked in

**keyparam:**

**snapshot\_type** - type of snapshot this checkin will have

**description** - description related to this checkin

**file\_type** - the type of file that will be associated with this group

**is\_current** - makes this snapshot current

**level\_key** - the search key of the level if used

**metadata** - add metadata to snapshot

**mode** - determines whether the files passed in should be copied, moved

or uploaded. By default, this is 'copy'

**is\_revision** - flag to set this as a revision instead of a version

**checkin\_type** - auto or strict which controls whether to auto create versionless

**return:**

**dictionary** - snapshot
