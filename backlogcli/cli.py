# coding: utf-8

import os
import argparse

USAGE="""
mars_octopus [subcommand]
"""

CONFIG_SKELETON_YAML="""
backlog:
  default_project: default_project_key
  user: alice
  api_key: api_key
"""


def main():
    parser = argparse.ArgumentParser(usage=USAGE,
                                     description="Backlog CLI utility")

    parser.add_argument("-c", "--conf-file", type=str,
                        dest="conf", default=os.getcwd(),
                        help="Configuration yaml. defaults: current dir")
    parser.add_argument("--generate-config-skeleton", action="store_true",
                        dest="generate_config_skeleton",
                        help="Generate conf.default.yml skeleton in current directory."
                             "Rename 'conf.yml' and edit yourself environ to use.")

    args = parser.parse_args()

    if args.generate_config_skelton:
        conf_name = "conf.default.yml"
        if os.path.exists(conf_name):
            print("Abort. {} already exists.".format(conf_name))

        with open(conf_name, "w") as f:
            f.write(CONFIG_SKELETON_YAML)

    return args
