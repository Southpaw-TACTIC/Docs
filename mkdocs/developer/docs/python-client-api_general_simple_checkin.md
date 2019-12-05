# simple\_checkin

**simple\_checkin( search\_key, context, file\_path, snapshot\_type="file", description="No description", use\_handoff\_dir=False, file\_type="main", is\_current=True, level\_key=None, breadcrumb=False, metadata={}, mode=None, is\_revision=False, info={}, keep\_file\_name=False, create\_icon=True, checkin\_cls='pyasm.checkin.FileCheckin', context\_index\_padding=None, checkin\_type="strict", source\_path=None, version=None )**

Simple method that checks in a file.

**param:**

**search\_key** - a unique identifier key representing an sobject

**context** - the context of the checkin

**file\_path** - path of the file that was previously uploaded

**keyparam:**

**snapshot\_type** - \[optional\] descibes what kind of a snapshot this is.

More information about a snapshot type can be found in the

prod/snapshot\_type sobject

**description** - \[optional\] optional description for this checkin

**file\_type** - \[optional\] optional description for this file\_type

**is\_current** - flag to determine if this checkin is to be set as current

**level\_key** - the unique identifier of the level that this

is to be checked into

**breadcrumb** - flag to leave a .snapshot breadcrumb file containing

information about what happened to a checked in file

**metadata** - a dictionary of values that will be stored as metadata

on the snapshot

**mode** - inplace, upload, copy, move

**is\_revision** - flag to set this as a revision instead of a version

**create\_icon** - flag to create an icon on checkin

**info** - dict of info to pass to the ApiClientCmd

**keep\_file\_name** - keep the original file name

**checkin\_cls** - checkin class

**context\_index\_padding** - determines the padding used for context

indexing: ie: design/0001

**checkin\_type** - auto or strict which controls whether to auto create versionless

**source\_path** - explicitly give the source path

**version** - force a version for this check-in

**return:**

**dictionary** - representation of the snapshot created for this checkin
