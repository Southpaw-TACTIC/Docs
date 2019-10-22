# Configuring SSL

This document discusses security layers that can be implemented on top
of the TACTIC service.

**Services covered**

-   Apache HTTP server

-   IIS HTTP server

-   PPTP server

-   IPsec

Southpaw Technology does not provide any support, either direct or
implied, for remote access.

Any application that is put on a public network can potentially be
compromised, even with rigorous security testing. TACTIC, in its current
version, has not been production tested for security scenarios outside
of completely trusted networks like intranets. This document does not
make any claims that TACTIC has any level of security beyond what its
current architecture design allows.

TACTIC is a bandwidth-intensive application, and client-server
performance will be affected by any number of network issues between the
client and the server.

There are numerous elements of functionality that go beyond utilizing
HTTP port access in enterprise applications of TACTIC. Many 3rd party
applications that communicate with TACTIC will produce unexpected
behavior when utilized in a fashion that was not intended for the
product, such as use in remote applications.

**TACTIC on public networks**

HTTP transport co-services can be configured to provide authentication
services to TACTIC.

**HTTP zone access**

The simplest form of HTTP security authentication zone access. To enable
different security scenarios, the HTTP service must be configured for
use of these scenarios. Configuration files (usually called .htaccess
files) contain a number of settings that can be used for integrating the
application with the capabilities of the Web server.

When enabling password zone access, the password is transmitted to the
server in cleartext, unless TLS is enabled.

**Apache**

Apache uses either directives for directory access in the httpd.conf
file, or can be enabled on a per-directory basis, with the use of a
.htaccess file. Either way can be used. Apache provides modules for
LDAP, MySQL, flat-file, ADS, and many other authentication mechanisms.

**IIS**

IIS can be configured at the top level through the IIS snap-in, or by
individual configuration file. IIS 7 uses a file called Web.config to
hold settings for integration with applications. The Web.config file
contains information that control module loading, security
configuration, session state configuration, and application language and
compilation settings.

## SSL

### Overview

TACTIC can be configured to use the SSL transport layer. This layer is
independent of the TACTIC service, and can be tailored to the needs of
the deployment without major changes to the TACTIC service.

Both major HTTP servers can be configured for SSL support. There are
many materials online available for configuration of the various flavors
of these two major HTTP service projects.

Since there are many different versions of these servers, a simple
search of Windows 2003 IIS SSL as an example will yield many HOWTOs
and configuration references. Please consult the documentation for these
services.

The configuration examples that have been set out below are by no means
complete. Depending on the HTTP service used, and the platform used,
these examples may not be enough set directives or steps to properly
complete the SSL process. They are given as guides.

**Steps**

The major steps to utilizing SSL in with TACTIC are

-   Enabling TACTIC to converse with SSL

-   Enabling the SSL service

-   Creating a Virtual Server, or extending the existing server to accept
    SSL

-   Providing CA certificates


### TACTIC configuration

The SSL HTTP layer is kept separate from TACTIC via a proxy, so the only
configuration change required of TACTIC is in the tactic\_(OS).conf file.
The &lt;security&gt;&lt;protocol&gt; directive must tell TACTIC to expect an SSL
delivery.

    <security>
        <protocol>https</protocol>
    </security>

The setting can be set to either "http" or "https".

### Apache

The apache project uses mod\_ssl as a modular way of inserting SSL
capabilities into the HTTP service.

The example OS is Fedora 11. "Yum" is used to add SSL to apache.

    [root@lindsay conf.d]# yum install mod_ssl
    Loaded plugins: refresh-packagekit
    …
    Complete!
    [root@lindsay conf.d]#

Once mod\_ssl is added, the Apache configuration should contain at least
these directives. The example directives are contained in
conf.d/ssl.conf in the Fedora 11 example. File locations will vary
according to OS.

    LoadModule ssl_module modules/mod_ssl.so
    Listen 443

    SSLPassPhraseDialog  builtin
    SSLSessionCache         shmcb:/var/cache/mod_ssl/scache(512000)
    SSLSessionCacheTimeout  300
    SSLMutex default
    SSLRandomSeed startup file:/dev/urandom  256
    SSLRandomSeed connect builtin
    SSLCryptoDevice builtin
    <VirtualHost _default_:443>
    SSLEngine on
    SSLProtocol all -SSLv2
    SSLCipherSuite ALL:!ADH:!EXPORT:!SSLv2:RC4+RSA:+HIGH:+MEDIUM:+LOW
    SLCertificateFile /etc/pki/tls/certs/localhost.crt
    SSLCertificateFile /etc/pki/tls/certs/localhost.crt
    SSLCertificateKeyFile /etc/pki/tls/private/localhost.key

As soon as its added and the server is restarted, the SSL service
becomes available on the network interface that apache is running on.

### IIS

IIS can be configured at the top level through the IIS snap-in, or by
individual configuration file.

To configure SSL on a Web server or a Web site,

1. In IIS Manager, double-click the local computer, and then
double-click the Web Sites folder. 
2. Right-click the Web site or file
that you want to protect with SSL, and then click Properties. 
3. Under Web site identification click Advanced. 
4. In the Advanced Web site
identification box, under Multiple identities for this Web site, verify
that the Web site IP address is assigned to port 443, the default port
for secure communications, and then click OK. Optionally, to configure
more SSL ports for this Web site, click Add under Multiple identities of
this Web site, and then click OK. 
5. On the Directory Security or File
Security tab, under Secure communications, click Edit. 
6. In the Secure
Communications box, select the Require secure channel (SSL) check box.
7. To enable SSL client certificate authentication and mapping features,
select the Enable client certificate mapping check box, click Edit, add
the 1-to-1 or many-to-1 mappings you need, and then click OK three
times.

### Secure transaction processing

Processing transactions securely on the web means that there is a need
to be able to transmit information between the web site and the customer
in a manner that makes it difficult for other people to intercept and
read. SSL, or Secure Sockets Layer, takes care of this. It works through
a combination of programs and encryption/decryption routines that exist
on the web services host, and in browser programs (like Firefox and
Internet Explorer)

### Performance

TLS has encryption/decryption routines as part of its security. These
routines can be bandwidth/CPU intensive. Any usage of TLS can compromise
TACTIC, if the routines are incorporated into the same host as the
TACTIC service. See guides on load-balancing for details on offsetting
this.

## VPN

A VPN will provide the most trouble-free access to TACTIC remotely. In
this scenario, the authentication/encryption routines are completely
removed from the realm of TACTIC configuration. This not only helps to
isolate TACTIC from complex configuration issues, but also allows for
isolated troubleshooting of remote access issues.

## PPTP

PPTP is Microsoft supplied product. If an enterprise deployment of
TACTIC includes ADS authentication, then PPTP can be used as the VPN
transport layer. Usually, deployment is quite easily done. In PPTP,
usernames and passwords are used to complete the VPN link. PPTP can be
considered the "road-warrior" VPN, meaning that it is easily deployed
to users.

## IPsec

Ipsec is a suite of protocols used to secure data between hosts. A VPN
can be transported on top of this protocol. Typically, two remote hosts
are configured to communicate with each other, such as routers. This
type of VPN is typically used to connect two offices together.

## Hardware VPNs

Hardware VPNs such as offerings provided by companies like Cisco, can be
easily implemented. These Systems are designed for minimal ramp-up, and
can be implemented quickly.

##  Security Terms

**MITM** 

“is a form of active eavesdropping in which the attacker makes
independent connections with the victims and relays messages between
them, making them believe that they are talking directly to each other
over a private connection, when in fact the entire conversation is
controlled by the attacker. The attacker must be able to intercept all
messages going between the two victims and inject new ones, which is
straightforward in many circumstances (for example, an attacker within
reception range of an unencrypted Wi-Fi wireless access point, can
insert himself as a man-in-the-middle).

**SSL (Wikipedia)**

“Transport Layer Security (TLS) and its predecessor, Secure Sockets
Layer (SSL), are cryptographic protocols that provide security for
communications over networks such as the Internet. TLS and SSL encrypt
the segments of network connections at the Transport Layer end-to-end.

**Cleartext (Wikipedia)**

Cleartext is transmitted, unencrypted text.

“In a cryptosystem, weaknesses can be introduced through insecure
handling of plaintext, allowing an attacker to bypass the cryptography
altogether. Plaintext is vulnerable in use and in storage, whether in
electronic or paper format. “

**PPTP (wikipedia)**

The Point-to-Point Tunneling Protocol (PPTP) is a method for
implementing virtual private networks. PPTP uses a control channel over
TCP and a GRE tunnel operating to encapsulate PPP packets.

The PPTP specification does not describe encryption or authentication
features and relies on the PPP protocol being tunneled to implement
security functionality. However the most common PPTP implementation,
shipping with the Microsoft Windows product families, implements various
levels of authentication and encryption natively as standard features of
the Windows PPTP stack. The intended use of this protocol is to provide
similar levels of security and remote access as typical VPN products.

**IPSEC (Wikipedia)**

Internet Protocol Security (IPsec) is a protocol suite for securing
Internet Protocol (IP) communications by authenticating and encrypting
each IP packet of a data stream. IPsec also includes protocols for
establishing mutual authentication between agents at the beginning of
the session and negotiation of cryptographic keys to be used during the
session. IPsec can be used to protect data flows between a pair of hosts
(e.g. computer users or servers), between a pair of security gateways
(e.g. routers or firewalls), or between a security gateway and a
host.
