
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
