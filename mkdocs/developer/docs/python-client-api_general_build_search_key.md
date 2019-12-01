# build\_search\_key

**build\_search\_key(search\_type, code, project\_code=None, column='code')**

Convenience method to build a search key from its components. A
search\_key uniquely indentifies a specific sobject. This string
that is returned is heavily used as an argument in the API to
identify an sobject to operate one

A search key has the form: "prod/shot?project=bar&code=XG001"
where search\_type = "prod/shot", project\_code = "bar" and code = "XG001"

**param:**

**search\_type** - the unique identifier of a search type: ie prod/asset

**code** - the unique code of the sobject

**keyparam:**

**project\_code** - an optional project code. If this is not

included, the project from get\_ticket() is added.

**return:**

**string** - search key

**example:**

            search_type = "prod/asset"

            code = "chr001"

            search_key = server.build_search_key(search_type, code)

            e.g. search_key = prod/asset?project=code=chr001

            search_type = "sthpw/login"

            code = "admin"

            search_key = server.build_search_key(search_type, code, column='code')

            e.g. search_key = sthpw/login?code=admin
