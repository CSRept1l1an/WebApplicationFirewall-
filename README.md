# Web Application Firewall 
This is a lightweight and robust Web Application Firewall (WAF) developed from scratch in just 24 hours during the Hackathon event. This project aims to enhance web application security by providing a simple yet effective defense mechanism against common web attacks.
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
3. Start the server 
    * python3 server.py - Linux
    The server by default runs on the http://localhost:5000

## Checking Database
* sqlite3 waf.db
* SELECT * FROM attacks
