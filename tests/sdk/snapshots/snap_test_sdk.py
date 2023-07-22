# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot
from snapshottest.file import FileSnapshot


snapshots = Snapshot()

snapshots['test_streaming_sdk __init__'] = FileSnapshot('snap_test_sdk/test_streaming_sdk __init__.py')

snapshots['test_streaming_sdk client'] = FileSnapshot('snap_test_sdk/test_streaming_sdk client.py')

snapshots['test_streaming_sdk core___init__'] = FileSnapshot('snap_test_sdk/test_streaming_sdk core___init__.py')

snapshots['test_streaming_sdk core_api_error'] = FileSnapshot('snap_test_sdk/test_streaming_sdk core_api_error.py')

snapshots['test_streaming_sdk core_client_wrapper'] = FileSnapshot('snap_test_sdk/test_streaming_sdk core_client_wrapper.py')

snapshots['test_streaming_sdk core_datetime_utils'] = FileSnapshot('snap_test_sdk/test_streaming_sdk core_datetime_utils.py')

snapshots['test_streaming_sdk core_jsonable_encoder'] = FileSnapshot('snap_test_sdk/test_streaming_sdk core_jsonable_encoder.py')

snapshots['test_streaming_sdk core_remove_none_from_dict'] = FileSnapshot('snap_test_sdk/test_streaming_sdk core_remove_none_from_dict.py')

snapshots['test_streaming_sdk filepaths'] = [
    '__init__.py',
    'client.py',
    'core/__init__.py',
    'core/api_error.py',
    'core/client_wrapper.py',
    'core/datetime_utils.py',
    'core/jsonable_encoder.py',
    'core/remove_none_from_dict.py',
    'resources/__init__.py',
    'resources/ai/__init__.py',
    'resources/ai/client.py',
    'resources/ai/types/__init__.py',
    'resources/ai/types/stream_response.py'
]

snapshots['test_streaming_sdk resources___init__'] = FileSnapshot('snap_test_sdk/test_streaming_sdk resources___init__.py')

snapshots['test_streaming_sdk resources_ai___init__'] = FileSnapshot('snap_test_sdk/test_streaming_sdk resources_ai___init__.py')

snapshots['test_streaming_sdk resources_ai_client'] = FileSnapshot('snap_test_sdk/test_streaming_sdk resources_ai_client.py')

snapshots['test_streaming_sdk resources_ai_types___init__'] = FileSnapshot('snap_test_sdk/test_streaming_sdk resources_ai_types___init__.py')

snapshots['test_streaming_sdk resources_ai_types_stream_response'] = FileSnapshot('snap_test_sdk/test_streaming_sdk resources_ai_types_stream_response.py')
