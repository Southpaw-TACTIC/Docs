# Install TACTIC on CentOS 8

>Updated September 2020

These instructions are for a TACTIC server that will use PostgreSQL and Apache on a Cent OS server. Refer to the General TACTIC Installation for other OSes. For other database types, refer to guides in Install TACTIC Application.

## Install PostgreSQL (>= 9.4)

    dnf install postgresql-server postgresql-contrib postgresql-devel
    postgresql-setup initdb


### Start PostgreSQL and enable the service

    systemctl start postgresql
    systemctl enable postgresql


## EPEL

Enable Extra Packages for Enterprise Linux (EPEL).

    dnf --enablerepo=extras install epel-release


## Install Python 3 and supporting modules

    dnf install python3

    dnf install python3-pillow
    dnf install python3-pycryptodomex
    dnf install python3-lxml
    dnf install python3-requests
    dnf install python3-pytz

Install Python DB connectivity module.

- PostgreSQL:

    dnf install python3-psycopg2

Note: psycopg2 needs to be (>= 2.5.4).


Set python3 as the system-wide default python:

    alternatives --set python /usr/bin/python3


## Install ImageMagick

To install ImageMagick-devel on CentOS 8, you need the PowerTools repository.


    dnf config-manager --set-enabled PowerTools

Install ImageMagick:

    dnf install ImageMagick
    dnf install ImageMagick-devel ImageMagick-perl

## Install ffmpeg

    dnf install https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm
    dnf install ffmpeg


## Install Apache

    dnf install httpd
    firewall-cmd --add-service=http --permanent
    firewall-cmd --reload
    /usr/sbin/setsebool -P httpd_can_network_connect 1

### Start Apache and enable the service for the startup

    sudo systemctl start httpd
    sudo systemctl enable httpd


## Install TACTIC

Download the TACTIC RPM from community site <a href="http://community.southpawtech.com/tactic/community/downloads">downloads</a> page.

Note that we need ``--nodeps`` (no dependency checking) because of python2 vs. python3 issues in CentOS 8. CentOS 8 doesn't have "default" ``/usr/bin/python``. It's either python2 or python3. ``alternatives --config python`` doesn't seem to solve rpm checking ``/usr/bin/python`` dependency error. For now, ``--nodeps`` will allow the rpm to be successfully installed. We know there is python3 because we installed it above. ``--nodeps`` is a workaround for now.

    sudo rpm -i --nodeps <TACTIC-RPM-file>

### Configure PostgreSQL

> Note: TACTIC requires database access, and for ease of installation, we recommend using the PostgreSQL configuration file provided in the source code. After installation, you can further configure and secure your database.


Replace the file,

    /var/lib/pgsql/data/pg_hba.conf

with,

    /opt/tactic/tactic/src/install/postgresql/pg_hba.conf


Restart PostgreSQL,

    systemctl restart postgresql


## Run TACTIC Bootstrap

    sudo su - tactic
    python3 /opt/tactic/tactic/src/pyasm/search/upgrade/postgresql/bootstrap_load.py


## Start TACTIC service

    sudo systemctl start tactic

Or from the command line:

    python3 /opt/tactic/tactic/src/bin/startup_dev.py




