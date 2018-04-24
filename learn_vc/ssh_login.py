#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pexpect
import os
import sys


def ssh(user, server, mypassword=''):
    rows, columns = os.popen('stty size', 'r').read().split()
    child = pexpect.spawn('ssh %s@%s' % (user, server))
    child.setwinsize(int(rows), int(columns))
    child.expect('password:')
    child.sendline(mypassword)
    child.interact(escape_character=None)

if __name__ == '__main__':
    captcha = sys.argv[1]
    ssh("XXX", "XXX", mypassword="XXXX{}".format(captcha))
