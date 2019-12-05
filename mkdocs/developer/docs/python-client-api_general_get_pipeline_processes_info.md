# get\_pipeline\_processes\_info

**get\_pipeline\_processes\_info(search\_key, recurse=False, related\_process=None)**

Retrieve the pipeline processes information of a specific sobject. It provides information from the perspective of a particular process if related\_process is specified.

**param:**

**search\_key** - a unique identifier key representing an sobject

**keyparams:**

**recurse** - boolean to control whether to display sub pipeline processes

**related\_process** - given a process, it shows the input and output processes and contexts

**return:**

**dictionary** - process names of the pipeline or a dictionary if related\_process is specified
