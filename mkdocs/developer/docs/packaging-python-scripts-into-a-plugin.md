# TACTIC - Packaging Python Scripts into a Plugin

**Creating Plugin for Scripts**

1.  Prepare a folder or folder structure containing all of the python scripts you would like to include in the plugin. The scripts can be contained within any folder level in the hierarchy. The plugin will allow you to have access to every one of those scripts.

2.  Copy your folder of scripts.

3.  On the server, go to the TACTIC installation location and locate the tactic\_data/plugins folder. For example, /home/tactic/tactic\_data/plugins. In this "plugins" folder, paste the folder of your scripts here.

    This specific "plugins" folder is tied directly into the TACTIC UI. By pasting your folder of scripts here, a series of plugins are created for each of the lowest level folders. Each of these lowest level folders could contain many different scripts. Essentially, only one folder could contain all the scripts and this would be the plugin. The entire folder structure with subfolders and final low level folders (plugins) will show up in the TACTIC "Plugin Manager" in the Administrative layer of TACTIC.

    For example, if there is a top level folder called "example\_scripts" with a lower level folder called "python\_scripts" that contained all of the scripts. If this entire "example\_scripts" folder was pasted into the /home/tactic/tactic\_data/plugins location on the server, the "Plugin Manager" in TACTIC will show that "example\_scripts" is a drop down folder and underneath there is a plugin called "python\_scripts" available in TACTIC for activation. This "python\_scripts" plugin would contain all of your scripts.

4.  Go to the Administrative layer in TACTIC and from the "Admin Link Startup" page, select "Plugin Manager".

5.  In the Plugin Manager, on the left side, there should be a list of files. Go to the folder that has all of your scripts and locate your plugin or plugins. The plugins are determined based on the description provided in Step 3.

6.  Click on one plugin and in the "Info" tab in the view that appears, click on the "Activate" button to activate the plugin. Wait until there is a notification in the view indicating that the plugin activated successfully. Activate each of the other plugins you have one at a time.

7.  Once all plugins are activated, refresh the browser. It will ensure proper activation.

8.  With the plugins installed, all of the classes contained within the scripts that were loaded with the plugin are accessible from the Script Editor in TACTIC. All you would need to do is know where the classes are located within the files. For example:

<!-- -->

    from example_scripts.python_scripts import python_class

**Updating Plugins with New and Modified Scripts**

To update the plugins with more scripts or apply changes to the scripts in the plugins, perform the following:

1.  Go to the "Plugin Manager" and select the plugin (package of scripts) to be modified.

2.  In the "Info" tab in the view, click the "Remove" button. This will deactivate the plugin. Wait for a message to appear that indicates that the plugin was removed successfully.

3.  Replace or modify any scripts in the folder or plugin that was deactivated in the /home/tactic/tactic\_data/plugins location.

4.  Once any new or modified scripts are added, go back to the "Plugin Manager", select the plugin that was modified, and in the "Info" tab in the view, click on the "Activate" button. Wait for a message to indicate the plugin activated successfully.

5.  Refresh the browser to ensure proper activation.

6.  You will now have access to the modified scripts from the Script Editor in TACTIC.


