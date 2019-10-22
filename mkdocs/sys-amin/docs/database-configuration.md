# TACTIC Database Configuration

By default TACTIC will look at localhost to the database. This is the
simplest implementation and most installations will have the database on
the same physical server as the TACTIC application servers. However, in
scaling up TACTIC, it may become necessary to separate the database
server from the TACTIC applications servers.

TACTIC can be configured to look at an external database by connecting
through sockets of TCP/IP. This can be set in the TACTIC configuration
file.

While it is possible to edit this file manually, it is often simpler to
use the provided utility found in:
&lt;TACTIC\_INSTALL\_DIR&gt;/src/bin/util/change\_db\_info.py

This command line script will ask a series of questions and update the
appropriate configuration file

**Usage:**

python change\_db\_info.py

When executing, the script will ask configuration questions and show a
default value in brackets. If the default is sufficient, merely press
enter without entering anything in will accept the default.

Below is a sample output where all the default values are accepted:

**TACTIC Database Configuration**

Please enter the database vendor (PostgreSQL or Oracle):

(PostgreSQL) →

Please enter database server hostname or IP address:

(localhost) →

Please enter user name accessing the database:

(postgres) →

Please enter database password:

(ENTER to keep password, '*EMPTY*' for empty password)

Enter Password →

Vendor: \[PostgreSQL\]

Server: \[localhost\]

User: \[postgres\]

Save to config (N/y) →

Once the values have been saved, a restart of TACTIC is required to
start using the new database configuration.




## Configure PostgreSQL


PostgreSQL is used as the database co-service in the following sample
configuration. PostgreSQL has only two configuration files that are
required to be examined in order to function with TACTIC; pg\_hba.conf
and postgresql.conf

### pg\_hba.conf

The pg\_hba.conf configuration file contains a list of users and hosts
with clearance levels. In the default pg\_hba.conf file that comes with
TACTIC, the network trust level is set for the most open access by the
localhost;

    # TYPE  DATABASE    USER        CIDR-ADDRESS          METHOD
    local      all  all  trust
    # IPv4 local connections:
    host    all         all         127.0.0.1/32          trust
    # IPv6 local connections:
    host    all         all         ::1/128               trust

In this example, all local connections to PostgreSQL are trusted. This
configuration matches the correct configuration required by a single
machine.

    host   all     all  <TACTIC_HOST_IP_ADDR>     trust

### postgresql.conf

The postgresql.conf configuration file has a setting that will allow the
PostgreSQL service to bind to the particular interface required.

Of concern is the "listen\_addresses" attribute.

    listen_addresses = 'localhost'

By default, the PostgreSQL service is only bound to the localhost. This
is fine for single machine operation of the TACTIC service.

    listen_addresses = '*'

This setting or specific IP addresses can be used if the DB service is
not on the same machine as the TACTIC service
