# add\_initial\_tasks

**add\_initial\_tasks(search\_key, pipeline\_code=None, processes=\[\], skip\_duplicate=True, offset=0)**

Add initial tasks to an sobject

**param:**

**search\_key** - the key identifying a type of sobject as registered in

the search\_type table.

**keyparam:**

**pipeline\_code** - override the sobject’s pipeline and use this one instead

**processes** - create tasks for the given list of processes

**skip\_duplicate** - boolean to skip duplicated task

**offset** - a number to offset the start date from today’s date

**return:**

**list** - tasks created
