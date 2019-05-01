#!/usr/bin/env python

import os
from os import path
from subprocess import check_call

import arg_parser
import context


def main():
    args = arg_parser.receiver_first()

    cc_repo = path.join(context.third_party_dir, 'copt')
    recv_src = path.join(cc_repo, 'server.py')
    send_src = path.join(cc_repo, 'client.py')

    if args.option == 'deps':
        print ('deps for copt')
        return

    if args.option == 'setup':
        check_call(['make'])
        check_call(['sudo','insmod','tcp_pcc.ko'])
        return

    if args.option == 'receiver':
        cmd = [recv_src, args.port]
        check_call(cmd)
        return

    if args.option == 'sender':
        cmd = [send_src, args.port]
        check_call(cmd)
        return


if __name__ == '__main__':
    main()
