# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot
from snapshottest.file import FileSnapshot


snapshots = Snapshot()

snapshots['test_fastapi __init__'] = FileSnapshot('snap_test_fastapi/test_fastapi __init__.py')

snapshots['test_fastapi core___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi core___init__.py')

snapshots['test_fastapi core_abstract_fern_service'] = FileSnapshot('snap_test_fastapi/test_fastapi core_abstract_fern_service.py')

snapshots['test_fastapi core_datetime_utils'] = FileSnapshot('snap_test_fastapi/test_fastapi core_datetime_utils.py')

snapshots['test_fastapi core_exceptions___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi core_exceptions___init__.py')

snapshots['test_fastapi core_exceptions_fern_http_exception'] = FileSnapshot('snap_test_fastapi/test_fastapi core_exceptions_fern_http_exception.py')

snapshots['test_fastapi core_exceptions_handlers'] = FileSnapshot('snap_test_fastapi/test_fastapi core_exceptions_handlers.py')

snapshots['test_fastapi core_exceptions_unauthorized'] = FileSnapshot('snap_test_fastapi/test_fastapi core_exceptions_unauthorized.py')

snapshots['test_fastapi core_route_args'] = FileSnapshot('snap_test_fastapi/test_fastapi core_route_args.py')

snapshots['test_fastapi core_security___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi core_security___init__.py')

snapshots['test_fastapi core_security_bearer'] = FileSnapshot('snap_test_fastapi/test_fastapi core_security_bearer.py')

snapshots['test_fastapi filepaths'] = [
    '__init__.py',
    'core/__init__.py',
    'core/abstract_fern_service.py',
    'core/datetime_utils.py',
    'core/exceptions/__init__.py',
    'core/exceptions/fern_http_exception.py',
    'core/exceptions/handlers.py',
    'core/exceptions/unauthorized.py',
    'core/route_args.py',
    'core/security/__init__.py',
    'core/security/bearer.py',
    'register.py',
    'resources/__init__.py',
    'resources/admin/__init__.py',
    'resources/admin/service/__init__.py',
    'resources/admin/service/service.py',
    'resources/admin/service/store_traced_test_case_request.py',
    'resources/admin/service/store_traced_workspace_request.py',
    'resources/admin/types/__init__.py',
    'resources/admin/types/test.py',
    'resources/commons/__init__.py',
    'resources/commons/types/__init__.py',
    'resources/commons/types/binary_tree_node_and_tree_value.py',
    'resources/commons/types/binary_tree_node_value.py',
    'resources/commons/types/binary_tree_value.py',
    'resources/commons/types/debug_key_value_pairs.py',
    'resources/commons/types/debug_map_value.py',
    'resources/commons/types/debug_variable_value.py',
    'resources/commons/types/doubly_linked_list_node_and_list_value.py',
    'resources/commons/types/doubly_linked_list_node_value.py',
    'resources/commons/types/doubly_linked_list_value.py',
    'resources/commons/types/file_info.py',
    'resources/commons/types/generic_value.py',
    'resources/commons/types/key_value_pair.py',
    'resources/commons/types/language.py',
    'resources/commons/types/list_type.py',
    'resources/commons/types/map_type.py',
    'resources/commons/types/map_value.py',
    'resources/commons/types/node_id.py',
    'resources/commons/types/problem_id.py',
    'resources/commons/types/singly_linked_list_node_and_list_value.py',
    'resources/commons/types/singly_linked_list_node_value.py',
    'resources/commons/types/singly_linked_list_value.py',
    'resources/commons/types/test_case.py',
    'resources/commons/types/test_case_with_expected_result.py',
    'resources/commons/types/user_id.py',
    'resources/commons/types/variable_type.py',
    'resources/commons/types/variable_value.py',
    'resources/homepage/__init__.py',
    'resources/homepage/service/__init__.py',
    'resources/homepage/service/service.py',
    'resources/lang_server/__init__.py',
    'resources/lang_server/types/__init__.py',
    'resources/lang_server/types/lang_server_request.py',
    'resources/lang_server/types/lang_server_response.py',
    'resources/migration/__init__.py',
    'resources/migration/service/__init__.py',
    'resources/migration/service/service.py',
    'resources/migration/types/__init__.py',
    'resources/migration/types/migration.py',
    'resources/migration/types/migration_status.py',
    'resources/playlist/__init__.py',
    'resources/playlist/errors/__init__.py',
    'resources/playlist/errors/playlist_id_not_found_error.py',
    'resources/playlist/errors/unauthorized_error.py',
    'resources/playlist/service/__init__.py',
    'resources/playlist/service/service.py',
    'resources/playlist/types/__init__.py',
    'resources/playlist/types/playlist.py',
    'resources/playlist/types/playlist_create_request.py',
    'resources/playlist/types/playlist_id.py',
    'resources/playlist/types/playlist_id_not_found_error_body.py',
    'resources/playlist/types/reserved_keyword_enum.py',
    'resources/playlist/types/update_playlist_request.py',
    'resources/problem/__init__.py',
    'resources/problem/service/__init__.py',
    'resources/problem/service/get_default_starter_files_request.py',
    'resources/problem/service/service.py',
    'resources/problem/types/__init__.py',
    'resources/problem/types/create_problem_error.py',
    'resources/problem/types/create_problem_request.py',
    'resources/problem/types/create_problem_response.py',
    'resources/problem/types/generic_create_problem_error.py',
    'resources/problem/types/get_default_starter_files_response.py',
    'resources/problem/types/problem_description.py',
    'resources/problem/types/problem_description_board.py',
    'resources/problem/types/problem_files.py',
    'resources/problem/types/problem_info.py',
    'resources/problem/types/update_problem_response.py',
    'resources/problem/types/variable_type_and_name.py',
    'resources/submission/__init__.py',
    'resources/submission/service/__init__.py',
    'resources/submission/service/service.py',
    'resources/submission/types/__init__.py',
    'resources/submission/types/actual_result.py',
    'resources/submission/types/building_executor_response.py',
    'resources/submission/types/code_execution_update.py',
    'resources/submission/types/compile_error.py',
    'resources/submission/types/custom_test_cases_unsupported.py',
    'resources/submission/types/error_info.py',
    'resources/submission/types/errored_response.py',
    'resources/submission/types/exception_info.py',
    'resources/submission/types/exception_v_2.py',
    'resources/submission/types/execution_session_response.py',
    'resources/submission/types/execution_session_state.py',
    'resources/submission/types/execution_session_status.py',
    'resources/submission/types/existing_submission_executing.py',
    'resources/submission/types/expression_location.py',
    'resources/submission/types/finished_response.py',
    'resources/submission/types/get_execution_session_state_response.py',
    'resources/submission/types/get_submission_state_response.py',
    'resources/submission/types/get_trace_responses_page_request.py',
    'resources/submission/types/graded_response.py',
    'resources/submission/types/graded_response_v_2.py',
    'resources/submission/types/graded_test_case_update.py',
    'resources/submission/types/initialize_problem_request.py',
    'resources/submission/types/internal_error.py',
    'resources/submission/types/invalid_request_cause.py',
    'resources/submission/types/invalid_request_response.py',
    'resources/submission/types/lightweight_stackframe_information.py',
    'resources/submission/types/recorded_response_notification.py',
    'resources/submission/types/recorded_test_case_update.py',
    'resources/submission/types/recording_response_notification.py',
    'resources/submission/types/running_response.py',
    'resources/submission/types/running_submission_state.py',
    'resources/submission/types/runtime_error.py',
    'resources/submission/types/scope.py',
    'resources/submission/types/share_id.py',
    'resources/submission/types/stack_frame.py',
    'resources/submission/types/stack_information.py',
    'resources/submission/types/stderr_response.py',
    'resources/submission/types/stdout_response.py',
    'resources/submission/types/stop_request.py',
    'resources/submission/types/stopped_response.py',
    'resources/submission/types/submission_file_info.py',
    'resources/submission/types/submission_id.py',
    'resources/submission/types/submission_id_not_found.py',
    'resources/submission/types/submission_request.py',
    'resources/submission/types/submission_response.py',
    'resources/submission/types/submission_status_for_test_case.py',
    'resources/submission/types/submission_status_v_2.py',
    'resources/submission/types/submission_type_enum.py',
    'resources/submission/types/submission_type_state.py',
    'resources/submission/types/submit_request_v_2.py',
    'resources/submission/types/terminated_response.py',
    'resources/submission/types/test_case_grade.py',
    'resources/submission/types/test_case_hidden_grade.py',
    'resources/submission/types/test_case_non_hidden_grade.py',
    'resources/submission/types/test_case_result.py',
    'resources/submission/types/test_case_result_with_stdout.py',
    'resources/submission/types/test_submission_state.py',
    'resources/submission/types/test_submission_status.py',
    'resources/submission/types/test_submission_status_v_2.py',
    'resources/submission/types/test_submission_update.py',
    'resources/submission/types/test_submission_update_info.py',
    'resources/submission/types/trace_response.py',
    'resources/submission/types/trace_response_v_2.py',
    'resources/submission/types/trace_responses_page.py',
    'resources/submission/types/trace_responses_page_v_2.py',
    'resources/submission/types/traced_file.py',
    'resources/submission/types/traced_test_case.py',
    'resources/submission/types/unexpected_language_error.py',
    'resources/submission/types/workspace_files.py',
    'resources/submission/types/workspace_ran_response.py',
    'resources/submission/types/workspace_run_details.py',
    'resources/submission/types/workspace_starter_files_response.py',
    'resources/submission/types/workspace_starter_files_response_v_2.py',
    'resources/submission/types/workspace_submission_state.py',
    'resources/submission/types/workspace_submission_status.py',
    'resources/submission/types/workspace_submission_status_v_2.py',
    'resources/submission/types/workspace_submission_update.py',
    'resources/submission/types/workspace_submission_update_info.py',
    'resources/submission/types/workspace_submit_request.py',
    'resources/submission/types/workspace_traced_update.py',
    'resources/sysprop/__init__.py',
    'resources/sysprop/service/__init__.py',
    'resources/sysprop/service/service.py',
    'resources/v_2/__init__.py',
    'resources/v_2/resources/__init__.py',
    'resources/v_2/resources/problem/__init__.py',
    'resources/v_2/resources/problem/service/__init__.py',
    'resources/v_2/resources/problem/service/service.py',
    'resources/v_2/resources/problem/types/__init__.py',
    'resources/v_2/resources/problem/types/assert_correctness_check.py',
    'resources/v_2/resources/problem/types/basic_custom_files.py',
    'resources/v_2/resources/problem/types/basic_test_case_template.py',
    'resources/v_2/resources/problem/types/create_problem_request_v_2.py',
    'resources/v_2/resources/problem/types/custom_files.py',
    'resources/v_2/resources/problem/types/deep_equality_correctness_check.py',
    'resources/v_2/resources/problem/types/default_provided_file.py',
    'resources/v_2/resources/problem/types/file_info_v_2.py',
    'resources/v_2/resources/problem/types/files.py',
    'resources/v_2/resources/problem/types/function_implementation.py',
    'resources/v_2/resources/problem/types/function_implementation_for_multiple_languages.py',
    'resources/v_2/resources/problem/types/function_signature.py',
    'resources/v_2/resources/problem/types/generated_files.py',
    'resources/v_2/resources/problem/types/get_basic_solution_file_request.py',
    'resources/v_2/resources/problem/types/get_basic_solution_file_response.py',
    'resources/v_2/resources/problem/types/get_function_signature_request.py',
    'resources/v_2/resources/problem/types/get_function_signature_response.py',
    'resources/v_2/resources/problem/types/get_generated_test_case_file_request.py',
    'resources/v_2/resources/problem/types/get_generated_test_case_template_file_request.py',
    'resources/v_2/resources/problem/types/lightweight_problem_info_v_2.py',
    'resources/v_2/resources/problem/types/non_void_function_definition.py',
    'resources/v_2/resources/problem/types/non_void_function_signature.py',
    'resources/v_2/resources/problem/types/parameter.py',
    'resources/v_2/resources/problem/types/parameter_id.py',
    'resources/v_2/resources/problem/types/problem_info_v_2.py',
    'resources/v_2/resources/problem/types/test_case_expects.py',
    'resources/v_2/resources/problem/types/test_case_function.py',
    'resources/v_2/resources/problem/types/test_case_id.py',
    'resources/v_2/resources/problem/types/test_case_implementation.py',
    'resources/v_2/resources/problem/types/test_case_implementation_description.py',
    'resources/v_2/resources/problem/types/test_case_implementation_description_board.py',
    'resources/v_2/resources/problem/types/test_case_implementation_reference.py',
    'resources/v_2/resources/problem/types/test_case_metadata.py',
    'resources/v_2/resources/problem/types/test_case_template.py',
    'resources/v_2/resources/problem/types/test_case_template_id.py',
    'resources/v_2/resources/problem/types/test_case_v_2.py',
    'resources/v_2/resources/problem/types/test_case_with_actual_result_implementation.py',
    'resources/v_2/resources/problem/types/void_function_definition.py',
    'resources/v_2/resources/problem/types/void_function_definition_that_takes_actual_result.py',
    'resources/v_2/resources/problem/types/void_function_signature.py',
    'resources/v_2/resources/problem/types/void_function_signature_that_takes_actual_result.py',
    'resources/v_2/resources/v_3/__init__.py',
    'resources/v_2/resources/v_3/resources/__init__.py',
    'resources/v_2/resources/v_3/resources/problem/__init__.py',
    'resources/v_2/resources/v_3/resources/problem/service/__init__.py',
    'resources/v_2/resources/v_3/resources/problem/service/service.py',
    'resources/v_2/resources/v_3/resources/problem/types/__init__.py',
    'resources/v_2/resources/v_3/resources/problem/types/assert_correctness_check.py',
    'resources/v_2/resources/v_3/resources/problem/types/basic_custom_files.py',
    'resources/v_2/resources/v_3/resources/problem/types/basic_test_case_template.py',
    'resources/v_2/resources/v_3/resources/problem/types/create_problem_request_v_2.py',
    'resources/v_2/resources/v_3/resources/problem/types/custom_files.py',
    'resources/v_2/resources/v_3/resources/problem/types/deep_equality_correctness_check.py',
    'resources/v_2/resources/v_3/resources/problem/types/default_provided_file.py',
    'resources/v_2/resources/v_3/resources/problem/types/file_info_v_2.py',
    'resources/v_2/resources/v_3/resources/problem/types/files.py',
    'resources/v_2/resources/v_3/resources/problem/types/function_implementation.py',
    'resources/v_2/resources/v_3/resources/problem/types/function_implementation_for_multiple_languages.py',
    'resources/v_2/resources/v_3/resources/problem/types/function_signature.py',
    'resources/v_2/resources/v_3/resources/problem/types/generated_files.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_basic_solution_file_request.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_basic_solution_file_response.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_function_signature_request.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_function_signature_response.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_generated_test_case_file_request.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_generated_test_case_template_file_request.py',
    'resources/v_2/resources/v_3/resources/problem/types/lightweight_problem_info_v_2.py',
    'resources/v_2/resources/v_3/resources/problem/types/non_void_function_definition.py',
    'resources/v_2/resources/v_3/resources/problem/types/non_void_function_signature.py',
    'resources/v_2/resources/v_3/resources/problem/types/parameter.py',
    'resources/v_2/resources/v_3/resources/problem/types/parameter_id.py',
    'resources/v_2/resources/v_3/resources/problem/types/problem_info_v_2.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_expects.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_function.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_id.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_implementation.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_implementation_description.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_implementation_description_board.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_implementation_reference.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_metadata.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_template.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_template_id.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_v_2.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_with_actual_result_implementation.py',
    'resources/v_2/resources/v_3/resources/problem/types/void_function_definition.py',
    'resources/v_2/resources/v_3/resources/problem/types/void_function_definition_that_takes_actual_result.py',
    'resources/v_2/resources/v_3/resources/problem/types/void_function_signature.py',
    'resources/v_2/resources/v_3/resources/problem/types/void_function_signature_that_takes_actual_result.py',
    'resources/v_2/service/__init__.py',
    'resources/v_2/service/service.py',
    'security.py'
]

snapshots['test_fastapi register'] = FileSnapshot('snap_test_fastapi/test_fastapi register.py')

snapshots['test_fastapi resources___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources___init__.py')

snapshots['test_fastapi resources_admin___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_admin___init__.py')

snapshots['test_fastapi resources_admin_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_admin_service___init__.py')

snapshots['test_fastapi resources_admin_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_admin_service_service.py')

snapshots['test_fastapi resources_admin_service_store_traced_test_case_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_admin_service_store_traced_test_case_request.py')

snapshots['test_fastapi resources_admin_service_store_traced_workspace_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_admin_service_store_traced_workspace_request.py')

snapshots['test_fastapi resources_admin_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_admin_types___init__.py')

snapshots['test_fastapi resources_admin_types_test'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_admin_types_test.py')

snapshots['test_fastapi resources_commons___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons___init__.py')

snapshots['test_fastapi resources_commons_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types___init__.py')

snapshots['test_fastapi resources_commons_types_binary_tree_node_and_tree_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_binary_tree_node_and_tree_value.py')

snapshots['test_fastapi resources_commons_types_binary_tree_node_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_binary_tree_node_value.py')

snapshots['test_fastapi resources_commons_types_binary_tree_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_binary_tree_value.py')

snapshots['test_fastapi resources_commons_types_debug_key_value_pairs'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_debug_key_value_pairs.py')

snapshots['test_fastapi resources_commons_types_debug_map_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_debug_map_value.py')

snapshots['test_fastapi resources_commons_types_debug_variable_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_debug_variable_value.py')

snapshots['test_fastapi resources_commons_types_doubly_linked_list_node_and_list_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_doubly_linked_list_node_and_list_value.py')

snapshots['test_fastapi resources_commons_types_doubly_linked_list_node_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_doubly_linked_list_node_value.py')

snapshots['test_fastapi resources_commons_types_doubly_linked_list_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_doubly_linked_list_value.py')

snapshots['test_fastapi resources_commons_types_file_info'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_file_info.py')

snapshots['test_fastapi resources_commons_types_generic_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_generic_value.py')

snapshots['test_fastapi resources_commons_types_key_value_pair'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_key_value_pair.py')

snapshots['test_fastapi resources_commons_types_language'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_language.py')

snapshots['test_fastapi resources_commons_types_list_type'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_list_type.py')

snapshots['test_fastapi resources_commons_types_map_type'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_map_type.py')

snapshots['test_fastapi resources_commons_types_map_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_map_value.py')

snapshots['test_fastapi resources_commons_types_node_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_node_id.py')

snapshots['test_fastapi resources_commons_types_problem_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_problem_id.py')

snapshots['test_fastapi resources_commons_types_singly_linked_list_node_and_list_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_singly_linked_list_node_and_list_value.py')

snapshots['test_fastapi resources_commons_types_singly_linked_list_node_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_singly_linked_list_node_value.py')

snapshots['test_fastapi resources_commons_types_singly_linked_list_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_singly_linked_list_value.py')

snapshots['test_fastapi resources_commons_types_test_case'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_test_case.py')

snapshots['test_fastapi resources_commons_types_test_case_with_expected_result'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_test_case_with_expected_result.py')

snapshots['test_fastapi resources_commons_types_user_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_user_id.py')

snapshots['test_fastapi resources_commons_types_variable_type'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_variable_type.py')

snapshots['test_fastapi resources_commons_types_variable_value'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_commons_types_variable_value.py')

snapshots['test_fastapi resources_homepage___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_homepage___init__.py')

snapshots['test_fastapi resources_homepage_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_homepage_service___init__.py')

snapshots['test_fastapi resources_homepage_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_homepage_service_service.py')

snapshots['test_fastapi resources_lang_server___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_lang_server___init__.py')

snapshots['test_fastapi resources_lang_server_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_lang_server_types___init__.py')

snapshots['test_fastapi resources_lang_server_types_lang_server_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_lang_server_types_lang_server_request.py')

snapshots['test_fastapi resources_lang_server_types_lang_server_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_lang_server_types_lang_server_response.py')

snapshots['test_fastapi resources_migration___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_migration___init__.py')

snapshots['test_fastapi resources_migration_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_migration_service___init__.py')

snapshots['test_fastapi resources_migration_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_migration_service_service.py')

snapshots['test_fastapi resources_migration_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_migration_types___init__.py')

snapshots['test_fastapi resources_migration_types_migration'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_migration_types_migration.py')

snapshots['test_fastapi resources_migration_types_migration_status'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_migration_types_migration_status.py')

snapshots['test_fastapi resources_playlist___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist___init__.py')

snapshots['test_fastapi resources_playlist_errors___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_errors___init__.py')

snapshots['test_fastapi resources_playlist_errors_playlist_id_not_found_error'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_errors_playlist_id_not_found_error.py')

snapshots['test_fastapi resources_playlist_errors_unauthorized_error'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_errors_unauthorized_error.py')

snapshots['test_fastapi resources_playlist_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_service___init__.py')

snapshots['test_fastapi resources_playlist_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_service_service.py')

snapshots['test_fastapi resources_playlist_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_types___init__.py')

snapshots['test_fastapi resources_playlist_types_playlist'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_types_playlist.py')

snapshots['test_fastapi resources_playlist_types_playlist_create_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_types_playlist_create_request.py')

snapshots['test_fastapi resources_playlist_types_playlist_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_types_playlist_id.py')

snapshots['test_fastapi resources_playlist_types_playlist_id_not_found_error_body'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_types_playlist_id_not_found_error_body.py')

snapshots['test_fastapi resources_playlist_types_reserved_keyword_enum'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_types_reserved_keyword_enum.py')

snapshots['test_fastapi resources_playlist_types_update_playlist_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_playlist_types_update_playlist_request.py')

snapshots['test_fastapi resources_problem___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem___init__.py')

snapshots['test_fastapi resources_problem_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_service___init__.py')

snapshots['test_fastapi resources_problem_service_get_default_starter_files_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_service_get_default_starter_files_request.py')

snapshots['test_fastapi resources_problem_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_service_service.py')

snapshots['test_fastapi resources_problem_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types___init__.py')

snapshots['test_fastapi resources_problem_types_create_problem_error'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_create_problem_error.py')

snapshots['test_fastapi resources_problem_types_create_problem_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_create_problem_request.py')

snapshots['test_fastapi resources_problem_types_create_problem_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_create_problem_response.py')

snapshots['test_fastapi resources_problem_types_generic_create_problem_error'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_generic_create_problem_error.py')

snapshots['test_fastapi resources_problem_types_get_default_starter_files_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_get_default_starter_files_response.py')

snapshots['test_fastapi resources_problem_types_problem_description'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_problem_description.py')

snapshots['test_fastapi resources_problem_types_problem_description_board'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_problem_description_board.py')

snapshots['test_fastapi resources_problem_types_problem_files'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_problem_files.py')

snapshots['test_fastapi resources_problem_types_problem_info'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_problem_info.py')

snapshots['test_fastapi resources_problem_types_update_problem_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_update_problem_response.py')

snapshots['test_fastapi resources_problem_types_variable_type_and_name'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_problem_types_variable_type_and_name.py')

snapshots['test_fastapi resources_submission___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission___init__.py')

snapshots['test_fastapi resources_submission_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_service___init__.py')

snapshots['test_fastapi resources_submission_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_service_service.py')

snapshots['test_fastapi resources_submission_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types___init__.py')

snapshots['test_fastapi resources_submission_types_actual_result'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_actual_result.py')

snapshots['test_fastapi resources_submission_types_building_executor_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_building_executor_response.py')

snapshots['test_fastapi resources_submission_types_code_execution_update'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_code_execution_update.py')

snapshots['test_fastapi resources_submission_types_compile_error'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_compile_error.py')

snapshots['test_fastapi resources_submission_types_custom_test_cases_unsupported'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_custom_test_cases_unsupported.py')

snapshots['test_fastapi resources_submission_types_error_info'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_error_info.py')

snapshots['test_fastapi resources_submission_types_errored_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_errored_response.py')

snapshots['test_fastapi resources_submission_types_exception_info'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_exception_info.py')

snapshots['test_fastapi resources_submission_types_exception_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_exception_v_2.py')

snapshots['test_fastapi resources_submission_types_execution_session_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_execution_session_response.py')

snapshots['test_fastapi resources_submission_types_execution_session_state'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_execution_session_state.py')

snapshots['test_fastapi resources_submission_types_execution_session_status'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_execution_session_status.py')

snapshots['test_fastapi resources_submission_types_existing_submission_executing'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_existing_submission_executing.py')

snapshots['test_fastapi resources_submission_types_expression_location'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_expression_location.py')

snapshots['test_fastapi resources_submission_types_finished_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_finished_response.py')

snapshots['test_fastapi resources_submission_types_get_execution_session_state_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_get_execution_session_state_response.py')

snapshots['test_fastapi resources_submission_types_get_submission_state_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_get_submission_state_response.py')

snapshots['test_fastapi resources_submission_types_get_trace_responses_page_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_get_trace_responses_page_request.py')

snapshots['test_fastapi resources_submission_types_graded_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_graded_response.py')

snapshots['test_fastapi resources_submission_types_graded_response_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_graded_response_v_2.py')

snapshots['test_fastapi resources_submission_types_graded_test_case_update'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_graded_test_case_update.py')

snapshots['test_fastapi resources_submission_types_initialize_problem_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_initialize_problem_request.py')

snapshots['test_fastapi resources_submission_types_internal_error'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_internal_error.py')

snapshots['test_fastapi resources_submission_types_invalid_request_cause'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_invalid_request_cause.py')

snapshots['test_fastapi resources_submission_types_invalid_request_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_invalid_request_response.py')

snapshots['test_fastapi resources_submission_types_lightweight_stackframe_information'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_lightweight_stackframe_information.py')

snapshots['test_fastapi resources_submission_types_recorded_response_notification'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_recorded_response_notification.py')

snapshots['test_fastapi resources_submission_types_recorded_test_case_update'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_recorded_test_case_update.py')

snapshots['test_fastapi resources_submission_types_recording_response_notification'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_recording_response_notification.py')

snapshots['test_fastapi resources_submission_types_running_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_running_response.py')

snapshots['test_fastapi resources_submission_types_running_submission_state'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_running_submission_state.py')

snapshots['test_fastapi resources_submission_types_runtime_error'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_runtime_error.py')

snapshots['test_fastapi resources_submission_types_scope'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_scope.py')

snapshots['test_fastapi resources_submission_types_share_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_share_id.py')

snapshots['test_fastapi resources_submission_types_stack_frame'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_stack_frame.py')

snapshots['test_fastapi resources_submission_types_stack_information'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_stack_information.py')

snapshots['test_fastapi resources_submission_types_stderr_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_stderr_response.py')

snapshots['test_fastapi resources_submission_types_stdout_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_stdout_response.py')

snapshots['test_fastapi resources_submission_types_stop_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_stop_request.py')

snapshots['test_fastapi resources_submission_types_stopped_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_stopped_response.py')

snapshots['test_fastapi resources_submission_types_submission_file_info'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_submission_file_info.py')

snapshots['test_fastapi resources_submission_types_submission_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_submission_id.py')

snapshots['test_fastapi resources_submission_types_submission_id_not_found'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_submission_id_not_found.py')

snapshots['test_fastapi resources_submission_types_submission_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_submission_request.py')

snapshots['test_fastapi resources_submission_types_submission_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_submission_response.py')

snapshots['test_fastapi resources_submission_types_submission_status_for_test_case'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_submission_status_for_test_case.py')

snapshots['test_fastapi resources_submission_types_submission_status_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_submission_status_v_2.py')

snapshots['test_fastapi resources_submission_types_submission_type_enum'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_submission_type_enum.py')

snapshots['test_fastapi resources_submission_types_submission_type_state'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_submission_type_state.py')

snapshots['test_fastapi resources_submission_types_submit_request_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_submit_request_v_2.py')

snapshots['test_fastapi resources_submission_types_terminated_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_terminated_response.py')

snapshots['test_fastapi resources_submission_types_test_case_grade'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_test_case_grade.py')

snapshots['test_fastapi resources_submission_types_test_case_hidden_grade'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_test_case_hidden_grade.py')

snapshots['test_fastapi resources_submission_types_test_case_non_hidden_grade'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_test_case_non_hidden_grade.py')

snapshots['test_fastapi resources_submission_types_test_case_result'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_test_case_result.py')

snapshots['test_fastapi resources_submission_types_test_case_result_with_stdout'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_test_case_result_with_stdout.py')

snapshots['test_fastapi resources_submission_types_test_submission_state'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_test_submission_state.py')

snapshots['test_fastapi resources_submission_types_test_submission_status'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_test_submission_status.py')

snapshots['test_fastapi resources_submission_types_test_submission_status_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_test_submission_status_v_2.py')

snapshots['test_fastapi resources_submission_types_test_submission_update'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_test_submission_update.py')

snapshots['test_fastapi resources_submission_types_test_submission_update_info'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_test_submission_update_info.py')

snapshots['test_fastapi resources_submission_types_trace_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_trace_response.py')

snapshots['test_fastapi resources_submission_types_trace_response_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_trace_response_v_2.py')

snapshots['test_fastapi resources_submission_types_trace_responses_page'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_trace_responses_page.py')

snapshots['test_fastapi resources_submission_types_trace_responses_page_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_trace_responses_page_v_2.py')

snapshots['test_fastapi resources_submission_types_traced_file'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_traced_file.py')

snapshots['test_fastapi resources_submission_types_traced_test_case'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_traced_test_case.py')

snapshots['test_fastapi resources_submission_types_unexpected_language_error'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_unexpected_language_error.py')

snapshots['test_fastapi resources_submission_types_workspace_files'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_files.py')

snapshots['test_fastapi resources_submission_types_workspace_ran_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_ran_response.py')

snapshots['test_fastapi resources_submission_types_workspace_run_details'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_run_details.py')

snapshots['test_fastapi resources_submission_types_workspace_starter_files_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_starter_files_response.py')

snapshots['test_fastapi resources_submission_types_workspace_starter_files_response_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_starter_files_response_v_2.py')

snapshots['test_fastapi resources_submission_types_workspace_submission_state'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_submission_state.py')

snapshots['test_fastapi resources_submission_types_workspace_submission_status'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_submission_status.py')

snapshots['test_fastapi resources_submission_types_workspace_submission_status_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_submission_status_v_2.py')

snapshots['test_fastapi resources_submission_types_workspace_submission_update'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_submission_update.py')

snapshots['test_fastapi resources_submission_types_workspace_submission_update_info'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_submission_update_info.py')

snapshots['test_fastapi resources_submission_types_workspace_submit_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_submit_request.py')

snapshots['test_fastapi resources_submission_types_workspace_traced_update'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_submission_types_workspace_traced_update.py')

snapshots['test_fastapi resources_sysprop___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_sysprop___init__.py')

snapshots['test_fastapi resources_sysprop_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_sysprop_service___init__.py')

snapshots['test_fastapi resources_sysprop_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_sysprop_service_service.py')

snapshots['test_fastapi resources_v_2___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2___init__.py')

snapshots['test_fastapi resources_v_2_resources___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources___init__.py')

snapshots['test_fastapi resources_v_2_resources_problem___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem___init__.py')

snapshots['test_fastapi resources_v_2_resources_problem_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_service___init__.py')

snapshots['test_fastapi resources_v_2_resources_problem_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_service_service.py')

snapshots['test_fastapi resources_v_2_resources_problem_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types___init__.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_assert_correctness_check'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_assert_correctness_check.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_basic_custom_files'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_basic_custom_files.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_basic_test_case_template'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_basic_test_case_template.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_create_problem_request_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_create_problem_request_v_2.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_custom_files'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_custom_files.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_deep_equality_correctness_check'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_deep_equality_correctness_check.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_default_provided_file'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_default_provided_file.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_file_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_file_info_v_2.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_files'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_files.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_function_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_function_implementation.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_function_implementation_for_multiple_languages'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_function_implementation_for_multiple_languages.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_function_signature.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_generated_files'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_generated_files.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_get_basic_solution_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_get_basic_solution_file_request.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_get_basic_solution_file_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_get_basic_solution_file_response.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_get_function_signature_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_get_function_signature_request.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_get_function_signature_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_get_function_signature_response.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_get_generated_test_case_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_get_generated_test_case_file_request.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_get_generated_test_case_template_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_get_generated_test_case_template_file_request.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_lightweight_problem_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_lightweight_problem_info_v_2.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_non_void_function_definition'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_non_void_function_definition.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_non_void_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_non_void_function_signature.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_parameter'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_parameter.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_parameter_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_parameter_id.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_problem_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_problem_info_v_2.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_expects'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_expects.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_function'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_function.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_id.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_implementation.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_implementation_description'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_implementation_description.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_implementation_description_board'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_implementation_description_board.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_implementation_reference'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_implementation_reference.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_metadata'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_metadata.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_template'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_template.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_template_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_template_id.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_v_2.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_test_case_with_actual_result_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_test_case_with_actual_result_implementation.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_void_function_definition'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_void_function_definition.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_void_function_definition_that_takes_actual_result'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_void_function_definition_that_takes_actual_result.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_void_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_void_function_signature.py')

snapshots['test_fastapi resources_v_2_resources_problem_types_void_function_signature_that_takes_actual_result'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_problem_types_void_function_signature_that_takes_actual_result.py')

snapshots['test_fastapi resources_v_2_resources_v_3___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3___init__.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources___init__.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem___init__.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_service___init__.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_service_service.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types___init__.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_assert_correctness_check'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_assert_correctness_check.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_basic_custom_files'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_basic_custom_files.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_basic_test_case_template'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_basic_test_case_template.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_create_problem_request_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_create_problem_request_v_2.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_custom_files'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_custom_files.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_deep_equality_correctness_check'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_deep_equality_correctness_check.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_default_provided_file'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_default_provided_file.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_file_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_file_info_v_2.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_files'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_files.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_function_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_function_implementation.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_function_implementation_for_multiple_languages'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_function_implementation_for_multiple_languages.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_function_signature.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_generated_files'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_generated_files.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_basic_solution_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_basic_solution_file_request.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_basic_solution_file_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_basic_solution_file_response.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_function_signature_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_function_signature_request.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_function_signature_response'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_function_signature_response.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_generated_test_case_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_generated_test_case_file_request.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_generated_test_case_template_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_get_generated_test_case_template_file_request.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_lightweight_problem_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_lightweight_problem_info_v_2.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_non_void_function_definition'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_non_void_function_definition.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_non_void_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_non_void_function_signature.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_parameter'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_parameter.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_parameter_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_parameter_id.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_problem_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_problem_info_v_2.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_expects'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_expects.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_function'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_function.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_id.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_implementation.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_description'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_description.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_description_board'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_description_board.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_reference'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_reference.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_metadata'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_metadata.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_template'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_template.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_template_id'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_template_id.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_v_2.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_with_actual_result_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_test_case_with_actual_result_implementation.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_void_function_definition'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_void_function_definition.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_void_function_definition_that_takes_actual_result'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_void_function_definition_that_takes_actual_result.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_void_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_void_function_signature.py')

snapshots['test_fastapi resources_v_2_resources_v_3_resources_problem_types_void_function_signature_that_takes_actual_result'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_resources_v_3_resources_problem_types_void_function_signature_that_takes_actual_result.py')

snapshots['test_fastapi resources_v_2_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_service___init__.py')

snapshots['test_fastapi resources_v_2_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi resources_v_2_service_service.py')

snapshots['test_fastapi security'] = FileSnapshot('snap_test_fastapi/test_fastapi security.py')

snapshots['test_fastapi_async __init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async __init__.py')

snapshots['test_fastapi_async core___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async core___init__.py')

snapshots['test_fastapi_async core_abstract_fern_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async core_abstract_fern_service.py')

snapshots['test_fastapi_async core_datetime_utils'] = FileSnapshot('snap_test_fastapi/test_fastapi_async core_datetime_utils.py')

snapshots['test_fastapi_async core_exceptions___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async core_exceptions___init__.py')

snapshots['test_fastapi_async core_exceptions_fern_http_exception'] = FileSnapshot('snap_test_fastapi/test_fastapi_async core_exceptions_fern_http_exception.py')

snapshots['test_fastapi_async core_exceptions_handlers'] = FileSnapshot('snap_test_fastapi/test_fastapi_async core_exceptions_handlers.py')

snapshots['test_fastapi_async core_exceptions_unauthorized'] = FileSnapshot('snap_test_fastapi/test_fastapi_async core_exceptions_unauthorized.py')

snapshots['test_fastapi_async core_route_args'] = FileSnapshot('snap_test_fastapi/test_fastapi_async core_route_args.py')

snapshots['test_fastapi_async core_security___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async core_security___init__.py')

snapshots['test_fastapi_async core_security_bearer'] = FileSnapshot('snap_test_fastapi/test_fastapi_async core_security_bearer.py')

snapshots['test_fastapi_async filepaths'] = [
    '__init__.py',
    'core/__init__.py',
    'core/abstract_fern_service.py',
    'core/datetime_utils.py',
    'core/exceptions/__init__.py',
    'core/exceptions/fern_http_exception.py',
    'core/exceptions/handlers.py',
    'core/exceptions/unauthorized.py',
    'core/route_args.py',
    'core/security/__init__.py',
    'core/security/bearer.py',
    'register.py',
    'resources/__init__.py',
    'resources/admin/__init__.py',
    'resources/admin/service/__init__.py',
    'resources/admin/service/service.py',
    'resources/admin/service/store_traced_test_case_request.py',
    'resources/admin/service/store_traced_workspace_request.py',
    'resources/admin/types/__init__.py',
    'resources/admin/types/test.py',
    'resources/commons/__init__.py',
    'resources/commons/types/__init__.py',
    'resources/commons/types/binary_tree_node_and_tree_value.py',
    'resources/commons/types/binary_tree_node_value.py',
    'resources/commons/types/binary_tree_value.py',
    'resources/commons/types/debug_key_value_pairs.py',
    'resources/commons/types/debug_map_value.py',
    'resources/commons/types/debug_variable_value.py',
    'resources/commons/types/doubly_linked_list_node_and_list_value.py',
    'resources/commons/types/doubly_linked_list_node_value.py',
    'resources/commons/types/doubly_linked_list_value.py',
    'resources/commons/types/file_info.py',
    'resources/commons/types/generic_value.py',
    'resources/commons/types/key_value_pair.py',
    'resources/commons/types/language.py',
    'resources/commons/types/list_type.py',
    'resources/commons/types/map_type.py',
    'resources/commons/types/map_value.py',
    'resources/commons/types/node_id.py',
    'resources/commons/types/problem_id.py',
    'resources/commons/types/singly_linked_list_node_and_list_value.py',
    'resources/commons/types/singly_linked_list_node_value.py',
    'resources/commons/types/singly_linked_list_value.py',
    'resources/commons/types/test_case.py',
    'resources/commons/types/test_case_with_expected_result.py',
    'resources/commons/types/user_id.py',
    'resources/commons/types/variable_type.py',
    'resources/commons/types/variable_value.py',
    'resources/homepage/__init__.py',
    'resources/homepage/service/__init__.py',
    'resources/homepage/service/service.py',
    'resources/lang_server/__init__.py',
    'resources/lang_server/types/__init__.py',
    'resources/lang_server/types/lang_server_request.py',
    'resources/lang_server/types/lang_server_response.py',
    'resources/migration/__init__.py',
    'resources/migration/service/__init__.py',
    'resources/migration/service/service.py',
    'resources/migration/types/__init__.py',
    'resources/migration/types/migration.py',
    'resources/migration/types/migration_status.py',
    'resources/playlist/__init__.py',
    'resources/playlist/errors/__init__.py',
    'resources/playlist/errors/playlist_id_not_found_error.py',
    'resources/playlist/errors/unauthorized_error.py',
    'resources/playlist/service/__init__.py',
    'resources/playlist/service/service.py',
    'resources/playlist/types/__init__.py',
    'resources/playlist/types/playlist.py',
    'resources/playlist/types/playlist_create_request.py',
    'resources/playlist/types/playlist_id.py',
    'resources/playlist/types/playlist_id_not_found_error_body.py',
    'resources/playlist/types/reserved_keyword_enum.py',
    'resources/playlist/types/update_playlist_request.py',
    'resources/problem/__init__.py',
    'resources/problem/service/__init__.py',
    'resources/problem/service/get_default_starter_files_request.py',
    'resources/problem/service/service.py',
    'resources/problem/types/__init__.py',
    'resources/problem/types/create_problem_error.py',
    'resources/problem/types/create_problem_request.py',
    'resources/problem/types/create_problem_response.py',
    'resources/problem/types/generic_create_problem_error.py',
    'resources/problem/types/get_default_starter_files_response.py',
    'resources/problem/types/problem_description.py',
    'resources/problem/types/problem_description_board.py',
    'resources/problem/types/problem_files.py',
    'resources/problem/types/problem_info.py',
    'resources/problem/types/update_problem_response.py',
    'resources/problem/types/variable_type_and_name.py',
    'resources/submission/__init__.py',
    'resources/submission/service/__init__.py',
    'resources/submission/service/service.py',
    'resources/submission/types/__init__.py',
    'resources/submission/types/actual_result.py',
    'resources/submission/types/building_executor_response.py',
    'resources/submission/types/code_execution_update.py',
    'resources/submission/types/compile_error.py',
    'resources/submission/types/custom_test_cases_unsupported.py',
    'resources/submission/types/error_info.py',
    'resources/submission/types/errored_response.py',
    'resources/submission/types/exception_info.py',
    'resources/submission/types/exception_v_2.py',
    'resources/submission/types/execution_session_response.py',
    'resources/submission/types/execution_session_state.py',
    'resources/submission/types/execution_session_status.py',
    'resources/submission/types/existing_submission_executing.py',
    'resources/submission/types/expression_location.py',
    'resources/submission/types/finished_response.py',
    'resources/submission/types/get_execution_session_state_response.py',
    'resources/submission/types/get_submission_state_response.py',
    'resources/submission/types/get_trace_responses_page_request.py',
    'resources/submission/types/graded_response.py',
    'resources/submission/types/graded_response_v_2.py',
    'resources/submission/types/graded_test_case_update.py',
    'resources/submission/types/initialize_problem_request.py',
    'resources/submission/types/internal_error.py',
    'resources/submission/types/invalid_request_cause.py',
    'resources/submission/types/invalid_request_response.py',
    'resources/submission/types/lightweight_stackframe_information.py',
    'resources/submission/types/recorded_response_notification.py',
    'resources/submission/types/recorded_test_case_update.py',
    'resources/submission/types/recording_response_notification.py',
    'resources/submission/types/running_response.py',
    'resources/submission/types/running_submission_state.py',
    'resources/submission/types/runtime_error.py',
    'resources/submission/types/scope.py',
    'resources/submission/types/share_id.py',
    'resources/submission/types/stack_frame.py',
    'resources/submission/types/stack_information.py',
    'resources/submission/types/stderr_response.py',
    'resources/submission/types/stdout_response.py',
    'resources/submission/types/stop_request.py',
    'resources/submission/types/stopped_response.py',
    'resources/submission/types/submission_file_info.py',
    'resources/submission/types/submission_id.py',
    'resources/submission/types/submission_id_not_found.py',
    'resources/submission/types/submission_request.py',
    'resources/submission/types/submission_response.py',
    'resources/submission/types/submission_status_for_test_case.py',
    'resources/submission/types/submission_status_v_2.py',
    'resources/submission/types/submission_type_enum.py',
    'resources/submission/types/submission_type_state.py',
    'resources/submission/types/submit_request_v_2.py',
    'resources/submission/types/terminated_response.py',
    'resources/submission/types/test_case_grade.py',
    'resources/submission/types/test_case_hidden_grade.py',
    'resources/submission/types/test_case_non_hidden_grade.py',
    'resources/submission/types/test_case_result.py',
    'resources/submission/types/test_case_result_with_stdout.py',
    'resources/submission/types/test_submission_state.py',
    'resources/submission/types/test_submission_status.py',
    'resources/submission/types/test_submission_status_v_2.py',
    'resources/submission/types/test_submission_update.py',
    'resources/submission/types/test_submission_update_info.py',
    'resources/submission/types/trace_response.py',
    'resources/submission/types/trace_response_v_2.py',
    'resources/submission/types/trace_responses_page.py',
    'resources/submission/types/trace_responses_page_v_2.py',
    'resources/submission/types/traced_file.py',
    'resources/submission/types/traced_test_case.py',
    'resources/submission/types/unexpected_language_error.py',
    'resources/submission/types/workspace_files.py',
    'resources/submission/types/workspace_ran_response.py',
    'resources/submission/types/workspace_run_details.py',
    'resources/submission/types/workspace_starter_files_response.py',
    'resources/submission/types/workspace_starter_files_response_v_2.py',
    'resources/submission/types/workspace_submission_state.py',
    'resources/submission/types/workspace_submission_status.py',
    'resources/submission/types/workspace_submission_status_v_2.py',
    'resources/submission/types/workspace_submission_update.py',
    'resources/submission/types/workspace_submission_update_info.py',
    'resources/submission/types/workspace_submit_request.py',
    'resources/submission/types/workspace_traced_update.py',
    'resources/sysprop/__init__.py',
    'resources/sysprop/service/__init__.py',
    'resources/sysprop/service/service.py',
    'resources/v_2/__init__.py',
    'resources/v_2/resources/__init__.py',
    'resources/v_2/resources/problem/__init__.py',
    'resources/v_2/resources/problem/service/__init__.py',
    'resources/v_2/resources/problem/service/service.py',
    'resources/v_2/resources/problem/types/__init__.py',
    'resources/v_2/resources/problem/types/assert_correctness_check.py',
    'resources/v_2/resources/problem/types/basic_custom_files.py',
    'resources/v_2/resources/problem/types/basic_test_case_template.py',
    'resources/v_2/resources/problem/types/create_problem_request_v_2.py',
    'resources/v_2/resources/problem/types/custom_files.py',
    'resources/v_2/resources/problem/types/deep_equality_correctness_check.py',
    'resources/v_2/resources/problem/types/default_provided_file.py',
    'resources/v_2/resources/problem/types/file_info_v_2.py',
    'resources/v_2/resources/problem/types/files.py',
    'resources/v_2/resources/problem/types/function_implementation.py',
    'resources/v_2/resources/problem/types/function_implementation_for_multiple_languages.py',
    'resources/v_2/resources/problem/types/function_signature.py',
    'resources/v_2/resources/problem/types/generated_files.py',
    'resources/v_2/resources/problem/types/get_basic_solution_file_request.py',
    'resources/v_2/resources/problem/types/get_basic_solution_file_response.py',
    'resources/v_2/resources/problem/types/get_function_signature_request.py',
    'resources/v_2/resources/problem/types/get_function_signature_response.py',
    'resources/v_2/resources/problem/types/get_generated_test_case_file_request.py',
    'resources/v_2/resources/problem/types/get_generated_test_case_template_file_request.py',
    'resources/v_2/resources/problem/types/lightweight_problem_info_v_2.py',
    'resources/v_2/resources/problem/types/non_void_function_definition.py',
    'resources/v_2/resources/problem/types/non_void_function_signature.py',
    'resources/v_2/resources/problem/types/parameter.py',
    'resources/v_2/resources/problem/types/parameter_id.py',
    'resources/v_2/resources/problem/types/problem_info_v_2.py',
    'resources/v_2/resources/problem/types/test_case_expects.py',
    'resources/v_2/resources/problem/types/test_case_function.py',
    'resources/v_2/resources/problem/types/test_case_id.py',
    'resources/v_2/resources/problem/types/test_case_implementation.py',
    'resources/v_2/resources/problem/types/test_case_implementation_description.py',
    'resources/v_2/resources/problem/types/test_case_implementation_description_board.py',
    'resources/v_2/resources/problem/types/test_case_implementation_reference.py',
    'resources/v_2/resources/problem/types/test_case_metadata.py',
    'resources/v_2/resources/problem/types/test_case_template.py',
    'resources/v_2/resources/problem/types/test_case_template_id.py',
    'resources/v_2/resources/problem/types/test_case_v_2.py',
    'resources/v_2/resources/problem/types/test_case_with_actual_result_implementation.py',
    'resources/v_2/resources/problem/types/void_function_definition.py',
    'resources/v_2/resources/problem/types/void_function_definition_that_takes_actual_result.py',
    'resources/v_2/resources/problem/types/void_function_signature.py',
    'resources/v_2/resources/problem/types/void_function_signature_that_takes_actual_result.py',
    'resources/v_2/resources/v_3/__init__.py',
    'resources/v_2/resources/v_3/resources/__init__.py',
    'resources/v_2/resources/v_3/resources/problem/__init__.py',
    'resources/v_2/resources/v_3/resources/problem/service/__init__.py',
    'resources/v_2/resources/v_3/resources/problem/service/service.py',
    'resources/v_2/resources/v_3/resources/problem/types/__init__.py',
    'resources/v_2/resources/v_3/resources/problem/types/assert_correctness_check.py',
    'resources/v_2/resources/v_3/resources/problem/types/basic_custom_files.py',
    'resources/v_2/resources/v_3/resources/problem/types/basic_test_case_template.py',
    'resources/v_2/resources/v_3/resources/problem/types/create_problem_request_v_2.py',
    'resources/v_2/resources/v_3/resources/problem/types/custom_files.py',
    'resources/v_2/resources/v_3/resources/problem/types/deep_equality_correctness_check.py',
    'resources/v_2/resources/v_3/resources/problem/types/default_provided_file.py',
    'resources/v_2/resources/v_3/resources/problem/types/file_info_v_2.py',
    'resources/v_2/resources/v_3/resources/problem/types/files.py',
    'resources/v_2/resources/v_3/resources/problem/types/function_implementation.py',
    'resources/v_2/resources/v_3/resources/problem/types/function_implementation_for_multiple_languages.py',
    'resources/v_2/resources/v_3/resources/problem/types/function_signature.py',
    'resources/v_2/resources/v_3/resources/problem/types/generated_files.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_basic_solution_file_request.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_basic_solution_file_response.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_function_signature_request.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_function_signature_response.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_generated_test_case_file_request.py',
    'resources/v_2/resources/v_3/resources/problem/types/get_generated_test_case_template_file_request.py',
    'resources/v_2/resources/v_3/resources/problem/types/lightweight_problem_info_v_2.py',
    'resources/v_2/resources/v_3/resources/problem/types/non_void_function_definition.py',
    'resources/v_2/resources/v_3/resources/problem/types/non_void_function_signature.py',
    'resources/v_2/resources/v_3/resources/problem/types/parameter.py',
    'resources/v_2/resources/v_3/resources/problem/types/parameter_id.py',
    'resources/v_2/resources/v_3/resources/problem/types/problem_info_v_2.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_expects.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_function.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_id.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_implementation.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_implementation_description.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_implementation_description_board.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_implementation_reference.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_metadata.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_template.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_template_id.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_v_2.py',
    'resources/v_2/resources/v_3/resources/problem/types/test_case_with_actual_result_implementation.py',
    'resources/v_2/resources/v_3/resources/problem/types/void_function_definition.py',
    'resources/v_2/resources/v_3/resources/problem/types/void_function_definition_that_takes_actual_result.py',
    'resources/v_2/resources/v_3/resources/problem/types/void_function_signature.py',
    'resources/v_2/resources/v_3/resources/problem/types/void_function_signature_that_takes_actual_result.py',
    'resources/v_2/service/__init__.py',
    'resources/v_2/service/service.py',
    'security.py'
]

snapshots['test_fastapi_async register'] = FileSnapshot('snap_test_fastapi/test_fastapi_async register.py')

snapshots['test_fastapi_async resources___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources___init__.py')

snapshots['test_fastapi_async resources_admin___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_admin___init__.py')

snapshots['test_fastapi_async resources_admin_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_admin_service___init__.py')

snapshots['test_fastapi_async resources_admin_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_admin_service_service.py')

snapshots['test_fastapi_async resources_admin_service_store_traced_test_case_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_admin_service_store_traced_test_case_request.py')

snapshots['test_fastapi_async resources_admin_service_store_traced_workspace_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_admin_service_store_traced_workspace_request.py')

snapshots['test_fastapi_async resources_admin_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_admin_types___init__.py')

snapshots['test_fastapi_async resources_admin_types_test'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_admin_types_test.py')

snapshots['test_fastapi_async resources_commons___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons___init__.py')

snapshots['test_fastapi_async resources_commons_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types___init__.py')

snapshots['test_fastapi_async resources_commons_types_binary_tree_node_and_tree_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_binary_tree_node_and_tree_value.py')

snapshots['test_fastapi_async resources_commons_types_binary_tree_node_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_binary_tree_node_value.py')

snapshots['test_fastapi_async resources_commons_types_binary_tree_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_binary_tree_value.py')

snapshots['test_fastapi_async resources_commons_types_debug_key_value_pairs'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_debug_key_value_pairs.py')

snapshots['test_fastapi_async resources_commons_types_debug_map_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_debug_map_value.py')

snapshots['test_fastapi_async resources_commons_types_debug_variable_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_debug_variable_value.py')

snapshots['test_fastapi_async resources_commons_types_doubly_linked_list_node_and_list_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_doubly_linked_list_node_and_list_value.py')

snapshots['test_fastapi_async resources_commons_types_doubly_linked_list_node_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_doubly_linked_list_node_value.py')

snapshots['test_fastapi_async resources_commons_types_doubly_linked_list_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_doubly_linked_list_value.py')

snapshots['test_fastapi_async resources_commons_types_file_info'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_file_info.py')

snapshots['test_fastapi_async resources_commons_types_generic_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_generic_value.py')

snapshots['test_fastapi_async resources_commons_types_key_value_pair'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_key_value_pair.py')

snapshots['test_fastapi_async resources_commons_types_language'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_language.py')

snapshots['test_fastapi_async resources_commons_types_list_type'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_list_type.py')

snapshots['test_fastapi_async resources_commons_types_map_type'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_map_type.py')

snapshots['test_fastapi_async resources_commons_types_map_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_map_value.py')

snapshots['test_fastapi_async resources_commons_types_node_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_node_id.py')

snapshots['test_fastapi_async resources_commons_types_problem_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_problem_id.py')

snapshots['test_fastapi_async resources_commons_types_singly_linked_list_node_and_list_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_singly_linked_list_node_and_list_value.py')

snapshots['test_fastapi_async resources_commons_types_singly_linked_list_node_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_singly_linked_list_node_value.py')

snapshots['test_fastapi_async resources_commons_types_singly_linked_list_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_singly_linked_list_value.py')

snapshots['test_fastapi_async resources_commons_types_test_case'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_test_case.py')

snapshots['test_fastapi_async resources_commons_types_test_case_with_expected_result'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_test_case_with_expected_result.py')

snapshots['test_fastapi_async resources_commons_types_user_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_user_id.py')

snapshots['test_fastapi_async resources_commons_types_variable_type'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_variable_type.py')

snapshots['test_fastapi_async resources_commons_types_variable_value'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_commons_types_variable_value.py')

snapshots['test_fastapi_async resources_homepage___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_homepage___init__.py')

snapshots['test_fastapi_async resources_homepage_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_homepage_service___init__.py')

snapshots['test_fastapi_async resources_homepage_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_homepage_service_service.py')

snapshots['test_fastapi_async resources_lang_server___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_lang_server___init__.py')

snapshots['test_fastapi_async resources_lang_server_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_lang_server_types___init__.py')

snapshots['test_fastapi_async resources_lang_server_types_lang_server_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_lang_server_types_lang_server_request.py')

snapshots['test_fastapi_async resources_lang_server_types_lang_server_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_lang_server_types_lang_server_response.py')

snapshots['test_fastapi_async resources_migration___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_migration___init__.py')

snapshots['test_fastapi_async resources_migration_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_migration_service___init__.py')

snapshots['test_fastapi_async resources_migration_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_migration_service_service.py')

snapshots['test_fastapi_async resources_migration_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_migration_types___init__.py')

snapshots['test_fastapi_async resources_migration_types_migration'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_migration_types_migration.py')

snapshots['test_fastapi_async resources_migration_types_migration_status'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_migration_types_migration_status.py')

snapshots['test_fastapi_async resources_playlist___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist___init__.py')

snapshots['test_fastapi_async resources_playlist_errors___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_errors___init__.py')

snapshots['test_fastapi_async resources_playlist_errors_playlist_id_not_found_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_errors_playlist_id_not_found_error.py')

snapshots['test_fastapi_async resources_playlist_errors_unauthorized_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_errors_unauthorized_error.py')

snapshots['test_fastapi_async resources_playlist_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_service___init__.py')

snapshots['test_fastapi_async resources_playlist_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_service_service.py')

snapshots['test_fastapi_async resources_playlist_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_types___init__.py')

snapshots['test_fastapi_async resources_playlist_types_playlist'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_types_playlist.py')

snapshots['test_fastapi_async resources_playlist_types_playlist_create_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_types_playlist_create_request.py')

snapshots['test_fastapi_async resources_playlist_types_playlist_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_types_playlist_id.py')

snapshots['test_fastapi_async resources_playlist_types_playlist_id_not_found_error_body'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_types_playlist_id_not_found_error_body.py')

snapshots['test_fastapi_async resources_playlist_types_reserved_keyword_enum'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_types_reserved_keyword_enum.py')

snapshots['test_fastapi_async resources_playlist_types_update_playlist_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_playlist_types_update_playlist_request.py')

snapshots['test_fastapi_async resources_problem___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem___init__.py')

snapshots['test_fastapi_async resources_problem_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_service___init__.py')

snapshots['test_fastapi_async resources_problem_service_get_default_starter_files_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_service_get_default_starter_files_request.py')

snapshots['test_fastapi_async resources_problem_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_service_service.py')

snapshots['test_fastapi_async resources_problem_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types___init__.py')

snapshots['test_fastapi_async resources_problem_types_create_problem_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_create_problem_error.py')

snapshots['test_fastapi_async resources_problem_types_create_problem_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_create_problem_request.py')

snapshots['test_fastapi_async resources_problem_types_create_problem_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_create_problem_response.py')

snapshots['test_fastapi_async resources_problem_types_generic_create_problem_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_generic_create_problem_error.py')

snapshots['test_fastapi_async resources_problem_types_get_default_starter_files_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_get_default_starter_files_response.py')

snapshots['test_fastapi_async resources_problem_types_problem_description'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_problem_description.py')

snapshots['test_fastapi_async resources_problem_types_problem_description_board'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_problem_description_board.py')

snapshots['test_fastapi_async resources_problem_types_problem_files'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_problem_files.py')

snapshots['test_fastapi_async resources_problem_types_problem_info'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_problem_info.py')

snapshots['test_fastapi_async resources_problem_types_update_problem_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_update_problem_response.py')

snapshots['test_fastapi_async resources_problem_types_variable_type_and_name'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_problem_types_variable_type_and_name.py')

snapshots['test_fastapi_async resources_submission___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission___init__.py')

snapshots['test_fastapi_async resources_submission_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_service___init__.py')

snapshots['test_fastapi_async resources_submission_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_service_service.py')

snapshots['test_fastapi_async resources_submission_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types___init__.py')

snapshots['test_fastapi_async resources_submission_types_actual_result'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_actual_result.py')

snapshots['test_fastapi_async resources_submission_types_building_executor_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_building_executor_response.py')

snapshots['test_fastapi_async resources_submission_types_code_execution_update'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_code_execution_update.py')

snapshots['test_fastapi_async resources_submission_types_compile_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_compile_error.py')

snapshots['test_fastapi_async resources_submission_types_custom_test_cases_unsupported'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_custom_test_cases_unsupported.py')

snapshots['test_fastapi_async resources_submission_types_error_info'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_error_info.py')

snapshots['test_fastapi_async resources_submission_types_errored_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_errored_response.py')

snapshots['test_fastapi_async resources_submission_types_exception_info'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_exception_info.py')

snapshots['test_fastapi_async resources_submission_types_exception_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_exception_v_2.py')

snapshots['test_fastapi_async resources_submission_types_execution_session_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_execution_session_response.py')

snapshots['test_fastapi_async resources_submission_types_execution_session_state'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_execution_session_state.py')

snapshots['test_fastapi_async resources_submission_types_execution_session_status'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_execution_session_status.py')

snapshots['test_fastapi_async resources_submission_types_existing_submission_executing'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_existing_submission_executing.py')

snapshots['test_fastapi_async resources_submission_types_expression_location'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_expression_location.py')

snapshots['test_fastapi_async resources_submission_types_finished_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_finished_response.py')

snapshots['test_fastapi_async resources_submission_types_get_execution_session_state_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_get_execution_session_state_response.py')

snapshots['test_fastapi_async resources_submission_types_get_submission_state_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_get_submission_state_response.py')

snapshots['test_fastapi_async resources_submission_types_get_trace_responses_page_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_get_trace_responses_page_request.py')

snapshots['test_fastapi_async resources_submission_types_graded_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_graded_response.py')

snapshots['test_fastapi_async resources_submission_types_graded_response_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_graded_response_v_2.py')

snapshots['test_fastapi_async resources_submission_types_graded_test_case_update'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_graded_test_case_update.py')

snapshots['test_fastapi_async resources_submission_types_initialize_problem_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_initialize_problem_request.py')

snapshots['test_fastapi_async resources_submission_types_internal_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_internal_error.py')

snapshots['test_fastapi_async resources_submission_types_invalid_request_cause'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_invalid_request_cause.py')

snapshots['test_fastapi_async resources_submission_types_invalid_request_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_invalid_request_response.py')

snapshots['test_fastapi_async resources_submission_types_lightweight_stackframe_information'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_lightweight_stackframe_information.py')

snapshots['test_fastapi_async resources_submission_types_recorded_response_notification'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_recorded_response_notification.py')

snapshots['test_fastapi_async resources_submission_types_recorded_test_case_update'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_recorded_test_case_update.py')

snapshots['test_fastapi_async resources_submission_types_recording_response_notification'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_recording_response_notification.py')

snapshots['test_fastapi_async resources_submission_types_running_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_running_response.py')

snapshots['test_fastapi_async resources_submission_types_running_submission_state'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_running_submission_state.py')

snapshots['test_fastapi_async resources_submission_types_runtime_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_runtime_error.py')

snapshots['test_fastapi_async resources_submission_types_scope'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_scope.py')

snapshots['test_fastapi_async resources_submission_types_share_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_share_id.py')

snapshots['test_fastapi_async resources_submission_types_stack_frame'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_stack_frame.py')

snapshots['test_fastapi_async resources_submission_types_stack_information'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_stack_information.py')

snapshots['test_fastapi_async resources_submission_types_stderr_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_stderr_response.py')

snapshots['test_fastapi_async resources_submission_types_stdout_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_stdout_response.py')

snapshots['test_fastapi_async resources_submission_types_stop_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_stop_request.py')

snapshots['test_fastapi_async resources_submission_types_stopped_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_stopped_response.py')

snapshots['test_fastapi_async resources_submission_types_submission_file_info'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_submission_file_info.py')

snapshots['test_fastapi_async resources_submission_types_submission_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_submission_id.py')

snapshots['test_fastapi_async resources_submission_types_submission_id_not_found'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_submission_id_not_found.py')

snapshots['test_fastapi_async resources_submission_types_submission_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_submission_request.py')

snapshots['test_fastapi_async resources_submission_types_submission_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_submission_response.py')

snapshots['test_fastapi_async resources_submission_types_submission_status_for_test_case'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_submission_status_for_test_case.py')

snapshots['test_fastapi_async resources_submission_types_submission_status_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_submission_status_v_2.py')

snapshots['test_fastapi_async resources_submission_types_submission_type_enum'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_submission_type_enum.py')

snapshots['test_fastapi_async resources_submission_types_submission_type_state'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_submission_type_state.py')

snapshots['test_fastapi_async resources_submission_types_submit_request_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_submit_request_v_2.py')

snapshots['test_fastapi_async resources_submission_types_terminated_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_terminated_response.py')

snapshots['test_fastapi_async resources_submission_types_test_case_grade'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_test_case_grade.py')

snapshots['test_fastapi_async resources_submission_types_test_case_hidden_grade'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_test_case_hidden_grade.py')

snapshots['test_fastapi_async resources_submission_types_test_case_non_hidden_grade'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_test_case_non_hidden_grade.py')

snapshots['test_fastapi_async resources_submission_types_test_case_result'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_test_case_result.py')

snapshots['test_fastapi_async resources_submission_types_test_case_result_with_stdout'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_test_case_result_with_stdout.py')

snapshots['test_fastapi_async resources_submission_types_test_submission_state'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_test_submission_state.py')

snapshots['test_fastapi_async resources_submission_types_test_submission_status'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_test_submission_status.py')

snapshots['test_fastapi_async resources_submission_types_test_submission_status_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_test_submission_status_v_2.py')

snapshots['test_fastapi_async resources_submission_types_test_submission_update'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_test_submission_update.py')

snapshots['test_fastapi_async resources_submission_types_test_submission_update_info'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_test_submission_update_info.py')

snapshots['test_fastapi_async resources_submission_types_trace_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_trace_response.py')

snapshots['test_fastapi_async resources_submission_types_trace_response_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_trace_response_v_2.py')

snapshots['test_fastapi_async resources_submission_types_trace_responses_page'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_trace_responses_page.py')

snapshots['test_fastapi_async resources_submission_types_trace_responses_page_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_trace_responses_page_v_2.py')

snapshots['test_fastapi_async resources_submission_types_traced_file'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_traced_file.py')

snapshots['test_fastapi_async resources_submission_types_traced_test_case'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_traced_test_case.py')

snapshots['test_fastapi_async resources_submission_types_unexpected_language_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_unexpected_language_error.py')

snapshots['test_fastapi_async resources_submission_types_workspace_files'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_files.py')

snapshots['test_fastapi_async resources_submission_types_workspace_ran_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_ran_response.py')

snapshots['test_fastapi_async resources_submission_types_workspace_run_details'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_run_details.py')

snapshots['test_fastapi_async resources_submission_types_workspace_starter_files_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_starter_files_response.py')

snapshots['test_fastapi_async resources_submission_types_workspace_starter_files_response_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_starter_files_response_v_2.py')

snapshots['test_fastapi_async resources_submission_types_workspace_submission_state'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_submission_state.py')

snapshots['test_fastapi_async resources_submission_types_workspace_submission_status'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_submission_status.py')

snapshots['test_fastapi_async resources_submission_types_workspace_submission_status_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_submission_status_v_2.py')

snapshots['test_fastapi_async resources_submission_types_workspace_submission_update'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_submission_update.py')

snapshots['test_fastapi_async resources_submission_types_workspace_submission_update_info'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_submission_update_info.py')

snapshots['test_fastapi_async resources_submission_types_workspace_submit_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_submit_request.py')

snapshots['test_fastapi_async resources_submission_types_workspace_traced_update'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_submission_types_workspace_traced_update.py')

snapshots['test_fastapi_async resources_sysprop___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_sysprop___init__.py')

snapshots['test_fastapi_async resources_sysprop_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_sysprop_service___init__.py')

snapshots['test_fastapi_async resources_sysprop_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_sysprop_service_service.py')

snapshots['test_fastapi_async resources_v_2___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2___init__.py')

snapshots['test_fastapi_async resources_v_2_resources___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources___init__.py')

snapshots['test_fastapi_async resources_v_2_resources_problem___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem___init__.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_service___init__.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_service_service.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types___init__.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_assert_correctness_check'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_assert_correctness_check.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_basic_custom_files'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_basic_custom_files.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_basic_test_case_template'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_basic_test_case_template.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_create_problem_request_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_create_problem_request_v_2.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_custom_files'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_custom_files.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_deep_equality_correctness_check'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_deep_equality_correctness_check.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_default_provided_file'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_default_provided_file.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_file_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_file_info_v_2.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_files'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_files.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_function_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_function_implementation.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_function_implementation_for_multiple_languages'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_function_implementation_for_multiple_languages.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_function_signature.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_generated_files'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_generated_files.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_get_basic_solution_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_get_basic_solution_file_request.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_get_basic_solution_file_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_get_basic_solution_file_response.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_get_function_signature_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_get_function_signature_request.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_get_function_signature_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_get_function_signature_response.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_get_generated_test_case_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_get_generated_test_case_file_request.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_get_generated_test_case_template_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_get_generated_test_case_template_file_request.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_lightweight_problem_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_lightweight_problem_info_v_2.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_non_void_function_definition'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_non_void_function_definition.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_non_void_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_non_void_function_signature.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_parameter'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_parameter.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_parameter_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_parameter_id.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_problem_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_problem_info_v_2.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_expects'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_expects.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_function'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_function.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_id.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_implementation.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_implementation_description'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_implementation_description.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_implementation_description_board'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_implementation_description_board.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_implementation_reference'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_implementation_reference.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_metadata'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_metadata.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_template'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_template.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_template_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_template_id.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_v_2.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_test_case_with_actual_result_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_test_case_with_actual_result_implementation.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_void_function_definition'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_void_function_definition.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_void_function_definition_that_takes_actual_result'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_void_function_definition_that_takes_actual_result.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_void_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_void_function_signature.py')

snapshots['test_fastapi_async resources_v_2_resources_problem_types_void_function_signature_that_takes_actual_result'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_problem_types_void_function_signature_that_takes_actual_result.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3___init__.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources___init__.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem___init__.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_service___init__.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_service_service.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types___init__.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_assert_correctness_check'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_assert_correctness_check.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_basic_custom_files'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_basic_custom_files.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_basic_test_case_template'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_basic_test_case_template.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_create_problem_request_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_create_problem_request_v_2.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_custom_files'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_custom_files.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_deep_equality_correctness_check'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_deep_equality_correctness_check.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_default_provided_file'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_default_provided_file.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_file_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_file_info_v_2.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_files'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_files.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_function_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_function_implementation.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_function_implementation_for_multiple_languages'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_function_implementation_for_multiple_languages.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_function_signature.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_generated_files'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_generated_files.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_basic_solution_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_basic_solution_file_request.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_basic_solution_file_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_basic_solution_file_response.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_function_signature_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_function_signature_request.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_function_signature_response'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_function_signature_response.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_generated_test_case_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_generated_test_case_file_request.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_generated_test_case_template_file_request'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_get_generated_test_case_template_file_request.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_lightweight_problem_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_lightweight_problem_info_v_2.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_non_void_function_definition'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_non_void_function_definition.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_non_void_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_non_void_function_signature.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_parameter'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_parameter.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_parameter_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_parameter_id.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_problem_info_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_problem_info_v_2.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_expects'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_expects.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_function'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_function.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_id.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_implementation.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_description'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_description.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_description_board'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_description_board.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_reference'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_implementation_reference.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_metadata'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_metadata.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_template'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_template.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_template_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_template_id.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_v_2'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_v_2.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_with_actual_result_implementation'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_test_case_with_actual_result_implementation.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_void_function_definition'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_void_function_definition.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_void_function_definition_that_takes_actual_result'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_void_function_definition_that_takes_actual_result.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_void_function_signature'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_void_function_signature.py')

snapshots['test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_void_function_signature_that_takes_actual_result'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_resources_v_3_resources_problem_types_void_function_signature_that_takes_actual_result.py')

snapshots['test_fastapi_async resources_v_2_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_service___init__.py')

snapshots['test_fastapi_async resources_v_2_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_async resources_v_2_service_service.py')

snapshots['test_fastapi_async security'] = FileSnapshot('snap_test_fastapi/test_fastapi_async security.py')

snapshots['test_fastapi_error_status_code __init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code __init__.py')

snapshots['test_fastapi_error_status_code core___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code core___init__.py')

snapshots['test_fastapi_error_status_code core_abstract_fern_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code core_abstract_fern_service.py')

snapshots['test_fastapi_error_status_code core_datetime_utils'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code core_datetime_utils.py')

snapshots['test_fastapi_error_status_code core_exceptions___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code core_exceptions___init__.py')

snapshots['test_fastapi_error_status_code core_exceptions_fern_http_exception'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code core_exceptions_fern_http_exception.py')

snapshots['test_fastapi_error_status_code core_exceptions_handlers'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code core_exceptions_handlers.py')

snapshots['test_fastapi_error_status_code core_exceptions_unauthorized'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code core_exceptions_unauthorized.py')

snapshots['test_fastapi_error_status_code core_route_args'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code core_route_args.py')

snapshots['test_fastapi_error_status_code core_security___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code core_security___init__.py')

snapshots['test_fastapi_error_status_code core_security_bearer'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code core_security_bearer.py')

snapshots['test_fastapi_error_status_code filepaths'] = [
    '__init__.py',
    'core/__init__.py',
    'core/abstract_fern_service.py',
    'core/datetime_utils.py',
    'core/exceptions/__init__.py',
    'core/exceptions/fern_http_exception.py',
    'core/exceptions/handlers.py',
    'core/exceptions/unauthorized.py',
    'core/route_args.py',
    'core/security/__init__.py',
    'core/security/bearer.py',
    'register.py',
    'resources/__init__.py',
    'resources/movie/__init__.py',
    'resources/movie/errors/__init__.py',
    'resources/movie/errors/invalid_movie_error.py',
    'resources/movie/errors/movie_already_exists_error.py',
    'resources/movie/errors/movie_not_found_error.py',
    'resources/movie/service/__init__.py',
    'resources/movie/service/service.py',
    'resources/movie/types/__init__.py',
    'resources/movie/types/movie.py',
    'resources/movie/types/movie_id.py'
]

snapshots['test_fastapi_error_status_code register'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code register.py')

snapshots['test_fastapi_error_status_code resources___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources___init__.py')

snapshots['test_fastapi_error_status_code resources_movie___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources_movie___init__.py')

snapshots['test_fastapi_error_status_code resources_movie_errors___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources_movie_errors___init__.py')

snapshots['test_fastapi_error_status_code resources_movie_errors_invalid_movie_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources_movie_errors_invalid_movie_error.py')

snapshots['test_fastapi_error_status_code resources_movie_errors_movie_already_exists_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources_movie_errors_movie_already_exists_error.py')

snapshots['test_fastapi_error_status_code resources_movie_errors_movie_not_found_error'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources_movie_errors_movie_not_found_error.py')

snapshots['test_fastapi_error_status_code resources_movie_service___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources_movie_service___init__.py')

snapshots['test_fastapi_error_status_code resources_movie_service_service'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources_movie_service_service.py')

snapshots['test_fastapi_error_status_code resources_movie_types___init__'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources_movie_types___init__.py')

snapshots['test_fastapi_error_status_code resources_movie_types_movie'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources_movie_types_movie.py')

snapshots['test_fastapi_error_status_code resources_movie_types_movie_id'] = FileSnapshot('snap_test_fastapi/test_fastapi_error_status_code resources_movie_types_movie_id.py')
