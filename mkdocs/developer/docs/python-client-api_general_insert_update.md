# insert\_update

**insert\_update(search\_key, data, metadata={}, parent\_key=None, info={}, use\_id=False, triggers=True)**

Insert if the entry does not exist, update otherwise

**param:**

**search\_key** - a unique identifier key representing an sobject.

**data** - a dictionary of name/value pairs which will be used to update

the sobject defined by the search\_key

**keyparam:**

**metadata** - a dictionary of values that will be stored in the metadata attribute if available

**parent\_key** - set the parent key for this sobject

**info** - a dictionary of info to pass to the ApiClientCmd

**use\_id** - use id in the returned search key

**triggers** - boolean to fire trigger on insert

**return:**

**dictionary** - represent the sobject with its current data.
