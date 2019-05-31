# Python Payment Request QR Generator

[![Buy me a coffee](https://www.buymeacoffee.com/assets/img/custom_images/black_img.png)](http://buymeacoff.ee/oelegeirnaert)

This project will help you generate a QR code for a payment request making use of http://scan2pay.info

Scan one of the following QR Codes to see the result.

![Alt text](qr_examples/qr_with_branding.jpg?raw=true "QR With Branding")

![Alt text](qr_examples/qr_without_branding.jpg?raw=true "QR Without Branding")

It will open your banking app and request you to pay.

1. Create a payment request.
2. Check if all the information is correct
3. Generate the QR code.

## Code Example:

```
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
```

### Prerequisites

You need to install the following modules: Pillow & Schwifty:
```
pip install Pillow
pip install schwifty
```

## Authors

* **Oele Geirnaert** - *Initial work* - (https://github.com/oelegeirnaert)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is free to use!
