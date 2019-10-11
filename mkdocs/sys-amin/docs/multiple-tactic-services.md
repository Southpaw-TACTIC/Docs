# Multiple TACTIC Services

Multiple versions of TACTIC can be easily run side by side on the same
machine. This is extremely useful for testing purposes. Running a newer
version of TACTIC on a production server machine using the production
server environment and production database. You can run this without
interrupting service ot the production server.

If this is not explicitly set, TACTIC will use whatever settings exist
when TACTIC was first installed. These are defined in the tacticenv
module which is first imported on all command line TACTIC scripts by:

    import tacticenv

These values are typically found in the Python distribution
site-packages. The exact location of these files can vary between
differing operarting systems, but common examples are:

    windows: C:\Python27\site-packages\Lib\site-packages\tacticenv

    linux: /usr/lib/python2.7/site-packages

When TACTIC starts up, it will first look at the environment variable
TACTIC\_INTALL\_DIR to determine which distribution of TACTIC will be
used. Before a newer version of TACTIC is executed, it is necessary to
upgrade to the newer database schema. Unless clearly stated in the
distribution release, it is always safe to upgrade the database for a
newer version. Changes to the database are always backwards compatible,
so that older versions of TACTIC can always run on newer schema of the
database.

**Steps**

1.  Unzip a TACTIC distribution anywhere in the file system. For
    purposes of examples, /home/apache will be used as the base directory
    for TACTIC

        cd /home/apache
        unzip tactic-3.0.0.zip

2.  Set the environment variable TACTIC\_INSTALL\_DIR

        export TACTIC_INSTALL_DIR=/home/apache/tactic-3.0.0

3.  Upgrade the database.

        su apache
        cd tactic-3.0.0.src/bin
        python upgrade.py

4.  Execute tactic

        python startup_dev.py

This will execute TACTIC from the command line in dev mode. All output
will go to this console.
