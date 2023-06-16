import requests


class Mailgun:
    MAILGUN_API_URL = 'https://api.mailgun.net/v3/sandboxca10adb917df4a688faedf4bd3c1e285.mailgun.org/messages'
    MAILGUN_API_KEY = '4efb77e663f5f8179b111303813cb677-70c38fed-f1851c13'

    FROM_NAME = 'Paul'
    FROM_EMAIL = 'sales@sandboxca10adb917df4a688faedf4bd3c1e285.mailgun.org'

    @classmethod
    def send_email(cls, to_emails, subject, content):
        requests.post(
            cls.MAILGUN_API_URL,
            auth=('api', cls.MAILGUN_API_KEY),
            data={
                'from': f'{cls.FROM_NAME} < {cls.FROM_EMAIL}>',
                'to': to_emails,
                'subject': subject,
                'text': content
            })
