# Active Directory Integration

TACTIC provides the ability to easily connect to any active directory
installation for both authentication and for synchronization of user
data. With a set of directives in the TACTIC configuration file, it is
possible to connect to Active Directory for authentication and user
information.

This synchronization takes place at login time. At this point, TACTIC
takes the desired information for a particular user and caches it into
the "sthpw/login" search type. Subsequent requests would normally use an
issued ticket given at login time. On these requests, no further
querying of active directory is needed until the ticket expires or the
user signs out the application.

The active directory modules make use of win32 libraries for python.
These must be installed in order for the connection to active directory
to function properly

## TACTIC Configuration

There are a number of directives in the TACTIC config file that can be
used to configure the active directory settings. These allow you to
adjust TACTIC behavior to suit the needs of the facility.

In order to turn on active directory authentication, you must change the
authenticate class to the following:

```
<security>
    ...
    <authenticate_class>tactic.active_directory.ADAuthenticate</authenticate_class>
    ...
</security>
```

The following directives can be set under the active directory category:

**domains** - This is a "|" delimited list of the domains that exist in the
network. If specified, a selection box for domains will be added to the
login page.

**allow** - Can be "all", which allows everyone to log in if authentication
is approved or it can point to the name of a specific Active Directory
attribute that must be set to True. If a person is denied access, the
will receive the error: "Permission denied due to insufficient Active
Directory clearance".

**default_groups:** - Defines the default groups that a user will belong to
if none is specified. Multiple groups are delimited by "|".

**default_license_type:** - Determines the default license type for a user if
none is specified in the Active Directory attribute "tacticLicenceType".


## Example Configurations 
Below is an example of a typical entry in the TACTIC config file,

```
<active_directory>
    <domains>xxx|yyy|zzz</domains>
    <allow>tacticEnabled</allow>
    <default_groups>client</default_groups>
    <default_license_type>user</default_license_type>
</active_directory>

```

Allow anyone to login,

```
<active_directory>
    <allow>all</allow>
</active_directory>
```

Allow anyone to login and will be put in the "client" group if user has
no groups specified,


<!-- FIXME: Default groups should probably be specified... -->
```
<active_directory>
    <allow>all</allow>
</active_directory>
```

Only allow those with the attribute tacticEnabled in Active Directory set
to "true",

```
<active_directory>
    <allow>tacticEnabled</allow>
</active_directory>
```

Enable users to select a domain (xxx, yyy or zzz) in the login screen

```
<active_directory>
    <allow>all</allow>
    <domains>xxx|yyy|zzz</domains>
</active_directory>
```

## Synchronization

Active Directory attributes use camel case notation (aaaBbbCcc), while
TACTIC users lowercase with underscore separators for columns(
aaa_bbb\_ccc). In order to maintain consistency within the TACTIC
application, a mapping of columns from active directory to TACTIC is
provided. The following mappings are made by default:

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>mail</p></td>
<td><p>email</p></td>
</tr>
<tr class="even">
<td><p>telephoneNumber</p></td>
<td><p>phone_number</p></td>
</tr>
<tr class="odd">
<td><p>department</p></td>
<td><p>department</p></td>
</tr>
<tr class="even">
<td><p>displayName</p></td>
<td><p>first_name, last_name (broken up)</p></td>
</tr>
<tr class="odd">
<td><p>tacticLicenceType</p></td>
<td><p>license_type</p></td>
</tr>
</tbody>
</table>

The Active Directory variable "tacticLicenseType" is a custom variable
that indicates which type of license a particular user can occupy in
TACTIC. If this attribute is missing from a users active directory
profile, then they will be denied a login. This attribute can be used to
determine if a particular user in active directory is allowed to login
to TACTIC.

The only supported license for this attribute are "user" and "default".
Other license types have not yet been implemented yet.

On log in, TACTIC will look at all of the groups that a user belongs to
in Active Directory and match those group names to the "ad_login\_group"
column in the "sthpw/login_group" search type. This grouping list will
synchronized at this time, removing the users from groups not specified
in Active Directory and add those that are specified. This means that
Active Directory is in full control of the groups that a user is part of
and therefore must be managed entirely in Active Directory.

For the name of the group, TACTIC only looks at the root of the path to
map the group name. For example, an active directory group with the
following distinguished name:

memberOf: CN=supervisor,OU=Users,OU=EIS,DC=domain,DC=us,DC=xxxx,DC=com

TACTIC will need only "supervisor" to be entered in the "ad_login\_group"
column.

If on logging in, the number of users exceeds the number of users in the
license, then that user will be denied access and an entry in the
"sthpw/login" search type will not be made. However, all other users
currently registered can continue to work normally.
