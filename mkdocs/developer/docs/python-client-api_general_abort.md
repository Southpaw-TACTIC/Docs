# abort

**abort(ignore\_files=False)**

Abort the transaction. This undos all commands that occurred
from the beginning of the transactions

**keyparam:**

**ignore\_files: (boolean)** - determines if any files moved into the

repository are left as is. This is useful for very long processes

where it is desireable to keep the files in the repository

even on abort.

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
