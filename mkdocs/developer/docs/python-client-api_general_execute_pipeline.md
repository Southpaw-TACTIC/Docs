# execute\_pipeline

**execute\_pipeline(pipeline\_xml, package)**

Spawn an execution of a pipeline as delivered from
'get\_pipeline\_xml()'. The pipeline is a xml document that describes
a set of processes and their handlers

**param:**

**pipeline\_xml** - an xml document describing a standard Tactic pipeline.

**package** - a dictionary of data delivered to the handlers

**return:**

**instance** - a reference to the interpreter
