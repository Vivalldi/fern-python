# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot
from snapshottest.file import FileSnapshot


snapshots = Snapshot()

snapshots['test_circular_imports filepaths'] = [
    'src/fern/api/__init__.py',
    'src/fern/api/core/__init__.py',
    'src/fern/api/core/datetime_utils.py',
    'src/fern/api/resources/__init__.py',
    'src/fern/api/resources/bank_lookup/__init__.py',
    'src/fern/api/resources/bank_lookup/bank_address.py',
    'src/fern/api/resources/bank_lookup/bank_lookup_response.py',
    'src/fern/api/resources/commons/__init__.py',
    'src/fern/api/resources/commons/address.py',
    'src/fern/api/resources/commons/approval_policy_id.py',
    'src/fern/api/resources/commons/birth_date.py',
    'src/fern/api/resources/commons/comment_id.py',
    'src/fern/api/resources/commons/entity_id.py',
    'src/fern/api/resources/commons/entity_user_id.py',
    'src/fern/api/resources/commons/full_name.py',
    'src/fern/api/resources/commons/individual_government_id.py',
    'src/fern/api/resources/commons/invoice_id.py',
    'src/fern/api/resources/commons/itin.py',
    'src/fern/api/resources/commons/order_direction.py',
    'src/fern/api/resources/commons/payment_method_id.py',
    'src/fern/api/resources/commons/payment_method_schema_id.py',
    'src/fern/api/resources/commons/phone_number.py',
    'src/fern/api/resources/commons/ssn.py',
    'src/fern/api/resources/entity/__init__.py',
    'src/fern/api/resources/entity/account_type.py',
    'src/fern/api/resources/entity/business_profile_request.py',
    'src/fern/api/resources/entity/business_profile_response.py',
    'src/fern/api/resources/entity/business_type.py',
    'src/fern/api/resources/entity/ein.py',
    'src/fern/api/resources/entity/entity_add_payees_request.py',
    'src/fern/api/resources/entity/entity_request.py',
    'src/fern/api/resources/entity/entity_response.py',
    'src/fern/api/resources/entity/entity_status.py',
    'src/fern/api/resources/entity/entity_update_request.py',
    'src/fern/api/resources/entity/individual_profile_request.py',
    'src/fern/api/resources/entity/individual_profile_response.py',
    'src/fern/api/resources/entity/profile_request.py',
    'src/fern/api/resources/entity/profile_response.py',
    'src/fern/api/resources/entity/resources/__init__.py',
    'src/fern/api/resources/entity/resources/approval_policy/__init__.py',
    'src/fern/api/resources/entity/resources/approval_policy/amount_trigger.py',
    'src/fern/api/resources/entity/resources/approval_policy/approval_policy_request.py',
    'src/fern/api/resources/entity/resources/approval_policy/approval_policy_response.py',
    'src/fern/api/resources/entity/resources/approval_policy/approval_policy_update_request.py',
    'src/fern/api/resources/entity/resources/approval_policy/approver_rule.py',
    'src/fern/api/resources/entity/resources/approval_policy/identifier_list.py',
    'src/fern/api/resources/entity/resources/approval_policy/rule.py',
    'src/fern/api/resources/entity/resources/approval_policy/trigger.py',
    'src/fern/api/resources/entity/resources/counterparty/__init__.py',
    'src/fern/api/resources/entity/resources/counterparty/counterparty_response.py',
    'src/fern/api/resources/entity/resources/counterparty/find_counterparties_response.py',
    'src/fern/api/resources/entity/resources/invoice/__init__.py',
    'src/fern/api/resources/entity/resources/invoice/invoice_metrics_response.py',
    'src/fern/api/resources/entity/resources/representative/__init__.py',
    'src/fern/api/resources/entity/resources/representative/representative_id.py',
    'src/fern/api/resources/entity/resources/representative/representative_request.py',
    'src/fern/api/resources/entity/resources/representative/representative_response.py',
    'src/fern/api/resources/entity/resources/representative/responsibilities.py',
    'src/fern/api/resources/entity/resources/user/__init__.py',
    'src/fern/api/resources/entity/resources/user/entity_user_request.py',
    'src/fern/api/resources/entity/resources/user/entity_user_response.py',
    'src/fern/api/resources/entity/tax_id.py',
    'src/fern/api/resources/invoice/__init__.py',
    'src/fern/api/resources/invoice/approver_action.py',
    'src/fern/api/resources/invoice/assigned_approver.py',
    'src/fern/api/resources/invoice/associated_approval_action.py',
    'src/fern/api/resources/invoice/invoice_approver_response.py',
    'src/fern/api/resources/invoice/invoice_line_item_request.py',
    'src/fern/api/resources/invoice/invoice_line_item_response.py',
    'src/fern/api/resources/invoice/invoice_order_by_field.py',
    'src/fern/api/resources/invoice/invoice_request.py',
    'src/fern/api/resources/invoice/invoice_response.py',
    'src/fern/api/resources/invoice/invoice_status.py',
    'src/fern/api/resources/invoice/resources/__init__.py',
    'src/fern/api/resources/invoice/resources/approval/__init__.py',
    'src/fern/api/resources/invoice/resources/approval/approval_request.py',
    'src/fern/api/resources/invoice/resources/comment/__init__.py',
    'src/fern/api/resources/invoice/resources/comment/comment_request.py',
    'src/fern/api/resources/invoice/resources/comment/comment_response.py',
    'src/fern/api/resources/invoice/resources/document/__init__.py',
    'src/fern/api/resources/invoice/resources/document/document_response.py',
    'src/fern/api/resources/ocr/__init__.py',
    'src/fern/api/resources/ocr/attachments.py',
    'src/fern/api/resources/ocr/email_ocr_request.py',
    'src/fern/api/resources/ocr/ocr_mailbox.py',
    'src/fern/api/resources/ocr/ocr_response.py',
    'src/fern/api/resources/ocr/vendor_network.py',
    'src/fern/api/resources/organization/__init__.py',
    'src/fern/api/resources/organization/color_scheme_request.py',
    'src/fern/api/resources/organization/color_scheme_response.py',
    'src/fern/api/resources/organization/email_log_response.py',
    'src/fern/api/resources/organization/email_provider_request.py',
    'src/fern/api/resources/organization/email_provider_response.py',
    'src/fern/api/resources/organization/email_sender_provider.py',
    'src/fern/api/resources/organization/email_sender_request.py',
    'src/fern/api/resources/organization/email_sender_response.py',
    'src/fern/api/resources/organization/organization_id.py',
    'src/fern/api/resources/organization/organization_request.py',
    'src/fern/api/resources/organization/organization_response.py',
    'src/fern/api/resources/organization/payment_methods_request.py',
    'src/fern/api/resources/organization/payment_methods_response.py',
    'src/fern/api/resources/organization/payment_rail_markup.py',
    'src/fern/api/resources/organization/payment_rail_markup_type.py',
    'src/fern/api/resources/organization/payment_rail_request.py',
    'src/fern/api/resources/organization/payment_rail_response.py',
    'src/fern/api/resources/payment_method/__init__.py',
    'src/fern/api/resources/payment_method/bank_account_base_request.py',
    'src/fern/api/resources/payment_method/bank_account_base_response.py',
    'src/fern/api/resources/payment_method/bank_account_request.py',
    'src/fern/api/resources/payment_method/bank_account_response.py',
    'src/fern/api/resources/payment_method/bank_status.py',
    'src/fern/api/resources/payment_method/bank_type.py',
    'src/fern/api/resources/payment_method/card_base_request.py',
    'src/fern/api/resources/payment_method/card_base_response.py',
    'src/fern/api/resources/payment_method/card_brand.py',
    'src/fern/api/resources/payment_method/card_request.py',
    'src/fern/api/resources/payment_method/card_response.py',
    'src/fern/api/resources/payment_method/card_type.py',
    'src/fern/api/resources/payment_method/check_base_request.py',
    'src/fern/api/resources/payment_method/check_base_response.py',
    'src/fern/api/resources/payment_method/check_request.py',
    'src/fern/api/resources/payment_method/check_response.py',
    'src/fern/api/resources/payment_method/currency_code.py',
    'src/fern/api/resources/payment_method/custom_payment_method_base_request.py',
    'src/fern/api/resources/payment_method/custom_payment_method_base_response.py',
    'src/fern/api/resources/payment_method/custom_payment_method_request.py',
    'src/fern/api/resources/payment_method/custom_payment_method_response.py',
    'src/fern/api/resources/payment_method/custom_payment_method_update_base_request.py',
    'src/fern/api/resources/payment_method/custom_payment_method_update_request.py',
    'src/fern/api/resources/payment_method/payment_method_request.py',
    'src/fern/api/resources/payment_method/payment_method_response.py',
    'src/fern/api/resources/payment_method/payment_method_type.py',
    'src/fern/api/resources/payment_method/payment_method_update_request.py',
    'src/fern/api/resources/payment_method_schema/__init__.py',
    'src/fern/api/resources/payment_method_schema/payment_method_schema_field.py',
    'src/fern/api/resources/payment_method_schema/payment_method_schema_field_type.py',
    'src/fern/api/resources/payment_method_schema/payment_method_schema_request.py',
    'src/fern/api/resources/payment_method_schema/payment_method_schema_response.py',
    'src/fern/api/resources/process_invoice/__init__.py',
    'src/fern/api/resources/process_invoice/process_invoice_request.py',
    'src/fern/api/resources/transaction/__init__.py',
    'src/fern/api/resources/transaction/transaction_id.py',
    'src/fern/api/resources/transaction/transaction_response.py',
    'src/fern/api/resources/transaction/transaction_response_expanded.py',
    'src/fern/api/resources/transaction/transaction_status.py'
]

snapshots['test_circular_imports src_fern_api___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api___init__.py')

snapshots['test_circular_imports src_fern_api_core___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_core___init__.py')

snapshots['test_circular_imports src_fern_api_core_datetime_utils'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_core_datetime_utils.py')

snapshots['test_circular_imports src_fern_api_resources___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources___init__.py')

snapshots['test_circular_imports src_fern_api_resources_bank_lookup___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_bank_lookup___init__.py')

snapshots['test_circular_imports src_fern_api_resources_bank_lookup_bank_address'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_bank_lookup_bank_address.py')

snapshots['test_circular_imports src_fern_api_resources_bank_lookup_bank_lookup_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_bank_lookup_bank_lookup_response.py')

snapshots['test_circular_imports src_fern_api_resources_commons___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons___init__.py')

snapshots['test_circular_imports src_fern_api_resources_commons_address'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_address.py')

snapshots['test_circular_imports src_fern_api_resources_commons_approval_policy_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_approval_policy_id.py')

snapshots['test_circular_imports src_fern_api_resources_commons_birth_date'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_birth_date.py')

snapshots['test_circular_imports src_fern_api_resources_commons_comment_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_comment_id.py')

snapshots['test_circular_imports src_fern_api_resources_commons_entity_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_entity_id.py')

snapshots['test_circular_imports src_fern_api_resources_commons_entity_user_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_entity_user_id.py')

snapshots['test_circular_imports src_fern_api_resources_commons_full_name'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_full_name.py')

snapshots['test_circular_imports src_fern_api_resources_commons_individual_government_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_individual_government_id.py')

snapshots['test_circular_imports src_fern_api_resources_commons_invoice_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_invoice_id.py')

snapshots['test_circular_imports src_fern_api_resources_commons_itin'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_itin.py')

snapshots['test_circular_imports src_fern_api_resources_commons_order_direction'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_order_direction.py')

snapshots['test_circular_imports src_fern_api_resources_commons_payment_method_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_payment_method_id.py')

snapshots['test_circular_imports src_fern_api_resources_commons_payment_method_schema_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_payment_method_schema_id.py')

snapshots['test_circular_imports src_fern_api_resources_commons_phone_number'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_phone_number.py')

snapshots['test_circular_imports src_fern_api_resources_commons_ssn'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_commons_ssn.py')

snapshots['test_circular_imports src_fern_api_resources_entity___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity___init__.py')

snapshots['test_circular_imports src_fern_api_resources_entity_account_type'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_account_type.py')

snapshots['test_circular_imports src_fern_api_resources_entity_business_profile_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_business_profile_request.py')

snapshots['test_circular_imports src_fern_api_resources_entity_business_profile_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_business_profile_response.py')

snapshots['test_circular_imports src_fern_api_resources_entity_business_type'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_business_type.py')

snapshots['test_circular_imports src_fern_api_resources_entity_ein'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_ein.py')

snapshots['test_circular_imports src_fern_api_resources_entity_entity_add_payees_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_entity_add_payees_request.py')

snapshots['test_circular_imports src_fern_api_resources_entity_entity_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_entity_request.py')

snapshots['test_circular_imports src_fern_api_resources_entity_entity_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_entity_response.py')

snapshots['test_circular_imports src_fern_api_resources_entity_entity_status'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_entity_status.py')

snapshots['test_circular_imports src_fern_api_resources_entity_entity_update_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_entity_update_request.py')

snapshots['test_circular_imports src_fern_api_resources_entity_individual_profile_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_individual_profile_request.py')

snapshots['test_circular_imports src_fern_api_resources_entity_individual_profile_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_individual_profile_response.py')

snapshots['test_circular_imports src_fern_api_resources_entity_profile_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_profile_request.py')

snapshots['test_circular_imports src_fern_api_resources_entity_profile_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_profile_response.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources___init__.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_approval_policy___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_approval_policy___init__.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_approval_policy_amount_trigger'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_approval_policy_amount_trigger.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_approval_policy_approval_policy_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_approval_policy_approval_policy_request.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_approval_policy_approval_policy_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_approval_policy_approval_policy_response.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_approval_policy_approval_policy_update_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_approval_policy_approval_policy_update_request.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_approval_policy_approver_rule'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_approval_policy_approver_rule.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_approval_policy_identifier_list'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_approval_policy_identifier_list.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_approval_policy_rule'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_approval_policy_rule.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_approval_policy_trigger'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_approval_policy_trigger.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_counterparty___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_counterparty___init__.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_counterparty_counterparty_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_counterparty_counterparty_response.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_counterparty_find_counterparties_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_counterparty_find_counterparties_response.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_invoice___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_invoice___init__.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_invoice_invoice_metrics_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_invoice_invoice_metrics_response.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_representative___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_representative___init__.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_representative_representative_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_representative_representative_id.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_representative_representative_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_representative_representative_request.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_representative_representative_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_representative_representative_response.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_representative_responsibilities'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_representative_responsibilities.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_user___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_user___init__.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_user_entity_user_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_user_entity_user_request.py')

snapshots['test_circular_imports src_fern_api_resources_entity_resources_user_entity_user_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_resources_user_entity_user_response.py')

snapshots['test_circular_imports src_fern_api_resources_entity_tax_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_entity_tax_id.py')

snapshots['test_circular_imports src_fern_api_resources_invoice___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice___init__.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_approver_action'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_approver_action.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_assigned_approver'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_assigned_approver.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_associated_approval_action'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_associated_approval_action.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_invoice_approver_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_invoice_approver_response.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_invoice_line_item_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_invoice_line_item_request.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_invoice_line_item_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_invoice_line_item_response.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_invoice_order_by_field'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_invoice_order_by_field.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_invoice_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_invoice_request.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_invoice_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_invoice_response.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_invoice_status'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_invoice_status.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_resources___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_resources___init__.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_resources_approval___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_resources_approval___init__.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_resources_approval_approval_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_resources_approval_approval_request.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_resources_comment___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_resources_comment___init__.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_resources_comment_comment_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_resources_comment_comment_request.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_resources_comment_comment_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_resources_comment_comment_response.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_resources_document___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_resources_document___init__.py')

snapshots['test_circular_imports src_fern_api_resources_invoice_resources_document_document_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_invoice_resources_document_document_response.py')

snapshots['test_circular_imports src_fern_api_resources_ocr___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_ocr___init__.py')

snapshots['test_circular_imports src_fern_api_resources_ocr_attachments'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_ocr_attachments.py')

snapshots['test_circular_imports src_fern_api_resources_ocr_email_ocr_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_ocr_email_ocr_request.py')

snapshots['test_circular_imports src_fern_api_resources_ocr_ocr_mailbox'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_ocr_ocr_mailbox.py')

snapshots['test_circular_imports src_fern_api_resources_ocr_ocr_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_ocr_ocr_response.py')

snapshots['test_circular_imports src_fern_api_resources_ocr_vendor_network'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_ocr_vendor_network.py')

snapshots['test_circular_imports src_fern_api_resources_organization___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization___init__.py')

snapshots['test_circular_imports src_fern_api_resources_organization_color_scheme_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_color_scheme_request.py')

snapshots['test_circular_imports src_fern_api_resources_organization_color_scheme_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_color_scheme_response.py')

snapshots['test_circular_imports src_fern_api_resources_organization_email_log_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_email_log_response.py')

snapshots['test_circular_imports src_fern_api_resources_organization_email_provider_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_email_provider_request.py')

snapshots['test_circular_imports src_fern_api_resources_organization_email_provider_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_email_provider_response.py')

snapshots['test_circular_imports src_fern_api_resources_organization_email_sender_provider'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_email_sender_provider.py')

snapshots['test_circular_imports src_fern_api_resources_organization_email_sender_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_email_sender_request.py')

snapshots['test_circular_imports src_fern_api_resources_organization_email_sender_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_email_sender_response.py')

snapshots['test_circular_imports src_fern_api_resources_organization_organization_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_organization_id.py')

snapshots['test_circular_imports src_fern_api_resources_organization_organization_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_organization_request.py')

snapshots['test_circular_imports src_fern_api_resources_organization_organization_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_organization_response.py')

snapshots['test_circular_imports src_fern_api_resources_organization_payment_methods_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_payment_methods_request.py')

snapshots['test_circular_imports src_fern_api_resources_organization_payment_methods_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_payment_methods_response.py')

snapshots['test_circular_imports src_fern_api_resources_organization_payment_rail_markup'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_payment_rail_markup.py')

snapshots['test_circular_imports src_fern_api_resources_organization_payment_rail_markup_type'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_payment_rail_markup_type.py')

snapshots['test_circular_imports src_fern_api_resources_organization_payment_rail_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_payment_rail_request.py')

snapshots['test_circular_imports src_fern_api_resources_organization_payment_rail_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_organization_payment_rail_response.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method___init__.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_bank_account_base_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_bank_account_base_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_bank_account_base_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_bank_account_base_response.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_bank_account_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_bank_account_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_bank_account_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_bank_account_response.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_bank_status'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_bank_status.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_bank_type'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_bank_type.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_card_base_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_card_base_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_card_base_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_card_base_response.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_card_brand'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_card_brand.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_card_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_card_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_card_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_card_response.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_card_type'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_card_type.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_check_base_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_check_base_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_check_base_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_check_base_response.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_check_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_check_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_check_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_check_response.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_currency_code'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_currency_code.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_base_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_base_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_base_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_base_response.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_response.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_update_base_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_update_base_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_update_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_custom_payment_method_update_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_payment_method_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_payment_method_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_payment_method_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_payment_method_response.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_payment_method_type'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_payment_method_type.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_payment_method_update_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_payment_method_update_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_schema___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_schema___init__.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_schema_payment_method_schema_field'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_schema_payment_method_schema_field.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_schema_payment_method_schema_field_type'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_schema_payment_method_schema_field_type.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_schema_payment_method_schema_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_schema_payment_method_schema_request.py')

snapshots['test_circular_imports src_fern_api_resources_payment_method_schema_payment_method_schema_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_payment_method_schema_payment_method_schema_response.py')

snapshots['test_circular_imports src_fern_api_resources_process_invoice___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_process_invoice___init__.py')

snapshots['test_circular_imports src_fern_api_resources_process_invoice_process_invoice_request'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_process_invoice_process_invoice_request.py')

snapshots['test_circular_imports src_fern_api_resources_transaction___init__'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_transaction___init__.py')

snapshots['test_circular_imports src_fern_api_resources_transaction_transaction_id'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_transaction_transaction_id.py')

snapshots['test_circular_imports src_fern_api_resources_transaction_transaction_response'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_transaction_transaction_response.py')

snapshots['test_circular_imports src_fern_api_resources_transaction_transaction_response_expanded'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_transaction_transaction_response_expanded.py')

snapshots['test_circular_imports src_fern_api_resources_transaction_transaction_status'] = FileSnapshot('snap_test_pydantic_model/test_circular_imports src_fern_api_resources_transaction_transaction_status.py')
