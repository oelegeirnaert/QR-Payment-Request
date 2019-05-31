
from payment import PaymentRequest
import pytest
import os

from custom_exceptions import *

pr = PaymentRequest()

def resetPaymentRequest():
    pr.iban = "BE24651151080738"
    pr.remittanceInfo = "Free Reference"
    pr.creditorReference = ""
    pr.amount = 10
    pr.billerName = "Oele Geirnaert"

def test_no_biller_name():
    resetPaymentRequest()
    pr.billerName = ""
    with pytest.raises(BillerNameError) as target:
        pr.is_valid()

def test_invalid_iban():
    resetPaymentRequest()
    pr.iban = "invalidiban"
    with pytest.raises(Exception) as e_info:
        print(e_info)
        pr.is_valid()

def test_invalid_amount():
    resetPaymentRequest()
    pr.amount = 0
    with pytest.raises(AmountError) as target:
        pr.is_valid()

def test_structured_or_free_reference():
    resetPaymentRequest()
    pr.remittanceInfo = "Free Reference"
    pr.creditorReference = "Structured Reference"
    with pytest.raises(FreeOrStructuredReferenceError) as target:
        pr.is_valid()

def test_full_valid_payment_request():
    resetPaymentRequest()
    assert pr.is_valid() == True

def test_qr_code_generation():
    resetPaymentRequest()
    file = pr.generate_qr_code()
    assert os.path.isfile(file)
