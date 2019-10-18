# Install TACTIC on RHEL

<!-- TODO: Set up link to downloads page -->
For installing on RHEL environments, we recommend using the TACTIC RPM that is available on the community site <a href="http://community.southpawtech.com/tactic/community/downloads">downloads</a> page.


## Install PostgreSQL:

```
sudo dnf install postgresql-server
sudo /usr/bin/postgresql-setup --initdb
sudo systemctl enable postgresql
sudo systemctl start postgresql
yum install postgresql-contrib postgresql-devel
```

## Install Python

```
yum install python-pillow
yum install python-psycopg2
yum install python2-lxml
yum install pycryptodomex
```

## Install Image Utilities

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
RUN RPM sets up all files and directories
- move pg_hba.conf to correct place with correct permissions or configure database


