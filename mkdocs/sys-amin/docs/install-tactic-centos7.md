# Install TACTIC on CentOS 7

>Updated December 2019

These instructions are for a TACTIC server that will use PostgreSQL and Apache on a Cent OS server. Refer to the General TACTIC Installation for other OSes. For other database types, refer to guides in Install TACTIC Application.


## Install PostgreSQL

CentOS 7 comes with PostgreSQL 9.2 by default. TACTIC needs PostgreSQL 9.4 and higher.

Here are instructions to install PostgreSQL 11 using official PostgreSQL packages.

    rpm -Uvh https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
    yum update
    yum install postgresql11-server postgresql11-contrib postgresql11-devel
    /usr/pgsql-11/bin/postgresql-11-setup initdb



### Starting PostgreSQL and enabling the service

    systemctl start postgresql-11
    systemctl enable postgresql-11


## Configure PostgreSQL

> Note: TACTIC requires database access, and for ease of installation, we recommend using the PostgreSQL configuration file provided in the source code. After installation, you can further configure and secure your database.

Replace the file,

    /var/lib/pgsql11/data/pg_hba.conf

with,

    /opt/tactic/tactic/src/install/postgresql/pg_hba.conf

Restart PostgreSQL,


    systemctl restart postgresql


> Sample authentication rules:

    # "local" is for Unix domain socket connections only
    local   all             all                                     trust
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            trust
    # IPv6 local connections:
    host    all             all             ::1/128                 trust



## EPEL

Enable Extra Packages for Enterprise Linux (EPEL).

    yum --enablerepo=extras install epel-release


## Install Python 3 and supporting modules

Check if Python 3 is already installed on your system by running the following shell command and reviewing the Python 3 console:

```
[tactic@localhost ~]$ python3
Python 3.6.8 (default, Aug  7 2019, 17:28:10)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Python 3.7 is recommended for TACTIC 4.7. If Python 3.7 is not available, Python 3.6 can be used instead.

Install Python 3 using yum:

    yum install python3

In CentOS 7, the above command will install Python 3.6 by default. We will need to install Python 3 supporting modules. In CentOS 7, the modules are python36-xxx instread of python3-xxx.

    yum install python36-pycryptodomex
    yum install python36-lxml
    yum install python36-requests
    yum install python36-pytz

Alternatively you can also install these modules using `pip`.


    pip3 install pycryptodomex
    pip3 install lxml
    pip3 install requests
    pip3 install pytz



Install Python DB connectivity module.

- PostgreSQL:

    yum install python3-psycopg2



## Installing ImageMagick

    yum install ImageMagick
    yum install ImageMagick-devel
    yum install ImageMagick-perl


## Installing ffmpeg

    rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro
    rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
    yum install ffmpeg



## Installing Apache

    yum install httpd
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    /usr/sbin/setsebool -P httpd_can_network_connect 1


### Starting Apache and enabling the service for the startup

    sudo systemctl start httpd
    sudo systemctl enable httpd



## Install TACTIC RPM

Download the TACTIC RPM from community site <a href="http://community.southpawtech.com/tactic/community/downloads">downloads</a> page.


    rpm -Uhv <TACTIC-RPM-file>



## Run TACTIC Bootstrap


    python3 /opt/tactic/tactic/src/pyasm/search/upgrade/postgresql/bootstrap_load.py



## Starting TACTIC service

    sudo systemctl start tactic

Or run the server from the command line:

    python3 /opt/tactic/tactic/src/bin/startup_dev.py



