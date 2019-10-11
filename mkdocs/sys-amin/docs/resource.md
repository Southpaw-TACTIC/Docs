# Database Resource

TACTIC can map to any supported database platform. A single TACTIC
installation can map on to any number of external databases and use them
as a database resource. These database resources are treated as first
class citizens in the TACTIC. All of the features that are inherent to
any native TACTIC data are also available to these external database
resources. To implement this functionality, db\_resource can be used to
connect a project to a database resource. It defines the location and
connection credentials to access a database server. Database resources
can be added under the side bar menu **Global → Database Resource**.

Specify (or look up) the Database Resource under **Admin Views →
Global**.

The database resource entry in Database Resource contains all the
information needed to connect to a database. In order for TACTIC to
access another database, it has to have a database resource registered
and then it has to be mapped to a project.

In the example below, the new database’s code is named:
**my\_new\_db\_resource**, which is the reference of this entry. Host, which
refers to the IP address of the server, is set to be a tested address.
The Login and Password are the information used to log in the database.

Since all TACTIC projects have a single database resource that it uses
as a persistent store for sObjects. By default, the project will use the
same resource as the sthpw database and is defined in the TACTIC
config file. However, this can be configured to point to another
database resource.

Note that the search type uses a project to find the corresponding
database. Any project configured to look at a database resource with the
db\_resource and database columns. The db resource defines the connection
criteria and the column determines which database to connect to that
resource.

To add new a database as pure resource database, Specify (or look up)
the 'Add Project' and 'Projects' columns under **Admin Views → Global →
Database Resource**.

In the example below, the new database called **test\_database001** from
the db\_resource **my\_new\_db\_resource** has been added to a Project called
**Testing**.

For a project to become a full TACTIC project (complete with separate
URL space: `http://<server>/<project&gt;` and separate themes an interfaces),
all that is required is the config tables to exist in that database
resource. Thus a database resource can start off as a data source and
then, at any time, be upgraded to a full TACTIC project if that is ever
required by importing the appropriate config tables that the search type
uses in the project to find the corresponding database. The project is
configured to look at a database resource with the db\_resource and
database column. The db resource defines the connection criteria and
the column determines which database to connect to on that resource.

In order for TACTIC to access another database, it has to have a
database resource registered and then it has to be mapped to a project.
This mapping is currently required because all search types are scoped
and searched using the notation:

    <namespace>/<table>?project=<project>&code=<code>

An example search\_type entry would be:

    jobs/media?project=my_test_project
