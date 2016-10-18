#!/usr/bin/python
'''
# *****************************************
# Copyright  2016
# AMCC, Inc. All Rights Reserved
# Proprietary and Confidential
# *****************************************
# Author: HuyLe,email: hule@apm.com
###########################################
The script testing performance ethernet
'''
import sys, getopt, os
import time
#define time running iperf
time_t=30;
command=sys.argv[1];
server=sys.argv[2];

#print ('CMD ' + str(command) + ' -c' + float(server) + '-t ' + (time_t));
print ('CMD: %s -c %s -t %d -P ' % (command, server, time_t));
#os.system('%s -c %s -t %d' % (command, server, time));
threads=['1', '4', '8'];
for i in range(len(threads)):
    print ('No.threads: %s' %threads[i]);
    os.system('%s -c %s -t %d -P %s' % (command, server, time_t, threads[i]));
    time.sleep(10);
