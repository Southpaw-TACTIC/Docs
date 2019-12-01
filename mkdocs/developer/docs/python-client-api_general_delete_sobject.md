# delete\_sobject

**delete\_sobject(search\_key, include\_dependencies=False)**

Invoke the delete method. Note: this function may fail due
to dependencies. Tactic will not cascade delete. This function
should be used with extreme caution because, if successful, it will
permanently remove the existence of an sobject

**param:**

**search\_key** - a unique identifier key representing an sobject.

Note: this can also be an array.

**keyparam:**

**include\_dependencies** - True/False

**return:**

**dictionary** - a sobject that represents values of the sobject in the

form name:value pairs
