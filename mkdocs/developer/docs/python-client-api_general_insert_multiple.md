# insert\_multiple

**insert\_multiple(data, metadata=\[\], parent\_key=None, use\_id=False, triggers=True)**

Insert for several sobjects in one function call. The
data structure contains all the infon needed to update and is
formated as follows:

data = \[
{ column1: value1, column2: value2, column3: value3 },
{ column1: value1, column2: value2, column3: value3 }
}

metadata = \[
{ color: blue, height: 180 },
{ color: orange, height: 170 }
\]

**params:**

**search\_type** - the search\_type attribute of the sType

**data** - a dictionary of name/value pairs which will be used to update

the sobject defined by the search\_key

Note: this can also be an array. Each data dictionary element in

the array will be applied to the corresponding search key

**keyparam:**

**parent\_key** - set the parent key for this sobject

**use\_id** - boolean to control if id is used in the search\_key in returning sobject dict

**triggers** - boolean to fire trigger on insert

**return:**

a list of all the inserted sobjects
