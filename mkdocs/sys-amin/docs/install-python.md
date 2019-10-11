# Python Installation

Python is a core element of the TACTIC application. The TACTIC
application has been developed around the the python programming
language.

The installations of both python and supporting modules is a reqirement
in a successful installation of TACTIC. Although the TACTIC core files
can exist on the host machine, it is the existance of both Python and
the supporting modules.

Python 2.5 is the defacto standard for deployments of the TACTIC
application. 2.6 and 2.7 are supported as well. Currently, Python 3.0 is
unsupported.

The installation of core Python is not enough for the successful
installation of TACTIC. Several modules must be installed. These modules
provide the following functions:

-   Extensive **XML support**

-   Connectivity to **DB co-service**

-   \*Win32\*support on windows

-   **Cryptography** support

-   **JSON** support

-   Imaging support

The TACTIC application can support different different Python Supporting
Modules, depending on the version of TACTIC.

There are a number of variables that will affect which modules will be
required to install on a host machine. These considerations are;

-   DB Co-service deployed

-   Desired support module deployed when multiple support module types exist.

<table>
<colgroup>
<col width="34%" />
<col width="32%" />
<col width="32%" />
</colgroup>
<thead>
<tr class="header">
<th>Support Module Type</th>
<th>Module name</th>
<th>TACTIC supported version</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>XML support</p></td>
<td><p>lxml</p></td>
<td><p>All</p></td>
</tr>
<tr class="even">
<td><p>DB Co-Service Support</p></td>
<td><p>Psycopg2 or CX-Oracle (psycopg2 is preferred for postgres database set-up)</p></td>
<td><p>All</p></td>
</tr>
<tr class="odd">
<td><p>Win32 (used in client computers interacting with the server)</p></td>
<td><p>PyWin32</p></td>
<td><p>All</p></td>
</tr>
<tr class="even">
<td><p>Cryptography</p></td>
<td><p>PyCrypto</p></td>
<td><p>All</p></td>
</tr>
<tr class="odd">
<td><p>JSON (not needed since Python 2.6)</p></td>
<td><p>SimpleJSON</p></td>
<td><p>All</p></td>
</tr>
<tr class="even">
<td><p>Imaging</p></td>
<td><p>PIL and ImageMagick (optional)</p></td>
<td><p>All</p></td>
</tr>
</tbody>
</table>

On Windows systems, TACTIC Python and supporting module availability is
through the websites of the supporting module projects. Additionally,
Southpaw Technology supports redistribution of installers for these
modules on the support web site.

On UNIX/Linux systems, the system package manager typically has options
for installing all the required Python packages onto the UNIX host
machine. To find the official distribution of a supporting package, the
search functionality of a package manager is useful.

    #/ yum search lxml
