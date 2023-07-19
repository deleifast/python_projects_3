from escpos.printer import Usb


# Adapt to your needs
p = Usb(0x04b8, 0x0e03)

# Print software and then hardware barcode with the same content
p.soft_barcode('code39', '123456')
p.text('\n')
p.text('\n')
p.barcode('123456', 'CODE39')