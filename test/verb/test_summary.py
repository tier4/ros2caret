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

from caret_analyze import Lttng
from caret_analyze.infra.lttng.event_counter import EventCounter
from caret_analyze.infra.lttng.lttng_info import LttngInfo
from caret_analyze.infra.lttng.records_source import RecordsSource
from caret_analyze.infra.lttng.ros2_tracing.data_model import (DataModel,
                                                               Ros2DataModel)

import pandas as pd

from ros2caret.verb.summary import Summary


class TestSummary:

    def test_get_summary_df(self, mocker):
        data_mock = mocker.Mock(spec=DataModel)
        mocker.patch.object(Lttng, '_parse_lttng_data',
                            return_value=(data_mock, {}))

        lttng_info_mock = mocker.Mock(spec=LttngInfo)
        mocker.patch('caret_analyze.infra.lttng.lttng_info.LttngInfo',
                     return_value=lttng_info_mock)

        records_source_mock = mocker.Mock(spec=RecordsSource)
        mocker.patch('caret_analyze.infra.lttng.records_source.RecordsSource',
                     return_value=records_source_mock)

        data_dict = {
            'node_name': ['node_0', 'node_1', '-', 'node_0', 'node_2'],
            'topic_name': ['topic_0', 'topic_1', '-', 'topic_2', 'topic_3'],
            'size': [1, 2, 1, 3, 1],
            'trace_point': ['tp_0', 'tp_1', 'tp_1', 'tp_1', 'tp_2']
        }
        count_df = pd.DataFrame(data_dict)
        mocker.patch.object(EventCounter, '_build_count_df',
                            return_value=count_df)
        ros2_data_model_mock = mocker.Mock(spec=Ros2DataModel)
        event_counter = EventCounter(ros2_data_model_mock, validate=False)
        mocker.patch('caret_analyze.infra.lttng.event_counter.EventCounter',
                     return_value=event_counter)

        lttng_with_mock_counter = Lttng('trace_dir', force_conversion=False)

        # Test
        summary_df = Summary._get_summary_df(lttng_with_mock_counter,
                                             'node_name')
        assert 'node_name' in summary_df.columns
        assert 'size' not in summary_df.columns
        assert 'number_of_trace_points' in summary_df.columns
        assert len(summary_df) == 3
        assert any(summary_df['node_name'].str.contains('-')) is False

        summary_df = Summary._get_summary_df(lttng_with_mock_counter,
                                             'topic_name')
        assert 'topic_name' in summary_df.columns
        assert 'size' not in summary_df.columns
        assert 'number_of_trace_points' in summary_df.columns
        assert len(summary_df) == 4
        assert any(summary_df['topic_name'].str.contains('-')) is False

        summary_df = Summary._get_summary_df(lttng_with_mock_counter,
                                             'trace_point')
        assert 'trace_point' in summary_df.columns
        assert 'size' not in summary_df.columns
        assert 'number_of_trace_points' in summary_df.columns
        assert len(summary_df) == 3
        assert any(summary_df['trace_point'].str.contains('-')) is False
