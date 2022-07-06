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
from typing import List, Optional, Tuple

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

        Summary._print_summary(lttng, summary_df)

    @staticmethod
    def _print_summary(
        lttng: Lttng,
        summary_df: pd.DataFrame
    ) -> None:
        print('\n')
        print('Trace creation datetime: '
              f'{lttng.get_trace_creation_datetime()}')
        st, ft = lttng.get_trace_range()
        print(f'Trace range [ns]: {st} ~ {ft}')
        if Lttng._last_filters:
            fi_st, fi_ft = Summary._get_filtered_duration(lttng)
            print(f'Filtered range [ns]: {fi_st} ~ {fi_ft}')
        print('\n')
        print(tabulate(summary_df,
                       summary_df.columns,
                       tablefmt='presto',
                       showindex=False))

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
    def _get_filters(
        d_filter_args: Optional[List[float]],
        s_filter_args: Optional[List[float]]
    ) -> Optional[List[LttngEventFilter]]:
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

        return filters or None
