# Copyright 2021 Research Institute of Systems Planning, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from logging import Formatter, getLogger, INFO, StreamHandler

import os

import subprocess
from typing import Callable, List, Set

from ros2caret.verb import VerbExtension

handler = StreamHandler()
handler.setLevel(INFO)

fmt = '%(levelname)-8s: %(asctime)s | %(message)s'
formatter = Formatter(
    fmt,
    datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)

logger = getLogger(__name__)
logger.setLevel(INFO)
logger.addHandler(handler)


class CheckCaretRclcppVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            'workspace', type=str,
            help='the path to the workspace to be checked'
        )

    def main(self, *, args):
        root_dir_path = args.workspace + '/build/'
        RclcppCheck(root_dir_path)

# NOTE: It looks good to move symbol check to caret_analyze.
# Just call caret_analyze's API in ros2caret.


ros_builtin_tp_symbol_names = [
    'ros_trace_rclcpp_publish'
    'ros_trace_rclcpp_subscription_init',
    'ros_trace_rclcpp_subscription_callback_added',
]

caret_fork_tp_symbol_names = [
    'ros_trace_dispatch_intra_process_subscription_callback',
    'ros_trace_dispatch_subscription_callback',
    'ros_trace_message_construct',
    'ros_trace_rclcpp_intra_publish'
]


class RclcppCheck():

    def __init__(self, root_dir_path: str) -> None:
        RclcppCheck._ensure_dir_exist(root_dir_path)

        get_package_name = RclcppCheck._create_get_package_name(root_dir_path)
        ros_obj_paths = RclcppCheck._get_obj_paths(root_dir_path)

        """
        TODO: Need to speed up.
            When this command is run against Autoware,
            it takes approximately one minute to complete.
        """

        # Check whether at least one CARET fork implemented trace point exists
        all_packages = {get_package_name(obj_path)
                        for obj_path
                        in ros_obj_paths}

        ok_packages = {get_package_name(obj_path)
                       for obj_path
                       in ros_obj_paths
                       if RclcppCheck._has_caret_rclcpp_tp(obj_path)}

        # Logging
        ng_packages = all_packages - ok_packages
        if ng_packages:
            msg = ('The following packages have not been built '
                   'using caret-rclcpp:\n')
            for ng_package in ng_packages:
                msg += f'\t{ng_package}\n'
            logger.warning(msg)
        else:
            logger.info('All packages are built using caret-rclcpp.')

    @staticmethod
    def _get_obj_paths(root_dir_path: str) -> Set[str]:
        filtered_file_paths = RclcppCheck._get_file_paths(root_dir_path)

        # Check whether at least one ros implemented trace point exists
        return {path
                for path
                in filtered_file_paths
                if RclcppCheck._has_ros_builtin_tp(path)}

    @staticmethod
    def _get_file_paths(dir_path: str) -> List[str]:
        cmd = f'find {dir_path} -type f ! -size 0 -executable \
                ! -name "*.o"            ! -name "*.cpp" \
                ! -name "*.make"         ! -name "*.cmake" \
                ! -name "Makefile"       ! -name "*.internal" \
                ! -name "*.includecache" ! -name "*.in" \
                ! -name "*.txt"          ! -name "*.a" \
                ! -name "*.stamp"        ! -name "*.genexp" \
                ! -name "*.sample"       ! -name "*.py" \
                ! -name "*.cu"           ! -name "*.sh" \
                ! -name "*.md"           ! -name "polygraphy" \
                ! -name "gen-data"       ! -name "*.ipynb" \
                ! -name "*.png"          ! -name "*.jpg" \
                ! -name "*.json"         ! -name "*.toml"'
        return (subprocess.Popen(cmd,
                                 stdout=subprocess.PIPE,
                                 shell=True).communicate()[0]
                ).decode('utf-8').split('\n')[:-1]

    @staticmethod
    def _has_ros_builtin_tp(obj_path: str) -> bool:
        cmd = (f'nm -D {obj_path} 2> /dev/null | '
               f'grep -e {" -e ".join(ros_builtin_tp_symbol_names)}')
        stdout = (subprocess.Popen(cmd,
                                   stdout=subprocess.PIPE,
                                   shell=True).communicate()[0]
                  )

        return bool(stdout)

    @staticmethod
    def _has_caret_rclcpp_tp(obj_path: str) -> bool:
        cmd = (f'nm -D {obj_path} 2> /dev/null | '
               f'grep -e {" -e ".join(caret_fork_tp_symbol_names)}')
        stdout = (subprocess.Popen(cmd,
                                   stdout=subprocess.PIPE,
                                   shell=True
                                   ).communicate()[0]
                  ).decode('utf-8')

        return bool(stdout)

    @staticmethod
    def _create_get_package_name(root_dir_path: str) -> Callable[[str], bool]:
        def get_package_name(file_path: str):
            return file_path.replace(root_dir_path, '').split('/')[0]
        return get_package_name

    @staticmethod
    def _ensure_dir_exist(path: str):
        if(os.path.exists(path)):
            return

        logger.error('"build" directory not found. '
                     'Specify the path to the workspace '
                     'where the build command completed.')
        exit(1)

    @staticmethod
    def get_package_name_from_path(root_dir_path: str, path: str) -> str:
        package_name = path.replace(root_dir_path, '').split('/')[0]

        return package_name
