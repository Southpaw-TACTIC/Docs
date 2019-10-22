# Configure Logrotate

In a default installation tactic stores its logs in a single file. For
proper maintenance, this file must be rotated by the host operating
system. This action must be set in the host operating system. 

The host operating system must have a facility to rotate text logs on a
regular chronological basis.

Logrotate is used as a tool to rotate text files on a chronological
basis. The tool allows automatic rotation, compression, removal and
mailing of log files.

## Directives

This is a partial list of logrotate directives.

-   **missingok**: If the log file is missing, go on to the next log file
    without issuing an error message.

-   **copytruncate**: Truncate the original log file to zero size in place
    after creating a copy, instead of moving the old log file and optionally
    creating a new one

-   **rotate 7** : Log files are rotated 7 times before being removed or
    mailed to the address specified in a mail directive. If count is 0, old
    versions are removed rather then rotated.

-   **compress**: Old versions of log files are compressed with gzip to save
    disk space.

-   **notifempty**: Do not rotate the log if it is empty

-   **sharedscripts postrotate /etc/init.d/lighttpd reload endscript**:

## Default configuration

Logrotate’s main configuration file `/etc/logrotate.conf`

Applies the main configuration settings from this file to all log
rotation settings, unless overridden by individual directives on a
per-log basis.

    # see "man logrotate" for details
    # rotate log files weekly
    weekly
    # keep 4 weeks worth of backlogs
    rotate 4
    # create new (empty) log files after rotating old ones
    create
    # uncomment this if you want your log files compressed
    #compress
    # RPM packages drop log rotation information into this directory
    include /etc/logrotate.d
    # no packages own wtmp -- we'll rotate them here
    /var/log/wtmp {
    monthly
    create 0664 root utmp
    rotate 1
    }

## Example Service Configuration

This is an example logrotate configuration for HTTP. The configuration
file is \`/etc/logrotate.d/httpd \`

    /var/log/httpd/*.log {
     weekly
     rotate 52
     compress
      missingok
      notifempty
      sharedscripts
      postrotate
          /bin/kill -HUP `cat /var/run/httpd.pid 2>/dev/null` 2> /dev/null || true    endscript
    }

On the example linux system, service or server specific configurations
are stored in `/etc/logrotate.d` directory. 

In this example, HTTP logs are not deleted until they are at least a
year old, and are rotated on a weekly basis. There are other
configuration options available, but they will not be discussed in this
tutorial. Please look online for more information on these other
options. Depending on the requirement, each log file may be handled at
different intervals.

The lines between postrotate and endscript (both of which must appear on
lines by themselves) are executed after the log file is rotated. These
directives may only appear inside a log file definition. In our case we
are reloading lighttpd.

## Example TACTIC configuration

The configuration goal is get logrotate to get the tactic log files
rotated for our needs and requirements.

This is an example logrotate configuration for TACTIC.
The configuration file is \`/etc/logrotate.d/tactic \`

Remember to restart the logrotate services after any additions to
logrotate configuration.

    /home/apache/tacticTemp/log/stdout.log {
        notifempty
        daily
        rotate 365
        missingok
        copytruncate
        create 0600 apache apache
    }
