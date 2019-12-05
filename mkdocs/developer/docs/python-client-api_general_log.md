# log

**log(level, message, category="default")**

Log a message in the logging queue. It is often difficult to see output
of a trigger unless you are running the server in debug mode.
In production mode, the server sends the output to log files.
The log files are general buffered.
It cannot be predicted exactly when buffered output will be dumped to a file.

This log() method will make a request to the server.
The message will be immediately stored in the database in the debug log table.

**param:**

**level - critical|error|warning|info|debug** - arbitrary debug level category

**message** - freeform string describing the entry

**keyparam:**

**category** - a label for the type of message being logged.

It defaults to "default"
