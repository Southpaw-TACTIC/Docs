# update

**update(search\_key, data={}, metadata={}, parent\_key=None, info={}, use\_id=False, triggers=True)**

General update for updating sobject

**param:**

**search\_key** - a unique identifier key representing an sobject.

Note: this can also be an array, in which case, the data will

be updated to each sobject represented by this search key

**keyparam:**

**data** - a dictionary of name/value pairs which will be used to update

the sobject defined by the search\_key

Note: this can also be an array. Each data dictionary element in

the array will be applied to the corresponding search key

**parent\_key** - set the parent key for this sobject

**info** - a dictionary of info to pass to the ApiClientCmd

**metadata** - a dictionary of values that will be stored in the metadata attribute if available

**use\_id** - use id in the returned search key

**triggers** - boolean to fire trigger on update

**return:**

**dictionary** - represent the sobject with its current data.

If search\_key is an array, This will be an array of dictionaries
