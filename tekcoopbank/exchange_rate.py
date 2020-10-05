"""
Exchange Rate subclass of Bank.
"""
import requests
from . import bank


class ExchangeRate(bank.Bank):
    def send(
        self,
        messageReference,
        fromCurrencyCode="KES",
        toCurrencyCode="USD",
        callback=None,
    ):
        token = self.token
        url = self.host + "/Enquiry/ExchangeRate/1.0.0"
        payload = {
            "MessageReference": messageReference,
            "FromCurrencyCode": fromCurrencyCode,
            "ToCurrencyCode": toCurrencyCode,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.post(url, headers=headers, json=payload,verify=False)
        if callback is not None:
            return callback(response)
        else:
            return response
