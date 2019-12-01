# build\_search\_type

**build\_search\_type(search\_type, project\_code=None)**

Convenience method to build a search type from its components. It is
a simple method that build the proper format for project scoped search
types. A full search type has the form:
prod/asset?project=bar.
It uniquely defines a type of sobject in a project.

**param:**

**search\_type** - the unique identifier of a search type: ie prod/asset

**project\_code (optional)** - an optional project code. If this is not

included, the project from get\_ticket() is added.

**return:**

**string** - search type

**example:**

            search_type = "prod/asset"

            full_search_type = server.build_search_type(search_type)
