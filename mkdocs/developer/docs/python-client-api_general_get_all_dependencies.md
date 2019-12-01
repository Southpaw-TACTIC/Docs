# get\_all\_dependencies

**get\_all\_dependencies(snapshot\_code, mode='explicit', type='ref', include\_paths=False, include\_paths\_dict=False, include\_files=False, repo\_mode='client\_repo', show\_retired=False):**

Retrieve the latest dependent snapshots of the given snapshot

**param:**

**snapshot\_code** - the unique code of the snapshot

**keyparam:**

**mode** - explicit (get version as defined in snapshot)

-   latest

-   current

**type** - one of ref or input\_ref

**include\_paths** - flag to specify whether to include a *paths* property

containing all of the paths in the dependent snapshots

**include\_paths\_dict** - flag to specify whether to include a

*paths\_dict* property containing a dict of all paths in the

dependent snapshots

**include\_files** - includes all of the file objects referenced in the

snapshots

**repo\_mode** - client\_repo, web, lib, relative

**show\_retired** - defaults to False so that it doesn’t show retired dependencies

**return:**

**list** - snapshots
