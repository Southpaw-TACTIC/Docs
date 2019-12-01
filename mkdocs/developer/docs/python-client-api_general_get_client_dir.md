# get\_client\_dir

**get\_client\_dir(snapshot\_code, file\_type='main', mode='client\_repo')**

Get a dir segment from a snapshot

**param:**

**snapshot\_code** - the unique code of the snapshot

**keyparam:**

**file\_type** - each file in a snapshot is identified by a file type.

This parameter specifies which type. Defaults to 'main'

**mode** - Forces the type of folder path returned to use the value from the

appropriate tactic\_&lt;SERVER\_OS&gt;-conf.xml configuration file.

Values include 'lib', 'web', 'local\_repo', 'sandbox', 'client\_repo', 'relative'

lib = the NFS asset directory from the server point of view

web = the http asset directory from the client point of view

local\_repo = the local sync of the TACTIC repository

sandbox = the local sandbox (work area) designated by TACTIC

client\_repo (default) = the asset directory from the client point of view

If there is no value for win32\_client\_repo\_dir or linux\_client\_repo\_dir

in the config, then the value for asset\_base\_dir will be used instead.

relative = the relative direcory without any base

**return:**

**string** - directory segment for a snapshot and file type

**example:**

If the tactic\_&lt;SERVER\_OS&gt;-conf.xml configuration file contains the following:

            <win32_client_repo_dir>T:/assets</win32_client_repo_dir>

and if the call to the method is as follows:

            snapshot = server.create_snapshot(search_key, context)

            code = snapshot.get('code')

            server.get_path_from_snapshot(snapshot.get('code'))

Then, on a Windows client, get\_client\_dir() will return:

            T:/assets/sample3d/asset/chr/chr003/scenes
