import requests

MAILGUN_API_URL = 'https://ecomjunkie.ipzmarketing.com/api/v1/send_emails'
MAILGUN_API_KEY = '26uaMGK238FGGqsvLQmJxzvBDxExkNwz5QsZXjQC'


FROM_NAME = 'Paul'
FROM_EMAIL = 'info@ecomjunkie.com'

TO_EMAILS = ['paul@stonefallmarketing.com']
SUBJECT = 'Test Email'
CONTENT = """
Dear Paul,

This is a mailrelay email sent by Python.

    Bloody good innit?

Cheers
        Paul
"""

requests.post(
    MAILGUN_API_URL,
    auth=('api', MAILGUN_API_KEY),
    data={
        'from': f'{FROM_NAME} < {FROM_EMAIL}>',
        'to': TO_EMAILS,
        'subject': SUBJECT,
        'text': CONTENT
    }
)
