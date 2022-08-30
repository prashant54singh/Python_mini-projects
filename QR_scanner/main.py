import qrcode

from PIL import Image


choice=input('Press 1 for encode a text or 2 for decode\n')

if choice == '1':
    data = input("Enter a string to encode\n")

    # img=qrcode.make(data)
    qr = qrcode.QRCode(version=1, box_size=10, border=1)
    qr.add_data(data)

    qr.make(fit=True)
    img=qr.make_image(fill_color = input("Enter QR color\n"),back_color = input("Enter background color\n"))

    img.save('D:/SKILL/python_proj/QR_scanner/my_QR.png')


elif choice == '2':
    from pyzbar.pyzbar import decode
    img= Image.open('D:/SKILL/python_proj/QR_scanner/my_QR.png')
    result = decode(img)
    print(result)

else:
    print("You chose something wrong \n")

