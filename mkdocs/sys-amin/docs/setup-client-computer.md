# Client Computer Setup Requirements

The following are requirements for a client using TACTIC.

**TACTIC Temp Directory Creation**

TACTIC needs to be able to create the TACTIC temporary directory. TACTIC
uses this directory as scratch pad space to store temporary files.

The location of this directory depends on the client operating system:

-   Linux: `/tmp/sthpw`

-   Windows: `C:/sthpw`

-   Mac OS X: `/tmp/sthpw`

**Set environment variables**

`$TACTIC_ASSET_DIR`

This environment variable is used to point to the root of
`asset_base_dir` (the directory where assets are stored). This value
defaults to "/home/apache/assets" in the TACTIC server. On Windows
machines, this path is usually mapped as a letter drive (for example,
Z:\\) or as a UNC path (for example, \\\\server\\volume\\directory\\). This
environment variable is set by the server on the client machine during
loading if it does not already exist.

On a per-project basis, you can set the project setting with the keys
"win32\_client\_repo\_dir" and "linux\_client\_repo\_dir" so one project can
have its asset directory mapped to Drive Z: and another mapped to Drive
T:.

**Browser Plugins**

With the security concerns over Java plugin, TACTIC has lowered the use of Java plugin
in many cases to communicate with the client
computer’s operating system. HTML5 features, where applicable, is adopted instead.
A good example is uploading of files.

To download the latest version of the Java plugin, go to
[www.java.com](http://www.java.com)
