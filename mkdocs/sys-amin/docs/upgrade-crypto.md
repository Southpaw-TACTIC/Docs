
# PyCryptodome Update

If your TACTIC installation uses PyCrypto, we reccomend upgrading to PyCryptodome. PyCrypto has been flagged as insecure by the Python Community.
Support for PyCryptodome has been added in latest 4.7. You will need 

1. Install PyCryptodome
2. Update the TACTIC License File

## pip Install
If you are you using pip to install, run

Python 3:
    
    python3 -m pip install pycryptodomex

Python 2:
    
    python -m pip install pycryptodomex

## dnf Install

If you are using to install, run:

    yum install python3-pycryptodomex

## Update the TACTIC License
Once you've installed pycryptodome, you will see warnings in your server logs related to the TACTIC license functionality. These should not cause errors, but can you resolve these warnings by replacing the license file, usually found on Linux in,

    /opt/tactic/tactic_data/config/tactic-license.xml

and on Windows in,
   
    C:\ProgramData\Southpaw\Tactic\config\tactic-license.xml

with the updated license file found in,

    TACTIC/src/install/start/config/tactic-license.xml
