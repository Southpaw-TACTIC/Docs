# Messaging

**Description**

The Subscription Bar Widget allows user to subscribe to an sObject. This
widget provides a convenient way to track any actions or behaviors on an
sObject, including actions from different users. All the messages will
be recorded into Subscription Bar Widget and Message History.

**Info**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Subscription Bar Widget</p></td>
</tr>
<tr class="even">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.app.SubscriptionBarWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>4.1+</p></td>
</tr>
<tr class="even">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>

**Implementation**

Specify (or look up) the name of the *Inject Subscription Action* under
**Admin Views → Project → Custom Layout Editor→Gear Menu**.

In the example below, in order to activate the *Subscription Bar*, a
sample script has been created and named **Test\_Messaging**:

Look up and edit that Test\_Messaging script in the custom layout editor.
Use the following HTML code as an example of what to add to the sample
script:

![image](media/131030075724.png)

    <div class="Test_Messaging">
      <element>
        <display class="tactic.ui.app.SubscriptionBarWdg">
      </display>
      </element>
    </div>

After running the test button, a Test Custom layout window will appear:

Once the subscription bar has been set up, users can select the sObject
they want to subscribe by right clicking the sObject and choosing the
option **Subscribe to Item**:

Now a simple subscription bar has been set up and targeted to selected
sObject. Any actions, such as checking in files, editing description and
changing status, from other users will be recorded.

**Advanced**

A detailed subscription history could be viewed in **Message History**.
This tab can be found by clicking the **Subscription History** icon in
every message:

Each entry contains all the detailed information of the message, such as
'Code', 'Category' and 'Login'.

![image](media/131030072813.png)
