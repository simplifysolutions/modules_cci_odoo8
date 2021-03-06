{
    "name" : "CCI Salesman",
    "version" : "1.2",
    "author" : "PCSOL",
    "category" : "Profile",
    "website": "http://www.pcsol.be",
    "description": """CCI Salesman""",
    "depends" : ['base', 'base_contact', 'product','crm', 'account'],
    "data" : [
            'security/security.xml',
            'security/ir.model.access.csv',
            'wizard/partner_interest_order.xml',
            'cci_salesman_wizard.xml',
            'wizard/partner_interest_next.xml',
            'wizard/interest_archive.xml',
            'wizard/create_histo_from_interest_view.xml',
            'wizard/create_histo_from_mark_view.xml',
            'wizard/create_interests_wizard_view.xml',
            'wizard/extra_actions_wizard_view.xml',
            'wizard/extract_comm_results_view.xml',
            'wizard/extract_commissions_wizard_view.xml',
            'wizard/extract_pipeline_wizard_view.xml',
            'wizard/get_cci_product_turnover_view.xml',
            'wizard/get_todos_wizard.xml',
            'wizard/interest_archive.xml',
            'wizard/partner_interest_next.xml',
            'wizard/partner_interest_order.xml',
            'crm_data.xml',
            'partner_view.xml',
            'users_view.xml',
            
            ],
    "auto_install": False,
    "installable": True
}
