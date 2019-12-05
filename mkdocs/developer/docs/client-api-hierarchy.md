# Navigating Search Type Hierarchy

**Hierarchies**

Each project in TACTIC contains a collection of search types. The schema
defines how these search types are related to each other. There is a
wide variety of possible ways that two search types can be related to
each other. The schema abstracts these relationships so that it is easy
to navigate through these hierarchies.

The following relationship types are used:

-   **parent\_code**: The column named "parent\_code" is used to define the
    parent code. You would need to look at the schema definition to know the
    exact search\_type of each parent. This relationship type has the
    advantage that it standardizes the name of the parent column.

-   **sobject\_code**: A naming convention of &lt;parent\_table&gt;\_code is used to
    define the parent code. SObjects reference each other through the "code"
    column, which is guaranteed to be unique. (The code column is used
    instead of "id" because it is easier to read.) This is a more intuitive
    relationship type than "parent\_code".

-   **search\_type**: The parent code is defined by an arbitrary relationship
    using two columns: search\_type and search\_id. Together, they uniquely
    identify parent SObjects.

-   **search\_key**: The parent code is defined by a single column called
    "search\_key," which contains a unique identifier for the parent.

Of the above types, sobject\_code and search\_type are used most often.
Any of these types can be used at any time and be related to each other.
Having an intimate knowledge of these relationships can be confusing, so
to keep things organized a project schema is used to define which
search\_types can be related to other search\_types and in which ways. In
other words, TACTIC uses the schema definition for the project to
abstract relationships and make them easier to understand.

**Methods**

**get\_parent()**

There are a number of methods to help navigate through the search type
hierarchy.

Every search type can have a single parent type. You can query this type
with get\_parent\_type(). For example, to find the parent type of a
"prod/asset":

    search_type = "prod/asset"
    parent_type = server.get_parent_type(search_type)
    print parent_type

When executed, the above code snippet would return the string
"prod/asset\_library".

**get\_child\_types()**

When the parent/child relationship is search\_type or search\_key, each
SObject will have its own parent. In this case, the parent would return
"\*", which indicates that all search types are a possible parent.

To find child types, use the get\_child\_types() function. This function
returns a list because a search\_type can and will have a number of
search types as children. This method will return all of the possible
search types.

**get\_parent()**

Most search\_types will only have one parent type (except those that
defer the parentage to the SObject itself). The get\_parent() method
allows you to obtain the individual parent SObject of an SObject.

    search_type = "prod/asset"
    code = "vehicle011"
    search_key = server.build_search_key(search_type, code)
    parent = server.get_parent(search_key)
    print parent.get('code')

Executing the above code snippet would result in the output:

    vehicles

because the parent type of "prod/asset" is "prod/asset\_library" and the
parent of "vehicle011" is the asset library "vehicles"

**get\_all\_children()**

Search types can and will have a number of child types. Some types defer
the parentage to the SObject itself to determine the parent type. So
when searching for children of parents, it is necessary to pass in a
child type to narrow down the search. The options for child types can be
found by the method get\_child\_types().

    search_type = "prod/asset_library"
    code = "vehicles"
    search_key = server.build_search_key(search_type, code)
    child_type = "prod/asset"
    children = server.get_all_children(search_key, child_type)
    for child in children:
        print child.get('code')

This code snippet will print out all of the codes of the children of
this particular asset library, namely all of the assets in the asset
library "vehicles."

get\_all\_children() can also be used to get snapshots (sthpw/snapshot) or
tasks (sthpw/task) as well. These are special child types that defer the
parent type to the individual SObjects.

    search_type = 'prod/asset'
    code = 'vehicle011'
    search_key = seaver.build_search_key(search_type, code)
    child_type = 'sthpw/task'
    tasks = server.get_all_children(search_key, child_type)

This code snippet will obtain all of the tasks associated with
vehicle011.
