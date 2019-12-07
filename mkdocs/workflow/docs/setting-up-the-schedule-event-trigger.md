# Setting Up The Schedule Event Trigger

The schedule event trigger is a server trigger that fires based on a defined time event, rather than changes made to sTypes within TACTIC. It can be set up to run daily or on particular time intervals.

1.  Create a &lt;scheduler&gt; tag in the &lt;services&gt; section tactic-conf.xml file in tactic\_data/config and set the tag to "true":

        <services>
        ...
        ...
        <scheduler>true</scheduler>
        </services>

    > **Note**
    >
    > Ensure that the &lt;process\_count&gt; is set to 3: &lt;process\_count&gt;3&lt;/process\_count&gt;

2.  Restart the TACTIC service (as the root user): service tactic restart

3.  Go to the Server Trigger table in the TACTIC Administrative layer and enter the following information:

    <table>
    <colgroup>
    <col width="30%" />
    <col width="30%" />
    <col width="40%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td><p>Event</p></td>
    <td><p>Script Path</p></td>
    <td><p>Data (Drop Down)</p></td>
    </tr>
    <tr class="even">
    <td><p>schedule</p></td>
    <td><p>scripts/script_path</p></td>
    <td><p>To Run Trigger Daily (24 Hour Clock):</p>
    <p>{ &quot;script_path&quot;: &quot;trigger/schedule_script&quot;, &quot;time&quot;: &quot;10:00&quot;, &quot;type&quot;: &quot;daily&quot;, }</p>
    <p>OR</p>
    <p>To Run Trigger on Set Interval (Interval and Delay Attributes in Seconds):</p>
    <p>{ &quot;script_path&quot;: &quot;trigger/schedule_script&quot;, &quot;type&quot;: &quot;interval&quot;, &quot;interval&quot;: &quot;20&quot;, &quot;delay&quot;: &quot;10&quot; }</p></td>
    </tr>
    </tbody>
    </table>

    > **Note**
    >
    > In the table that drops down from the Data column in the "Server Triggers" view, there is a table column in that drop down that is also called "Data". In this column, type one of the preceding setups set the trigger to run daily or at a set interval. Adjust the settings accordingly for the desired time.

4.  Save the drop down table from the "Data" column in the "Server Triggers" view by clicking the floppy disk button in the drop down.

5.  Save the schedule trigger by clicking the floppy disk button at the top of the "Server Triggers" view.

6.  Restart the TACTIC service again (as the root/sudo user) by typing "service tactic restart"

    > **Note**
    >
    > Every time you update this trigger, you will need to restart the TACTIC service for it to take effect

Here is a sample script. Batch() is required if the script needs to access information in TACTIC:

    import datetime
    from client.tactic_client_lib import TacticServerStub
    from pyasm.security import Batch

    print " >> Run schedule:", str(datetime.datetime.now())
    Batch()
    server = TacticServerStub.get()

    res = server.eval("@GET(sthpw/login.first_name)")

    print "First names in the system:", res
