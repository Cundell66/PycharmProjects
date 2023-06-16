MAILGUN_API_URL,
    auth=('api', MAILGUN_API_KEY),
    data={
        'from': f'{FROM_NAME} < {FROM_EMAIL}>',
        'to': TO_EMAILS,
        'subject': SUBJECT,
        'text': CONTENT
    }
