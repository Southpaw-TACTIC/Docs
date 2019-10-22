
# TACTIC Configuration Checklist

## Checklist

For a proper production deployment of TACTIC, the following configurations must be considered in the context of your business needs:

- Assets Storage 
- Database
- Webserver 
- SSL
- Authentication
- Webserver for notifications

The Server Configuration section of this documentation provides advanced configuration information for each of these areas. Further, it is recommended that system administrators read the following sections:

- Scalability: Network architecture examples and load balancing configuration
- Maintenance: Configuring backups and logging 

## Location of Configuration File

Most advanced server in TACTIC is done in the TACTIC configuration file.
The configuration file is typically found on Linux systems at,

    /opt/tactic/tactic_data/config/tactic-conf.xml

and on Windows systems at,

    C:\ProgramData\Southpaw\Tactic\config\tactic-conf.xml


Southpaw supplies the TACTIC config file as a template on installation.
Once installed, this file can be modified to reflect any of the options
described in the sections below. You must restart the TACTIC service for 
changes to take effect.


## System Config tool

Most of the parameters can be modified in the UI through Global &gt; System Config as well. If an option tag does not exist in a particular section in your config file, TACTIC will assume a default or
it can simply be added in.
