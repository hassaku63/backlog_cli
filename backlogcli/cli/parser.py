import argparse
import logging

from backlogcli.actions.project import Project
from backlogcli.actions.user import User
from backlogcli.actions.issue import Issue
from backlogcli.actions.wiki import Wiki

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

__all__ = [
    'build_parser'
]

actions_mapping = {
    # Project
    "project.list": Project.list,
    "project.get": Project.get,
    "project.list_users": Project.list_users,
    "project.list_issue_types": Project.list_issue_types,
    "project.list_categories": Project.list_categories,
    # User
    "user.list": User.list,
    "user.get": User.get,
    # Issue
    "issue.list": Issue.list,
    "issue.get": Issue.get,
    # Wiki
    "wiki.list": Wiki.list,
    "wiki.get": Wiki.get
}


def build_parser():
    # Root parser
    root_parser = argparse.ArgumentParser(description='Backlog CLI (beta)')

    # Global args
    root_parser.add_argument('--conf', type=str, dest='conf', default='conf.yml')
    # root_parser.add_argument('--api-key', type=str, dest='api_key')
    # root_parser.add_argument('--space', type=argparse.FileType('r'))

    """
    level1 subparsers
    """
    subparsers = root_parser.add_subparsers()
    parser_project = subparsers.add_parser('project', description='Project operations')
    parser_user = subparsers.add_parser('user', description='User operations')
    parser_issue = subparsers.add_parser('issue', aliases=['iss'], description='Issue operations')
    parser_wiki = subparsers.add_parser('wiki', description='Wiki operations')

    """
    level2 subparsers
    """
    project_subparsers = parser_project.add_subparsers()
    user_subparsers = parser_user.add_subparsers()
    issue_subparsers = parser_issue.add_subparsers()
    wiki_subparsers = parser_wiki.add_subparsers()

    # Project subparser
    project_list_subparser = project_subparsers.add_parser('list', aliases=['ls'])
    project_get_subparser = project_subparsers.add_parser('get')
    project_list_users_subparser = project_subparsers.add_parser('list-users', aliases=['lu'])
    project_list_issue_types = project_subparsers.add_parser('list-issue-types', aliases=['li'])
    project_list_categories = project_subparsers.add_parser('list-categories', aliases=['lc'])

    # User
    user_list_subparser = user_subparsers.add_parser('list', aliases=['ls'])
    user_get_subparser = user_subparsers.add_parser('get')

    # Issue subparser
    issue_list_parser = issue_subparsers.add_parser('list', aliases=['ls'])
    issue_get_parser = issue_subparsers.add_parser('get')

    # Wiki subparser
    wiki_list_parser = wiki_subparsers.add_parser('list', aliases=['ls'])
    wiki_get_parser = wiki_subparsers.add_parser('get')

    """
    level3 subcommand's arguments
    """
    #
    # Project subcommands
    #
    project_list_subparser.add_argument('--action', dest='action', default=actions_mapping["project.list"], help='DO NOT SPECIFY')

    project_get_subparser.add_argument('--action', dest='action', default=actions_mapping["project.get"], help='DO NOT SPECIFY')
    project_get_subparser.add_argument('--project-id-or-key', dest='project_id_or_key', required=True)

    project_list_users_subparser.add_argument('--action', dest='action', default=actions_mapping["project.list_users"], help='DO NOT SPECIFY')
    project_list_users_subparser.add_argument('--project-id-or-key', dest='project_id_or_key', required=True)
    project_list_users_subparser.add_argument('--exclude-group-members', dest='exclude_group_members', type=bool, default=False)

    project_list_issue_types.add_argument('--action', dest='action', default=actions_mapping["project.list_issue_types"], help='DO NOT SPECIFY')
    project_list_issue_types.add_argument('--project-id-or-key', dest='project_id_or_key', required=True)

    project_list_categories.add_argument('--action', dest='action', default=actions_mapping["project.list_categories"], help='DO NOT SPECIFY')
    project_list_categories.add_argument('--project-id-or-key', dest='project_id_or_key', required=True)

    #
    # User subcommands
    #
    user_list_subparser.add_argument('--action', dest='action', default=actions_mapping["user.list"], help='DO NOT SPECIFY')

    user_get_subparser.add_argument('--action', dest='action', default=actions_mapping["user.list"], help='DO NOT SPECIFY')
    user_get_subparser.add_argument('--user-id', dest='user_id', required=True)

    #
    # Issue subcommands
    #
    issue_list_parser.add_argument('--action', dest='action', default=actions_mapping["issue.list"], help='DO NOT SPECIFY')
    issue_list_parser.add_argument('--query', type=str, default=None,
                                   help="Key1=Value1&Key2=Value2&... \
                                   https://developer.nulab.com/ja/docs/backlog/api/2/get-issue-list/")

    issue_get_parser.add_argument('--action', dest='action', default=actions_mapping["issue.get"], help='DO NOT SPECIFY')
    issue_get_parser.add_argument('--issue-id-or-key', dest='issue_id_or_key', required=True)

    #
    # Wiki subcommands
    #
    wiki_list_parser.add_argument('--action', dest='action', default=actions_mapping["wiki.list"], help='DO NOT SPECIFY')
    wiki_list_parser.add_argument('--project-id-or-key', dest='project_id_or_key', required=True)

    wiki_get_parser.add_argument('--action', dest='action', default=actions_mapping["wiki.get"], help='DO NOT SPECIFY')
    wiki_get_parser.add_argument('--wiki-id', dest='wiki_id', required=True)

    return root_parser

