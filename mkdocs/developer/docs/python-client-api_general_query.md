# query

**query(search\_type, filters=\[\], columns=\[\], order\_bys=\[\], show\_retired=False, limit=None, offset=None, single=False, distinct=None, return\_sobjects=False)**

General query for sobject information

**param:**

**search\_type** - the key identifying a type of sobject as registered in

the search\_type table.

**keyparam:**

**filters** - an array of filters to alter the search

**columns** - an array of columns whose values should be

retrieved

**order\_bys** - an array of order\_by to alter the search

**show\_retired** - sets whether retired sobjects are also

returned

**limit** - sets the maximum number of results returned

**single** - returns only a single object

**distinct** - specify a distinct column

**return\_sobjects** - return sobjects instead of dictionary. This

works only when using the API on the server.

**parent\_key** - filter to specify a parent sobject

**return:**

**list of dictionary/sobjects** - Each array item represents an sobject

and is a dictionary of name/value pairs

**example:**

                filters = []

                filters.append( ("code", "XG002") )

                order_bys = ['timestamp desc']

                columns = ['code']

                server.query(ticket, "prod/shot", filters, columns, order_bys)

The arguments "filters", "columns", and "order\_bys" are optional

The "filters" argument is a list. Each list item represents an

individual filter. The forms are as follows:

            (column, value)             -> where column = value

            (column, (value1,value2))   -> where column in (value1, value2)

            (column, op, value)         -> where column op value

                where op is ('like', '<=', '>=', '>', '<', 'is', '~', '!~','~*','!~*)

            (value)                     -> where value
