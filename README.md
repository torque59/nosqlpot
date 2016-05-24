[![Baikal](https://baikal.io/badges/torque59/nosqlpot)](https://baikal.io/torque59/nosqlpot)

NoSQL-Honeypot-Framework (NoPo)
==

NoSQL-Honeypot-Framework (NoPo) is an open source honeypot for nosql databases that automates the process of detecting attackers,logging attack incidents. The simulation engines are deployed using the twisted framework.Currently the framework holds support for redis.

N.B : The framework is under development and is prone to bugs 

Screenshots
----
* Server Deployed
![Screenshot](http://i.imgur.com/4cCX3Me.png)

Installation
----

You can download NoPo by cloning the [Git](https://github.com/torque59/nosqlpot) repository:

    git clone https://github.com/torque59/nosqlpot.git
    
    pip install -r requirements.txt

NoPo works out of the box with [Python](http://www.python.org/download/) version **2.6.x** and **2.7.x** on any platform.


Added Features:
============================

- First Ever Honeypot for NoSQL Databases
- Support For Config Files 
- Simulates Protocol Specification as of Servers
- Support for Redis


Usage
----

Get a list of basic options :

    python nosqlpot.py -h

Deploy an nosql engine:

    python nosqlpot.py -deploy redis
    pythom nosqlpot.py -deplot couch

Deploy an nosql engine with a configuration file:

    python nosqlpot.py -deploy redis -config filename
    
Log commands,session to file :

    python nosqlpot.py -deploy redis -out log.out

