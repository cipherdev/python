#!/usr/bin/python
"""
# *****************************************
# Copyright  2016
# AMCC, Inc. All Rights Reserved
# Proprietary and Confidential
# *****************************************
# Author: HuyLe,email: hule@apm.com
###########################################
The script testing performance ethernet
"""

import sys, getopt, os, errno
import time, py_compile

if len(sys.argv) != 3:
    print """\
    ------------------------------------------------------------
    Usage: ./iperf.py <iperf|iperf3> <serverip>
    iperf or iperf3        The tools the testing performance networking
    serverip               Server IP-Address
    Notes: No.times running: [t=30]
    ------------------------------------------------------------
    """
    sys.exit(1)
#Define time running iperf
time_t=30;
command=sys.argv[1];
server=sys.argv[2];
#print ('CMD ' + str(command) + ' -c' + float(server) + '-t ' + (time_t));
#print ('CMD: %s -c %s -t %d -P ' % (command, server, time_t));
#os.system('%s -c %s -t %d' % (command, server, time));
threads=['1', '4', '8'];
try:
    for i in range(len(threads)):
        print ('------------------------------------------------------------');
        print ('No.threads: %s' %threads[i]);
        print ('CMD: %s -c %s -t %d -P %s' % (command, server, time_t, threads[i]));
        os.system('%s -c %s -t %d -P %s' % (command, server, time_t, threads[i]));
        time.sleep(1);
except IOError as err:
    print err.errno 
    print err.strerror
    print 'Does not see the server run %s -s' %command
else:
    print 'Run perfect!'
finally:
    print 'DONE.'
