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

import glob
from logging import ERROR, getLogger
import os
import re
import sys
from typing import List, Optional, Tuple

import bt2

from caret_analyze import Lttng, LttngEventFilter

import pandas as pd

from tabulate import tabulate


class Summary:

    def __init__(self, args, groupby: str) -> None:
        if not args.display_check:
            root_logger = getLogger()
            root_logger.setLevel(ERROR)

        filters = Summary._get_filters(args.d_filter_args,
                                       args.s_filter_args)
        lttng = Lttng(args.trace_dir, event_filters=filters)
        summary_df = Summary._get_summary_df(lttng, groupby)

        # Logging
        print('\n')
        print(Summary._get_trace_creation_datetime(args.trace_dir))
        st, ft = Summary._get_measure_duration(args.trace_dir)
        print(f'measurement_duration [ns]: {st} ~ {ft}')
        if filters:
            fi_st, fi_ft = Summary._get_filtered_duration(lttng)
            print(f'filtered_duration [ns]: {fi_st} ~ {fi_ft}')
        print('\n')
        print(tabulate(summary_df,
                       summary_df.columns,
                       tablefmt='presto',
                       showindex=False))

    @staticmethod
    def _get_trace_creation_datetime(
        trace_dir: str
    ) -> str:
        metadata_path = os.path.dirname(glob.glob(f'{trace_dir}/**/metadata',
                                                  recursive=True)[0])
        result = bt2.QueryExecutor(
            bt2.find_plugin('ctf').source_component_classes['fs'],
            'metadata-info',
            {'path': metadata_path}
        ).query()
        datetime = re.search(r'trace_creation_datetime = "\S+"',
                             str(result['text'])).group().replace(' =', ':')

        return datetime

    @staticmethod
    def _get_summary_df(
        lttng: Lttng,
        groupby: str
    ) -> pd.DataFrame:
        count_df = lttng.get_count(groupby=[groupby]).reset_index()
        count_df.rename(columns={'size': 'number_of_trace_points'},
                        inplace=True)
        count_df = count_df[count_df[groupby] != '-']

        return count_df

    @staticmethod
    def _get_filtered_duration(
        lttng: Lttng
    ) -> Tuple[int, int]:
        cb_records = lttng.compose_callback_records()
        cb_df = cb_records.to_dataframe()

        return (cb_df['callback_start_timestamp'].min(),
                cb_df['callback_end_timestamp'].max())

    @staticmethod
    def _get_measure_duration(
        trace_dir: str
    ) -> Tuple[int, int]:
        msgs = bt2.TraceCollectionMessageIterator(
            trace_dir,
            stream_intersection_mode=True
        )

        earliest_stream_st = sys.maxsize
        latest_stream_ft = 0
        for stream_st, stream_ft in msgs._stream_inter_port_to_range.values():
            if earliest_stream_st > stream_st:
                earliest_stream_st = stream_st
            if latest_stream_ft < stream_ft:
                latest_stream_ft = stream_ft

        return earliest_stream_st, latest_stream_ft

    @staticmethod
    def _get_filters(
        d_filter_args: Optional[List[float]],
        s_filter_args: Optional[List[float]]
    ) -> List[Optional[LttngEventFilter]]:
        filters = []
        if d_filter_args:
            filters.append(
                LttngEventFilter.duration_filter(
                    d_filter_args[0],
                    d_filter_args[1]
                ))
        if s_filter_args:
            filters.append(
                LttngEventFilter.strip_filter(
                    s_filter_args[0],
                    s_filter_args[1]
                ))

        return filters
