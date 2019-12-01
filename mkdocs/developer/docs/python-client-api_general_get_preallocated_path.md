# get\_preallocated\_path

**get\_preallocated\_path(snapshot\_code, file\_type='main', file\_name='', mkdir=True, protocol='client\_repo', ext='', checkin\_type='strict')**

Get the preallocated path for this snapshot. It assumes that
this checkin actually exists in the repository and will create virtual
entities to simulate a checkin. This method can be used to determine
where a checkin will go. However, the snapshot must exist
using create\_snapshot() or some other method. For a pure virtual naming
simulator, use get\_virtual\_snapshot\_path().

**param:**

**snapshot\_code** - the code of a preallocated snapshot. This can be

create by get\_snapshot()

**keyparam:**

**file\_type** - the type of file that will be checked in. Some naming

conventions make use of this information to separate directories

for different file types

**file\_name** - the desired file name of the preallocation. This information

may be ignored by the naming convention or it may use this as a

base for the final file name

**mkdir** - an option which determines whether the directory of the

preallocation should be created

**protocol** - It’s either client\_repo, sandbox, or None. It determines whether the

path is from a client or server perspective

**ext** - force the extension of the file name returned

**checkin\_type** - strict, auto , or '' can be used.. A naming entry in the naming, if found, will be used to determine the checkin type

**return:**

**string** - the path where add\_file() expects the file to be checked into

**example:**

it saves time if you get the path and copy it to the final destination first.

            snapshot = my.server.create_snapshot(search_key, context)

            snapshot_code = snapshot.get('code')

            file_name = 'input_file_name.txt'

            orig_path = 'C:/input_file_name.txt'

            path = my.server.get_preallocated_path(snapshot_code, file_type, file_name)



            # the path where it is supposed to go is generated

            new_dir = os.path.dirname(path)

            if not os.path.exists(new_dir):

                os.makedirs(new_dir)

            shutil.copy(orig_path, path)

            my.server.add_file(snapshot_code, path, file_type, mode='preallocate')
