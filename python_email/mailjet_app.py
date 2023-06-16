import os

from mailjet_rest import Client

api_key = os.environ['MJ_APIKEY_PUBLIC']
api_secret = os.environ['MJ_APIKEY_PRIVATE']
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "paul@stonefallworld.com",
        "Name": "Paul"
      },
      "To": [
        {
          "Email": "paul@stonefallmarketing.com",
          "Name": "Stonefall Marketing"
        }
      ],
      "Subject": "My first Mailjet Email!",
      "TextPart": "Greetings from Mailjet!",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3>"
                  "<br />May the delivery force be with you!"
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())


FROM_NAME = 'Paul'
FROM_EMAIL = 'paul@sandboxca10adb917df4a688faedf4bd3c1e285.mailgun.org'

TO_EMAILS = ['paul@stonefallworld.com']
SUBJECT = 'Test Email'
CONTENT = """
Dear Paul,

This is a mailgun email sent by Python.

    Bloody good innit?

Cheers
        Paul
"""
