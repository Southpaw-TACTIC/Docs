# Naming Convention Classes

**TACTIC Directory and File Naming**

TACTIC has a default file naming convention that has proven to work for
a wide variety of productions. A production facility may simply choose
to use this default naming convention, or could also override it to
match the convention used by its current system. Customizing the
directory and file naming conventions has proven to be the most time
consuming part of integrating TACTIC into a system. The difficulty
required to do this depends largely on being able to access the
directories and file names procedurally.

TACTIC allows you to define different project types in the Site Admin →
Projects Types View. Here you can define a different type of project and
set up the various types of naming conventions for a particular project.
When creating a project, you select a project type and it will make use
of the information in the project type.

The various naming conventionn are as follows:

1.  file\_naming\_cls: this class determines the file name of every file
    checked into TACTIC.

2.  dir\_naming\_cls: this class determines the directory of every file
    checked into TACTIC

3.  app\_naming\_cls: this class determines the node names within an
    application such as Maya.

The following code snippet is an example of overriding the directory for
all files checked into a shot:

    from pyasm.prod.biz import ProdDirNaming

    class CustomDirNaming(ProdDirNaming):
        def prod_shot(my, dirs):

            shot = my.sobject

            dirs = my.get_base_dir()

            # add the sequence code
            sequence_code = shot.get_value("sequence_code")
            dirs.append(sequence_code)

            # add the shot code
            shot_code = shot.get_code()
            dirs.append(shot_code)

            # put all files in the "scenes" directory
            dirs.append("scenes")

            return dirs

This will create a directory name that looks something like

`/<base_dir>/<sequence_code>/<shot_code>/scenes`

or

/sample3d/shot/XG/XG002/scenes

Overriding naming conventions is a simple matter of defining your own
implementation class and implementing specific functions in this class.
Each SObject has its own SObject type. For example a shot in a
production may have the type "prod/shot". This naming uniquely
identifies this type of SObject.

To customize the naming convention for this class, you replace the
slashes "/" in the Search Type with underscores "\_" and use this as the
name of the function. So in the example above, to customize a Shot
(prod/shot), you define a function called prod\_shot. Whenever TACTIC is
asked to produce a directory for a particular SObject, an implementation
function such as this is called. If no such function exists, then the
default is used.

get\_base\_dir() simply gets the base directory of this SObject (default
&lt;base&gt;/&lt;project&gt;/&lt;table&gt;)

Overriding the file naming is similar.

    from pyasm.prod.biz import ProdFileNaming

    class CustomFileNaming(ProdFileNaming):
        def prod_shot(my):

            parts = []

            parts.append(my.sobject.get_code())

            parts.append('custom')
            parts.append(my.snapshot.get_context())
            version = my.snapshot.get_value("version")

            version = "v%0.3d" % int(version)
            parts.append(version)
            ext = my.get_ext()
            name = '_'.join(parts)
            name = '%s%s'%(name, ext)
            return name

This will create a file name that looks something like

`<shot_code>_<custom>_<context>_<version>.<ext>`

or

\`XG002\_bedroom\_anim\_v004.jpg \`

Custom in this case is a custom attribute added to a shot. So with these
two classes, we would have a full path for this file of:

\`/assets/sample3d/shot/XG/XG002/scenes/XG002\_bedroom\_anim\_v004.jpg \`

**Default Naming Conventions**

TACTIC comes with a default file and directory naming convention. You
may choose to adopt this default naming convention as specified above,
or you may create your own naming convention. The choice of which naming
conventions should be used is often a hard one. Using TACTIC’s default
naming convention makes it much simpler and quicker to start using
TACTIC in production. This is the recommended route if there is no
legacy within the facility. If, however, you have many scripts and
processes that rely on a previous naming convention, then you may
customize TACTIC to map to your current naming convention.

The rest of this section describes TACTIC’s default naming conventions.

To start, there is a base directory under which all asset files are
stored. This base directory is specified in the Tactic conf file in
&lt;sites\_dir&gt;/config/tactic\_linux.conf (tactic\_win32.conf for windows).
The next level is divided by project and then the type of the sobject.
All projects of this same type are located under this directory:

`<base_asset_dir>`

The default for any search type checked into a specific context is
represented with the following convention:

The next levels represent the subdirectory component and are all
associated with metadata for the SObject types in some way. The details
are up to the implementation function for each specific SObject type.

    <base_asset_dir>/<project_code>/<search_type>/<sobject_code>/<sobject_code>_<snapshot_context>_<snapshot_version>.<original_file_ext>

**Default**

If an SObject type does not have any overriding function, then there is
a default implementation:

Subdir: empty File: &lt;filename&gt;\_&lt;file\_code&gt;.&lt;ext&gt;

        Subdir: empty

        File: <filename>_<file_code>.<ext>

        example: /home/apache/assets/storyboard/castle01_00034355BAR.jpg

The file code ensures that the file name is unique. This uniqueness
prevents files from overwriting each other, even when files of the same
name are checked in. In recent versions TACTIC has moved away from
adding the file code to the file name in favor of the clearer v002\_BAR
ending. (However, the file name format can still exist for numerous
asset types where the file name is of little consequence.)
