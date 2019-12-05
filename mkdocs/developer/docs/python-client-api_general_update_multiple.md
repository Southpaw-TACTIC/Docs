# update\_multiple

**update\_multiple(data, triggers=True)**

Update for several sobjects with different data in one function call. The
data structure contains all the information needed to update and is
formated as follows:

data = {
search\_key1: { column1: value1, column2: value2 }
search\_key2: { column1: value1, column2: value2 }
}

**params:**

**data** - data structure containing update information for all

sobjects

**keyparam:**

**data** - a dictionary of name/value pairs which will be used to update

the sobject defined by the search\_key

Note: this can also be an array. Each data dictionary element in

the array will be applied to the corresponding search key

**triggers** - boolean to fire trigger on insert

**return:**

None
