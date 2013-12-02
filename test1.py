#!/usr/local/bin/python

import sys
import subprocess

HOST="%s@%s" % ("kusyjan","fray1.fit.cvut.cz")
	# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="ls -la"
ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
   		           shell=False,
                   stdout=subprocess.PIPE,
                   stderr=subprocess.PIPE)
print ssh.stdout.readlines()
if result == []:
	error = 1
	error = ssh.stderr.readlines()
	print >>sys.stderr, "ERROR: %s" % error
else:
	print result