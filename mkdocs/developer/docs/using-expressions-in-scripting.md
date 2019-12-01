# Using Expressions in Scripting

**Using Expressions in Python - Server code**

Expressions can be accessed directly through Python code. The expression
language is often very convenient to quickly perform relatively complex
searches quickly and easily.

To access the expressions in Python, you would use the following code:

    from pyasm.biz import ExpressionParser
    parser = ExpressionParser()
    expr = "@GET(prod/shot['code','chr001'].prod/shot_instance.prod/asset.code)"
    result = parser.eval(expr)

It is often more convenient just to access it through the Search module:

    from pyasm.search import Search
    expr = "@GET(prod/shot['code','chr001'].prod/shot_instance.prod/asset.code)"
    result = Search.eval(expr)

**Using Expressions in Python - Client API code**

To access the expressions in the Python Client API, you would use the
following code:

    server = TacticServerStub.get()
    expr = "@GET(prod/shot['code','chr001'].prod/shot_instance.prod/asset.code)"
    result = server.eval(expr)

When the expression language returns sobjects, these will be in the form
of a dictionary like all other sobjects in the client API.

**Using Expressions in Javascript - Client API code**

To access the expressions in the Javascript Client API, you would use
the following code:

    var server = TacticServerStub.get()
    expr = "@GET(prod/shot['code','chr001'].prod/shot_instance.prod/asset.code)"
    var result = server.eval(expr)

**Using Expressions in Widget Config**

The main widget to use expressions is
"tactic.ui.table.ExpressionElementWdg".

When using the ExpressionElementWdg, the starting point of the
expression is automatically the SObject associated with the row. This
allows you to use the shorthand form without having to filter.

    <element name='code'>
      <display class='tactic.ui.table.ExpressionElementWdg'>
        <expression>@GET(.code)</expression>
      </display>
    </element>

**Using Expressions inline in HTML**

When using the CustomLayoutWdg, inline expressions are supported using a
\[expr\]\[/expr\] tag formatting.

    <div>
      <h2>There are [expr]@COUNT(prod/asset['asset_library', 'chr'])[/expr] Characters</h2>
    </div>

**Using Expressions in CustomLayoutWdg**

The custom layout widget has a special html tag which can have html
embedded within it. CustomLayoutWdg provides the ability to embed
expressions within its html definition.

The following demonstrates a widget config using expressions:

            <?xml version='1.0' encoding='UTF-8'?>
    <config>
    <example>
    <html>
      <table>
        <tr><td>[expr]$LOGIN[/expr]</td></tr>
        <tr><td>[expr]{@GET(.code)} : {@GET(.description)}[/expr]</td></tr>
      </table>
    </html>
    </example>
    </config>

Please refere to the CustomLayoutWdg in the Widget Reference
documentation for more information on how to use the CustomLayoutWdg.
