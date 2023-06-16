import http.client

conn = http.client.HTTPSConnection("ecomjunkie.ipzmarketing.com")

payload = '''{
        "from": {
            "email": "info@ecomjunkie.com",
            "name": "string"
          },
          "to": [
            {
              "email": "paul@stonefallsales.com",
              "name": "string"
            }
          ],
          "subject": "Test Email",
          "html_part": "<html>\n<head></head>\n<body><p>Test HTML</p></body>\n</html>\n",
          "text_part": "Test Text",
          "text_part_auto": true,
          "headers": {
            "X-CustomHeader": "Header value"
          },
          "smtp_tags": [
            "string"
          ],
        }
 '''
headers = {
    'content-type': "application/json",
    'x-auth-token': "26uaMGK238FGGqsvLQmJxzvBDxExkNwz5QsZXjQC"
    }

conn.request("POST", "/api/v1/send_emails", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
