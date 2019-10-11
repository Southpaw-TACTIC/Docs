# Moving VM Data

To transfer data from one VM to another, you need to do the following:

In the old TSI VM shell:

`cd /home/apache`

`pg_dumpall -U postgres -c > tactic_database.sql`

In your host machine assuming windows, start a new window of Windows
Explorer in the address, type in:

`\\<your old VM IP address>`

when prompted for uid, password, type in :

`apache`

`south123paw`

navigate into the apache folder, you should see the file
**tactic\_database.sql**, **assets folder** and **projects folder**

You need to move the old VM’s **tactic\_database.sql**, **assets folder** and
**projects** folder to the same location of the VM you just downloaded and
installed.

Same as above, open a new windows explorer, but type in the new VM IP
address and carry out the copying

In the new TACTIC VM shell, assuming you have copied the
**tactic\_database.sql**, **assets folder** and **projects folder** in the new
IP from the VM, Type in:

`dropdb -U postgres sthpw`

`psql -U postgres < tactic_database.sql`

Upgrade the TACTIC database in the VM according to the version you are
upgrading to

Now you can just shut down the old VM by closing the VMware player
window
