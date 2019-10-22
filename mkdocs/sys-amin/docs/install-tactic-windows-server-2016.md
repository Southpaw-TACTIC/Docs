# Install TACTIC on Windows Server 2016
*Last Updated October 2019*

This is an installation guide for installing TACTIC on Windows Server using either PostgreSQL or MySQL.


## Install PostgreSQL



## Install MySQL

Install microsoft c++ resitributable 
Install MySQL 8

Install MySQL 8: Choose Only Server option, Legacy authentication
error when trying to use service account... chose windows default.
Add ProgramFiles\MySQL\bin. to System PATH variable 

- > VC for Python
- MySQL connoctor C ...after install copy this folder from Program Files to Program Files 86x
- > python -m pip install MySQL-python


## Install Python 3 and supporting modules

Unfortunately, Python is not preinstalled on Windows machines; however,
with the installer this is not difficult.</p><p>The Python installer does not set the Python path, so this must be added</p><p>Go to
Start→Control Panel→System
Click on the "Advanced" tab.
Select "Path" under "System Variables" and click the "Edit" button.
Add Python to the environment path: "C:\Python26\" to the end of the
"Variable Value"
To test that Python is working from the command prompt, run the command:
<code class="literal">python</code></p><p>You should get the following prompt:</p><pre class="screen">Python 2.6.2 (#67, Sep 28 2009, 12:41:11) [MSC v.1310 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
&gt;&gt;&gt;</pre>

<p>Note: You may be required to restart the server after updating the PATH variable.</p>
Not necessary on windows 2016


pip is the reccomended method of installing on Windows. 
python -m pip install requests



## Install Image Utilities ImageMagick and FFMPEG




## Install Apache




## Install TACTIC

Install TACTIC:

<p>If you haven’t done so already above, unzip Tactic Enterprise in a
temporary location like C:/temp</p><p>Go to
C:/temp/tactic_#../src/install/</p><pre class="screen"># cd C:/temp/tactic_#.#.#.#/src/install</pre><p>Execute:
install.py</p>

Execute

install.py -i false -t MySQL
* Need write permission to C:\ProgramFiles and C:\ProgramData

Modify configuration file for database information: vendor, port, username, password

src/pyasm/search/upgrade/mysql/bootstrap_load.py

