# HTTP Co-Service Installation/Configuration

The aim of this document is to be able to configure Apache to proxy
TACTIC on a UNIX machine. For Apache on Windows machines, there may be
some slight differences in behavior or steps.

1.  User must have sufficient technical knowledge to navigate the OS
    directories, edit text files, and start/stop services. Knowledge of the
    target web server is required.

2.  TACTIC must be installed on the host machine. It should be runnable
    to the point where all diagnostics presume no error in the TACTIC configuration. In the below examples, TACTIC is installed with all
    default options.

3.  The web server must be installed on the host machine. Since
    different OS’s can have vastly different HTTP service default
    configurations, configuration files will need to be found by command or
    appropriate documentation consultation.

The TACTIC host machine should have the following prerequisites

-   A working TACTIC installation

-   An OS capable of running the target HTTP co-service

The HTTP configuration assumes that the main server is being used to
proxy TACTIC requests, without SSL or virtual servers. TACTIC requires
that the appropriate modules or 3rd party modules are activated.

This document assumes that TACTIC has been configured correctly and is
functioning as expected. It is assumed that TACTIC is installed with
default ports 8081 through 8083. This is the typical default TACTIC
configuration.
