from datetime import datetime
from datetime import timedelta

today_date = datetime.today().strftime("%d/%m/%Y")
future_date = (datetime.now() + timedelta(days=5) ).strftime('%d-%m-%y')
past_date = (datetime.now() + timedelta(days=-3) ).strftime('%d-%m-%y')

print("Now : " + today_date)
print("future: " + future_date)
print("past: " + past_date)

create_order_payload = {
  "marketDirection": "buy",
  "currency": "EUR",
  "amount": "250200.20",
  "counterCurrency": "USD",
  "beneficiaryAccountRef":"BA-LV455BK5B",
  "valueDate": today_date
}

create_order_past_payload = {
  "marketDirection": "buy",
  "currency": "EUR",
  "amount": "250200.20",
  "counterCurrency": "USD",
  "beneficiaryAccountRef":"BA-LV455BK5B",
  "valueDate": past_date
}

create_order_future_payload = {
  "marketDirection": "buy",
  "currency": "EUR",
  "amount": "250200.20",
  "counterCurrency": "USD",
  "beneficiaryAccountRef":"BA-LV455BK5B",
  "valueDate": future_date
}
orders_quote_payload = {
  "marketDirection": "buy",
  "currency": "EUR",
  "amount": "250200.20",
  "counterCurrency": "USD",
  "valueDate": "02/11/2018"
}

empty_body = {}

missing_required_field = {
  "marketDirection": "buy",
  "amount": "250200.20",
  "counterCurrency": "USD",
  "valueDate": "02/11/2024"
}

get_company_orders_body = {"currency": "USD",
"marketDirection": "buy",
"counterCurrency": "GBP"
}

