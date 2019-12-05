# finish

**finish(description='')**

End the current transaction and cleans it up

**keyparam:**

description: this will be recorded in the transaction log as the

description of the transction

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
