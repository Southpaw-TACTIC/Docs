# Setup Email

## Configuration
In order to send out notifications as email in TACTIC, the mailserver must be configured
in TACTIC. Below is an example of a mailserver configuration in the TACTIC configuration file. See Configuration Directives > Services for a full list of directives.


Example,

```
<services>
    ...
    <mailserver>smtp.googlemail.com</mailserver>
    <mail_tls_enabled>true</mail_tls_enabled>
    <mail_name>TACTIC</mail_name>
    <mail_user>tactic@southpawtech.com</mail_user>
    <mail_password>password</mail_password>
    <mail_port>587</mail_port>
    <mail_default_admin_email>admin@southpawtech.com</mail_default_admin_email>
    <notify_user>exceptions@southpawtech.com</notify_user>
    ...
</services>
```

## Test Notifications

Go to the Notifications view under:

**Admin Views → Site Admin → Notifications**

Click on the green plus button on the tool shelf to insert new a
notification.

Fill in the following the minimum fields to create a test notification:

![image](media/2_setup_email_email_test.png)

Click on the **Email Test** button to send out a test email to the
recipient.

For further details on setting up advanced notifications, please refer
to the doc titled: **Advanced Notification Setup**.
