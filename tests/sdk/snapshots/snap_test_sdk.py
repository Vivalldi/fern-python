# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot
from snapshottest.file import FileSnapshot


snapshots = Snapshot()

snapshots['test_circular_imports filepaths'] = [
    'src/my_org/__init__.py',
    'src/my_org/client.py',
    'src/my_org/core/__init__.py',
    'src/my_org/core/api_error.py',
    'src/my_org/core/client_wrapper.py',
    'src/my_org/core/datetime_utils.py',
    'src/my_org/core/jsonable_encoder.py',
    'src/my_org/core/remove_none_from_headers.py',
    'src/my_org/resources/__init__.py',
    'src/my_org/resources/a/__init__.py',
    'src/my_org/resources/a/types/__init__.py',
    'src/my_org/resources/a/types/a.py',
    'src/my_org/types/__init__.py',
    'src/my_org/types/importing_a.py',
    'src/my_org/types/root_type.py'
]

snapshots['test_circular_imports src_my_org___init__'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org___init__.py')

snapshots['test_circular_imports src_my_org_client'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_client.py')

snapshots['test_circular_imports src_my_org_core___init__'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_core___init__.py')

snapshots['test_circular_imports src_my_org_core_api_error'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_core_api_error.py')

snapshots['test_circular_imports src_my_org_core_client_wrapper'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_core_client_wrapper.py')

snapshots['test_circular_imports src_my_org_core_datetime_utils'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_core_datetime_utils.py')

snapshots['test_circular_imports src_my_org_core_jsonable_encoder'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_core_jsonable_encoder.py')

snapshots['test_circular_imports src_my_org_core_remove_none_from_headers'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_core_remove_none_from_headers.py')

snapshots['test_circular_imports src_my_org_resources___init__'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_resources___init__.py')

snapshots['test_circular_imports src_my_org_resources_a___init__'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_resources_a___init__.py')

snapshots['test_circular_imports src_my_org_resources_a_types___init__'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_resources_a_types___init__.py')

snapshots['test_circular_imports src_my_org_resources_a_types_a'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_resources_a_types_a.py')

snapshots['test_circular_imports src_my_org_types___init__'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_types___init__.py')

snapshots['test_circular_imports src_my_org_types_importing_a'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_types_importing_a.py')

snapshots['test_circular_imports src_my_org_types_root_type'] = FileSnapshot('snap_test_sdk/test_circular_imports src_my_org_types_root_type.py')
