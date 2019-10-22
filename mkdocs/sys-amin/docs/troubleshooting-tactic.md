# TACTIC Service Troubleshooting

## FAQ
1.  **I get a proxy error in my browser that looks like the following:**

        Proxy Error

        The proxy server received an invalid response from an upstream server.
        The proxy server could not handle the request /POST /tactic/admin/
        <http://192.168.14.113/tactic/admin/>/

        Reason: *Error reading from remote server

    This message tells you the TACTIC service has stopped. If you are
    running other processes on port 80 (for example, Skype), this can cause
    a problem with the TACTIC service. Stop the conflicting service. Then
    restart TACTIC in the TSI by logging in as root and running the command:

        service tactic start

2.  **What if the TACTIC host memory is full?**

    If the memory is full, restarting the TACTIC service will remove this memory. If the problem persists or occurs again, contact Southpaw. A
    memory leak can occasionally occur when a user is repeatedly viewing a
    very large table with a huge number of entries (&gt;5000). Restarting the
    service will clear this memory.

3.  **What if the TACTIC host CPU is at 100%?**

    Use the Windows Task Manager to kill the process that is taking 100% of
    the CPU. The TACTIC service will automatically recreate the process.
    Normally, this will clear the problem.

4.  **What if the user sees a Proxy Error?**

    This means that the IIS service cannot contact the TACTIC application server. Look in the Windows services and restart the TACTIC service. If
    the problem persists, contact Southpaw.

## Diagnostics

This command line tool reveals active ports on the local machine.

    leowiz:~ root# netstat -a
    Active Internet connections (including servers)
    Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
    tcp4       0      0  192.168.80.128.ssh     192.168.80.1.46575     ESTABLISHED
    tcp4       0      0  *.*                    *.*                    CLOSED
    tcp46      0      0  *.http                 *.*                    LISTEN
    tcp4       0      0  192.168.80.128.ssh     192.168.80.1.50126     ESTABLISHED
    tcp46      0      0  *.vnc-server           *.*                    LISTEN
    tcp4       0      0  *.ssh                  *.*                    LISTEN
    tcp6       0      0  *.ssh                  *.*                    LISTEN
    tcp4       0      0  localhost.ipp          *.*                    LISTEN
    tcp6       0      0  localhost.ipp          *.*                    LISTEN
    udp4       0      0  *.net-assistant        *.*
    udp4       0      0  192.168.80.128.ntp     *.*
    udp6       0      0  localhost.ntp          *.*
    udp4       0      0  localhost.ntp          *.*
    udp6       0      0  localhost.ntp          *.*
    udp6       0      0  *.ntp                  *.*
    udp4       0      0  *.ntp                  *.*
    udp6       0      0  *.mdns                 *.*
    udp4       0      0  *.mdns                 *.*
    Active LOCAL (UNIX) domain sockets
    Address  Type   Recv-Q Send-Q    Inode     Conn     Refs  Nextref Addr
    41ad880 stream      0      0  46ad830        0        0        0 /private/tmp/ARD_ABJMMRT
    41ce770 stream      0      0        0  3e22e58        0        0 /var/run/mDNSResponder
    3e22e58 stream      0      0        0  41ce770        0        0
    41ce5d8 stream      0      0        0  41ceb28        0        0 /var/tmp/SCDynamicStoreNotifyFileDescriptor-20739
    41ceb28 stream      0      0        0  41ce5d8        0        0
    41cef68 stream      0      0        0  3e22dd0        0        0
    3e22dd0 stream      0      0        0  41cef68        0        0
    3e22088 stream      0      0        0  41ad330        0        0
    41ad330 stream      0      0        0  3e22088        0        0
    41ce6e8 stream      0      0        0  41ce908        0        0
    leowiz:~ root#

This command line tool allows port-scanning of an IP address. It can be
used to remotely determine if a host is running HTTP.

    [root@espresso ~]# nmap 192.168.80.128

    Starting Nmap 4.76 ( http://nmap.org ) at 2010-03-23 15:58 EDT
    Interesting ports on 192.168.80.128:
    Not shown: 997 closed ports
    PORT     STATE SERVICE
    22/tcp   open  ssh
    80/tcp   open  http
    5900/tcp open  vnc
    MAC Address: 00:0C:29:9D:E8:46 (VMware)

    Nmap done: 1 IP address (1 host up) scanned in 6.66 seconds
    [root@espresso ~]#

In the above example, an http service seems to be running on the machine
with the IP of 192.168.80.128

    [root@tactic-tsi ~]#  nmap localhost
    Starting Nmap 4.52 ( http://insecure.org ) at 2010-03-23 16:10 EDT
    Interesting ports on tactic-tsi.localdomain (127.0.0.1):
    Not shown: 1705 closed ports
    PORT      STATE SERVICE
    22/tcp    open  ssh
    80/tcp    open  http
    111/tcp   open  rpcbind
    139/tcp   open  netbios-ssn
    445/tcp   open  microsoft-ds
    5432/tcp  open  postgres
    8081/tcp  open  blackice-icecap
    8082/tcp  open  blackice-alerts
    10000/tcp open  snet-sensor-mgmt

    Nmap done: 1 IP address (1 host up) scanned in 0.101 seconds
    [root@tactic-tsi ~]#

In this example, TACTIC and Apache are running on the same local
machine, with TACTIC taking up 2 processes, and 2 ports, 8081, and 8082
