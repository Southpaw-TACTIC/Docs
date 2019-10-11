# TACTIC Scalable Configuration Examples

TACTIC and its co-services can be distributed over multiple machines.
This can be specific combinations of TACTIC and co-services.

For purposes of instruction and brevity, the configuration examples are
not targeted towards particular multiple machine solutions; rather, the
configuration examples can be altered to suit the individual
environment.

Here are some examples:

-   HTTP server, DB, and TACTIC server

-   HTTP server, HTTP server, DB server, and TACTIC server

-   HTTP server, TACTIC server 1, TACTIC server 2, and DB server,

and so on.

**Example Configuration: One Server**

Single machine for small scale environment, limited usage

-   all services on one machine

**Example Configuration: Two Servers**

Two machines to spread workload.

-   HTTP and TACTIC server

-   DB server

**Example Configuration: Three Servers**

For larger environments where automated usage and heavy reporting usage
by users through the GUI.

-   HTTP & DB server

-   TACTIC server 1

-   TACTIC server 2


