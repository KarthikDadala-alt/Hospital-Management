{
    'name': "Dental Hospital Management",
    'description': """
        Comprehensive dental hospital management system for handling
        patients, appointments, doctors, treatments, prescriptions,
        billing, and overall clinical workflows.
    """,
    'summary': """
        Full-featured dental clinic management module for Odoo 18.
    """,
    'author': "Karthik Dadala",
    'company': "Open Source Community",
    'maintainer': "Karthik Dadala",
    'website': "https://github.com/karthikdadala",
    'license': "LGPL-3",
    'category': 'Healthcare',
    'version': '18.0.1.0.0',
    'depends': [
        'base',
        'hr',
        'account',
        'sale',
        'product',
        'web',
        'stock',
    ],
    'data': [
        'data/patient_id_sequence.xml',
        'data/dental_specialist_data.xml',
        'data/treatment_category_data.xml',
        'data/dental_treatment_data.xml',
        'data/dental_time_shift_data.xml',
        'data/medicine_frequency_data.xml',

        'views/patient_view.xml',
        'views/dental_appointment_views.xml',
        'views/dental_doctor_views.xml',
        'views/dental_prescription_views.xml',
        'views/dental_payment_log_views.xml',
        'views/teeth_chart_views.xml',
        'views/dental_treatment_views.xml',
        'views/treatment_category_views.xml',
        'views/medicine_frequency_views.xml',
        'views/dental_medicine_views.xml',
        'views/medical_questions_views.xml',
        'views/dental_specialist_views.xml',
        'views/dental_time_shift_views.xml',

        'report/dental_prescription_report.xml',
        'report/dental_prescription_templates.xml',

        'security/ir.model.access.csv',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
