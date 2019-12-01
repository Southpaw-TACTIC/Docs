# get\_all\_paths\_from\_snapshot

**get\_all\_paths\_from\_snapshot(snapshot\_code, mode='client\_repo', expand\_paths=False, filename\_mode='')**

Get all paths from snapshot

**param:**

**snapshot\_code** - the unique code of the snapshot

**keyparam:**

**mode** - forces the type of folder path returned to use the value from the

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

**expand\_paths** - expand the paths of a sequence check-in or for a directory check-in, it will list the contents of the directory as well

**filename\_mode** - source or '', where source reveals the source\_path of the check-in

**file\_types** - list: only return files in snapshot with these types

**return:**

**list** - paths
