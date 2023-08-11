# parlab.py
#   library to ease multiple process launch across lab
# by: John Zelle

import os
import socket
import time
import glob


IP_FILES = "/labhome/PUBLIC/labhosts/*"


def runlocal(command, wait=False):
    os.system(command + (" " if wait else " &"))


def runhost(host, command, wait=False):
    template = "ssh -q {host:} 'cd {dir:} ; {command:}' " + \
        ("" if wait else "&")
    cstr = template.format(host=host, dir=os.getcwd(), command=command)
    os.system(cstr)


def get_hostmap():
    hosts = {}
    for fname in glob.glob(IP_FILES):
        with open(fname) as infile:
            host = fname.split("/")[-1]
            ip = infile.read().strip()
            hosts[host] = ip
    return hosts


def is_alive(ip):
    s = socket.socket()
    try:
        s.connect((ip, 22))
    except:
        return False
    s.close()
    return True


class Runner:
    """Class for running local or remote commands

    >>> r = Runner()
    >>> r.local("hostname", True)
    gourami
    >>> r.remote("hostname", True)
    guppy
    """

    def __init__(self):
        self.hostname = socket.gethostname()
        self.addresses = get_hostmap()
        hosts = [host for host, addr in self.addresses.items()
                 if is_alive(addr)]
        self.deadhosts = list(set(self.addresses) - set(hosts)) 
        hosts.remove(self.hostname)
        self.remotehosts = hosts
        self.nhosts = len(self.remotehosts)
        self.nexthost = 0

    def remote(self, command, wait=False):
        host = self.remotehosts[self.nexthost]
        runhost(self.addresses[host], command, wait)
        self.nexthost = (self.nexthost+1) % self.nhosts
        return host

    def local(self, command, wait=False):
        runlocal(command, wait)
