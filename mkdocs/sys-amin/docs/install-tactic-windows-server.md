# Install TACTIC on Windows Server
*Last Updated October 2019*

This is an installation guide for installing TACTIC on Windows Server 2019 using PostgreSQL. For other database types, see guides in Install TACTIC Application.
TACTIC has been tested on Windows Server 2008 and later.

> Tip: Install Google Chrome as Windows Server 2019 will come with Internet Explorer as the default browser.

Before you start the installation, download the TACTIC source code, available from <a href="http://github.com/Southpaw-TACTIC/TACTIC">GitHub</a> or the <a href="http://community.southpawtech.com/community/link/downloads">community downloads page</a>.

## Install PostgreSQL

1. Download the latest version from the <a href="https://www.postgresql.org/download/windows/">PostgreSQL site</a>. The visual installer is recommended as it is easy to use.

    The visual installer will have you set the following settings:

    - Password for postgres superuser
    - PostgreSQL data folder 
    - PostgreSQL port 

    > Note: It is recomended to install PostgreSQL on the default port 5432.

    > Note: You will need the password when connecting with TACTIC later in the installation.

2. After installing PostgreSQL, add the psql executable to the system PATH variable.
    You will need to add the path,

        <PostgreSQL install dir>\bin

    For example,

        C:\Program Files\PostgreSQL\12\bin

    See "System PATH variable" for instructions to edit the PATH variable.

    Test that PostgreSQL was added to the system PATH variable running the command,

        psql

<!-- TODO: You should get the following output -->

3. Finally, for the TACTIC installation, backup the file,

        <PostgreSQL install dir>\data\pg_hba.conf

    and replace with,

        <TACTIC source code>\src\install\postgresql\pg_hba.conf

    Restart PostgreSQL from the Services manager.

<!-- TODO: Mention that PostgreSQL no longer allows local connections -->



## Install Python 3 and supporting modules

1. Download the installer from the <a href="https://www.postgresql.org/download/windows/">Python website</a>. 
    Python 3.7+ is reccomended for TACTIC 4.7. Run the installer.

2. Add the Python executable to the system PATH variable:

        <Python install dir>

    This could vary based on your installation. For example,
        
        C:\Users\Adminstrator\AppData\Local\Programs\Python\Python37


3. Test that Python was added to the system PATH variable by running the command:

        python

    You should get the following output,

        C:\Users\Administrator>python
        Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>>

4. Install supporting support with pip. In the command prompt, run the following command,

        python -m pip install pillow lxml pycryptodomex requests jaraco.windows pytz pywin32

    If you are installing with PostgreSQL, install the Python PostgreSQL connectivity module,

        python -m pip install psycopg2


## Install Image Utilities ImageMagick and FFMPEG

Download <a href="https://imagemagick.org/index.php">ImageMagick</a> and run the installation wizard.
Be sure to select the following options during installation:
    
- Install FFMPEG
- Install legacy utilities
- Add to System PATH variable

## Install HTTP Apache

Visit the Apache website and download installation files for <a href="https://httpd.apache.org/docs/current/platform/windows.html">Windows</a>.

Unzip the installation achive and place the Apache folder in C,

    C:\Apache24

Install the Apache service by running the command,

    C:\Apache24\bin\httpd.exe -k install

Start the Apache service from the Services manager and test Apache by visiting "127.0.0.1" in browser.


## Install TACTIC

Execute install.py from the TACTIC source code:

    python <TACTIC source code dir>\src\install\install.py

> Note: The installation requires write permission to C:\ProgramFiles and C:\ProgramData
and you may need to run this with adminstrator priviledges.

During the installation, you will set the TACTIC Install Directory.

Test the installation by opening a command prompt and running,

    python <TACTIC Install Directory>\src\bin\startup_dev.py

<!--  TODO: Screen shot of output -->



## Configure PostgreSQL

For ease of installation, the provided TACTIC pg_hba.conf file configures PostgreSQL to not use a password.
To reconfigure PostgreSQL to use the password set during PostgreSQL installation, replace the TACTIC pg_hba.conf file
with the original. Restart PostgreSLQ after replacing with the original file.


## Configure HTTP Apache

1. **Enable Apache Modules**

    In the file,
        
        C:\Apache24\conf\httpd.conf

    Make sure the following lines are uncommented,

        LoadModule rewrite_module modules/mod_rewrite.so
        LoadModule proxy_module modules/mod_proxy.so
        LoadModule proxy_http_module modules/mod_proxy_http.so
        LoadModule proxy_balancer_module modules/mod_proxy_balancer.so
        LoadModule deflate_module modules/mod_deflate.so
        LoadModule slotmem_shm_module modules/mod_slotmem_shm.so
        LoadModule filter_module modules/mod_filter.so
        LoadModule lbmethod_byrequests_module modules/mod_lbmethod_byrequests.so

    These lines may already be uncommented, depending on your distribution and version of Apache. 
    You need version 2.0.31 or later.

2. **Enable TACTIC Apache Configuration**

    An Apache configuration file for TACTIC is generated during installation. This file must be copied into the Apache 
    configuration folder.

    Copy,

        C:\ProgramData\Southpaw\Tactic\config\tactic_win32.conf

    Into,

        C:\Apache24\conf\

    Include the TACTIC configuration file in the Apache configuration file. Edit 

        C:\Apache24\conf\httpd.conf

    Add the following line to the end of this file,

        Include conf/tactic_win32.conf

3. **Restart the Apache service**


## Fix for Python Windows Service 

The TACTIC Windows service is installed during installation with install.py 

Unfortunately, at the time this documentation has been last updated, you will need to adjust the 
Python pywin32 module.

Copy contents from,

    <Python install directory>\Python37\Lib\site-packages\pywin32_system32 
    
into,

    <Python install directory>\Python37\Lib\site-packages\win32

You should now be able to start the TACTIC service from the Services manager. If the service fails to start,
you can try to debug by running the command,

    python <TACTIC Install Directory>\src\install\service\win32_service.py debug


<!-- TODO: Conclusion? -->


## System PATH Variable

To update the system PATH variable on Windows, navigate to,

    Start > Control Panel > System and Security> System > Advanced system settings

Click Environment Variables, under System variables select the "path" variable, and "Edit".


