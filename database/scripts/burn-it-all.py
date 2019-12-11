import os
import sys
import datetime
import logging
import argparse

from mongoengine import connect
from mongoengine.connection import _get_db
from apilib.lib import augment_args
from database.models.project import Project
from database.models.device import Device
from database.models.raw_data import RawData

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    execution = parser.add_argument_group()
    execution.add_argument(
        '-e', '--env', action='store_true', default=os.path.abspath('env.xml'), help='Env XML File'
    )
    execution.add_argument(
        '-y', '--yes', action='store_true', help='Whether or not you want to go through with this.'
    )
    logstuff = parser.add_argument_group()
    logstuff.add_argument('--loglevel', type=str, default='DEBUG', help='python logging level')
    logstuff.add_argument(
        '--logdir', type=str, default='/var/log/swarm', help='python logging path'
    )

    args = augment_args(parser.parse_args())

    print(
        '''WARNING! YOU ARE ATTEMPTING TO PERMANENTLY RAZE DB "{}". THIS DOES NOT INCLUDE A BACKUP STEP!'''
        .format(args.env.database.name)
    )

    if not args.yes:
        if sys.version_info[0] == 2:
            inp = raw_input('continue (y/n)? ')
        else:
            inp = input('continue (y/n)? ')
        if inp:
            args.yes = str(inp).lower()[0] == 'y'

    if args.yes:
        conn = connect(
            db=args.env.database.name,
            # username='user',
            # password='12345',
            host=args.env.database.hostname,
            port=args.env.database.port,
        )
        conn.drop_database(args.env.database.name)
    else:
        print('aborting operation')
