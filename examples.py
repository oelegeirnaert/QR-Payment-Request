import payment
from PIL import Image

pr = payment.PaymentRequest()
pr.amount = 0.1
pr.billerName = "Oele Geirnaert"
pr.iban = "BE24651151080738"
pr.remittanceInfo = "Python Payment - Thank you for your contribution"

if pr.is_valid():
    generated_qr_image_with_branding = pr.generate_qr_code(custom_filename = "qr_with_branding", crop = False)
    img = Image.open(generated_qr_image_with_branding)
    img.show()

    generated_qr_image_without_branding = pr.generate_qr_code(custom_filename = "qr_without_branding", crop = True)
    img = Image.open(generated_qr_image_without_branding)
    img.show()
