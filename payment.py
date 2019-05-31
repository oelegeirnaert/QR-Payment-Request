#https://app.digiteal.eu/papi/image-request/slip-image-anonymous-inline?iban=BE24651151080738&billerName=Oele%20Geirnaert&amount=0.10&remittanceInfo=Test&format=qr&language=nl&requestorEmail=oelegeirnaert%40hotmail.com
import requests, json, base64, sys, time
from schwifty import IBAN
from PIL import Image
from io import BytesIO

from custom_exceptions import *

class RequestAnswer():
    def __init__(self):
        self.status = ""
        self.image = ""

class PaymentRequest():
    def __init__(self):
        self.billerName = ""
        self.bic = ""
        self.iban = ""
        self.amount = 0
        self.creditorReference = ""
        self.remittanceInfo = ""
        self.requestorEmail = ""
        self.info = ""
        self.dueDate = ""
        self.format = "qr"
        self.language = ""
        self.purpose = ""

    def is_valid(self):

        IBAN(self.iban, allow_invalid=False)

        if len(self.billerName) <= 0:
            raise BillerNameError ("Please provide a name for the person that will receive the payment")

        if len(self.creditorReference) > 0 and len(self.remittanceInfo) > 0:
            raise FreeOrStructuredReferenceError ("Please choose one of both: Structured Reference or Free Text Reference.")

        if self.amount <= 0:
            raise AmountError("Please provide an amount greater than zero.")

        return True

    def generate_qr_code(self, custom_filename = None, crop = False):

        filename = self.filename()
        if not custom_filename is None:
            filename = custom_filename

        filename = "%s.jpg" %filename

        query_parameters = self.__dict__
        r = requests.get("https://app.digiteal.eu/papi/image-request/slip-image-anonymous-inline", params=query_parameters)
        ra = RequestAnswer()
        ra.__dict__ = json.loads(r.text)

        if ra.status == "0":
            imgdata = base64.b64decode(ra.image)
            if crop:
                img = Image.open(BytesIO(imgdata))
                w, h = img.size
                img = img.crop((50, 50, w-50, h-50))
                with BytesIO() as output:
                    img.save(output, format="jpeg")
                    imgdata = output.getvalue()


            with open(filename, 'wb') as f:
                f.write(imgdata)
                return filename
        else:
            print("An error occured!")
            print(r.text)

    def filename(self):
        my_filename = "%s_%s_EUR%s_%s" %(self.billerName, self.iban, self.amount, time.time())
        return my_filename.replace(" ", "_")
