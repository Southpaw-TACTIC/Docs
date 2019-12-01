# get\_virtual\_snapshot\_path

**get\_virtual\_snapshot\_path(search\_key, context, snapshot\_type="file", level\_key=None, file\_type='main', file\_name='', mkdirs=False, protocol='client\_repo', ext='', checkin\_type='strict')**

Create a virtual snapshot and returns a path that this snapshot
would generate through the naming conventions. This is most useful
testing naming conventions.

**param:**

snapshot creation:

    *search_key* - a unique identifier key representing an sobject

    *context* - the context of the checkin



    *keyparam:*

    *snapshot_type* - [optional] descibes what kind of a snapshot this is.

    More information about a snapshot type can be found in the

    prod/snapshot_type sobject

    *description* - [optional] optional description for this checkin

    *level_key* - the unique identifier of the level that this

    is to be checked into



    *keyparam:*

    path creation:

    --------------

    *file_type* - the type of file that will be checked in.  Some naming

    conventions make use of this information to separate directories

    for different file types

    *file_name* - the desired file name of the preallocation.  This information

    may be ignored by the naming convention or it may use this as a

    base for the final file name

    *mkdir* - an option which determines whether the directory of the

    preallocation should be created

    *protocol* - It's either client_repo, sandbox, or None. It determines whether the

    path is from a client or server perspective

    *ext* - force the extension of the file name returned



    *checkin_type* - strict, auto, '' can be used to preset the checkin_type







    *return:*

    *string* - path as determined by the naming conventions
