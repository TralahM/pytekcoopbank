"""
Account Send to Mpesa  subclass of Bank.
"""
import requests
from . import bank


class AccountToMpesa(bank.Bank):
    """Facilitate External Account To MPESA Funds Transfer."""

    def send(
        self,
        messageReference,
        mobileNumber,
        amount,
        transactionCurrency="KES",
        narration="Payment",
        destinations=[
            {
                "ReferenceNumber": None,
                "MobileNumber": None,
                "Amount": None,
                "Narration": None,
            },
        ],
        callback=None,
    ):
        token = self.token
        url = self.host + "/FundsTransfer/External/A2M/Mpesa/v1.0.0"
        adestinations = []
        for dest in destinations:
            if not dest.get("MobileNumber"):
                dest["MobileNumber"] = mobileNumber
            if not dest.get("Amount"):
                dest["Amount"] = amount
            if not dest.get("ReferenceNumber"):
                dest["ReferenceNumber"] = messageReference
            if not dest.get("Narration"):
                dest["Narration"] = narration
            adestinations.append(dest)

        payload = {
            "MessageReference": messageReference,
            "CallBackUrl": self.config.get("callback_url"),
            "Source": {
                "AccountNumber": self.config.get("accountNumber"),
                "Amount": amount,
                "TransactionCurrency": transactionCurrency,
                "Narration": narration,
            },
            "Destinations": adestinations,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.post(url, headers=headers, data=payload,verify=False)
        if callback is not None:
            return callback(response)
        else:
            return response
