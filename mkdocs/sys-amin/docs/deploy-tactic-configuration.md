# Configuring TACTIC and Co-Services

**TACTIC Service Configuration**

**Overview**

Multiple TACTIC servers can be leveraged in environments where there is
heavy report analysis, and where custom TACTIC environments are making
heavy use of API and GUI calls. To spread out the load of the requests
made, custom API scripts can be run on one TACTIC server, while another
TACTIC server can be used to serve GUI requests. The only consideration
then with multiple TACTIC machines will be where the database and the
asset directories.

**Database**

TACTIC needs to know where to find assets and asset metadata. To do
this, each installation of TACTIC must be able to have direct file
system access to assets storage, and network access to the database
co-service.

tactic\_(os).conf

needs to contain this information.

    <database>
    <server>[DB server IP]</server>
    </database>

All other settings, covered previously, can be set according to
individual requirements of the host machine and environment.

**Assets Storage**

TACTIC needs to know where to find assets. To do this, each installation
of TACTIC must be able to have direct file system access to assets
storage. The details of file system management are beyond the scope of
this document, but typically are within the realm of the system
administrator.

**Processes**

If the TACTIC server has no other services attached, there is probably
room to increase the number of processes running on each machine.

    <services>
    <process_count>6</process_count>
    </services>

Refer to Reference: TACTIC Default Configuration for the complete sample
configuration file.

Refer to Reference: TACTIC Service Configuration Directives for
configuration directives.

**HTTP Co-service Configuration**

**Apache**

Apache is used for the following sample HTTP configuration for TACTIC.
Some configuration knowledge of apache is required.

**Permissions – Allowing TACTIC to store and manipulate assets**

This section defines the location and availability of the assets
directory, which is the primary source of data for the apache server.
There is also the declaration of an alias to the TACTIC source
directory, which contains various objects that TACTIC uses, such as
widget elements.

    Alias /context         /home/apache/tactic/src/context
    Alias /assets       /home/apache/assets
    Alias /doc/           /home/apache/tactic/doc/

The section with &lt;Directory&gt; directives defines the access rules for the
assets directory and the "/tactic" directory, which is just a
conveniently named alias.

    <Directory "/home/apache/tactic" >
        Options FollowSymLinks
        AllowOverride None
        Order Allow,Deny
        Allow from All
    </Directory>
    <Directory "/home/apache/assets" >
        Options FollowSymLinks
        AllowOverride None
        Order Allow,Deny
        Allow from All
    </Directory>

**Proxying/Rewriting a single process – Redirecting requests to TACTIC**

Apache needs to know where to find the proxied TACTIC service in the
httpd.conf file. The below configuration takes advantage of only one
process being served from port 8081 on the local machine.

The second section, with RewriteRule directives, defines the re-write
rules for the TACTIC service, to segregate requests handled by the
TACTIC server, from static asset delivery through the HTTP service.
These rules channel any requests that are prefixed with the "/tactic"
path to the TACTIC server on port 8081.

    RewriteRule   ^/tactic/(.+)$ http://localhost:8081/tactic/$1 [P,L]
    RewriteRule   ^/tactic http://localhost:8081/tactic/ [P,L]
    RewriteRule   ^/projects/(.+)$ http://localhost:8081/tactic/$1 [P,L]
    RewriteRule   ^/projects http://localhost:8081/tactic/ [P,L]

**Proxying/Rewriting multiple processes – Redirecting requests to TACTIC**

The proxy configuration can be enhanced with a load balancing scheme for
one or more machines. Apache has the ability to randomly select from a
list of locations via a rewrite map.

    RewriteMap    lb    rnd:/home/apache/sites/load_balance.txt

This map can feed the rewrite rules with a dynamically assigned host
name.

    RewriteRule   ^/tactic/(.+)$ http://${lb:dynamic}/tactic/$1    [P,L]
    RewriteRule   ^/projects/(.+)$ http://${lb:dynamic}/tactic/$1  [P,L]
    RewriteRule   ^/tactic http://${lb:dynamic}/tactic/            [P,L]
    RewriteRule   ^/projects http://${lb:dynamic}/tactic/          [P,L]

The file load\_balance.txt is an arbitrarily named and located file that
contains the names of servers that will be referred to by the "rnd"
function in the Rewrite rules. The "lb:dynamic" reference will be
replaced by the name of the server file

The load\_balance.txt contains a pipe separated list of hosts named
"dynamic"

    dynamic localhost:8081|localhost:8082|localhost:8083

This list is dependent on the number of ports that TACTIC is running on,
specified by tactic\_(OS).conf. Note that apache can proxy from IP
addresses or hostnames external to the host that the service is parked
on.

On this single line list, add all machines and ports that are running
TACTIC. Since the scheme algorithm is random, it does not matter what
order the machines/ports are listed in, just that they are actually on
the list. In this case, there are multiple TACTIC machines, named
"tacticserver01" and "tacticserver02". The example assumes the machine
has either DNS entries for these machines or entries in the "hosts"
file. IP addresses can also be used.

    dynamic tacticserver01:8081|tacticserver02:8081|tacticserver01:8082
    # and so on, until all machines/ports are covered

Refer to Reference: Apache Configuration for TACTIC for the complete
sample configuration file.

**Database Co-service Configuration**

**PostgreSQL**

PostgreSQL is used as the database co-service in the following sample
configuration. PostgreSQL has only two configuration files that are
required to be examined in order to function with TACTIC; pg\_hba.conf
and postgresql.conf

**Network trust - pg\_hba.conf**

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

**Network interface - postgresql.conf.**

The postgresql.conf configuration file has a setting that will allow the
PostgreSQL service to bind to the particular interface required.

Of concern is the "listen\_addresses" attribute.

    listen_addresses = 'localhost'

By default, the PostgreSQL service is only bound to the localhost. This
is fine for single machine operation of the TACTIC service.

    listen_addresses = '*'

This setting or specific IP addresses can be used if the DB service is
not on the same machine as the TACTIC service
