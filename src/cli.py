""" punch command-line interface entry-point """

import time 
import argparse
import os
from db import Database


def execute(argv=None):
    
    parser = build_parser()

    args = parser.parse_args()

    db = Database()

    if args.task:
        db.log(args.task)

    if args.status:
        db.status(args.status)

    if args.end:
        db.end()

    if args.flush:
        db.clear()


def get_db_path(db_name):
    
    cwd = os.getcwd()
    parent_dir = os.path.dirname(cwd)
    
    return f'../databases/{db_name}.json'

def build_parser():

    parser = argparse.ArgumentParser(description='Log work activity')

    parser.add_argument(
            '-d', '--db_name',
            const='db',
            nargs='?',
            default='db',
            help="Select DB to work with"
    )

    parser.add_argument(
            '-t', '--task',
            action='store',
            help='add new start task'
    )

    parser.add_argument(
            '-s', '--status',
            const=1,
            nargs='?',
            action='store',
            default=False,
            help="Display today's tasks"
    )

    parser.add_argument(
            '-e', '--end',
            action='store_true',
            default=False,
            help="End all started task"
    )

    parser.add_argument(
            '-flush', '--flush',
            action='store_true',
            default=False,
            help="Clear existing history"
    )

    return parser
