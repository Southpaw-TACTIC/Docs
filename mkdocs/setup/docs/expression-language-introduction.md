# TACTIC Expression Language Introduction

**TACTIC Expression Language Introduction**

**Introduction**

This document describes the construct of the **TEL** TACTIC Expression
Language. This language is a shorthand form to quickly retrieve
information about related Search Objects. The expression either starts
with a list of Search Objects and the operations of the expression
language operate on these lists (this is quite similar to LISP in
concept) or it can be used as an absolute search.

The expression language also borrows from spreadsheet syntax which is
familiar to many people. The reason behind using an expression language
is that it is much simpler and compact that using code or direct SQL.
The TACTIC expression language is designed to be able to easily retrieve
data in a single command that would otherwise take many lines of code.

**Simple Example**

The expression often starts with a list of Search Objects and then
operates on these Search Objects.

If you have a list of "prod/sequence" Search Objects, then the
following:

    @GET(prod/shot.code)

will return a list of codes of these prod/shot Search Objects related to
the starting "prod/sequence". The notation for the method GET is of the
form &lt;search\_type&gt;.&lt;column&gt;. As will be shown below, multiple
search\_types can be strung together to navigate across related
search\_types. The @GET function operate on a list and returned a list.

If no starting sObject is given, this expression will return a list of
codes for every shot in the project. In the python or javascript API,
you can control whether there is a starting sobject with the kwarg
search\_keys

With the above example, here is how to get the shot codes for the given
sequence with the code "seq001":

**Python API**

server = TacticServerStub.get()

expr = "@GET(prod/shot.code)"

result = server.eval(expr,
search\_keys=\['prod/sequence?project=vfx&code=seq001'\])

By default, the result returned is a list unless you specify the kwarg
single=True in server.eval()

result = server.eval(expr,
search\_keys=\['prod/sequence?project=vfx&code=seq001'\], single=True)

In Javascript, via the Script Edtor, you can achieve the same result
with these scripts:

**Javascript API**

var server = TacticServerStub.get();

var expr = "@GET(prod/shot.code)"

var result = server.eval(expr, \\{search\_keys:
\['prod/sequence?project=vfx&code=seq001'\], single: true});

In certain places, like in a Custom Layout Element, Expression Element
in a Table, or notification set-up, there is an assumed starting
sObject, which is the one you are viewing or the notification event
refers to during an update or insert action.

**Searching**

The expression language can be used as a shorthand for search for Search
Objects. This is often convenient because the expression language is a
pure string and can be stored a number of formats, including XML.

The @SOBJECT method will retrieve entire Search Objects.

Search for all assets

    @SOBJECT(prod/asset)

Search only for characters by applying a filter

    @SOBJECT(prod/asset['asset_library','chr']

You can also apply multiple filters. And operation is implied

    @SOBJECT(prod/asset['asset_library','chr']['timestamp','>','2009-01-01'])

You can also apply multiple filters. To use OR operation with more than
2 filters. For example, with code containing the word prop1, OR
asset\_library is chr, OR timestamp after 2009-01-01. Note: EQ stands for
case-sensitive match.

    @SOBJECT(prod/asset['begin']['asset_library','chr']['timestamp','>','2009-01-01']['code','EQ','prop1']['or'])

To use OR operation with 2 filters followed by an AND operation. For
example, with asset\_library is chr OR timestamp after 2009-01-01 AND
code containing the word prop1. If there are only 2 filters, there is no
need to sandwich it with begin.

    @SOBJECT(prod/asset['begin']['asset_library','chr']['timestamp','>','2009-01-01']['or']['code','EQ','prop1'])

To

    @SOBJECT(prod/asset['begin']['asset_library','chr']['timestamp','>','2009-01-01']['or']['code','EQ','prop1'])

Note that full filter operations from the Client API are supported.

**Navigating Search Types**

One of the true powers of the expression language is the simplicity in
which it can navigate between various related Search Types using a
navigational syntax. The expression language makes use of the project
schema to navigate dependencies between the search\_types. For example a
sequence is related to a shot.

The navigational syntax is used as arguments for many aggregate methods.
When detected, the expression language will perform a search through the
hierarchy to retrieve the desired search results.

A simple example of the navigation syntax in the expression language is
as follows:

    @GET(prod/sequence.code)

This expression will get all of the codes of the sequences of related to
each Search Object.

The expression can also navigate multiple levels of search types to dig
deeply into the hierarchy. For example, this will get all of the
descriptions of all of the episodes that belong to the sequences of the
original shots.

    @GET(prod/sequence.prod/episode.description)

Another useful illustration is to get all of the tasks of all of the
shots:

    @SOBJECT(prod/shot.sthpw/task)

Get the last 50 tasks ordered by process of all of the shots:

    @SOBJECT(prod/shot.sthpw/task['@ORDER_BY','process']['@LIMIT','50'])

**Aggregate functions**

The expression language defines a number of aggregate functions which
will operate on the list.

This will give the addition of all the duration attributes of the
provided shots.

    @SUM(prod/shot.duration)

This will give the average duration attribute of all of the shots.

    @AVG(prod/shot.duration)

This will give a count of all of the Search Objects

    @COUNT(prod/shot)

All of these aggregates return a single value which can be used to
operate on other lists.

**Operations**

The expression language operates on lists. The operator will operate on
each element of the list independently and return a list For example
when doing a subtraction operation on items:

    @GET(prod/shot.end_frame) - @GET(prod/shot.start_frame)

The first @GET will return a list of start frames and the second @GET
will return a list end frames. When two lists are operated on the
results are calculated based on items at the same position in each list.
So if we had two lists:

    [300, 155, 100] - [100, 100, 100] = [200, 55, 0]

Similarly, lists will be multiplied as follows

    [5, 4, 3] * [5, 4, 3] = [25, 16, 9]

The expression language supports most operation support by the python
language itself.

    >>> Search.eval("5 * 25")
    125.0

    >>> Search.eval("5 + 25")
    30.0

    >>> Search.eval("(25 - 5) * 5")
    100.0

    >>> Search.eval("5 / 25") 0.20000000000000001

    >>> Search.eval("@COUNT(sthpw/task) * 5")
    2310.0

    >>> Search.eval("@COUNT(sthpw/task) > 0")
    True

    >>> Search.eval("@COUNT(sthpw/task) == 462")
    True

    >>> Search.eval("@COUNT(sthpw/task) != 462")
    False

The expression language also supports the regular expression syntax

The following tests whether the name\_first column starts with "John"

    @GET(.name_first) ~ '^John'

**More complex operations**

You can do more complex operations by combining the above. The following
will return a cost list of all of the shots (assigned user wage \* number
of hours worked).

    @GET(prod/shot.sthpw/task.sthpw/login.wage) * @GET(prod/shot.num_hours)

You could add them all together using @SUM this to get the total

    @SUM(
      @GET(prod/shot.sthpw/task.sthpw/login.wage) * @GET(prod/shot.num_hours)
    )

There are times the sObjects returned are not unique. The @UNIQUE
operator can be used to return a unique list of result. The following
returns the unique list of login sObjects related to the task list
provided. The @COUNT operator computes the total number of login
sObjects.

     # my.tasks is a list of tasks
     expression = "@COUNT(@UNIQUE(@SOBJECT(sthpw/login)))"
     result = my.parser.eval(expression, my.tasks)

**Manipulating Strings**

Most of the operations in the expression language operate on lists and
either return lists or return single values. However, it is often
required that expressions be used in string concatenation. A simplified
notation is to use curly brackets \\{} to represent an operation that
converts the result of an expression into a string.

For a file to be named chr001\_model.png, we could use:

    {@GET(prod/asset.code)}_{@GET(sthpw/snapshot.context)}.png

-   The file naming conventions do not current use the expression language. The presently use a simplified expression language. The plan
    is to merge the two at some point.

**String Formatting**

For string values, the string operator them can use standard print
formatting:

    v{@GET(sthpw/snapshot.version),%0.3d}

will return "v012", for example.

The expression language also supports formatting through regular
expressions

    { @GET(prod/asset.description),|^(\w{5})| }

This will get the first 5 word characters for the description. Since the
full expression language is supported, it is possible to extract a wide
variety of parts. Anything matched with () will be returned as the
value.

\*\*If there are multiple groupings, the expression language will
concatenate the values together.

The following will return the first 3 and last 3 characters of the
description.

    { @GET(prod/asset.description),|^(\w{3}).*(\w{3})$| }

The following will return the last 5 characters of the description of
the current SObject even if it is written in French or Chinese.

    { @GET(.description),|^(.{5})$| }

**Time related formatting**

The following formats a timestamp by extracting just the month and date
(old way):

    { @GET(.timestamp), %b-%m}

The following formats a timestamp by extracting just the year

    { @GET(.timestamp), %Y}

The following removes the hours, minutes and seconds from the built-in
$TODAY variable so only 2011-11-11 is displayed

    { $TODAY,|([^\s]+)| }

The following formats a timestamp by using the new @FORMAT function

    @FORMAT( @GET(.timestamp), '31/12/1999')

    @FORMAT( @GET(.timestamp), 'Dec 31, 1999')

The following formats it according to a project wide date-time setting
or date-only setting. You can define what DATETIME and DATE is in the
Project Settings page.

    @FORMAT( @GET(.timestamp), 'DATETIME')
    @FORMAT( @GET(.timestamp), 'DATE')

Either of the following formats a frame count into timecode

    @FORMAT( @GET(.frame_count), 'MM:SS.FF')

The following formats a frame count into hours, minutes and seconds in
30fps, leaving out the frames.

    @FORMAT( @GET(.frame_count), 'HH:MM:SS', '30')

The following formats a cost column in currency format

    @FORMAT(@GET(.cost), '-$1,234.00')

'31/12/99 13:37' can be used to show both date and time

**Shorthand (mostly for backwards compatibility)**

    @GET(sobject.end_frame) - @GET(sobject.start_frame)

    or

    @GET(.end_frame) - @GET(.start_frame)

Or replicate file naming conventions

    {sobject.code}_{snapshot.context}_v{version}.{ext}

In the file naming convention language, the are a number of short hand
keywords:

sObject Keywords: sobject, snapshot, file, parent , search\_type

Attribute Keywords: context, version, ext, basefile
