# TACTIC Configuration File

The TACTIC config file stores settings such as directory locations and
email server information.


## Install

This section defines the hostname for the server (if different from
"localhost") as well as the temp directory to be used for TACTIC. The
tmp\_dir is where temporary files are stored as well as the TACTIC log
files.

```
    <install>
        <hostname>localhost</hostname>
        <server>LA</server>
        <tmp_dir>/home/tactic/tactic_temp</tmp_dir>
        <default_project>default_project_code</default_project>
        <include_js>/context/some_external_lib.js</include_js>
        <include_css>plugins/styles.cs</include_css>
        <install_dir>/home/tactic/TACTIC</install_dir>
        <site_dir>/home/tactic/tactic_sites</site_dir>
        <plugin_dir>/home/tactic/TACTIC/spt/plugins</plugin_dir>
        <shutil_fix>enabled</shutil_fix>
        <default_project>workflow</default_project>
        <base_url>portal.southpawtech.com</base_url>
        <top_class_name>tactic.ui.app.PageNavContainerWdg</top_class_name>
        <header_class_name>tactic.ui.app.PageNavContainerWdg</header_class_name>
        <first_day_of_week>6</first_day_of_week>
        <layout>fixed</layout>
        <doc_dir></doc_dir>
        <cache_mode></cache_mode>
        <log_type><log_type>
    </install>
```

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>HOSTNAME</p></td>
<td><p>This section defines the hostname for the server (if different from &quot;localhost&quot;). The hostname is what TACTIC listens to.</p></td>
</tr>
<tr class="even">
<td><p>TMP_DIR</p></td>
<td><p>The temp directory to be used by TACTIC.</p></td>
</tr>
<tr class="odd">
<td><p>DEFAULT_PROJECT</p></td>
<td><p>Default project when the user browse the TACTIC base url.</p></td>
</tr>
<tr class="even">
<td><p>INCLUDE_JS</p></td>
<td><p>You can include one or more external js files you want to make use of. Separated by ,.</p></td>
</tr>
<tr class="odd">
<td><p>SERVER</p></td>
<td><p>A prefix for code generation to distinguish data from different servers</p></td>
</tr>
<tr class="even">
<td><p>INCLUDE_CSS</p></td>
<td><p>You can include one or more external css files you want to make use of. Separated by ,.</p></td>
</tr>
<tr class="odd">
<td><p>INSTALL_DIR</p></td>
<td><p>The installation directory for TACTIC</p></td>
</tr>
<tr class="even">
<td><p>HEADER_CLASS_NAME</p></td>
<td><p>this value will be returned by WebEnvironment.get_header_class_name()</p></td>
</tr>
<tr class="odd">
<td><p>PLUGIN_DIR</p></td>
<td><p>The directory storing plugins created</p></td>
</tr>
<tr class="even">
<td><p>DOC_DIR</p></td>
<td><p>The directory of tactic documents</p></td>
</tr>
<tr class="odd">
<td><p>CACHE_MODE</p></td>
<td><p></p></td>
</tr>
<tr class="even">
<td><p>FIRST_DAY_OF_WEEK</p></td>
<td><p>A number indicates the first day of the week, for example, 6 indicates Saturday.</p></td>
</tr>
<tr class="odd">
<td><p>LOG_TYPE</p></td>
<td><p>Default value is None, can also be "file_with_date" and "stream". "file_with_date" separates log files by date, the default value writes all log in the same file. Useful on Windows system without Logrotate.</p></td>
</tr>
<tr class="even">
<td><p>SHUTIL_FIX</p></td>
<td><p>once "enabled", disabling copystat method for windows shared folder mounted on Linux</p></td>
</tr>
<tr class="odd">
<td><p>DEFAULT_PROJECT</p></td>
<td><p>The default project of your user</p></td>
</tr>
<tr class="even">
<td><p>BASE_URL</p></td>
<td><p>the base url of you website</p></td>
</tr>
<tr class="odd">
<td><p>TOP_CLASS_NAME</p></td>
<td><p>the class name of default wdg of top container, will be returned by WebEnvironment.get_top_class_name()</p></td>
</tr>
</tbody>
</table>

## Services

This section defines information regarding the services external to
TACTIC.

```
<services>
    <mailserver>smtp.googlemail.com</mailserver>
    <mail_password>password</mail_password>
    <mail_user>tactic@southpawtech.com</mail_user>
    <mail_port>587</mail_port>
    <mail_sender_disabled>true</mail_sender_disabled>
    <mail_tls_enabled>true</mail_tls_enabled>
    <mail_name>TACTIC</mail_name>
    <mail_default_admin_email>admin@southpawtech.com</mail_default_admin_email>
    <notify_user>exceptions@southpawtech.com</notify_user>
    <python>python3</python>
    <python_path>/home/apache/custom</python_path>
    <render_submit_class>sites.racoon.modules.command.CustomRenderSubmit</render_submit_class>
    <process_count>3</process_count>
    <thread_count>50</thread_count>
    <process_time_alive>30</process_time_alive>
    <system_class></system_class>
    <mail_base_url></mail_base_url>
    <notify_user_name>username<notify_user_name>
    <use_periodic_restart>true</use_periodic_restart>
    <queue_process_timeout>86400</queue_process_timeout>
    <start_port>5510</start_port>
    <ports>5510|5511|5512</ports>
    <queue_process_count>5</queue_process_count>
    <scheduler>true</scheduler>
    <scheduler_sites>admin|user|name</scheduler_sites>
    <rsync><rsync>
</services>
```

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="even">
<td><p>MAIL_SERVER</p></td>
<td><p>The URL of the SMTP mail server</td></p>
</tr>
<tr class="odd">
<td><p>MAIL_PASSWORD</p></td>
<td><p>The password for accessing the SMTP mail server that requires authentication</p></td>
</tr>
<tr class="even">
<td><p>MAIL_USER</p></td>
<td><p>The user name for accessing the SMTP mail server that requires authentication</p></td>
</tr>
<tr class="odd">
<td><p>MAIL_PORT</p></td>
<td><p>The port for the SMTP mail server (if different that 25)</p></td>
</tr>
<tr class="even">
<td><p>MAIL_SENDER_DISABLED</p></td>
<td><p>Set as "true" to disable using the sender name in sending of email in case the email server does not allow sender’s email not owned by the sender</p></td>
</tr>
<tr class="odd">
<td><p>MAIL_TLS_ENABLED</p></td>
<td><p>
Set as "true" to enable TLS (Transport Layer Security) for the connection to email server
</p></td>
</tr>
<tr class="even">
<td><p>MAIL_DEFAULT_ADMIN_EMAIL</p></td>
<td><p>
Default email for admin user is no email is set. This is used for password recovery functionality and notifications.
</tr>
<tr class="odd">
<td><p>NOTIFY_USER</p></td>
<td><p>
Email to send system exceptions and errors to.
</p></td>
</tr>
<tr class="even">
<td><p>PYTHON</p></td>
<td><p>The root path of the Python installation. If your installation is using Python3, "python3" should be set as value.</p></td>
</tr>
<tr class="odd">
<td><p>PYTHON_PATH</p></td>
<td><p>The server-side location for client files. This location can also be mounted from a shared volume if you wish to maintain stricter server access for clients. For multiple paths, separate with | .e.g. /home/apache/custom|/home/apache/custom_two</p></td>
</tr>
<tr class="even">
<td><p>RENDER_SUBMIT_CLASS</p></td>
<td><p>The class used for render submissions.</p></td>
</tr>
<tr class="odd">
<td><p>PROCESS_COUNT</p></td>
<td><p>The number of processes the TACTIC service would spawn. It needs to match the number of ports used in the load balancing scheme in the Apache configuration.</p></td>
</tr>
<tr class="even">
<td><p>THREAD_COUNT</p></td>
<td><p>The number of worker threads generated for each instance of the TACTIC process. If not set, it defaults to 10 which is too low to handle rapid requests.. TACTIC’s default is 50 on new installation. A good balance of process_count and thread_count can improve response time of the server.</p></td>
</tr>
<tr class="odd">
<td><p>PROCESS_TIME_ALIVE</p></td>
<td><p>The number of minutes a TACTIC process gets respawned. It helps with the memory consumption inherent with a long-running Python process.</p></td>
</tr>
<tr class="even">
<td><p>SYSTEM_CLASS</p></td>
<td><p>Allows for an override some of the low level system functionality. For example 'mkdirs' and 'exists'</p></td>
</tr>
<tr class="odd">
<td><p>MAIL_BASE_URL</p></td>
<td><p>If base_url is not defined, expression language will use mail_base_url for expression variable.</p></td>
</tr>
<tr class="even">
<td><p>NOTIFY_USER_NAME</p></td>
<td><p>The name of the person who receives the system exceptions and errors.</p></td>
</tr>
<tr class="odd">
<td><p>USE_PERIODIC_RESTART</p></td>
<td><p>set as 'true' to enable killing TACTIC process periodically</p></td>
</tr>
<tr class="even">
<td><p>QUEUE_PROCESS_TIMEOUT</p></td>
<td><p>The interval for use_periodic_restart, has to be integer, unit: seconds</p></td>
</tr>
<tr class="odd">
<td><p>START_PORT</p></td>
<td><p>The first port that your TACTIC website can use. The proceeding PROCESS_COUNT number of ports will be used by TACTIC, defaulted to be 8081</p></td>
</tr>
<tr class="even">
<td><p>PORTS</p></td>
<td><p>the ports can be used by TACTIC, separated by "|". This config is exclusive with START_PORT and PROCESS_COUNT. When these two tags are not filled out, the PORTS config will be used to set the ports can be used by TACTIC.</p></td>
</tr>
<tr class="even">
<td><p>ENABLE</p></td>
<td><p>The services that will used by your TACTIC website, can be tactic, job_queue, watch_folder, scheduler, etc., separated by "|".</p></td>
</tr>
<tr class="odd">
<td><p>QUEUE_PROCESS_COUNT</p></td>
<td><p>The number of processes in the job queue, has to be integer</p></td>
</tr>
<tr class="even">
<td><p>SCHEDULER</p></td>
<td><p>set as "true" to enable the scheduler services</p></td>
</tr>
<tr class="even">
<td><p>SCHEDULER_SITES</p></td>
<td><p>The sites the scheduler service will run on.</p></td>
</tr>
<tr class="odd">
<td><p>rsync</p></td>
<td><p>rsync executable</p></td>
</tr>
</tbody>
</table>

## Security

This section defines information regarding the services external to
TACTIC.

    <security>
        <version>2</version>
        <ticket_expiry>10 hour</ticket_expiry>
        <authenticate_mode>default</authenticate_mode>
        <authenticate_class></authenticate_class>
        <authenticate_version>2</authenticate_version>
        <case_insensitive_login>>false</case_insensitive_login>
        <max_login_attempt>3</max_login_attempt>
        <account_lockout_duration>30</account_lockout_duration>
        <auto_create_user>false</auto_create_user>
        <api_require_password>true</api_require_password>
        <api_password>api password</api_password>
        <allow_guest>false</allow_guest>
        <guest_mode>restricted</guest_mode>
        <guest_url_allow>/guest_view</guest_url_allow>
        <api_method_restricted>true</api_method_restricted>
        <api_mode>query</api_mode>
        <api_cmd_restricted>true</api_cmd_restricted>
        <authenticate_encryption>drupal</authenticate_encryption>
        <ldap_server>server address</ldap_server>
        <bind_dn></bind_dn>
        <bind_password>bindDN password</bind_password>
        <base_dn></base_dn>
        <password>admin password</password>
        <site_class>pyasm.security.Site</site_class>
        <authenticate_ticket_class></authenticate_ticket_class>
        <inactive_ticket_expiry>2 days</inactive_ticket_expiry>
        <protocol>http</protocol>
        <hosts></hosts>

    </security>

<table>
<colgroup>
<col width="10%" />
<col width="89%" />
</colgroup>
<thead>
<tr class="header">
<th>TICKET_EXPIRY</th>
<th>The number of hours a login ticket expires after</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>AUTHENTICATE_MODE</p></td>
<td><p>default: This basically just looks at the tactic database for information.</p>
<p>autocreate: This autocreates the first time and then leaves the information alone.</p>
<p>cache: This caches the information to the tactic database on every login</p></td>
</tr>
<tr class="even">
<td><p>AUTHENTICATE_CLASS</p></td>
<td><p>A full class path to override the default class &quot;pyasm.security.TacticAuthenticate&quot;. Note: Your custom class needs to override the method verify() which takes two arguments: login and password.</p></td>
</tr>
<tr class="odd">
<td><p>AUTHENTICATE_VERSION</p></td>
<td><p>1 is the old way of authentication. 2 is the new way.</p></td>
</tr>
<tr class="even">
<td><p>CASE_INSENSITIVE_LOGIN</p></td>
<td><p>If set to 'true', it allows case insensitive login name. When autocreate mode is used, all login entries created will have a lowercase login name. It can be used in combination with Active Directory setup.</p></td>
</tr>
<tr class="odd">
<td><p>MAX_LOGIN_ATTEMPT</p></td>
<td><p>Number of times login attempt can fail before account is locked out.</p></td>
</tr>
<tr class="even">
<td><p>ACCOUNT_LOCKOUT_DURATION</p></td>
<td><p>Number of minutes a user account is locked out for failed login attempt if specified.</p></td>
</tr>
<tr class="odd">
<td><p>AUTO_CREATE_USER</p></td>
<td><p>Auto create user in TACTIC during authentication phase if it does not exist. (Deprecated: use &quot;authenticate_mode&quot; in new way of authentication)</p></td>
</tr>
<tr class="even">
<td><p>API_REQUIRE_PASSWORD</p></td>
<td><p>Client API script requires password to login or not</p></td>
</tr>
<tr class="odd">
<td><p>API_PASSWORD</p></td>
<td><p>A generic Client API password can be set here</p></td>
</tr>
<tr class="even">
<td><p>ALLOW_GUEST</p></td>
<td><p>true or false can be set to allow guest to access without login</p></td>
</tr>
<tr class="odd">
<td><p>GUEST_MODE</p></td>
<td><p>full or restricted can be set. In restricted mode, a /guest relative URL is expected to be defined in Custom URL to restrict the guest to only see a particular view</p></td>
</tr>
<tr class="even">
<td><p>GUEST_URL_ALLOW</p></td>
<td><p>In full mode, one can have multiple relative URLs predefined for guest, separated by |.</p></td>
</tr>
<tr class="odd">
<td><p>API_METHOD_RESTRICTED</p></td>
<td><p>set as "true" to restrict all API methods access. Certain users can access specific API methods by setting the access rules.</p></td>
</tr>
<tr class="even">
<td><p>API_MODE</p></td>
<td><p>can be "open", "closed", and "query". API's can be accessed by all users if "open"; API's can only be accessed by admin user if "closed"; API's access is specified by access rule if "query".</p></td>
</tr>
<tr class="even">
<td><p>API_CMD_RESTRICTED</p></td>
<td><p>set as "true" to disable command execution through API's, admin is the only user that can execute commands through API's.</p></td>
</tr>
<tr class="odd">
<td><p>AUTHENTICATE_ENCRYPTION</p></td>
<td><p>set as "drupal" to enable Drupal encryption method for user information. It will use md5 encryption by default.</p></td>
</tr>
<tr class="even">
<td><p>LDAP_SERVER</p></td>
<td><p>LDAP server</p></td>
</tr>
<tr class="odd">
<td><p>BIND_DN</p></td>
<td><p>BindDN for LDAP</p></td>
</tr>
<tr class="even">
<td><p>BIND_PASSWORD</p></td>
<td><p>The corresponding password for bindDN in LDAP</p></td>
</tr>
<tr class="odd">
<td><p>FORCE_LOWERCASE_LOGIN</p></td>
<td><p>set as "true" to restrict login names to be lowercase.</p></td>
</tr>
<tr class="even">
<td><p>VERSION</p></td>
<td><p>The security version of TACTIC</p></td>
</tr>
<tr class="odd">
<td><p>PASSWORD</p></td>
<td><p>The default password for admin</p></td>
</tr>
<tr class="even">
<td><p>SITE_CLASS</p></td>
<td><p>the class name for site objects</p></td>
</tr>
<tr class="odd">
<td><p>AUTHENTICATE_TICKET_CLASS</p></td>
<td><p>The class of an external tickets source, which is used to get the key when ticket doesn't exists</p></td>
</tr>
<tr class="even">
<td><p>INACTIVE_TICKET_EXPIRY</p></td>
<td><p>Life expectency of a ticket when user is inactive. Need to specify the time metric using, and time metrics can be "day", "week", "year". Time metric is defaulted to be "day". Sample input: "1 day"</p></td>
</tr>
<tr class="odd">
<td><p>PROTOCOL</p></td>
<td><p>the base url protocol, defaulted to be "http"</p></td>
</tr>
<tr class="even">
<td><p>SESSION_KEY</p></td>
<td><p>key for login tickets</p></td>
</tr>
<tr class="odd">
<td><p>AUTHENTICATE_DOMAINS</p></td>
<td><p>(DEPRECATED) Used for active directory/ldap authentication. Use active_directory, domains instead.</p></td>
</tr>
<tr class="even">
<td><p>HOSTS</p></td>
<td><p>the hosts for your website, separated by "|".</p></td>
</tr>
<tr class="odd">
<td><p>BASE_DN</p></td>
<td><p>BaseDN for LDAP</p></td>
</tr>
</tbody>
</table>

## Database

    <database>
        <vendor>PostgreSQL</vendor>
        <server>localhost</server>
        <port></port>
        <user>postgres</user>
        <password>none</password>
        <sobject_database>sthpw</sobject_database>
        <pool_max_connections>0</pool_max_connections>
        <sqlite_db_dir>/home/tactic_data/sql_lite</sqlite_db_dir>
        <join>false</join>
        <ORACLE_HOME>/home/tactic_data/oracle</ORACLE_HOME>
        <NLS_LANG></NLS_LANG>
        <sslmode></sslmode>
        <encoding>utf8</encoding>
        <charset>utf8</charset>
    </database>

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>VENDOR</p></td>
<td><p>The database vendor (software) the database will be installed on.</p></td>
</tr>
<tr class="even">
<td><p>SERVER</p></td>
<td><p>The hostname of the server. This is localhost if TACTIC and the database are on the same server</p></td>
</tr>
<tr class="odd">
<td><p>PORT</p></td>
<td><p>The database connection port</p></td>
</tr>
<tr class="even">
<td><p>USER</p></td>
<td><p>The user name for the database connection</p></td>
</tr>
<tr class="odd">
<td><p>PASSWORD</p></td>
<td><p>The password for the database connection.</p>

<!-- TODO: Include comment on encrypted passwords -->
</td>
</tr>
<tr class="even">
<td><p>SOBJECT_DATABASE</p></td>
<td><p>The database where SObject definitions will be stores</p></td>
</tr>
<tr class="odd">
<td><p>POOL_MAX_CONNECTIONS</p></td>
<td><p>The pool of connections available for connecting to the database. 0 is recommended for PostgreSQL implementation</p></td>
</tr>
<tr class="even">
<td><p>SQLITE_DB_DIR</p></td>
<td><p>the directory of sqlite database</p></td>
</tr>
<tr class="odd">
<td><p>JOIN</p></td>
<td><p>set as "false" to disable multi-database join</p></td>
</tr>
<tr class="even">
<td><p>ORACLE_HOME</p></td>
<td><p>The oracle home directory path</p></td>
</tr>
<tr class="odd">
<td><p>NLS_LANG</p></td>
<td><p>The NLS_LANG for Oracle</p></td>
</tr>
<tr class="even">
<td><p>SSLMODE</p></td>
<td><p>The sslmode for postgreSQL</p></td>
</tr>
<tr class="odd">
<td><p>ENCODING</p></td>
<td><p>The encoding of the MySQL database</p></td>
</tr>
<tr class="even">
<td><p>CHARSET</p></td>
<td><p>The charset of the MySQL database</p></td>
</tr>
</tbody>
</table>

## Perforce

    <perforce>
        <web_dir>perforce</web_dir>
        <p4>p4</p4>
        <port>1666</port>
        <depot>book</depot>
    </perforce>

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>WEB_DIR</p></td>
<td><p>The webdir for the perforce connection.</p></td>
</tr>
<tr class="even">
<td><p>P4</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>PORT</p></td>
<td><p>The port to be used for connection to perforce.</p></td>
</tr>
<tr class="even">
<td><p>depot</p></td>
<td>The depot of perforce</td>
</tr>
</tbody>
</table>

## Look

This setting provides a method of setting the TACTIC skin in the server
for all users. In this example, the 'BON\_NOCHE' palette specified:

    <look>
        <palette>BON_NOCHE</palette>
        <kiosk_mode>true</kiosk_mode>
    </look>

Other available palettes are 'AQUA', 'DARK', 'BRIGHT', 'DEFAULT', 'SILVER',
'AVIATOR', and 'ORIGAMI'. Alternatively, the whole palette can be
customized as follows:

    <look>
         <palette>{
                 'color':        '#000000',         # main font color
                 'color2':       '#FFFFFF',         # secondary font color
                 'color3':       '#FFFFFF',         # tertiary font color
                 'background':   '#FDEEA7',         # main background color
                 'background2':  '#1A9481',         # secondary background color
                 'background3':  '#003D5c',         # tertiary background color
                 'border':       '#666666'          # main border color
        }</palette>
    </palette>
    </look>

The side bar color may not change right away until the next TACTIC
service restart.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>PALETTE</p></td>
<td><p>The default palette setting for all TACTIC users.</p></td>
</tr>
<tr class='even'>
<td><p>kiosk_mode</p></td>
<td><p>set as "true" to disable spt.alert function, default is false</p></td>
</tr>
</tbody>
</table>


## Portal
    <portal>
        <auto_upgrade>true</auto_upgrade>
        <enabled>true</enabled>
    </portal>

<table>
<colgroup>
<col width="6%" />
<col width="93%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>AUTO_UPGRADE</p></td>
<td><p>This config is default to be false. Set as "true" to allow the site to auto-upgrade databases and plugins to the newest version when loading the project. Set as "false" or remove the config to disable the auto-upgrade.</p></td>
<tr class="even">
<td><p>ENABLED</p></td>
<td><p>set as "true" to indicate this is a portal website</p></td>
</tr>
</tbody>
</table>


## Schedule
    <schedule>
        <mode>from_end_date</mode>
    </schedule>
<table>
<colgroup>
<col width="6%" />
<col width="93%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>MODE</p></td>
<td><p>can be 'even', 'even_day', and 'from_end_date'. "even" mode creates tasks with the same duration that measured by hours; "even_day" mode creates tasks with the same duration that measured by days; "from_end_date" creates tasks with durations according to its "bid_start_date" and "bid_end_date"</p></td>
</tr>
</tbody>
</table>


## Async
    <async>
        <process_count>3</process_count>
    </async>
<table>
<colgroup>
<col width="6%" />
<col width="93%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>process_count</p></td>
<td><p>The number of processes for the aSync queue service, has to be integer.</p></td>
</tr>
</tbody>
</table>


## Load
    <load>
        <loader_use_namespace></loader_use_namespace>
    </load>
<table>
<colgroup>
<col width="6%" />
<col width="93%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>LOADER_USE_NAMESPACE</p></td>
<td><p>User by MayaFileLoaderCmd</p></td>
</tr>
</tbody>
</table>


## Master
    <master>
        <enabled>true</enabled>
        <project_code>workflow</project_code>
        <url></url>
        <forwarding_type>xmlrpc_only</forwarding_type>
        <site>user</site>
    </master>
<table>
<colgroup>
<col width="6%" />
<col width="93%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>enabled</p></td>
<td><p>Enables functionality required for multi-site database replication.</p></td>
</tr>
<tr class="even">
<td><p>project_code</p></td>
<td><p>project_code used in master server authentication</p></td>
</tr>
<tr class="odd">
<td><p>url</p></td>
<td><p>master server URL</p></td>
</tr>
<tr class="even">
<td><p>forwarding_type</p></td>
<td><p>default none, option "xmlrpc_only" disables javascript API get_master function.</p></td>
</tr>
<tr class="odd">
<td><p>site</p></td>
<td><p>Site used in master server authentication</p></td>
</tr>
</tbody>
</table>



## Active Directory
    <active_directory>
        <domains>d1|d2|d3</domains>
        <hosts>h1|h2|h3</hosts>
        <require_domain>true</require_domain>
        <domain_component>dc</domain_component>
        <allow_script>AD/validate</allow_script>
        <default_groups>group1|group2</default_groups>
        <handle_groups>false</handle_groups>
        <default_license_type>license</default_license_type>
    </active_directory>
<table>
<colgroup>
<col width="6%" />
<col width="93%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>domains</p></td>
<td><p>Domains for active directory/ldap authentication, separated by "|", need to match the number of hosts</p></td>
</tr>
<tr class="even">
<td><p>hosts</p></td>
<td><p>Hosts for active directory/ldap authentication, separated by "|", need to match the number of domains </p></td>
</tr>
<tr class="odd">
<td><p>require_domain</p></td>
<td><p>set as "true" to make domain required.</p></td>
</tr>
<tr class="even">
<td><p>domain_component</p></td>
<td><p>the domain component for LDAP, represents the top of an LDAP tree that uses DNS to define its namespace</p></td>
</tr>
<tr class="odd">
<td><p>allow_script</p></td>
<td><p>The path to the python script that sets the flag</p></td>
</tr>
<tr class="odd">
<td><p>default_groups</p></td>
<td><p>groups for users that are groupless, separated by "|"</p></td>
</tr>
<tr class="even">
<td><p>handle_groups</p></td>
<td><p>set as "false" to check if any user is groupless, and set users to default_groups if they are groupless</p></td>
</tr>
<tr class="odd">
<td><p>default_license_type</p></td>
<td><p>the default license type for active_directory. When user has no defined groups in Active Directory, they will be set as the default license type</p></td>
</tr>
</tbody>
</table>


## Checkin

TACTIC uses the following directory and path settings for internal and
client interaction. They are included in the tag (for checkins).

<table>
<colgroup>
<col width="6%" />
<col width="93%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>VERSIONLESS_MODE</p></td>
<td><p>COPY or SYMLINK: Turn on versionless mode for checkins for all projects. To set the versionless mode per project, go to PROJECT ADMIN → PROJECT SETTINGS and add a the key VERSIONLESS_MODE and the value: COPY or SYMLINK.</p></td>
</tr>
<tr class="even">
<td><p>ASSET_BASE_DIR</p></td>
<td><p>The directory where the assets are stored in the TACTIC server.</p></td>
</tr>
<tr class="odd">
<td><p>WEB_BASE_DIR</p></td>
<td><p>The root URL that maps the 'asset_base_dir' directory</p></td>
</tr>
<tr class="even">
<td><p>WIN32_LOCAL_BASE_DIR</p></td>
<td><p>The base directory in Windows client machines</p></td>
</tr>
<tr class="odd">
<td><p>LINUX_LOCAL_BASE_DIR</p></td>
<td><p>The base directory in Linux client machines</p></td>
</tr>
<tr class="even">
<td><p>WIN32_SANDBOX_DIR</p></td>
<td><p>The default sandbox directory in the Windows client machines (it can be overridden by Remote Repo)</p></td>
</tr>
<tr class="odd">
<td><p>LINUX_SANDBOX_DIR</p></td>
<td><p>The default sandbox directory in the Linux client machines (it can be overridden by Remote Repo)</p></td>
</tr>
<tr class="even">
<td><p>WIN32_CLIENT_REPO_DIR</p></td>
<td><p>Maps the asset_base_dir directory as seen by the Windows client. For example, if asset_base_dir is on a Linux server with a path like &quot;/home/apache/assets&quot; but from the Windows client, it is mapped as &quot;Z:/assets&quot;, then &quot;Z:/assets&quot; should be the value for this setting.</p>
<p>By default, this path is empty because the system assumes the client and server are on the same Windows machine.</p></td>
</tr>
<tr class="odd">
<td><p>LINUX_CLIENT_REPO_DIR</p></td>
<td><p>Same as 'win32_client_repo_dir' except it is from the perspective of a Linux client machine</p></td>
</tr>
<tr class="even">
<td><p>WIN32_CLIENT_HANDOFF_DIR</p></td>
<td><p>Windows client-side handoff directory for Client API transactions. (Find out more about the handoff directory below.)</p></td>
</tr>
<tr class="odd">
<td><p>WIN32_SERVER_HANDOFF_DIR</p></td>
<td><p>Windows server-side handoff directory for Client API transactions</p></td>
</tr>
<tr class="even">
<td><p>LINUX_CLIENT_HANDOFF_DIR</p></td>
<td><p>Linux client-side handoff directory for Client API transactions</p></td>
</tr>
<tr class="odd">
<td><p>LINUX_SERVER_HANDOFF_DIR</p></td>
<td><p>Linux server-side handoff directory for Client API transactions</p></td>
</tr>
<tr class="even">
<td><p>SUDO_NO_PASSWORD</p></td>
<td><p>It controls whether sudo can be run to change the user id and group id of the files checked in. It is particularly important if you want to ensure files checked in to the TACTIC repository are owned by TACTIC and not overwritable by just any users. If set to true, &quot;no password&quot; should be enabled for the user TACTIC is run as in the OS. e.g. For Fedora, assuming you have sudo installed:</p>
<p>In the file /etc/sudoers, the following line should be uncommented: %wheel ALL=(ALL) NOPASSWD: ALL</p>
<p>In the file /etc/group, apache should be added to the group wheel wheel:x:10:root,apache</p></td>
</tr>
<tr class="even">
<td><p>VERSION_PADDING</p></td>
<td><p>padding of 3 or more can be set for checked-in files</p></td>
</tr>
<tr class="odd">
<td><p>DEFAULT_NAMING_VERSION</p></td>
<td><p>The default version for checkin</p></td>
</tr>
<tr class="even">
<td><p>WIN32_LOCAL_REPO_DIR</p></td>
<td><p>The repo base directory in Windows client machines</p></td>
</tr>
<tr class="odd">
<td><p>LINUX_LOCAL_REPO_DIR</p></td>
<td><p>The repo base directory in Linux client machines</p></td>
</tr>
<tr class="even">
<td><p>BASE_DIR_ALIAS</p></td>
<td><p>the alias of asset_base_dir</p></td>
</tr>
<tr class="odd">
<td><p>APP_ASSET_BASE_DIR</p></td>
<td><p>asset_base_dir for maya</p></td>
</tr>
<tr class="even">
<td><p>LDAP_PATH</p></td>
<td><p>LDAP(Active Directory) Path</p></td>
</tr>
<tr class="odd">
<td><p>LDAP_SERVER</p></td>
<td><p>LDAP server</p></td>
</tr>
<tr class="even">
<td><p>COPY_BASE_URL</p></td>
<td><p>the base url for SobjectUploadWdg in copy mode</p></td>
</tr>
<tr class="odd">
<td><p>USE_APPLET</p></td>
<td><p>determines whether the applet should be used for local file operations, can only be "true" or "false"</p></td>
</tr>
<tr class="even">
<td><p>win32_dropbox_dir</p></td>
<td><p>a directory used when the base_dir is not defined when getting the transactions</p></td>
</tr>
<tr class="odd">
<td><p>REPO_TYPE</p></td>
<td><p></p></td>
</tr>
<tr class="even">
<td><p>CLIENT_DIR_MAP</p></td>
<td><p>maps server directories to client directories</p></td>
</tr>
</tbody>
</table>

### The Handoff Directories

Handoff directories can be seen by both the server and the client
machines. They are used for 3D checkins and client API interactions, and
are important for specifying how the client and server sides see the
same location.

For example, if you have the location //192.168.0.105/handoff available
on your network and it is mounted as /home/apache/handoff on a server,
then it would be important to include the following entries:

    <win32_client_handoff_dir>//192.168.0.105/handoff</win32_client_handoff_dir>
    <win32_server_handoff_dir></win32_server_handoff_dir>
    <linux_client_handoff_dir></linux_client_handoff_dir>
    <linux_server_handoff_dir>/home/apache/handoff</linux_server_handoff_dir>

### Directory Configuration Examples

Example 1

The assets directory is located on the TACTIC server and allows for
read-only access from client machines in the local subnet.

-   The assets directory is located on the TACTIC server and allows for
    read-only access from client machines in the local subnet.

-   The handoff directory is located on the TACTIC server and allows for
    read/write access from client machines in the local subnet

-   The Windows and Linux 'client\_repo\_dir' looks directly to the server for
    the available "assets" share

-   The Windows and Linux 'client\_handoff\_dir' looks directly to the server
    for the available "handoff" share

        <checkin>
            <asset_base_dir>/home/apache/assets</asset_base_dir>
            <web_base_dir>/assets</web_base_dir>
            <win32_local_base_dir>C:/sthpw</win32_local_base_dir>
            <linux_local_base_dir>/tmp/sthpw</linux_local_base_dir>
            <win32_sandbox_dir>C:/sthpw/sandbox</win32_sandbox_dir>
            <linux_sandbox_dir>/tmp/sthpw/sandbox</linux_sandbox_dir>
            <win32_client_repo_dir>//192.168.0.105/apache/assets</win32_client_repo_dir>
            <linux_client_repo_dir>/usr/assets</linux_client_repo_dir>
            <win32_client_handoff_dir>//192.168.0.105/apache/handoff<win32_client_handoff_dir>
            <win32_server_handoff_dir></win32_server_handoff_dir>
            <linux_client_handoff_dir>/home/apache/handoff</linux_client_handoff_dir>
            <linux_server_handoff_dir>/home/apache/handoff</linux_server_handoff_dir>
            <version_padding>3</version_padding>
        </checkin>

Example 2

-   The assets directory is located on another server and mounted locally
    on the TACTIC server to /mnt1/assets.

-   The Windows and Linux 'client\_repo\_dir' is mapped/mounted to the TACTIC
    'asset\_base\_dir'

-   The Windows and Linux 'client\_handoff\_dir' is mapped/mounted to the
    TACTIC 'server\_handoff\_dir'

        <checkin>
            <asset_base_dir>/mnt1/assets</asset_base_dir>
            <web_base_dir>/assets</web_base_dir>
            <win32_local_base_dir>C:/sthpw</win32_local_base_dir>
            <linux_local_base_dir>/tmp/sthpw</linux_local_base_dir>
            <win32_sandbox_dir>C:/sthpw/sandbox</win32_sandbox_dir>
            <linux_sandbox_dir>/tmp/sthpw/sandbox</linux_sandbox_dir>
            <win32_client_repo_dir>z:/assets</win32_client_repo_dir>
            <linux_client_repo_dir>/assets</linux_client_repo_dir>
            <win32_client_handoff_dir>z:/tactic_handoff<win32_client_handoff_dir>
            <win32_server_handoff_dir></win32_server_handoff_dir>
            <linux_client_handoff_dir>/tactic_handoff</linux_client_handoff_dir>
            <linux_server_handoff_dir>/home/apache/tactic_handoff</linux_server_handoff_dir>
            <version_padding>3</version_padding>
        </checkin>


