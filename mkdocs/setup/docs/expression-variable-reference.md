# Expression Variable Reference

**Expression Variable Reference**

There are a number of predefined variables in the expression language.
The following list all of the available variables:

-   LOGIN - the login of the current user

-   LOGIN\_ID - the login id of the current user

-   LOGINS\_IN\_GROUP - the group of logins belonging to the group the
    current user is in

-   PROJECT - code of the current project

-   PROJECT\_URL - the URL to the project’s home page (ex:
    <http://10.0.0.65/tactic/media>)

-   BASE\_URL - The base URL of the TACTIC installaiton (ex:
    <http://10.0.0.65/>)

**Table 1.**

<table>
<colgroup>
<col width="22%" />
<col width="43%" />
<col width="34%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Description</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NOW</p></td>
<td><p>Current day and time</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="even">
<td><p>TODAY</p></td>
<td><p>Current day at midnight (12:00 am)</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="odd">
<td><p>THIS_MINUTE</p></td>
<td><p>[multiblock cell omitted]</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="even">
<td><p>NEXT_MINUTE</p></td>
<td><p>Now + 1 minute</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="odd">
<td><p>PREV_MINUTE</p></td>
<td><p>Now + 1 minute</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="even">
<td><p>THIS_HOUR</p></td>
<td><p>This hour at 0 minutes</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="odd">
<td><p>NEXT_HOUR</p></td>
<td><p>THIS_HOUR + 1 hour</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="even">
<td><p>PREV_HOUR</p></td>
<td><p>THIS_HOUR - 1 hour</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="odd">
<td><p>NEXT_DAY</p></td>
<td><p>Today + 1 day</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="even">
<td><p>THIS_YEAR</p></td>
<td><p>The first day of this year at midnight (12:00am)</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="odd">
<td><p>NEXT_YEAR</p></td>
<td><p>THIS_YEAR + 1 year</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="even">
<td><p>PREV_YEAR</p></td>
<td><p>THIS_YEAR - year</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="odd">
<td><p>THIS_MONTH</p></td>
<td><p>the first day of this month at midnight (12:00am)</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="even">
<td><p>NEXT_MONTH</p></td>
<td><p>THIS_MONTH + 1 month</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="odd">
<td><p>PREV_MONTH</p></td>
<td><p>THIS_MONTH - 1 month</p></td>
<td><p>[multiblock cell omitted]</p></td>
</tr>
<tr class="even">
<td><p>NEXT_***DAY</p></td>
<td><p>Replace <strong>*</strong> with a particular day of the week</p></td>
<td><p>NEXT_MONDAY: the next day that is a Monday at midnight</p></td>
</tr>
<tr class="odd">
<td><p>PREV_***DAY</p></td>
<td><p>Replace <strong>*</strong> with a particular day of the week</p></td>
<td><p>PREV_SATURDAY: the last day that was a Saturday at midnight</p></td>
</tr>
<tr class="even">
<td><p>**_DAY_AGO</p></td>
<td><p>Replace ** with any number between 1 and 12</p></td>
<td><p>10_DAY_AGO: today - 10 days</p></td>
</tr>
<tr class="odd">
<td><p>**_DAY_AHEAD</p></td>
<td><p>Replace ** with any number between 1 and 12</p></td>
<td><p>5_DAY_AHEAD: today + 5 days</p></td>
</tr>
<tr class="even">
<td><p>**_WEEK_AGO</p></td>
<td><p>Replace ** with any number between 1 and 12</p></td>
<td><p>same usage as **_DAY_AGO</p></td>
</tr>
<tr class="odd">
<td><p>**_WEEK_AHEAD</p></td>
<td><p>Replace ** with any number between 1 and 12</p></td>
<td><p>same usage as **_DAY_AHEAD</p></td>
</tr>
<tr class="even">
<td><p>**_MONTH_AGO</p></td>
<td><p>Replace ** with any number between 1 and 12</p></td>
<td><p>same usage as **_DAY_AGO</p></td>
</tr>
<tr class="odd">
<td><p>**_MONTH_AHEAD</p></td>
<td><p>Replace ** with any number between 1 and 12</p></td>
<td><p>same usage as **_DAY_AHEAD</p></td>
</tr>
<tr class="even">
<td><p>**_YEAR_AGO</p></td>
<td><p>Replace ** with any number between 1 and 12</p></td>
<td><p>same usage as **_DAY_AGO</p></td>
</tr>
<tr class="odd">
<td><p>**_YEAR_AHEAD</p></td>
<td><p>Replace ** with any number between 1 and 12</p></td>
<td><p>same usage as **_DAY_AHEAD</p></td>
</tr>
</tbody>
</table>

These variables can be used for to refer to state information in
searches. This expression will retrieve all the login information for
the current user.

    @GET(sthpw/login['login',$LOGIN])

They can also be used to find items between certain dates. This
expression will retrieve all snapshots for this week starting at Sunday.

    @GET(sthpw/snapshot['timestamp','>',$LAST_SUNDAY]['timestamp','<',$NEXT_SUNDAY])

The following are shorthands that do not require a starting point or
environment sobject. They can be used in an absolute expression:

-   login - the currently logged in user login attribute

-   project - the current project

-   date - a date object with today’s date

-   palette - a palette object used for accessing different attributes of
    the palette for the current project. e.g. @GET(palette.background) can
    be used in the css for a Custom Layout Widget

The following are shorthands that require a starting point or
environment sobject:

-   parent - the parent of the current related sobject @GET(parent.code)

-   search\_type - the sType sobject. e.g. @GET(.search\_type.title)

-   connect - the connected sobject registered in the connection sType.
    Refer to the API methods like connect\_sobjects() and get\_connected\_sobjects()

    To filter down to a particular connected sobject based on the context
    attribute, which defaults to 'task', use @CONTEXT.

    e.g. @GET(prod/asset.connect\['@CONTEXT','some\_task'\].description)

The following variables are only used in Naming. Refer to the file
naming section for details.

-   EXT - file extension

-   BASEFILE - the filename portion of the file without the extension


