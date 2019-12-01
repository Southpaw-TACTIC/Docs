# create\_task

**create\_task(search\_key, process="publish", subcontext=None, description=None, bid\_start\_date=None, bid\_end\_date=None, bid\_duration=None, assigned=None)**

Create a task for a particular sobject

**param:**

**search\_key** - the key identifying a type of sobject as registered in

the search\_type table.

**keyparam:**

**process** - process that this task belongs to

**subcontext** - the subcontext of the process (context = procsss/subcontext)

**description** - detailed description of the task

**bid\_start\_date** - the expected start date for this task

**bid\_end\_date** - the expected end date for this task

**bid\_duration** - the expected duration for this task

**assigned** - the user assigned to this task

**return:**

**dictionary** - task created
