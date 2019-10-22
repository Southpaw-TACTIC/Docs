# Backup and Restore Server

Like any other data producing service, TACTIC requires a backup regimen.
The data in that TACTIC produces and manages must be backed up in
accordance with the backup policy of the departments that manage the
TACTIC service.

This documents outlines details of a proper backup policy and manual steps to carry out
a backup. To set up an automated backup, see Maintenance > Automated Backup.

## Backup Policy

TACTIC managers should create a backup policy for TACTIC data.
A backup policy is extremely important, as data loss within the TACTIC service is catastrophic.

The following components should be backed up as apart of the backup policy:

1. Assets - Versioned assets are all the files that are checked
    in and out of the tactic service.

2. Database - Asset metadata are all the data produced by user
    interaction with the tactic service.

3. TACTIC Application


### Frequency of backups

The frequency of backup of tactic data depends on
the policies of the TACTIC managers. An examination of the frequency of
use of the tactic service, combined with the down time potentially
required to back up tactic data should be considered.

### Backup methods

The only consideration that tactic managers should take
into account when creating a backup policy for tactic data is that
tactic data produced is synchronized. This is accomplished via a
transaction system within tactic. This transaction system relies on
co-services to store transacted data. During the backup process, tactic
and its co-services should be stopped to prevent any loss of

It is highly recommended that you back up your TACTIC server using a
regular schedule. In the event of a hardware failure, you will be able
to restore your TACTIC server fully from the latest backup.
synchronization to these co-services.

> **Note**
>
> You may want to stop the tactic service while you do your backup
> process. To do so, run the following commands:
>
> `service tactic stop`
>
> `service tactic start`

## Assets

Versioned assets are all the files that are checked in
and out of the tactic service. Typically the tactic service works in
conjunction with a co-service such as a network file storage service to
accomplish its tasks of asset management. Thus the task of backing up
tactic of versioned assets onto these systems usually overlaps with the
file management policies of the IT department. Most enterprise class
network file storage systems, and third party file backup systems can
accomplish the task of backing up tactic assets. Redundant raid storage,
snapshots, and offsite backups can all be utilized to accomplish version
and asset backups.

### Backup

The 'assets' directory is the repository where TACTIC stores all of the
asset files. By backing up this directory, you can restore all of your
asset files in the event of a database crash into a clean TACTIC-managed
directory structure.

> **Note**
>
> You may need to contact your TACTIC server administrator if your
> 'assets' directory has been redirected to another location.


**Windows**

The 'assets' directory on a Windows install is located by default in:

`C:\assets`

**Linux**

The 'assets' directory on a Linux install is located by default in:

`/home/apache/assets`

### Restore

To restore the TACTIC 'assets' directory, you have to restore your
backup to the current 'assets' location.

## Database

To dump the TACTIC data base you need to log in to the PostgreSQL
database and perform a database dump.

> **Note**
>
> For both Linux and Windows the database file is in the 'assets'
> directory, although you may redirect the location to your backup
> location. Also, the TACTIC default for the database is to have no
> password. If you have added a password, you may need to enter it into
> your postgres commands with the `-P` tag.

### Backup - PostgreSQL

**Windows**

`pg_dumpall -U postgres -c > c:\assets\tacticDatabase.sql`

**Linux**

`pg_dumpall -U postgres -c > /home/apache/assets/tacticDatabase.sql`

### Restore - PostgreSQL

To restore the TACTIC database run the command:

`psql -U postgres < tacticDatabase.sql`


## TACTIC Backup

This last step, although not completely necessary, is recommended
because it takes a snapshot of your TACTIC source code and project
settings at the time of backup.

### Backup

**Windows**

The folders to back up are:

`C:\Program Files\southpaw\tactic`

`C:\Program Files\southpaw\projects`

**Linux**

The folders to back up are:

`/home/apache/tactic`

`/home/apache/projects`

### Restore

To restore the TACTIC program files, you have to restore the `tactic`
and `projects` directories to their original locations.
