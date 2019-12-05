# eval

**eval(expression, search\_keys=\[\], mode=None, single=False, vars={}, show\_retired=False)**

Evaluate the expression. This expression uses the TACTIC expression
language to retrieve results. For more information, refer to the
expression language documentation.

**param:**

**expression** - string expression

**keyparam:**

**search\_keys** - the starting point for the expression.

**mode - string|expression** - determines the starting mode of the expression

**single - True|False** - True value forces a single return value

**vars** - user defined variable

**show\_retired** - defaults to False to not return retired items

**return:**

results of the expression. The results depend on the exact nature

of the expression.

**example:**

\#1. Search for snapshots with context beginning with 'model' for the asset with the search key 'prod/asset?project=sample3d&id=96'

            server = TacticServerStub.get()

            exp = "@SOBJECT(sthpw/snapshot['context','EQ','^model'])"

            result = server.eval(exp, search_keys=['prod/asset?project=sample3d&id=96'])

Please refer to the expression language documentation for numerous

examples on how to use the expression language.
