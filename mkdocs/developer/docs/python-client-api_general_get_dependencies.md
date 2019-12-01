# get\_dependencies

**get\_dependencies(snapshot\_code, mode='explicit', tag='main', include\_paths=False, include\_paths\_dict=False, include\_files=False, repo\_mode='client\_repo', show\_retired=False):**

Return the dependent snapshots of a certain tag

**params:**

**snapshot\_code** - unique code of a snapshot

**keyparams:**

**mode** - explict (get version as defined in snapshot)

-   latest

-   current

**tag** - retrieve only dependencies that have this named tag

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

a list of snapshots
