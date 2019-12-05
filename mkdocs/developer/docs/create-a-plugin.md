# Create a Plugin

**What is a technical description of a TACTIC plugin?**

A plugin is a self-contained package of files that TACTIC can make use
of to extend the base functionality. Virtually any functionality in
TACTIC can be made into a plugin.

A plugin can contain:

-   project configuration data

-   any database data

-   js files

-   css files

-   documentation

-   python files

**manifest.xml file**

The manifest file is a description of the entries in the database that
are owned by the plugin. This allows the plugin manager to extract the
appropriate database entries and commit the .spt files. It contains
elements like:

data: a collection of name/value pairs that describe information about
the plugin

-   code

-   description

-   version

sobject: describes which sobjects the plugin contains. It’s an
expression of the form &lt;sobject search\_type=”\[search\_type\]”&gt; with
attributes:

-   code: the specfic code of the object

-   expression: an expression of which all matched sobject will belong to
    the plugin

-   path: the relative .spt file path that all sobjects will be written to

-   ignore\_columns: a comma seperate list of columns for the plugin
    exporter to ignore

-   There are some special attributes for specific search types. The
    config/widget\_config search type has the attribute:

    -   view

**.spt files**

".spt" files are database files that contain database schema structure and
database data. These files enable TACTIC to read and write database data
that is both platform and database independent. This abstractions allows
TACTIC plugins to be used on any supported TACTIC platform. An important
design criteria of .spt files are that they are human readable even when
the database entry contains xml or software code. More importantly, they
can be easily diff’ed using standard software tools so that the code
produced can show proper diffs using any source code management system
(such as Perforce, SVN or Git). This is essential for collaborative work
building plugins to delivery to a 3rd party.

**Creating the Plugin**

Once you are in the plugin manager, you can the New button which creates
a new plugin outline. Afterwards, you can start filling in the details
like name, type, etc. On creation, a plugin type can be specified.
Depending on the plugin type a number of bootstrap data will be created
to support the structure of the plugin. After selecting Create, the
plugin will be created and you will be able to see it in the plugin
list.

If you go to the documentation tab, you will find that you are able to
create new documentation if the documentation doesn’t exist. This will
create a new file, doc.html, which you can edit now.

To add files to the plugin, select the plugin and go to the files tab.
Here, you will find many options like the ability to upload or simply
create a new file. The new files that you are uploading or creating are
used properly when their purpose is explained in the manifest.xml file.

After customizing the plugin to your needs, you can now package the
plugin to perhaps upload to the community site so others can use it.
Documentation on packaging can be found in this section under Packaging
a Plugin.

**Best Practices**

Widget config tables should not include code or id columns or they must
be explicitly set to values that are guaranteed to be unique on any
installation of TACTIC. Otherwise, the plugin should not depend on the
value of the code or id column.

This is also true of “custom\_scripts” written in the script editor.

When referring to an sobject, always search by code (not id). When doing
this, make sure the code contains a namespace that will not conflict
with any other plugin.
