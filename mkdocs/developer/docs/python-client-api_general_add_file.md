# add\_file

**add\_file(snapshot\_code, file\_path, file\_type='main', use\_handoff\_dir=False, mode=None, create\_icon=False)**

Add a file to an already existing snapshot. This method is used in
piecewise checkins. A blank snapshot can be created using
create\_snapshot(). This method can then be used to successively
add files to the snapshot.

In order to check in the file, the server will need to have access
to these files. There are a number of ways of getting the files
to the server. When using copy or move mode, the files are either
copied or moved to the "handoff\_dir". This directory
is an agreed upon directory in which to handoff the files to the
server. This mode is generally used for checking in user files.
For heavy bandwidth checkins, it is recommended to user preallocated
checkins.

**param:**

**snapshot\_code** - the unique code identifier of a snapshot

**file\_path** - path of the file to add to the snapshot.

Optional: this can also be an array to add multiple files at once.

This has much faster performance that adding one file at a time.

Also, note that in this case, file\_types must be an array

of equal size.

**keyparam:**

**file\_type** - type of the file to be added.

Optional: this can also be an array. See file\_path argument

for more information.

**use\_handoff\_dir** - DEPRECATED: (use mode arg) use handoff dir to checkin

file. The handoff dir is an agreed upon directory between the

client and server to transfer files.

**mode - upload|copy|move|manual|inplace** - determine the protocol which delievers

the file to the server.

**create\_icon** - (True|False) determine whether to create an icon for

this appended file. Only 1 icon should be created for each

snapshot.

**dir\_naming** - explicitly set a dir\_naming expression to use

**file\_naming** - explicitly set a file\_naming expression to use

**checkin\_type** - auto or strict which controls whether to auto create versionless and adopt some default dir/file naming

**return:**

**dictionary** - the resulting snapshot

**example:**

This will create a blank model snapshot for character chr001 and

add a file

            search_type = 'prod/asset'

            code = 'chr001'

            search_key = server.build_search_type(search_type, code)

            context = 'model'

            path = "./my_model.ma"



            snapshot = server.create_snapshot(search_key, context)

            server.add_file( snapshot.get('code'), path )

Different files should be separated by file type. For example,

to check in both a maya and houdin file in the same snapshot:

            maya_path = "./my_model.ma"

            houdini_path = "./my_model.hip"



            server.add_file( snapshot_code, maya_path, file_type='maya' )

            server.add_file( snapshot_code, houdini_path, file_type='houdini' )

To transfer files by uploading (using http protocol):

            server.add_file( snapshot_code, maya_path, mode='upload' )

To create an icon for this file

            path = 'image.jpg'

            server.add_file( snapshot_code, path, mode='upload', create_icon=True )

To add multiple files at once

            file_paths = [maya_path, houdini_path]

            file_types ['maya', 'houdini']

            server.add_file( snapshot_code, file_paths, file_types=file_types, mode='upload')
