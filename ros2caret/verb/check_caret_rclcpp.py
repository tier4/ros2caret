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
# limitations under the License.from caret_analyze import Application, Lttng

from logging import getLogger
import os
import subprocess

from ros2caret.verb import VerbExtension

logger = getLogger(__name__)


galactic_tp_symbol_names = [
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


class CheckCaretRclcppVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            '-d', '--check_directory', dest='check_directory', type=str,
            help='the path to the directory to be checked', required=True)

    def get_package_name_from_path(self, path: str) -> str:
        package_name = path.replace(self.root_dir_path, '').split('/')[0]

        return package_name

    def main(self, *, args):
        root_dir_path = args.check_directory + '/build/'
        if(os.path.exists(root_dir_path)):
            self.root_dir_path = root_dir_path
        else:
            logger.error('Specify the path to the directory where the build command completed.')
            exit(1)

        cmd = f'find {self.root_dir_path} -type f ! -size 0 -executable \
                ! -name "*.o"            ! -name "*.cpp"    ! -name "*.make" \
                ! -name "*.cmake"        ! -name "Makefile" ! -name "*.internal" \
                ! -name "*.includecache" ! -name "*.in"     ! -name "*.txt" \
                ! -name "*.a"            ! -name "*.stamp"  ! -name "*.genexp" \
                ! -name "*.sample"       ! -name "*.py"'
        filtered_file_paths = (subprocess.Popen(cmd,
                                                stdout=subprocess.PIPE,
                                                shell=True).communicate()[0]
                               ).decode('utf-8').split('\n')

        # Check whether at least one galactic implementation trace point exists
        exists_galactic_tp_file_paths = []
        for file_path in filtered_file_paths[:-1]:
            cmd = f'nm -D {file_path} | grep -e {" -e ".join(galactic_tp_symbol_names)}'
            out_str = (subprocess.Popen(cmd,
                                        stdout=subprocess.PIPE,
                                        shell=True).communicate()[0]
                       ).decode('utf-8')
            if(out_str):
                exists_galactic_tp_file_paths.append(file_path)

        # Check whether at least one CARET fork implementation trace point exists
        all_packages = set()
        ok_packages = set()
        for file_path in exists_galactic_tp_file_paths:
            all_packages.add(self.get_package_name_from_path(file_path))
            cmd = f'nm -D {file_path} | grep -e {" -e ".join(caret_fork_tp_symbol_names)}'
            out_str = (subprocess.Popen(cmd,
                                        stdout=subprocess.PIPE,
                                        shell=True
                                        ).communicate()[0]
                       ).decode('utf-8')
            if(out_str):
                ok_packages.add(self.get_package_name_from_path(file_path))

        # Logging
        ng_packages = all_packages - ok_packages
        if(ng_packages):
            msg = 'The following packages have not been built using caret-rclcpp:\n'
            for ng_package in ng_packages:
                msg += f'\t{ng_package}\n'
            logger.warning(msg)
        else:
            logger.info('All packages are built using caret-rclcpp.')
