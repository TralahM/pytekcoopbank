"""Accounts Module.

Defines the following Classes as subclasses of bank.Bank:
AccountBalance,
AccountTransactions,
AccountMiniStatement,
AccountFullStatement,
AccountValidation
"""
import requests
from . import bank


class AccountBalance(bank.Bank):
    def send(self, messageReference, accountNumber, callback=None):
        token = self.token
        url = self.host + "/Enquiry/AccountBalance/1.0.0"
        payload = {
            "MessageReference": messageReference,
            "AccountNumber": accountNumber,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.post(url, headers=headers,
                                 json=payload, verify=False)
        if callback is not None:
            return callback(response)
        else:
            return response


class AccountMiniStatement(bank.Bank):
    def send(self, messageReference, accountNumber, callback=None):
        token = self.token
        url = self.host + "/Enquiry/MiniStatement/Account/1.0.0"
        payload = {
            "MessageReference": messageReference,
            "AccountNumber": accountNumber,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.post(url, headers=headers,
                                 json=payload, verify=False)
        if callback is not None:
            return callback(response)
        else:
            return response


class AccountFullStatement(bank.Bank):
    def send(self, messageReference, accountNumber, callback=None):
        token = self.token
        url = self.host + "/Enquiry/FullStatement/Account/1.0.0"
        payload = {
            "MessageReference": messageReference,
            "AccountNumber": accountNumber,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.post(url, headers=headers,
                                 json=payload, verify=False)
        if callback is not None:
            return callback(response)
        else:
            return response


class AccountValidation(bank.Bank):
    def send(self, messageReference, accountNumber, callback=None):
        token = self.token
        url = self.host + "/Enquiry/Validation/Account/1.0.0"
        payload = {
            "MessageReference": messageReference,
            "AccountNumber": accountNumber,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.post(url, headers=headers,
                                 json=payload, verify=False)
        if callback is not None:
            return callback(response)
        else:
            return response


class AccountTransactions(bank.Bank):
    def send(self, messageReference, accountNumber, NoOfTransactions=1, callback=None):
        token = self.token
        url = self.host + "/Enquiry/AccountTransactions/1.0.0"
        payload = {
            "MessageReference": messageReference,
            "AccountNumber": accountNumber,
            "NoOfTransactions": NoOfTransactions,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.post(url, headers=headers,
                                 json=payload, verify=False)
        if callback is not None:
            return callback(response)
        else:
            return response
