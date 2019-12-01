# get\_unique\_sobject

**get\_unique\_sobject(search\_type, data={})**

This is a special convenience function which will query for an
sobject and if it doesn’t exist, create it. It assumes that this
object should exist and spares the developer the logic of having to
query for the sobject, test if it doesn’t exist and then create it.

**param:**

**search\_type** - the type of the sobject

**data** - a dictionary of name/value pairs that uniquely identify this

sobject

**return:**

**sobject** - unique sobject matching the critieria in data
