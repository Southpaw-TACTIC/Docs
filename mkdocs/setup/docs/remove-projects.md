# Remove Projects

There is no user interface in TACTIC to remove a project. This is
because the complete removal of a project has some pretty significant
consequences. When a project is created, a number of elements are
created. These are listed below.

> **Note**
>
> This task may need to be carried out by the Tactic System Admin as it
> involves manually accessing both the Tactic File system and the Tactic
> Database

In all of the following examples, &lt;project\_code&gt; represents the code of
the project when the project was created.

-   A database called &lt;project\_code&gt;

-   An assets directory in &lt;tactic\_asset\_dir&gt;

-   Entry in the project table

**A complete removal of a project should be handled with care. This is
most often desirably when a project has been created in properly. It is
one of the few operations that is not undo-able in TACTIC, so it is
recommended to be careful when proceeding with the following steps. It
is also recommended that a complete backup of TACTIC is performed before
carrying out this process.**

**Remove the project directory**

    cd <project_install_dir>/sites
    rm -rf <project_code>

**Remove the database**

    psql -U postgres sthpw
    drop database "<project_code>";

**Remove the assets directory**

    cd <project_asset_dir>
    rm -rf <project_code>

**Remove the entry in the projects table in the database**

    psql -U postgres sthpw
    delete from project where code='<project_code>';

**Remove connected entities in the sthpw database;**

In this process, Tactic may not allow removing a particular project due
to there being child tasks, notes, snapshots, files, wdg\_settings etc.
If Tactic denies revoval because, for example there is a connection in
the file table, you will need to do the following

    delete from file where project_code='<project_code>';
    delete from snapshot where project_code='<project_code>';
    delete from task where project_code='<project_code>';
    delete from note where project_code='<project_code>';
    delete from wdg_settings where project_code='<project_code>';
    delete from pref_setting where project_code='<project_code>';
