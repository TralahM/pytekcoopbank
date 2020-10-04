"""Cooperative Bank of Kenya Python SDK."""
from .accounts import (
    AccountBalance,
    AccountTransactions,
    AccountValidation,
    AccountMiniStatement,
    AccountFullStatement,
)
from .mpesa import AccountToMpesa
from .pesalink import (
    PesaLinkToAccount,
    PesaLinkToPhone,
)
from .ift import IFTAccountToAccount
from .transactions import TransactionStatus
from .exchange_rate import ExchangeRate


class CoopBank:
    """CoopBank Singleton Class."""

    balance = None
    transactions = None
    validation = None
    mini_statement = None
    full_statement = None
    to_mpesa = None
    ift_to_account = None
    transaction_status = None
    exchange_rate = None
    pesalink_to_account = None
    pesalink_to_phone = None


def setup_coop(config: dict):
    """Initialize and Return Singleton Class Coop Using Given config."""
    CoopBank.balance = AccountBalance(config)
    CoopBank.transactions = AccountTransactions(config)
    CoopBank.validation = AccountValidation(config)
    CoopBank.mini_statement = AccountMiniStatement(config)
    CoopBank.full_statement = AccountFullStatement(config)
    CoopBank.to_mpesa = AccountToMpesa(config)
    CoopBank.ift_to_account = IFTAccountToAccount(config)
    CoopBank.transaction_status = TransactionStatus(config)
    CoopBank.exchange_rate = ExchangeRate(config)
    CoopBank.pesalink_to_account = PesaLinkToAccount(config)
    CoopBank.pesalink_to_phone = PesaLinkToPhone(config)
    return CoopBank
