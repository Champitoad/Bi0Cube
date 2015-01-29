#!/usr/bin/bash

ip=$1

scp libs/* root@$ip:/usr/lib/python2.7
scp -r modules/* root@$ip:~
scp -r website/* root@$ip:/www/biocube
