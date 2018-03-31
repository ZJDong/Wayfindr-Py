# Wayfindr-Py

Zhijian Dong (17313074)

0. Introduction

This is python code for group 15's project 'Wayfindr' in module ASE. It's mainly used to regularly request the noise data from internet APIs and save them to mongoDB. Meanwhile, it can monitor the changes in mongoDB. Once it gets the data changes, it will unset the changing flag to let the GO APP know and then recalculate the route for users. More, it has the error handling ability. Even if any unexceped error happened like one of the machines on which runs the database is dead, it will automaticly change its connecting to the replication machine without terminating.

1. Setting up

(python 3.6.4) Required packages: threading, requests, pymongo, time.

(MongoDB 3.6.3) Require a three machine cluster on which the replica-set is deployed. Uri1 and uri2 should be the host and port parameter of the primary and the secondary machines. No parameter required for the arbiter node machine.

2. Deployment

1). Pull the code from github address: 'https://github.com/ZJDong/Wayfindr-Py'

2). Run python file 'multithread_EventListener.py' using command: python multithread_EventListener.py