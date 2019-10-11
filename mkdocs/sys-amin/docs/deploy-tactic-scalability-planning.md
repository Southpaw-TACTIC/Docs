# Scalable TACTIC Deployment Planning

The stages of a TACTIC deployment are:

1.   Determining usage requirements
2.   Determining hardware requirements
3.   Determining TACTIC Service and Co-Service Locations
4.   Post Deployment TACTIC upscaling

## Planning Notes

**Determining TACTIC Usage Requirements**

One of the first questions asked in a TACTIC deployment is "what kind of
deployment is required?" This is a hard question to answer unless it is
known beforehand exactly how TACTIC will be used. Since every TACTIC
deployment is customized by the licensee, there is really no way to
calculate accurately the type of load that will eventually be placed on
the TACTIC server. Fortunately, due to TACTIC’s scalable architecture, a
TACTIC deployment can be scaled up easily when there are unforeseen
increases in usage.

**Service Requirements**

In a TACTIC deployment, running the TACTIC service is the primary
function of the TACTIC host machine. The co-services can be deployed to
the location most appropriate for the environment. However, to ensure
scalability and high availability, the co-services should not be
deployed on the TACTIC host for any but the smallest of deployments.

TACTIC uses four major services and co-services in its operation:

-   TACTIC service: provides the API and GUI widget system.

-   Database co-service: provides indexing and storage for asset meta data.

-   HTTP co-service: provides delivery (and return) of raw asset data.

-   Assets storage co-service: provides storage and back-up capabilities
    of raw asset data.

**Limitations**

With TACTIC, you can simply add hardware and load-balance it to handle
more and more requests. You can expand scalability in this way until the
database server itself becomes the bottleneck. Fortunately, with the
introduction of multi-CPU and multi-core machines, database limits are
extremely high.

*User Interfaces:* For applications with end-user interfaces (especially
those using widgets, where complex interface elements need to be
constructed), the load required to process TACTIC requests will remain
much greater than the load required to process SQL calls, no matter how
much hardware is added to handle such requests.

*Client APIs:* Client APIs provide a much thinner layer to the database
and so are optimized to handle lower level requests very rapidly.
However, because API calls are typically used for automated processes,
they can generate a large number of requests quickly, creating a heavy
load on the TACTIC server.

*Load balancing:* this is especially important for render farms, which
can be massive in scale with thousands to tens of thousands of cores. It
ensures that the high volume of requests is evenly distributed to all of
the available TACTIC processes. The exact number of processes required
to handle the high volume is highly dependent on the number of requests
made and to the complexity of the requests. However, because load
balancing will provide near-linear scalability, the number of processes
can be increased to a level that is sufficient for the number of
requests being demanded of the client API.

*Report generation:* TACTIC’s reporting system is powerful and
comprehensive, and the load on host CPUs can increase significantly when
complex reports are being run. Administrators should focus on report
generation when investigating load utilization.

*Checkins:* There are two kinds of complexity when considering
scalability for checkins:

-   Large Checkins: TACTIC offers a wide variety of checkin configurations
    that will accommodate large bandwidth, large files, and complex
    dependency between files.

-   Many Checkins: There are few concerns with a large number of checkins.
    The number of checkins that occur even in the largest of productions is
    small compared to the limits of a database.

## Determining TACTIC Hardware Requirements

**Hardware Overview**

TACTIC works well with most types of hardware, but industry-standard
server level components are highly recommended. The exact configuration
will depend on the specific needs of your facility.

For most deployments, TACTIC can be installed on the typical commodity
hardware used by most small and large enterprises. TACTIC is a
purpose-built relational database at its core, and your hardware choices
can reflect that fact.

TACTIC service requirements: Assuming TACTIC is the only service on the
host, the minimal requirements for a production-level deployment of a
TACTIC host are:

-   CPU: dual core

-   Memory: 4G

-   Disk space needed for TACTIC to run on: 10G

    (assets should be stored elsewhere, on an enterprise quality server)

These requirements represent the recommended absolute minimal hardware
required to run a basic TACTIC service in a production environment. For
development and testing, TACTIC will run on most hardware including
laptops.

*Asset storage:* It is highly recommended that assets be stored on an
enterprise-quality, high-availability server, and not on the TACTIC
host.

*RAID Options:* You can use various RAID configurations to maximize
reliability and performance. For example, you could locate the Operating
System on one physical drive, and the database files on another. Or you
could locate the database on a RAID array.

*Asset meta data:* The amount of asset meta data stored on disk by
TACTIC is insignificant to today’s hardware specifications and need not
be a consideration when choosing a server: reliability and performance
should be higher concerns.

## Determining TACTIC Service Locations

**Segregating Services**

TACTIC offers a number of different services for different purposes. For
example, the TACTIC server can serve out complex widgets, serve out
large numbers of client API requests and perform large, complex
check-ins.

Each type of service has distinct needs, so it is often beneficial to
segregate the services to be independent of each other. This allows each
service to operate within a pool of assigned resources without affecting
(or being affected by) the other services.

For example, if a render farm used a client API script that heavily
loaded the TACTIC server and its requests were shared with user
interface requests, users would experience inconsistent (and
occasionally unacceptably slow) response times. This experience would
cause frustration amongst users, so it would be necessary to segregate
their user interface service from the render farm’s client API service.

Each type of service has very different demands and needs, so
segregating services also allows you to tune the hardware and software
to the specifications required for the service they are handling.
Ultimately, you can maximize the use of your available resources.

**How Load Balancing Works**

Load balancing distributes requests to various TACTIC processes using an
algorithm that determines which request is delegated to which process.
The default algorithm is a very simple randomizer.

For most applications, the default algorithm works perfectly fine. It is
left to chance whether a particular request will be assigned to a
heavily loaded process or one that is sitting idle, so there may be
inconsistent performance depending on load and availability of TACTIC
processes not already loaded.

IIS delegation algorithms (on MSWeb Server) are also supported. For
Apache, an example algorithm is provided you can customize to your
needs.

Each process, by default, is assigned two simultaneous requests at most.
This limit has proven in production to be the most effective because it
prevents the Python process itself from being overloaded waiting for
required I/O operations. If there are excess requests waiting to be
processed, they are kept in a queue and assigned sequentially to
processes as they become available.

Python’s GIL (global interpreter lock) prevents any Python process from
using more than one CPU or core, so the number of threads available for
any given process is limited. True scalability is achieved by
load-balancing requests over multiple processes. This method scales
seamlessly and linearly over multiple cores, multiple CPUs and
ultimately over multiple physical servers with only simple configuration
changes.

## Post Deployment TACTIC Upscaling

**Scenarios**

TACTIC is easily upscaled in most post deployment scenarios. Upscaling
does not require any significant downtime of TACTIC services.

Some scenario examples follow, with bullet points outlining why these
possible solutions would be followed:

- Increasing number of TACTIC processes on a single machine**

- Splitting TACTIC into multiple servers from one server**

    -   Easy way to upscale/troubleshoot

    -   Heavy reporting

    -   Many users/API calls from automated processes

- Splitting the HTTP co-service into multiple servers from one server**

    -   Many Checkins

    -   Large Checkins


