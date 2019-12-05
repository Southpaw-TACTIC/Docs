# create\_snapshot

**create\_snapshot(search\_key, context, snapshot\_type="file", description="No description", is\_current=True, level\_key=None, is\_revision=False, triggers=True )**

Create an empty snapshot

**param:**

**search\_key** - a unique identifier key representing an sobject

**context** - the context of the checkin

**keyparam:**

**snapshot\_type** - \[optional\] descibes what kind of a snapshot this is.

More information about a snapshot type can be found in the

prod/snapshot\_type sobject

**description** - \[optional\] optional description for this checkin

**is\_current** - flag to determine if this checkin is to be set as current

**is\_revision** - flag to set this as a revision instead of a version

**level\_key** - the unique identifier of the level that this

is to be checked into

**triggers** - boolean to fire triggers on insert

**return:**

**dictionary** - representation of the snapshot created for this checkin
