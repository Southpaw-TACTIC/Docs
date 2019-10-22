
# Asset Storage

Proper management of assets and asset metadata are essential to managing
the TACTIC service. Versioned assets are by far the most disk space
consuming element of asset management. TACTIC can store its asset data
in any filesystem path location. All that is required is that the tactic
configuration file contains the path to a directory writable by the
TACTIC service user.

-   **Local Access** -  In a simple configuration, the TACTIC service is
    enabled on the TACTIC host, and all assets checked in and checked out of
    TACTIC are stored on the local filesystem. Typically a user is created
    to run the TACTIC service, or an already assigned user is simply used to
    run the TACTIC service.

-   **Network Access** - In an addition to the simple configuration, the
    TACTIC service is enabled on the tactic host and all assets checked in
    and checked out tactic are stored on a network mount. Typically a user
    is created to run the TACTIC service and be able to write to the network mount.

-   **TACTIC user permissions** - It is important to note that in a network
    accessible filesystem, allocation of permissions are important only for
    the TACTIC user. Regular system users should not have access to the
    TACTIC assets directory.

-   **Browsable access to assets** -  During some conversions to the management
    of assets by TACTIC, a frequent request is for regular user access to
    the assets directory managed by TACTIC. There really is not the much to
    see in these directories as tactics naming convention for versioning of
    assets creates files and directories that are largely mysterious in
    their arrangement.

    Is very important that the files that are managed by tactic are not
    touched by regular users. Manipulating files or directories managed by
    tactic will definitely result in data loss. Regular users should not
    have writable access to tactic asset directories.

## Configure TACTIC

The asset storage directory must be configured in the TACTIC configuration file.
See Configuration Checklist for the location of this file.
Set asset_base_dir as the directory where TACTIC will checkin files.
You must restart the TACTIC service after changing the asset_base_dir.

```

<checkin>
    ...
    
    <asset_base_dir>path/to/assets/dir</asset_base_dir>
    ...
</checkin>
```



## Configure Webserver - Apache

The webserver must also have access to the asset storage directory.


For Apache, edit the provided tactic.conf file,

    /etc/httpd/conf.d/tactic.conf


- Change this: 

```
    <Directory "/home/apache/assets" >
        Options FollowSymLinks
        AllowOverride None
        Order Allow,Deny
        Allow from All
    </Directory>
```

- To:

```
    <Directory "path/to/assets/dir" >
        Options FollowSymLinks
        AllowOverride None
        Order Allow,Deny
        Allow from All
    </Directory>
```

- Change this:

```
    Alias /assets "/home/apache/assets"
```

- To:

```
    Alias /assets "path/to/assets/dir"
```

Restart Apache after making changes to the tactic.conf file.


<!-- TODO: Include section on base_dir_alias -->
