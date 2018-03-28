# Wayfindr-Py

ZJDong

0. Introduction

This is the python code for group 15's WAYFINDR project in module ASE. It's mainly used to regularly request the noise data from internet APIs and save the data to mongoDB. Meanwhile, it monitor the changes in mongoDB. Once it gets the changes, it will unset the changing flag for GO APP of the project.

1. Development Environment

(python 3.6.4) Required packages: threading, requests, pymongo, time.

(MongoDB 3.6.3) Require a three machine cluster on which the replica-set is deployed. Uri1 and uri2 should be the host and port parameter of the primary and the secondary machines. No parameter required for the arbiter node machine.
