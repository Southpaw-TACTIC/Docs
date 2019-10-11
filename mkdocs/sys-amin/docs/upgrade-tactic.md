# Upgrade TACTIC

Upgrading TACTIC is usually a relatively simple procedure:

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

    `python upgrade_db.py`

    First, you will be prompted to confirm whether the displayed version is
    the right one to upgrade to.

    On proceeding, it will check the upgrade script’s version tree against
    the currently installed TACTIC version (the new one).

    Normally, they should be the same. In case they are not, you will be
    prompted again to confirm if this is actually intended. Warning: if the
    versions do not match, it is very likely you have not stopped the old
    version from running or have not symlinked "tactic" to the new version yet.

8.  Restart the TACTIC service:

    `/etc/init.d/tactic start`

9.  Go to the "Projects" view in the Admin site.

10. Optional: Compare each project’s schema with the one used by TACTIC.

**Explanation of switching symbolic links**

By default, in your python installation, like
/usr/lib/python2.5/site-packages/tacticenv/tactic\_paths.py it defines
the TACTIC\_INSTALL\_DIR = '/home/apache/tactic' and so a convenient way
to upgrade is to untar the new release in /home/apache/ as e.g ,
/home/apache/tactic-2.5.0.rc04 cd /home/apache then delete any existing
symbolic link named "tactic" by running `rm tactic`. Afterwards, you can
create a new symlink using `ln -s tactic-2.5.0.rc04 tactic` With the
tactic service stopped, and the TACTIC\_INSTALL\_DIR practically pointing
to the new release because of the symlink, now you can safely run
src/bin/upgrade\_db.py in the new release.

1.  Download the new release of TACTIC from the Download section of
    support.southpawtech.com . TACTIC is delivered as a zipped (.zip) file.

2.  Copy the new version to the installed directory of TACTIC and unzip it.

3.  Stop the TACTIC service

    `Run services.msc`

    `Select the service Tactic Server, click on the Stop
                        button`

4.  Rename the top directory of the new version to TACTIC.

5.  In a cmd shell, cd to the bin directory of the new installation:

    `cd C:\Program Files\Southpaw\Tactic\src\bin`

6.  Back up the current database:

    `pg_dumpall -U postgres -c > database_<date>.sql`

7.  Run the upgrade script. The version number argument (for example, 2.6.0.v01) is optional.

    `python upgrade_db.py`

    First, you will be prompted to confirm whether the displayed version is
    the right one to upgrade to.

    On proceeding, it will check the upgrade script’s version tree against
    the currently installed TACTIC version (the new one).

    Normally, they should be the same. In case they are not, you will be
    prompted again to confirm if this is actually intended. Warning: if the
    versions do not match, it is very likely you have not stopped the old
    version from running or have not symlinked "tactic" to the new version yet.

8.  Restart the TACTIC service:

    `Select the service Tactic Server, click on the Start
                        button`

9.  Go to the "Projects" view in the Admin site.

10. Optional: Compare each project’s schema with the one used by TACTIC.


