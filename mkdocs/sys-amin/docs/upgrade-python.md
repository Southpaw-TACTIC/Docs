# Upgrade TACTIC to Python 3

If you have an existing server running Python 2, it is easy to upgrade to Python 3.
TACTIC 4.7 is compatible with both Python 2 and Python 3.

> Note: If you are installing pycryptodomex in Python 3, and do not have this module running in Python 2, see Upgrade TACTIC > Pycryptdome Update to upgrade from Pycrypto to Pycryptodome.

## General Upgrade

The following steps must be taken to upgrade your TACTIC server, 

1. Install Python 3
2. Upgrade \_\_init\_\_.py in Python 2 site-packages/tacticenv with latest 4.7 file /src/install/data/_\_init_\_.py
3. Copy site-packages/tacticenv from Python 2 site-packages to Python 3 site-packages
4. Install Python 3 Modules,

    - pillow
    - pycryptodomex
    - lxml
    - requests
    - pytz

5. Update your TACTIC config file to use Python 3 for all services by updating the python directive:
        
        <services>
            ...
            <python>python3</python>
            ...
        </services>

    See Server Configuration > Configuration Checklist for the location of your TACTIC configuration file.

6. Update the TACTIC service. For Windows, see Windows section below. For linux, copy the Python 3 service file from,
    
        /src/install/service/tactic_python3

    into,

        /etc/init.d

    Enable the service with commands,

        chkconfig --add tactic_python3
        chkconfig --level 235 tactic_python3 on


7. Remove all \*.pyc files from your TACTIC source code. Mako and some other packages have been moved into the 3rd_party sources directory.


## RHEL Upgrade


1. Install python3 

        dnf install python 3

2. Replace /lib/python2.7/site-packages/tacticenv/_\_init_\_.py with latest 4.7 file /src/install/data/_\_init_\_.py

3. Copy  /lib/python2.7/site-packages/tacticenv into /lib/python3.7/site-packages

4. Install updated Python 3 modules using dnf or pip,
    - pillow
    - pycryptodomex
    - lxml
    - requests
    - pytz
    - DB connectivity module: ie. psycopg2, mysqlclient, etc.

    Using dnf,

        dnf install python3-pillow

    Using pip,

        python3 -m pip install pycryptodomex

5. Update your TACTIC config file to use Python 3 for all services by updating <python> tag:

        <services>
        ...
        <python>python3</python>
        ...
        </services>

6. Update the TACTIC service. For Windows, see Windows section below. For linux, copy the Python 3 service file from,
    
        /src/install/service/tactic_python3

    into,

        /etc/init.d

    Enable the service with commands,

        chkconfig --add tactic_python3
        chkconfig --level 235 tactic_python3 on

7. Remove all \*.pyc files from your TACTIC source code. Mako and some other packages have been moved into the 3rd_party sources directory.


## Windows 

1. Install python3

2. Replace C:\Python27\Lib\site-packages\tacticenv\_\_init_\_.py with latest 4.7 file \src\install\data\_\_init_\_.py

3. Copy  C:\Python27\Lib\site-packages\tacticenv into C:\Python37\Lib\site-packages

4. Install updated Python 3 modules: 

    - pillow
    - lxml
    - pycryptodomex
    - requests
    - jaraco.windows
    - pytz
    - pywin32
    - DB connectivity module - ie. psycopg2, mysqlclient

    We reccomend using pip to install updated packages. 

        python3 -m pip install pycryptodomex

5. Update your TACTIC config file to use Python 3 for all services by updating <python> tag:

        <services>
        ...
        <python>python3</python>
        ...
        </services>

6. Upgrade the Windows TACTIC service.

    i. Install Windows service Python 3 module: 

        python -m pip install pywin32

    ii. Remove the service originally installed under Python 2,

        python TACTIC/src/install/service/win32_service.py remove

    iii. Install the service under Python 3,

        python3 TACTIC/src/install/service/win32_service.py install

    > Note: Since last tested (Sept 2019), we had issues running Python 3 Windows Services. 
    
    The workaround required us to copy dll files from,
        
        C:\Python37\Lib\site-packages\pywin32_system32
    
    to
       
        C:\Python37\Lib\site-packages\win32
    
    The TACTIC service should run after this. If this does not solve service issues, try running TACTIC in debug mode:
    
        python3 src/install/service/win32_service.py debug

7. We recommend removing all *.pyc files from your TACTIC source code since we have moved and updated certain packages into TACTIC/3rd_party/




