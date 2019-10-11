# Load-Balancing TACTIC

TACTIC runs on a multi-threaded application server ("Cherrypy"), but
this application server uses Python threads and not system threads. This
means that all of the threads in a single python process run on the same
processor.

To overcome this limitation, you should run a number of full TACTIC
processes across a number of different ports and allow the webserver to
load-balance requests across these ports. By default in the the tactic
installation config file, \`
/home/apache/projects/config/tactic\_linux-conf.xml\`, the
process count is set to 3. Add this entry if it does not exist.

    <services>
        ...
        ...
        <process_count>3</process_count>
    </services>

There are many ways to load-balance TACTIC. Two different ways will be
described in the following:

> **Note**
>
> Warning: For load balancing, only use either:
>
> \\1) the Proxy Balancer method (recommended)
>
> **or**
>
> \\2) the RewriteRule method (not recommended).
>
> Do **not** use both methods at the same time.

\\1. The first way (recommended way) is to make use of Apache’s
`proxy_balancer_module` . Ensure it is already enabled in the main
Apache config file in /etc/httpd/conf/httpd.conf. In the `tactic.conf`
file (provided with the TACTIC installation usually placed near the
Apache 2 installation config area like /etc/httpd/conf.d/.. or
/etc/apache2/..), make sure these lines below are present. This set-up
corresponds to a process\_count of 3 in the `tactic.conf` file. If there
are more, you just have to add more\*BalancerMember\* line accordingly.

    ProxyPreserveHost on

    # Using the ProxyPass directives
    <Proxy balancer://tactic>
      BalancerMember http://localhost:8081/tactic
      BalancerMember http://localhost:8082/tactic
      BalancerMember http://localhost:8083/tactic
    </Proxy>
    ProxyPass /tactic balancer://tactic
    ProxyPass /projects balancer://tactic

This method is more desirable as it doesn’t need the load\_balance.txt
required for the second method. In addition, it is mandatory if the
process\_time\_alive directive is used under services in the TACTIC config
file in /home/apache/projects/config/tactic\_linux-conf.xml.

\\2. The second way (old way) is to make use of Apache’s
`rewrite_module`. In the `tactic.conf` file (provided with the TACTIC
installation usually placed near the Apache 2 installation config area
like /etc/httpd/conf.d/.. or /etc/apache2/..), comment out the lines
under "for cherrypy":

    # for cherrypy
    #RewriteRule ^/tactic/(.+)$ http://localhost:8081/tactic/$1 [P,L]
    #RewriteRule ^/tactic http://localhost:8081/tactic/ [P,L]
    #RewriteRule ^/projects/(.+)$ http://localhost:8081/tactic/$1 [P,L]
    #RewriteRule ^/projects http://localhost:8081/tactic/ [P,L]

Then in the same file uncomment the lines for the random load balancing
scheme:

    # This is for using a random load_balancing scheme
    RewriteMap lb rnd:/home/apache/sites/load_balance.txt
    RewriteRule ^/tactic/(.+)$ http://${lb:dynamic}/tactic/$1 [P,L]
    RewriteRule ^/projects/(.+)$ http://${lb:dynamic}/tactic/$1 [P,L]
    RewriteRule ^/tactic http://${lb:dynamic}/tactic/ [P,L]
    RewriteRule ^/projects http://${lb:dynamic}/tactic/ [P,L]

These lines will look at the file
“/home/apache/sites/load\_balance.txt” to find out how to replace the
variable $\\{lb:dynamic} with a randomly chosen value from a list.

Note: The path for load\_balance.txt cannot have spaces in it or Apache
service will not start.

A sample `load_balance.txt` file looks like the following:

    ##
    ## load_balance.txt -- rewriting map
    ##
    dynamic localhost:8081|localhost:8082|localhost:8083

The process\_count being set to 3 corresponds to the three processes
running at port 8081, 8082, 8083 respectively. You can see the three
startup.py processes by running:

    ps -wef | grep python

The higher the process\_count is set, the more memory is needed in the
system. If you set it to 10 for heavier usage, the load\_balance.txt
should look like this:

    ## this is in one line in the file
    dynamic localhost:8081|localhost:8082|localhost:8083|localhost:8084|localhost:8085|localhost:8086
            |localhost:8087|localhost:8088|localhost:8089|localhost:8090

**Restart the apache service and tactic service after changing their
config files.**

To verify if you have set up load-balancing correctly, please follow
this tutorial in our support site:

    http://support.southpawtech.com/tutorial/simple-load-balance-test

For more information on load balancing using mod\_rewrite, refer to the
mod\_rewrite documentation located at:

**<http://httpd.apache.org/docs/2.0/mod/mod_rewrite.html>**
