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

from logging import ERROR, getLogger

from caret_analyze import Lttng
from ros2caret.verb import VerbExtension
from tabulate import tabulate


class TopicSummaryVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            '-d', '--trace_dir', dest='trace_dir', type=str,
            help='the path to the trace directory', required=True)
        parser.add_argument(
            '-c', '--display_check', dest='display_check', action='store_true',
            help='display the error checks to the trace results.',
            required=False
        )

    def main(self, *, args):
        if(not args.display_check):
            logger = getLogger()
            logger.setLevel(ERROR)

        lttng = Lttng(args.trace_dir)
        topic_count_df = lttng.get_count(groupby=['topic_name']).reset_index()
        topic_count_df.rename(columns={'size': 'number_of_trace_points'},
                              inplace=True)
        topic_count_df = topic_count_df[topic_count_df['topic_name'] != '-']

        print('\n')
        print(tabulate(topic_count_df,
                       topic_count_df.columns,
                       tablefmt='presto',
                       showindex=False))
