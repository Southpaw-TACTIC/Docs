# get\_snapshot

**get\_snapshot(search\_key, context="publish", version='-1', level\_key=None, include\_paths=False, include\_full\_xml=False, include\_paths\_dict=False, include\_files=False, include\_web\_paths\_dict=False, versionless=False)**

Method to retrieve an sobject’s snapshot
Retrieve the latest snapshot

**param:**

**search\_key** - unique identifier of sobject whose snapshot we are

looking for

**keyparam:**

**process** - the process of the snapshot

**context** - the context of the snapshot

**version** - snapshot version

**revision** - snapshot revision

**level\_key** - the unique identifier of the level in the form of a search key

**include\_paths** - flag to include a list of paths to the files in this

snapshot.

**include\_full\_xml** - whether to include full xml in the return

**include\_paths\_dict** - flag to specify whether to include a

*paths\_dict* property containing a dict of all paths in the

dependent snapshots

**include\_web\_paths\_dict** - flag to specify whether to include a

*web\_paths\_dict* property containing a dict of all web paths in

the returned snapshots

**include\_files** - includes all of the file objects referenced in the

snapshots

**versionless** - boolean to return the versionless snapshot, which takes a version of -1 (latest) or 0 (current)

**return:**

**dictionary** - the resulting snapshot

**example:**

                search_key = 'prod/asset?project=sample3d&code=chr001'

                snapshot = server.get_snapshot(search_key, context='icon', include_files=True)

                # get the versionless snapshot

                search_key = 'prod/asset?project=sample3d&code=chr001'

                snapshot = server.get_snapshot(search_key, context='anim', include_paths_dict=True, versionless=True)
