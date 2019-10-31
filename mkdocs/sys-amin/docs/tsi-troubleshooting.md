# TACTIC VM Troubleshooting

1.  **The IP address does not show up when I start up the VM.**

    It is possible that an IP address was not assigned because your host
    machine is not connected to a network. Or, you have a special network
    configuration that may require one of the following settings: 
    
    - Network with DHCP: bridged
    - Network without DHCP: NAT
    - No network: host-only

    **Changing Windows Special Network Configurations**

    In the top right corner of your VMware player, click on the down arrow
    beside the Ethernet button and choose **host-only** , **NAT**, or **bridged**.
    Make sure the **Connected** menu item is checked.

    **Changing Linux Special Network Configurations**

    In the top right corner of your VMware player, right-click on the
    Ethernet button and choose **host-only**, **NAT**, or **bridged**. Make sure
    the **Connected** menu item is checked.

    If the problem persists, refer to the VMware Player documentation by
    pressing F1.

2.  **I do not remember the IP address of the VMware virtual machine.**

    In the VMware player, run the following command in the shell:

        ifconfig

    The IP is the internet address; for example, "192.168.14.101."

    **Refreshing the IP Address**

    If you change the Ethernet settings, you may need to restart the network
    card in the VM. First, you will need to know its number: run the command
    `ifconfig` in the VM shell. You should see a name similar to "ethX",
    where X is the arbitrary number of the interface. To restart "ethX", run
    the following commands:

       ifdown ethX

       ifup ethX

3.  **I get a proxy error in my browser that looks like the following:**

        Proxy Error

        The proxy server received an invalid response from an upstream server.
        The proxy server could not handle the request /POST /tactic/admin/ <http://192.168.14.113/tactic/admin/>/

        Reason: *Error reading from remote server

    This message tells you the TACTIC service has stopped. If you are
    running other processes on port 80 (for example, Skype), this can cause
    a problem with the TACTIC service. Stop the conflicting service. Then
    restart TACTIC in the VM by logging in as root and running the command:

        service tactic start


