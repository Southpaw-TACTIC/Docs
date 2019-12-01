# log\_message

**log\_message(key, message, status=None, category="default")**

Log a message which will be seen by all who are subscribed to
the message "key". Messages are often JSON strings of data.

**params:**

**key** - unique key for this message

**message** - the message to be sent

**keyparam:**

**status** - arbitrary status for this message

**category** - value to categorize this message

**return:**

**string** - "OK"
