# Install TACTIC on RHEL

Updated October 2019

These instructions are for a TACTIC server that will use PostgreSQL and Apache on a RHEL server (FedoraOS, CentOS, Red Hat). Refer to the General TACTIC Installation for using other databases, webservers or OS. 



## Install PostgreSQL

```
sudo dnf install postgresql-server
sudo /usr/bin/postgresql-setup --initdb
sudo systemctl enable postgresql
sudo systemctl start postgresql
yum install postgresql-contrib postgresql-devel
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

Python 3.7 reccomended for TACTIC 4.7. If Python is not installed, install Python using yum,


```
yum install python3
```

Install Python 3 supporting modules,

```
yum install python3-pillow
yum install python3-pycryptodomex
yum install python3-lxml
yum install python3-requests
```

For Python 2,

```
yum install python-pillow
yum install python-pycryptodomex
yum install python2-lxml
yum install python-requests
```

Install Python DB connectivity module,

- PostgreSQL:
```
yum install python3-psycopg2
```


## Install Image Utilities ImageMagick and FFMPEG

```
yum install php-pear php-devel gcc
yum install ImageMagick ImageMagick-devel ImageMagick-perl
sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf -y install ffmpeg
```

## Install Apache

```
yum install httpd
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



## Run TACTIC Bootstrap


