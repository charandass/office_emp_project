mystr = {"code":0,"message":"The contact has been added.","contact":{"contact_id":"3674599000000090033","contact_name":"mohit","company_name":"mohit","first_name":"","last_name":"","designation":"","department":"","website":"","is_bcy_only_contact":True,"is_credit_limit_migration_completed":False,"language_code":"","language_code_formatted":"","contact_salutation":"","email":"","phone":"","mobile":"","portal_status":"disabled","is_client_review_asked":False,"has_transaction":False,"contact_type":"customer","customer_sub_type":"business","owner_id":"","owner_name":"","source":"api","documents":[],"twitter":"","facebook":"","is_crm_customer":False,"is_linked_with_zohocrm":False,"primary_contact_id":"","zcrm_account_id":"","zcrm_contact_id":"","crm_owner_id":"","payment_terms":0,"payment_terms_label":"Due On Receipt","credit_limit_exceeded_amount":0.00,"currency_id":"3674599000000000097","currency_code":"USD","currency_symbol":"$","price_precision":2,"exchange_rate":"","can_show_customer_ob":True,"can_show_vendor_ob":True,"opening_balance_amount":0.00,"opening_balance_amount_bcy":"","outstanding_ob_receivable_amount":0.00,"outstanding_ob_payable_amount":0.00,"outstanding_receivable_amount":0.00,"outstanding_receivable_amount_bcy":0.00,"outstanding_payable_amount":0.00,"outstanding_payable_amount_bcy":0.00,"unused_credits_receivable_amount":0.00,"unused_credits_receivable_amount_bcy":0.00,"unused_credits_payable_amount":0.00,"unused_credits_payable_amount_bcy":0.00,"unused_retainer_payments":0.00,"status":"active","payment_reminder_enabled":True,"is_sms_enabled":True,"is_consent_agreed":False,"consent_date":"","is_client_review_settings_enabled":False,"custom_fields":[],"custom_field_hash":{},"track_1099":False,"tax_id_type":"","tax_id_value":"","contact_category":"","sales_channel":"direct_sales","ach_supported":False,"portal_receipt_count":0,"opening_balances":[],"billing_address":{"address_id":"3674599000000090035","attention":"","address":"","street2":"","city":"","state_code":"","state":"","zip":"","country":"","country_code":"","phone":"","fax":""},"shipping_address":{"address_id":"3674599000000090037","attention":"","address":"","street2":"","city":"","state_code":"","state":"","zip":"","country":"","country_code":"","phone":"","fax":"","latitude":"","longitude":""},"contact_persons":[],"addresses":[],"pricebook_id":"","pricebook_name":"","default_templates":{"invoice_template_id":"","invoice_template_name":"","bill_template_id":"","bill_template_name":"","estimate_template_id":"","estimate_template_name":"","creditnote_template_id":"","creditnote_template_name":"","purchaseorder_template_id":"","purchaseorder_template_name":"","salesorder_template_id":"","salesorder_template_name":"","retainerinvoice_template_id":"","retainerinvoice_template_name":"","paymentthankyou_template_id":"","paymentthankyou_template_name":"","retainerinvoice_paymentthankyou_template_id":"","retainerinvoice_paymentthankyou_template_name":"","invoice_email_template_id":"","invoice_email_template_name":"","estimate_email_template_id":"","estimate_email_template_name":"","creditnote_email_template_id":"","creditnote_email_template_name":"","purchaseorder_email_template_id":"","purchaseorder_email_template_name":"","salesorder_email_template_id":"","salesorder_email_template_name":"","retainerinvoice_email_template_id":"","retainerinvoice_email_template_name":"","paymentthankyou_email_template_id":"","paymentthankyou_email_template_name":"","payment_remittance_email_template_id":"","payment_remittance_email_template_name":"","retainerinvoice_paymentthankyou_email_template_id":"","retainerinvoice_paymentthankyou_email_template_name":""},"associated_with_square":False,"cards":[],"checks":[],"bank_accounts":[],"vpa_list":[],"notes":"","created_time":"2022-11-29T06:08:33-0500","created_date":"29 Nov 2022","created_by_name":"Manoj Y.","last_modified_time":"2022-11-29T06:08:33-0500","tags":[],"zohopeople_client_id":"","customer_currency_summaries":[{"currency_id":"3674599000000000097","currency_code":"USD","currency_symbol":"$","price_precision":2,"is_base_currency":True,"currency_name_formatted":"USD- United States Dollar","outstanding_receivable_amount":0.00,"unused_credits_receivable_amount":0.00}]}}
print(type(mystr))

res = mystr['contact']['contact_id']
print(res)

# splitByComma=mystr.split(':')
# fValue = splitByComma[1].replace("access_token", '').strip()
# # fValue.index()
# token = fValue.split(',')
# final_value = token[0].replace("api_domain",'').strip()
# stripped_string = final_value.strip('"')
# replaced_string = final_value.replace('"',"")