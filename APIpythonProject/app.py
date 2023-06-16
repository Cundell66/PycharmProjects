# import requests
import time

from libs.openexchange import OpenExchangeClient

APP_ID = "2b989763233e473fbf97690da32a511e"
"""
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()
"""

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end-start)

print(f'USD{usd_amount} is GBP{gbp_amount:.2f}')

gbp_amount = 1000
start = time.time()
usd_amount = client.convert(usd_amount, "GBP", "USD")
end = time.time()

print(end-start)

print(f'GBP{gbp_amount} is USD{usd_amount:.2f}')
