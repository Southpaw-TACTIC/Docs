# get\_resource\_path

**get\_resource\_path(login=None)**

Get the resource path of the current user. It differs from
create\_resource\_paths() which actually create dir. The resource path
identifies the location of the file which is used to cache connection information.
An exmple of the contents is shown below:

            login=admin

            server=localhost

            ticket=30818057bf561429f97af59243e6ef21

            project=unittest

            site=vfx_site

The contents in the resource file represent the defaults to use
when connection to the TACTIC server, but may be overriden by the
API methods: set\_ticket(), set\_server(), set\_project() or the
environment variables: TACTIC\_TICKET, TACTIC\_SERVER, and TACTIC\_PROJECT

Typically this method is not explicitly called by API developers and
is used automatically by the API server stub. It attempts to get from
home dir first and then from temp\_dir is it fails.

The site key is optional and used for a portal setup.

**param:**

**login (optional)** - login code. If not provided, it gets the current system user

**return:**

**string** - resource file path
