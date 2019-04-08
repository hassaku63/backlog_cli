import os
import sys
import json
from backlog.util import load_conf
from backlog.base import BacklogAPI
from backlogcli.cli.parser import build_parser

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
stream_handler = logging.StreamHandler(sys.stderr)
stream_handler.setLevel(logging.ERROR)
logger.addHandler(stream_handler)


def main():
    cli_parser = build_parser()

    args = cli_parser.parse_args()

    if not os.path.exists(args.conf):
        if 'BACKLOG_SPACE' in os.environ.keys() and 'BACKLOG_API_KEY' in os.environ.keys():
            conf = dict(
                space=os.environ.get('BACKLOG_SPACE'),
                api_key=os.environ.get('BACKLOG_API_KEY')
            )
        else:
            logger.error('Env BACKLOG_SPACE and BACKLOG_API_KEY must be defined')
            return -1
    else:
        conf = load_conf(args.conf)['backlog']

    backlog_api = BacklogAPI(space=conf['space'], api_key=conf['api_key'])

    if 'action' in args:
        result = args.action(backlog_api, args)
        sys.stdout.write(json.dumps(result))
    else:
        raise KeyError('namespace has no attribute "action"')

    return 0
