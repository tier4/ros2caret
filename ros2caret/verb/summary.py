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

from datetime import datetime
from logging import ERROR, getLogger
from typing import List, Optional, Tuple

from caret_analyze import Lttng, LttngEventFilter

import pandas as pd

from tabulate import tabulate


logger = getLogger(__name__)


class Summary:

    def __init__(
        self,
        args,
        groupby: str
    ) -> None:
        if not args.display_check:
            root_logger = getLogger()
            root_logger.setLevel(ERROR)

        # NOTE: what happen if len(args.d_filter_args) > 2?
        # It look good to remove filter arguments,
        # if there are no use-cases to use them.

        filters = self._get_filters(args.d_filter_args,
                                    args.s_filter_args)
        self._lttng = Lttng(args.trace_dir, event_filters=filters)
        self._summary_df = self._get_summary_df(self._lttng, groupby)
        self._filtered = len(filters) > 0

    def print_summary(
        self
    ) -> None:
        msg = '=============================================\n'

        try:
            # FIXME: Index is difficult to understand what is being done.
            msg += ('Trace creation datetime | '
                    f'{str(self._lttng.get_trace_creation_datetime())[:-7]}\n')
            bt, et = self._lttng.get_trace_range()
            msg += ('Trace range             | '
                    f'{bt.strftime("%H:%M:%S")} ~ '
                    f'{et.strftime("%H:%M:%S")}\n'
                    f'Trace duration          | {str(et - bt)[:-7]}\n')
        except AttributeError as e:
            logger.error(f'{e}. Please update caret_analyze.')

        if self._filtered:
            fi_bt, fi_et = Summary._get_filtered_range(self._lttng)
            msg += (
                'Filtered trace range    | '
                f'{fi_bt.strftime("%H:%M:%S")} ~ '
                f'{fi_et.strftime("%H:%M:%S")}\n'
                f'Filtered trace duration | {str(fi_et - fi_bt)[:-7]}\n'
            )
        msg += '=============================================\n'
        print(msg)

        print(tabulate(self._summary_df,
                       self._summary_df.columns,
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
    def _get_filtered_range(
        lttng: Lttng
    ) -> Tuple[datetime, datetime]:
        cb_records = lttng.compose_callback_records()
        cb_df = cb_records.to_dataframe()

        return (datetime.fromtimestamp(
                    cb_df['callback_start_timestamp'].min() * 1.0e-9),
                datetime.fromtimestamp(
                    cb_df['callback_end_timestamp'].max() * 1.0e-9))

    @staticmethod
    def _get_filters(
        d_filter_args: Optional[List[float]],
        s_filter_args: Optional[List[float]]
    ) -> List[LttngEventFilter]:
        filters: List[LttngEventFilter] = []
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
