# query\_snapshots

**query\_snapshots(filters=None, columns=None, order\_bys=\[\], show\_retired=False, limit=None, offset=None, single=False, include\_paths=False, include\_full\_xml=False, include\_paths\_dict=False, include\_parent=False, include\_files=False, include\_web\_paths=False)**

thin wrapper around query, but is specific to querying snapshots
with some useful included flags that are specific to snapshots

**params:**

**ticket** - authentication ticket

**filters** - (optional) an array of filters to alter the search

**columns** - (optional) an array of columns whose values should be

retrieved

**order\_bys** - (optional) an array of order\_by to alter the search

**show\_retired - (optional)** - sets whether retired sobjects are also

returned

**limit** - sets the maximum number of results returned

**single** - returns a single sobject that is not wrapped up in an array

**include\_paths** - flag to specify whether to include a *paths* property

containing a list of all paths in the dependent snapshots

**include\_paths\_dict** - flag to specify whether to include a

*paths\_dict* property containing a dict of all paths in the

dependent snapshots

**include\_web\_paths\_dict** - flag to specify whether to include a

*web\_paths\_dict* property containing a dict of all web paths in

the returned snapshots

**include\_full\_xml** - flag to return the full xml definition of a snapshot

**include\_parent** - includes all of the parent attributes in a *parent* dictionary

**include\_files** - includes all of the file objects referenced in the

snapshots

**return:**

list of snapshots
