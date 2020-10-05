""" Bank Module.

Bank Module Representing a Cooperative Bank.
"""
import base64
import requests


class Bank:
    def __init__(self, config: dict):
        """Config should be.

        dict(
            "env"                 = "sandbox",
            "consumerKey"         = "ss0sD2ANhjvhx_rHU0a6Xf8ROdYa",
            "consumerSecret"      = "zOfReXCIwn1TfnEYJJJGNP6l3Tka",
            "accountNumber"       = "54321987654321",
            "bankCode"            = "011",
            "branchCode"          = "00011001",
            "callbackURL"         = "/coop/callback",
            "transactionCurrency" = "KES",
        )
        """
        self.config = config
        if self.config.get("env") == "sandbox":
            self.host = "https://developer.co-opbank.co.ke:8280"
            # self.host = "https://developer.co-opbank.co.ke:8243"
        else:
            self.host = "https://developer.co-opbank.co.ke:8280"

    @property
    def token(self):
        """Return the access token after authentication."""
        authorization = base64.b64encode(
            bytes(
                self.config.get("consumerKey")
                + ":"
                + self.config.get("consumerSecret"),
                "utf8",
            )
        )
        url = self.host + "/token"
        payload = {"grant_type": "client_credentials"}
        headers = {
            "Authorization": f"Basic {authorization}",
        }
        response = requests.post(
            url, data=payload, headers=headers, verify=False)
        try:
            return response.json().get("access_token")
        except Exception:
            return response
