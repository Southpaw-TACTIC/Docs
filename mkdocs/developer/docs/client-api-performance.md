# Performance

The TACTIC Client API interacts with teh server through an XMLRPC
connection. This has a number of advantages and disadvantages that the
developer should be aware of when programming the Client API. XMLRPC is
a standard web sevice protocol built on top of HTTP. This means that the
protocol is stateless. It also means that it requires an HTTP request
for every interaction.

HTTP requests are very slow when compared to running code directly on
the server, so care must be taken to minimize the number of interactions
that occur between the client code and the server code. However, if a
client side application is written with a few basic best practice
guidelines, performance issues should not be a problem.

The TACTIC server should be treated as a special resource. The more
client side processing you do, the lower the load on the server and the
more scalable your client side application.

If possible, it is always preferable to pool queries into a single
request with the use of proper filters: Unfortunately, this sometime
sacrifices pure Object Oriented elegance, but it is a tradeoff that is
well worth it in practice. For example, an object oriented approach to
aquiring data would be:

    shots = server.query("prod/shot", filters=[['sequence_code': 'XG']])
    for shot in shots:
        tasks = server.get_all_children( shot.get('__search_key__'), 'sthpw/task')

When using this approach, a call to the server will be made for every
shot. While, in principle, this will work, it could potentially be quire
slow. A faster way to do this would be to get all of the tasks for all
of the shots in a single statement:

    shots = server.query("prod/shot", filters=[['sequence_code': 'XG']])
    shot_keys = [ shot.get('__search_key__') for shot in shots)
    tasks = server.get_all_children( shot_keys, 'sthpw/task')

This will get all of the tasks for all of the shots in one call to the
server. Of course, some extra processing is required to relate the
retrived tasks to the shot, however, this is all done on the client side
and is executed very quickly.

    tasks_dict = {}
    for task in tasks:
        parent_key = task.get('__parent_key__')
        task_list = tasks_dict.get(parent_key)
        if not task_list:
            task_list = []
            task_dict['parent_key') = task_list
        tasks_list.append(task)

Creating this dictionary will enable rapid look up of the tasks for each
shot.

Of course, this is done for you by providing the "return\_mode" flag.

    tasks = server.get_all_children( shot_keys, 'sthpw/task', return_mode='dict' )

By default, the return mode is "list", which just returns a flat list
allow you to restructure as desired.

This applies to the more general "query" method:

    tasks = server.query("sthpw/task")
