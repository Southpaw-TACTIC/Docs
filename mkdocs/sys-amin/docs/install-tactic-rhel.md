# Install TACTIC on RHEL

Updated October 2019

These instructions are for a TACTIC server that will use PostgreSQL and Apache on a RHEL server (FedoraOS, CentOS, Red Hat). Refer to the General TACTIC Installation for using other OS. For other database types, refer to guides in Install TACTIC Application. 


## Install PostgreSQL

```
dnf install postgresql-server
/usr/bin/postgresql-setup --initdb
systemctl enable postgresql
systemctl start postgresql
dnf install postgresql-contrib postgresql-devel
```




## Install Python 3 and supporting modules

Check if Python 3 is already installed on your system by running the following shell command and reviewing the Python 3 console,

```
[root@localhost ~]# python3
Python 3.7.3 (default, Mar 27 2019, 13:36:35)
[GCC 9.0.1 20190227 (Red Hat 9.0.1-0.8)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Python 3.7 reccomended for TACTIC 4.7. If Python is not installed, install Python using dnf,


```
dnf install python3
```

Install Python 3 supporting modules,

```
dnf install python3-pillow
dnf install python3-pycryptodomex
dnf install python3-lxml
dnf install python3-requests
dnf install python3-pytz
```

For Python 2,

```
dnf install python-pillow
dnf install python-pycryptodomex
dnf install python2-lxml
dnf install python-requests
```

Install Python DB connectivity module,

- PostgreSQL:
```
dnf install python3-psycopg2
```


## Install Image Utilities ImageMagick and FFMPEG

```
dnf install php-pear php-devel gcc
dnf install ImageMagick ImageMagick-devel ImageMagick-perl
dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
dnf -y install ffmpeg
```

## Install Apache

```
dnf install httpd
firewall-cmd --add-service=http --permanent
firewall-cmd --reload
/usr/sbin/setsebool -P httpd_can_network_connect 1
```


## Install TACTIC RPM

Download the TACTIC RPM from community site <a href="http://community.southpawtech.com/tactic/community/downloads">downloads</a> page.

```
rpm -Uhv <TACTIC-RPM-file>
```

## Configure PostgreSQL

> Note: TACTIC requires database access, and for ease of installation, we reccomend using the PostgreSQL configuration file provided in the source code. After installation, you can further configure and secure your database. 

Replace the file, 

    /var/lib/pgsql/data/pg_hba.conf 
    
with, 

    /opt/tactic/tactic/src/install/postgresql/pg_hba.conf

Restart postgresql,

```
systemctl restart postgresql
```


## Run TACTIC Bootstrap

```
python3 /opt/tactic/tactic/src/pyasm/search/upgrade/postgresql/bootstrap_load.py
```



