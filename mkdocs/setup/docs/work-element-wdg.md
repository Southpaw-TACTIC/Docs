# Work Button

**Description**

The Work Element Widget is used for accessing the checkin and checkout
tool needed to handle a task assigned. After a task is assigned, an
artist can go to the "My Tasks" or any other task page where there is a
"Work" column which will expand to this widget. You can carry out
serveral typical functions related to check-in and check-out in the sub
tabs that open. You can even customize what tabs are opened when the
work button is clicked on.

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Name</strong></p></td>
<td><p>Work</p></td>
</tr>
<tr class="even">
<td><p><strong>Class</strong></p></td>
<td><p>tactic.ui.table.WorkElementWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>Category</strong></p></td>
<td><p>Table Element Widget</p></td>
</tr>
<tr class="even">
<td><p><strong>Supported Interfaces</strong></p></td>
<td><p>TableLayoutWdg</p></td>
</tr>
<tr class="odd">
<td><p><strong>TACTIC Version Support</strong></p></td>
<td><p>3.5.0<br />
</p></td>
</tr>
<tr class="even">
<td><p><strong>Required database columns</strong></p></td>
<td><p>none</p></td>
</tr>
</tbody>
</table>

**Usage**

When clicked on, it opens up a new Work area tab with 3 sub tabs
underneath which comprise all the functions an artitst would need when
assigned a task. He can enter notes, change task status, review check-in
history, check in, and check out files.

The General Check-in Widget appears in the Check-in sub tab. You can
click "Browse" here to select the file to be checked in. The is\_current
checkbox in Options can be used to make a snapshot current on checking
in. The link checkbox, when checked, links the sandbox directory to the
process tied to the task. It makes it easy for an artist to jump to a
different process and checks out their snapshots into the current
sandbox associated with the task. Otherwise, if you check out a file
from the model process, it will be copied to the model sandbox folder.

**Options**

<table>
<colgroup>
<col width="28%" />
<col width="71%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>checkout_panel_script_path</strong></p></td>
<td><p>Deprecated in 3.5. Use the tab_config_&lt;&gt; method to set up custom checkout tab</p></td>
</tr>
<tr class="even">
<td><p><strong>checkout_script_path</strong></p></td>
<td><p>A custom check-out script path you can specify to override the default check-out script. The default check-out script checks out everything under the selected snapshot. Refer to Example 4.</p></td>
</tr>
<tr class="odd">
<td><p><strong>validate_script_path</strong></p></td>
<td><p>A script path pointing to a JS script that is run before the actual check-in. If it throws an error using &quot;throw(&lt;error message&gt;)&quot;, the check-in will not initiate. You can also use it to run some client-side preprocessing of the file or directory.</p></td>
</tr>
<tr class="even">
<td><p><strong>transfer_mode</strong></p></td>
<td><p>Upload, copy, move, preallocate are supported. 'preallocate' can only be used if the client machine has direct disk write access to the TACTIC asset repo. It skips the need to hand off the files in the handoff directory. 'copy' is recommended for most situation when users are usually granted only read access to the TACTIC asset repo.</p></td>
</tr>
<tr class="odd">
<td><p><strong>mode</strong></p></td>
<td><p>Sequence, file, dir, and add are supported. 'sequence' is for file sequence checkin; 'file' is for single file checkin, 'dir' is for directory checkin and 'add' if for appending file or dir to an existing snapshot. If not specified, multiple selections will be available for the user to choose. Note: upload transfer mode only supports single file or file sequence check-in.</p></td>
</tr>
<tr class="even">
<td><p><strong>checkin_panel_script_path</strong></p></td>
<td><p>Deprecated in 3.5. Use the tab_config_&lt;&gt; method to set up custom checkin tab</p></td>
</tr>
<tr class="odd">
<td><p><strong>checkin_script_path</strong></p></td>
<td><p>A custom checkin script path you can specify to override the default check-in script. This can be used in conjunction with the validate_script_path.</p></td>
</tr>
<tr class="even">
<td><p><strong>process</strong></p></td>
<td><p>If set, the process specified will be pre-selected when the General Checkin Widget is drawn,</p></td>
</tr>
<tr class="odd">
<td><p><strong>lock_process</strong></p></td>
<td><p>If set to true, the user will not be able to choose a different process during check-in on the General Checkin-in Widget</p></td>
</tr>
<tr class="even">
<td><p><strong>checkin_relative_dir</strong></p></td>
<td><p>If specified, e.g. WIP, it is appended to the current sandbox directory and preselcted as the directory to be checked in. It’s applicable to Direcotry-type checkin</p></td>
</tr>
<tr class="odd">
<td><p><strong>checkin_ui_options</strong></p></td>
<td><p>It applies to the check-in options of the CheckinWdg. Supported attribute at the moment is &quot;is_current&quot; e.g. \{&quot;is_current&quot;:&quot;false&quot;} would make all check-ins non-current. \{&quot;is_current&quot;:&quot;optional&quot;} would make the checkbox unchecked by default. Not specifiying it would render the option available to the user to choose at the check-in time.</p></td>
</tr>
<tr class="even">
<td><p><strong>show_versionless_folder</strong></p></td>
<td><p>If set to true, it displays the latest and current versionless folders.</p></td>
</tr>
</tbody>
</table>

**Implementation**

The following defines the default "Work" element. It looks a bit
complicated but in most cases, you would just need to simply change the
different options available through "Edit Column Definition":

     <element name="work" title="Work on Task">
            <display class="tactic.ui.table.WorkElementWdg">
            <transfer_mode>upload</transfer_mode>
            <cbjs_action>
          var tbody = bvr.src_el.getParent(".spt_table_tbody");
          var element_name = tbody.getAttribute("spt_element_name");
          var search_key = tbody.getAttribute("spt_search_key");
          var checkin_script_path = bvr.checkin_script_path;
          var checkin_ui_options = bvr.checkin_ui_options;
          var validate_script_path = bvr.validate_script_path;
          var checkout_script_path = bvr.checkout_script_path;
          var checkin_mode = bvr.mode;
          var transfer_mode = bvr.transfer_mode;
          var sandbox_dir = bvr.sandbox_dir;
          var lock_process = bvr.lock_process;

          var server = TacticServerStub.get();
          var code = server.eval( "@GET(parent.code)", {search_keys: search_key} );

          spt.tab.set_main_body_tab();
          spt.tab.add_new();
          var kwargs = {
            'search_key': search_key,
            'checkin_script_path': checkin_script_path ,
            'checkin_ui_options': checkin_ui_options ,
            'validate_script_path': validate_script_path ,
            'checkout_script_path': checkout_script_path,
            'mode': checkin_mode ,
            'transfer_mode': transfer_mode,
            'sandbox_dir': sandbox_dir,
            'lock_process': lock_process

            }
          var title = "Task: " + code;
          var class_name = "tactic.ui.tools.sobject_wdg.TaskDetailWdg";
          spt.tab.load_selected(search_key, title, class_name, kwargs);
          </cbjs_action>
          <icon>WORK</icon>
          </display>
     </element>

The following defines a different usage of it using copy trasnfer mode,
a custom checkout script and a custom validating checkin script. The
value of the two script paths are the script\_path you have saved in the
Script Editor. lock\_process is set to false. To enable these options,
you can do it in the context menu "Edit Column Definition" and set the
following:

       checkout_script_path: checkout/all_processes
       validate_script_path: checkin/validate_frames
       transfer_mode: copy
       lock_process: false

The following shows a way to customize what the small check-out button
does in the checkout\_tool view. In widget config, we will set the column
definition for the element checkout for the "sthpw/snapshot" search
type. It can be accessed through "Edit Column Definition".

       checkout_script_path: checkout/checkout_tool_script

**Script Samples**

Example 1: checkin/validate\_frames

    var values = bvr.values;
    var file_path = values.file_paths[0];
    var sk = values.search_key;
    var applet = spt.Applet.get();

    var file_list = applet.list_dir(file_path);
    var server = TacticServerStub.get();
    var st = 'prod/shot';
    var shot = server.get_by_search_key(sk);
    var frame_count = parseInt(shot.frame_count, 10);
    for (var i=0; i <file_list.length; i++){

        var base =spt.path.get_basename(file_list[i]);
        if ( base == 'FRAMES') {
            var frames = applet.list_dir(file_list[i]);

            if (frames.length != frame_count) {
                 throw('Frames length in FRAMES [' + frames.length
                    + '] folder does not match shot\'s frame count');
            }

        }
    }

Example 2: checkout/all\_processes. It illustrates how to implement a
custom check-out that only checks out a portion of what has been checked
in.

    //back up the Work-in-progress folder
    function backup_WIP(bvr) {
         var sandbox_dir = bvr.sandbox_dir;
         var applet = spt.Applet.get();
         var found_WIP = false;
         var dirs = applet.list_dir(sandbox_dir, 0);

         for (var k=0; k < dirs.length; k++){
             if (/WIP$/.test(dirs[k])){
                found_WIP = true;
                break;
             }
         }
         if (!found_WIP) {
               alert('WIP folder not found. Backing up of WIP folder aborted')
         }
         else {

         var server = TacticServerStub.get();
         var folder = spt.path.get_basename(sandbox_dir);

         var date_obj = new Date();
         var suffix = date_obj.getFullYear().toString()
                 + spt.zero_pad((date_obj.getMonth() + 1).toString(), 2)
                 + spt.zero_pad(date_obj.getDate().toString(), 2) + '_'  +
                   spt.zero_pad(date_obj.getHours().toString(), 2)
                    + spt.zero_pad(date_obj.getMinutes().toString(),2);

         var parts = sandbox_dir.split(/[\/\\]/);


         sandbox_dir = sandbox_dir + '/WIP';
         var backup_dir = parts.join('/')  + '/WIP' + '_' + suffix;


         applet.copytree(sandbox_dir, backup_dir);

         //remove the contents of WIP
         applet.rmtree(sandbox_dir);
         applet.makedirs(sandbox_dir);

         }
    }

    // just checkout a subfolder named REF. if it's not found, just check out the
    // first subfolder
    function checkout_snapshot_table(bvr){

        var top = bvr.src_el.getParent(".spt_checkin_top");
        var table = top.getElement(".spt_table");
        var search_keys = spt.dg_table.get_selected_search_keys(table);
        if (search_keys.length == 0) {
             alert('Please check the checkbox(es) to check out a version.');
        }
        else if (search_keys.length > 1) {
            alert('Please check only 1 checkbox at a time. Multi-selection is' +
    ' only supported for Full Check-out Selected in the Gear menu.');
            return;
        }

        spt.app_busy.show("Custom Check-out snapshots", "Copying to Sandbox...");
        var server = TacticServerStub.get();

        var top = bvr.src_el.getParent('.spt_checkin_top');
        var sandbox_input = top.getElement('.spt_sandbox_dir');
        if (sandbox_input)
            bvr.sandbox_dir = sandbox_input.value;
        for (var i =0; i < search_keys.length; i++) {

            checkout_snapshot(bvr, search_keys[i]);
        }
        spt.app_busy.hide();
    }

    function checkout_snapshot(bvr, snapshot_key, downlevel) {
            var server = TacticServerStub.get();


            try {
            var paths = server.get_all_paths_from_snapshot(snapshot_key);


            //var sandbox_dir =
    server.get_client_dir(snapshot_key,{mode:'sandbox'});
            var sandbox_dir = bvr.sandbox_dir;
            var applet = spt.Applet.get();

            for (var i = 0; i < paths.length; i++ ) {
                var path = paths[i];
                var parts = path.split(/[\/\\]/);
                var dirs = applet.list_dir(path);


                var tar_dir = '';
                for (var j=0; j < dirs.length; j++) {
                     if ((/REF/i).test(dirs[j]))
                         tar_dir = dirs[j];
                }
                //just take the first one if REF is not found
                if (!tar_dir) {
                     alert('REF not found. First subfolder is checked out');
                     tar_dir = dirs[0];
                }

                var folder = spt.path.get_basename(tar_dir);
                var new_path = path + '/' + folder;

                var sand_paths = applet.list_dir(sandbox_dir, 0);
                for (var j=0; j< sand_paths.length; j++) {
                     var dst_folder = spt.path.get_basename(sand_paths[j]);
                     if (dst_folder == 'REF') {
                          alert('REF folder already exists in ['
                           + sandbox_dir + '] Please rename or remove it first.');
                          return;
                     }
                }

                // the applet can decide between copy_file or copytree

                applet.copytree(new_path, sandbox_dir + "/" + folder);

            }
            }
            catch(e){
              alert(spt.exception.handler(e));
            }
        }


    backup_WIP(bvr);
    var down_level = 1;
    checkout_snapshot_table(bvr, down_level);

Example 3: Custom Checkout button callback passing a specific script for
the Check-out Widget popup using display option
"checkout\_panel\_script\_path"

        var class_name = 'tactic.ui.widget.CheckoutWdg';

        var values = bvr.values;

        var search_key = values.search_key;
        var sandbox_dir = values.sandbox_dir;
        var process = values.process;

        var options = { 'show_publish': 'false',
            'process': process,
            'search_key': search_key,
            'checkout_script_path': 'checkout/custom_checkout',
            'sandbox_dir': sandbox_dir
                };
       var popup_id ='Check-out Widget';
       spt.panel.load_popup(popup_id, class_name, options);

Example 4: Custom check-out script for the small check-out button in the
checkout\_tool view. This can be used to customize a quick-checkout for
the latest or current snapshot without opening the Check-out popup
widget, using display option "checkout\_script\_path"

    function checkout_snapshot(bvr) {
        var values = bvr.values;

        var snapshot_key = values.search_key;
        var context = values.context;


            var server = TacticServerStub.get();
            // get the files for this snapshot, always get the latest
            // instead of relying on the last snapshot when the UI was drawn

            try {
            var paths = server.get_all_paths_from_snapshot(snapshot_key);

            //var sandbox_dir = server.get_client_dir(snapshot_key,{mode:'sandbox'});
            // This one comes from values as the sandbox_dir is determined by
            // the snapshot only
            var sandbox_dir = values.sandbox_dir;

            var applet = spt.Applet.get();

            for (var i = 0; i < paths.length; i++ ) {
                var path = paths[i];
                var parts = path.split(/[\/\\]/);
                var dirs = applet.list_dir(path);


                var tar_dir = '';
                for (var j=0; j < dirs.length; j++) {
                     if ((/REF/i).test(dirs[j]))
                         tar_dir = dirs[j];
                }
                //just take the first one if REF is not found
                if (!tar_dir) {
                     alert('REF not found. First subfolder is checked out');
                     tar_dir = dirs[0];
                }
                var folder = spt.path.get_basename(tar_dir)
                var new_path = path + '/' + folder;

                var sand_paths = applet.list_dir(sandbox_dir, 0);
                for (var j=0; j< sand_paths.length; j++) {
                     var dst_folder = spt.path.get_basename(sand_paths[j]);
                     if (dst_folder == 'REF') {
                          alert('REF folder already exists in [' + sandbox_dir + '] Please rename or remove it first to avoid mixing files.');
                          return;
                     }
                }

                // the applet can decide between copy_file or copytree
                applet.copytree(new_path, sandbox_dir + "/" + folder);
            }
            }
            catch(e){
              alert(spt.exception.handler(e));
            }
        }
    checkout_snapshot(bvr);

Example 5: Custom checkin\_script using display option
"checkin\_script\_path". The default snapshot\_type is file, if the file
extension is .mov, the snapshot\_type is set to 'mov'.

    var file_paths = bvr.values.file_paths;
    var description = bvr.values.description;
    var search_key = bvr.values.search_key;
    var context = bvr.values.context;
    var transfer_mode = bvr.values.transfer_mode
    var is_current = bvr.values.is_current;
    var path = file_paths[0]
    spt.app_busy.show("File Checkin", path);

    var snapshot_type = 'file';
    if (path.test(/\\.mov$/)){
        snapshot_type = 'mov';
    }
    var server = TacticServerStub.get();
    snapshot = server.simple_checkin(search_key, context, path,
    {description: description, mode: transfer_mode, is_current: is_current,
     snapshot_type:'mov'});
