# get\_paths

**get\_paths( search\_key, context="publish", version=-1, file\_type='main', level\_key=None, single=False, versionless=False)**

Get paths from an sobject

**params:**

**search\_key** - a unique identifier key representing an sobject

**keyparams:**

**context** - context of the snapshot

**version** - version of the snapshot

**file\_type** - file type defined for the file node in the snapshot

**level\_key** - the unique identifier of the level that this

was checked into

**single** - If set to True, the first of each path set is returned

**versionless** - boolean to return the versionless snapshot, which takes a version of -1 (latest) or 0 (current)

**process** - the process of the snapshot

**return**

A dictionary of lists representing various paths. The paths returned

are as follows:

-   client\_lib\_paths: all the paths to the repository relative to the client

-   lib\_paths: all the paths to the repository relative to the server

-   sandbox\_paths: all of the paths mapped to the sandbox

-   web: all of the paths relative to the http server


