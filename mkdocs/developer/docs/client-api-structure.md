# Client API Structure

**Directory Structure**

The client API files are located in the directory
&lt;tactic\_install\_dir&gt;/src/client. This directory contains all the files
need for the client API. Typically you would copy all of the files in
this directory to a location visible to the client machine.

There are a number of directories in this Client API directory:

-   bin: contains useful supported scripts.

-   test: contains unit tests for the client API.

-   examples: contains a number of small examples to be used for reference.

-   tactic\_client\_lib: the main directory for the Client API.

The main directory "tactic\_client\_lib" is the base module that you will
use to access all of the TACTIC client APIs. Typically, you would import
this module when working with the client API:

    from tactic_client_lib import TacticServerStub

There are a number of subdirectories under tactic\_client\_lib:

-   **tactic\_server\_stub.py**: contains the main server class "TacticServerStub". This class encapsulates all interactions to the
    TACTIC server and is generally the primary class used with the client API.

-   **(ALPHA) application**: contains all the classes that deal with
    interaction with third-party applications. It provides an abstraction
    layer for applications and allows you to set data that can be used by
    TACTIC’s introspection (verification).

-   **common**: contains a number of convenience functions that are commonly used.

-   **interpreter**: contains the client-side pipeline interpreter. This
    interpreter executes pipelines defined on the TACTIC server. These
    pipelines can be used to create highly complex modular client-side processes. Typical uses are for the checkin and checkout pipelines.

-   **test**: contains a number of test classes used by the unit tests.

You should point to the Client API by having the directory
src/client/tactic\_client\_lib stored somewhere accessible to client
machines. Import the Tactic\_Server\_Stub with the following line in your
script from tactic\_client\_lib:

    import Tactic_Server_Stub

(For more details, visit the Southpaw Support site.)

**tactic\_server\_stub.py**

This module contains the TacticServerStub class, which encapsulates all
interactions with the TACTIC server. This class lets you make full use
of the TACTIC architecture in your custom applications. Although the
TacticServerStub can be instantiated, it is often preferable to use it
as a singleton so you can set up the server once and make use of it from
various locations in your applications:

    from tactic_client_lib import TacticServerStub
    server = TacticServerStub.get()

Once you have a reference to the TacticServerStub, you must set it up
using three essential parameters: server, ticket, project. These
parameters are described in more detail in the client API setup
documentation.

**Interpreter**

This directory contains all the code needed to execute pipelines on the
client. Pipelines in TACTIC are arbitrary process flow graphs. These
pipelines have a number of advantages over other methods:

-   They promote reusability, with each process handler having a
    consistent interface from which it can extract information. Typically,
    handlers are like mini programs which for the most part are
    compartmentalized and have little to do with each other.

-   They can be visualized. Using the pipeline editor, the entire flow of
    the pipeline can be graphically visualized

-   They can be specialized. Each aspect of the pipeline can be written by
    those team members most suited for the task.

-   They lower the bar to creating complex pipelines. With a large library
    of well-written handlers, it becomes possible for non-developers to
    create pipelines by graphically piecing processes together.

**Application**

This directory handles all of TACTIC’s interaction with third-party
applications.

**Note**

This section is still in active development.
