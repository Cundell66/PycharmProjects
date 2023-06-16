import requests

MAILGUN_API_URL = 'https://api.mailgun.net/v3/sandboxca10adb917df4a688faedf4bd3c1e285.mailgun.org/messages'
MAILGUN_API_KEY = '4efb77e663f5f8179b111303813cb677-70c38fed-f1851c13'

MAILJET_API_URL = 'https://api.mailjet.com/'
MAILJET_API_SECRET_KEY = '485766034816b49bfc73f3cd5fbb5904'
MAILJET_API_KEY = '29fef8387f726c233df8223bf7951122'


FROM_NAME = 'Paul'
FROM_EMAIL = 'sales@sandboxca10adb917df4a688faedf4bd3c1e285.mailgun.org'

TO_EMAILS = ['paul@stonefallworld.com']
SUBJECT = 'Test Email'
CONTENT = """
Dear Paul,

This is a mailgun email sent by Python.

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
