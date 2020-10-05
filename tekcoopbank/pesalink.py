"""
Pesalink Send to Account  subclass of Bank.
"""
import requests
from . import bank


class PesaLinkToAccount(bank.Bank):
    """Facilitate External PesaLink To Account Funds Transfer."""

    def send(
        self,
        messageReference,
        accountNumber,
        amount,
        transactionCurrency="KES",
        narration="Payment",
        destinations=[
            {
                "ReferenceNumber": None,
                "AccountNumber": None,
                "BankCode": None,
                "Amount": None,
                "TransactionCurrency": None,
                "Narration": None,
            },
        ],
        callback=None,
    ):
        token = self.token
        url = self.host + "/FundsTransfer/External/A2A/PesaLink/1.0.0"
        adestinations = []
        for dest in destinations:
            if not dest.get("AccountNumber"):
                dest["AccountNumber"] = accountNumber
            if not dest.get("BranchCode"):
                dest["BranchCode"] = self.config.get("BranchCode")
            if not dest.get("BankCode"):
                dest["BankCode"] = self.config.get("BankCode")
            if not dest.get("Amount"):
                dest["Amount"] = amount
            if not dest.get("ReferenceNumber"):
                dest["ReferenceNumber"] = messageReference
            if not dest.get("TransactionCurrency"):
                dest["TransactionCurrency"] = transactionCurrency
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


class PesaLinkToPhone(bank.Bank):
    """Facilitate External Pesalink To Phone Funds Transfer."""

    def send(
        self,
        messageReference,
        phoneNumber,
        amount,
        transactionCurrency="KES",
        narration="Payment",
        destinations=[
            {
                "ReferenceNumber": None,
                "PhoneNumber": None,
                "Amount": None,
                "TransactionCurrency": None,
                "Narration": None,
            },
        ],
        callback=None,
    ):
        token = self.token
        url = self.host + "/FundsTransfer/External/A2M/PesaLink/1.0.0"
        adestinations = []
        for dest in destinations:
            if not dest.get("PhoneNumber"):
                dest["PhoneNumber"] = phoneNumber
            if not dest.get("Amount"):
                dest["Amount"] = amount
            if not dest.get("ReferenceNumber"):
                dest["ReferenceNumber"] = messageReference
            if not dest.get("TransactionCurrency"):
                dest["TransactionCurrency"] = transactionCurrency
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
        response = requests.post(url, headers=headers, data=payload)
        if callback is not None:
            return callback(response)
        else:
            return response
