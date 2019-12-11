import os
import sys
import datetime
import logging
import argparse

from mongoengine import connect
from apilib.lib import augment_args
from database.models.project import Project
from database.models.device import Device
from database.models.raw_data import RawData

LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(logging.NullHandler())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    execution = parser.add_argument_group()
    execution.add_argument('-p', '--project', type=str, help='Project name as a string.')
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
    projects_to_delete = [proj for proj in Project.objects(name=args.project)]
    devices_to_delete = [dev for dev in Device.objects(meta_data__project=args.project)]
    data_to_delete = [data for dev in devices_to_delete for data in RawData.objects(device=dev.id)]

    damned_projects = [p.id for p in projects_to_delete]
    damned_devices = [d.id for d in devices_to_delete]
    damned_data = [d.id for d in data_to_delete]

    print(
        'removing {} project: \n{}'.format(len(damned_projects), [str(e) for e in damned_projects])
    )
    print('removing {} devices: \n{}'.format(len(damned_devices), [str(e) for e in damned_devices]))
    print('removing {} data: \n{}'.format(len(damned_data), [str(e) for e in damned_data]))

    if not args.yes:
        if sys.version_info[0] == 2:
            inp = raw_input('continue (y/n)? ')
        else:
            inp = input('continue (y/n)? ')
        if inp:
            args.yes = str(inp).lower()[0] == 'y'

    if args.yes:
        for p in projects_to_delete:
            p.delete()
        for d in devices_to_delete:
            d.delete()
        for d in data_to_delete:
            d.delete()
    else:
        print('aborting operation')
