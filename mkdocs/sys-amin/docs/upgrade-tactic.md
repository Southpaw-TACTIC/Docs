# Upgrade TACTIC

Upgrading TACTIC version is a simple precedure and generally involves the following steps,

1. Stop the TACTIC service
2. Backup the database
3. Update source code
4. Run upgrade_db.py
5. Restart the TACTIC service

## Linux Upgrade

1.  Download the new release of TACTIC from the Download section of
    support.southpawtech.com . TACTIC is delivered as a zipped (.zip) file.

2.  Copy the new version to the installed directory of TACTIC and unpack it. e.g.

    `cd /home/apache/`

    `unzip tactic-2.6.0.v01.zip`

3.  Stop the TACTIC service

    `/etc/init.d/tactic stop`

4.  Switch the symbolic link. See explanation on symbolic link below.

5.  In a cmd shell, cd to the bin directory of the new installation:

    `cd /home/apache/tactic/src/bin`

6.  Back up the current database:

    `pg_dumpall -U postgres -c > database_<date>.sql`

7.  Run the upgrade script. The version number argument (for example, 2.6.0.v01) is optional.

    `python3 upgrade_db.py`

    First, you will be prompted to confirm whether the displayed version is
    the right one to upgrade to.

    On proceeding, it will check the upgrade script’s version tree against
    the currently installed TACTIC version (the new one).

    Normally, they should be the same. In case they are not, you will be
    prompted again to confirm if this is actually intended. 
    
    > Warning: If the versions do not match, it is very likely you have not stopped the old
    version from running or have not symlinked "tactic" to the new version yet.

8.  Restart the TACTIC service:

    `/etc/init.d/tactic start`

9.  Go to the "Projects" view in the Admin site.

10. Optional: Compare each project’s schema with the one used by TACTIC.

**Explanation of switching symbolic links**

By default, in your python installation, like

    /usr/lib/python2.5/site-packages/tacticenv/tactic\_paths.py 

it defines,

    TACTIC\_INSTALL\_DIR = '/home/apache/tactic' 

A convenient way to upgrade is to untar the new release in, 

    /home/apache/tactic-2.5.0.rc04 
    
then delete any existing symbolic link named "tactic",
    
    cd /home/apache 
    rm tactic 
    
Afterwards, you can create a new symlink using 

    ln -s tactic-2.5.0.rc04 tactic
    
With the tactic service stopped, and the TACTIC\_INSTALL\_DIR practically pointing
to the new release because of the symlink, now you can safely run

    python3 src/bin/upgrade\_db.py 

in the new release.

## Windows Upgrade

1.  Download the new release of TACTIC from the Download section of
    support.southpawtech.com . TACTIC is delivered as a zipped (.zip) file.

2.  Copy the new version to the installed directory of TACTIC and unzip it.

3.  Stop the TACTIC service from the services panel.

4.  Rename the top directory of the new version to TACTIC.

5.  In a cmd shell, cd to the bin directory of the new installation:

    `cd C:\Program Files\Southpaw\Tactic\src\bin`

6.  Back up the current database:

    `pg_dumpall -U postgres -c > database_<date>.sql`

7.  Run the upgrade script. The version number argument (for example, 2.6.0.v01) is optional.

    `python3 upgrade_db.py`

    First, you will be prompted to confirm whether the displayed version is
    the right one to upgrade to.

    On proceeding, it will check the upgrade script’s version tree against
    the currently installed TACTIC version (the new one).

    Normally, they should be the same. In case they are not, you will be
    prompted again to confirm if this is actually intended. 
    
    > Warning: if the versions do not match, it is very likely you have not stopped the old
    version from running or have not symlinked "tactic" to the new version yet.

8.  Restart the TACTIC service from the services panel.

9.  Go to the "Projects" view in the Admin site.

10. Optional: Compare each project’s schema with the one used by TACTIC.


