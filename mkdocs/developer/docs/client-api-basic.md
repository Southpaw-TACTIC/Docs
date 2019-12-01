# Basic Operations in Python and Javascript

**Note**

If you haven’t done so, please review the Client API Setup doc.

**Simple Ping**

The following is a skeleton script interacting with the Client API:

**Basic Operations**

    from tactic_client_lib import TacticServerStub

    def main():
        server = TacticServerStub()
        server.start("Ping Test")
        try:
            print server.ping()
        except:
            server.abort()
            raise
        else:
            server.finish()

    if __name__ == '__main__':
        main()

Executing this script will give the following output:

    $ python examples/ping.py
    OK

If you haven’t had a ticket in the user directory, please run python
get\_ticket.py. Otherwise, you will get an error like this:

     File "G:\TSI\3.0_client\client\tactic_client_lib\tactic_server_stub.py",
                line 2789, in _setup raise TacticApiException(msg)
                tactic_client_lib.tactic_server_stub.TacticApiException:
                [C:/sthpw/etc/<someuser>.tacticrc] does not exist yet. There is not enough
                information to authenticate the server. Either set the appropriate environment
                variables or run get_ticket.py

The first line imports the TacticServerStub class. This class is a stub
to the server and relays function calls between the TACTIC server and
the client API code. It handles all the details of how to connect to the
server. It also maintains status information, including the current
project and whether or not the session is authenticated.

All client API scripts should run within a transaction. This requirement
is achieved using server.start("Ping Test"), which initiates a new
transaction on the server. All subsequent server interactions are
grouped in the same transaction until server.finish() is executed. The
function server.abort() is used to abort the transaction should any
error occur in the body of the code.

**Querying data**

The most fundamental operation in the Client API is the query function,
which enables access to direct information on an SObject

The following example illustrates the use of the query function:

          # define the search type we are searching for
          search_type = "prod/asset"

          # define a filter
          filters = []
          filters.append( ("asset_library", "set") )

          # do the query
          assets = my.server.query(search_type, filters)

          print "found [%d] assets" % len(assets)

          # go through the asset and print the code
          for asset in assets:
              code = asset.get("code")
              print(code)

Executing this example will give the following output:

    $ python examples/query.py
    found [3] assets
    chr001
    chr002
    chr003

In this example, a search\_type is first defined. This search type is a
uniquely named identifier for a class of SObjects.

A list of filters is next defined. These filters allow you to narrow the
search to specific SObjects. In this example, only assets of the
asset\_library = "set" will be found.

Next, the assets are retrieved using the query() function, which returns
a list where each element is a serialized dictionary of an SObject. In
this example, the code for each asset is retrieved and printed.

Filters are very important in the query function because they narrow
down searches to find the specific SObjects you are looking for. The
filters are very flexible and support a wide range of different modes. A
sample of the supported modes is shown below:

            # simple search filter
            filters = []
            filters.append( ("name_first", "Joe") )
            results = my.server.query(search_type, filters, columns)


            # search with 'and': where name_first = 'Joe' and name_last = 'Smoe'
            filters = []
            filters.append( ("name_first", "Joe") )
            filters.append( ("name_last", "Smoe") )
            results = my.server.query(search_type, filters, columns)


            # search with 'or': where code in ('joe','mary')
            filters = []
            filters.append( ("code", ("jo e", "mary")) )
            results = my.server.query(search_type, filters, columns)


            # search with 'or': where code in ('joe','mary') order by code
            filters = []
            filters.append( ("code", ("joe", "mary")) )
            order_bys = ['name_first']
            results = my.server.query(search_type, filters, columns, order_bys)


            # search with like: where code like 'j%'
            filters = []
            filters.append( ("code", "like", "j%") )
            results = my.server.query(search_type, filters, columns)


            # search with regular expression: code ~ 'ma'
            filters = []
            filters.append( ("code", "~", "ma") )
            results = my.server.query(search_type, filters, columns)


            # search with regular expression: code !~ 'ma'
            filters = []
            filters.append( ("code", "!~", "ma") )

**Insert and Update**

It is essential to insert SObjects and update their values.

The following code creates a new asset in the database.

      # define a search type for which to add a new entry
          search_type = 'prod/asset'

          # build a data structure which is used as data for the new sobject
          data = {
            'code': 'chr001',
                'name': 'Bob',
            'description': 'The Bob Character'
          }

          server.insert(search_type, data)

The following code snippet updates an existing asset in the database:

          # define the search key we are searching for
          search_type = "prod/asset"
          code = 'vehicle001'
          search_key = server.build_search_key(search_type, code)

          # build a dataset of updated data
          data = {
              'description': 'This is a new description'
              }
          # do the update
          asset = my.server.update(search_key, data)

          print asset.get("description")

Note that the search key is used to identify the precise sObject being
updated. This search key uniquely identifies an sObject in TACTIC. With
this search key, TACTIC is able to precisely update the specified
sObject.

**Javascript Client API**

The TACTIC Client API can be accessed in Javascript as well as Python.
One can deduce its usage from the Python Client API doc. One main point
to notice is that the keyparams in the Client API doc, also known as
keyword argumnets, should be expressed as a hash \\{} in javascript. Here
are some examples:

\\1. Using the eval() function, we want to find all the anim snapshots
checked in with the asset chr001.

    var server = TacticServerStub.get();
    var exp = "@SOBJECT(sthpw/snapshot['context','anim'])";
    var result = server.eval(exp,{search_keys:['prod/asset?project=sample3d&code=chr001']});
    log.critical(result);

\\2. Display the notes written for the selected assets in the UI.

    var server = TacticServerStub.get()
    var search_keys = spt.table.get_selected_search_keys();
    var exp = "@SOBJECT(sthpw/note)";
    if (search_keys.length > 0){
        var result = server.eval(exp, {search_keys: search_keys});
        log.critical(result);
    }

\\3. Display only the task code in anim or lgt process with description
containing the word fire, not specific to any particular asset.

    var server = TacticServerStub.get();
    var exp = "@GET(sthpw/task['process', 'in', 'anim|lgt']['description','EQ','fire'].code)";
    var result = server.eval(exp);
    log.critical(result);

\\4. To insert a note for an asset chr001 under the model process and
context.

    var server = TacticServerStub.get();
    var sk = server.build_search_key('prod/asset','chr001');
    server.insert('sthpw/note', {'note': 'A test note', process: 'model', context: 'model', login: 'admin'},
    {parent_key: sk});

\\5. To get the latest snapshot of the asset chr001 for the current
project

    var server = TacticServerStub.get();
    var sk = server.build_search_key('prod/asset','chr001');
    var snapshot = server.get_snapshot(sk,  {context:'anim', include_paths_dict: true, versionless: false});
    log.critical(snapshot);

\\6. To run a query of snapshots using filters and limit keyword
argumnets

    var server = TacticServerStub.get();
    var filters = [];
    // use built-in expression operator EQ, NEQ, EQI, or NEQI to specify the search_type has to contain prod/shot
    filters.push(['search_type', 'EQ','prod/shot']);
    filters.push(['project_code','sample3d']);
    var snapshot = server.query_snapshots({filters: filters, limit: 5});
    log.critical(snapshot);
