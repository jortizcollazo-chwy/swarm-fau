import os
import sys
import datetime
import logging
import argparse

import mongoengine
from mongoengine import connect
from bson import ObjectId
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

    # db connection
    connect(
        db=args.env.database.name,
        # username='user',
        # password='12345',
        host=args.env.database.hostname,
        port=args.env.database.port,
    )

    # https://stackoverflow.com/a/18266321
    data_to_delete = []
    for data in RawData.objects():
        try:
            data.device
        except mongoengine.errors.DoesNotExist:
            data_to_delete.append(data)


    print('removing {}'.format(len(data_to_delete)))

    if not args.yes:
        if sys.version_info[0] == 2:
            inp = raw_input('continue (y/n)? ')
        else:
            inp = input('continue (y/n)? ')
        if inp:
            args.yes = str(inp).lower()[0] == 'y'

    if args.yes:
        for d in data_to_delete:
            d.delete()
    else:
        print('aborting operation')
