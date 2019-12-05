# get\_path\_from\_snapshot

**get\_path\_from\_snapshot(snapshot\_code, file\_type='main', mode='client\_repo')**

Get a full path from a snapshot

**param:**

**snapshot\_code** - the unique code / search\_key of the snapshot

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

**string** - the directory to copy a file to handoff to Tactic without having to

go through http protocol

**example:**

If the tactic\_&lt;SERVER\_OS&gt;-conf.xml configuration file contains the following:

            <win32_client_repo_dir>T:/assets</win32_client_repo_dir>

and if the call to the method is as follows:

            snapshot = server.create_snapshot(search_key, context)

            code = snapshot.get('code')

            server.get_path_from_snapshot(snapshot.get('code'))



            # in a trigger

            snapshot_key = my.get_input_value("search_key")

            server.get_path_from_snapshot(snapshot_key)

Then, on a Windows client, get\_path\_from\_snapshot() will return:

            T:/assets/sample3d/asset/chr/chr003/scenes/chr003_rig_v003.txt
