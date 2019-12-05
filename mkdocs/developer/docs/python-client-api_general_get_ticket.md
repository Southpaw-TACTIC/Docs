# get\_ticket

**get\_ticket(login, password, site=None)**

Get an authentication ticket based on a login and password.
This function first authenticates the user and the issues a ticket.
The returned ticket is used on subsequent calls to the client api

**param:**

**login** - the user that is used for authentications

**password** - the password of that user

**keyparam:**

**site** - name of the site used in a portal setup

**return:**

**string** - ticket key
