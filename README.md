# Web Application Firewall 


## Setting Up
1. Set up a virtual environment for python
    * Linux
        * sudo pip3 install virtualenv 
        * virtualenv venv
        * source ./venv/bin/activate - to activate the virtual environment
        * deactivate - you can use this to deactivate Venv when it is no longer required
2. Install all required dependencies after the activation of the virtual environment
    * pip3 install -r requirements.txt - Linux 
*Reference: https://note.nkmk.me/en/python-pip-install-requirements/* 
3. Set up the database via:
    * python3 init_db.py - if you are using Linux
4. Start the server 
    * python3 server.py - Linux
    The server by default runs on the http://localhost:5000

##Checking Database
*sqlite3 attacks.db
*SELECT * FROM attacks
