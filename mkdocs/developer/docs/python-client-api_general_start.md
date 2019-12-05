# start

**start(title, description='', transaction\_ticket='')**

Start a transaction. All commands using the client API are bound
in a transaction. The combination of start(), finish() and abort()
makes it possible to group a series of API commands in a single
transaction. The start/finish commands are not necessary for
query operations (like query(…​), get\_snapshot(…​), etc).

**keyparam:**

**title** - the title of the command to be executed. This will show up on

transaction log

**description** - the description of the command. This is more detailed.

**transaction\_ticket** - optionally, one can provide the transaction ticket sequence

**example:**

A full transaction inserting 10 shots. If an error occurs, all 10

inserts will be aborted.

            server.start('Start adding shots')

            try:

                for i in range(0,10):

                    server.insert("prod/shot", { 'code': 'XG%0.3d'%i } )

            except:

                server.abort()

            else:

                server.finish("10 shots added")
