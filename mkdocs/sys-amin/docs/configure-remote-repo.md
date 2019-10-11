# Configure the Remote Repo

The remote repository (repo) setting describes the specific environment
that remote users or a remote facility may use, in the situation where
it differs from the environment used by the master repository.

To set up a remote repo, you can insert an entry that represents users
or a group of users that fall under a certain IP address or IP mask
combo.

> **Note**
>
> If you want everyone at an IP address to use the same remote repo, a
> typical IP mask value is `255.255.255.255`

The login name is only required when you are not using an IP address or
IP mask combo to specify users. The sandbox path and local repo path can
be a network path like:

    \\<server_name>\<share_name>\..\repo

or (for Windows)

    Z:/repo
