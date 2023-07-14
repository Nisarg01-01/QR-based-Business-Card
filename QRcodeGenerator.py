import qrcode
import cv2

# Personal Details to be stored in QR code
fname = "Tejas"
lname = "Mehta"
designation = "Dy. Manager Digitalization"
company = "Linde Enigneering India Pvt. Ltd."
phone = "8306206161"
email = "tejas.mehta@linde.com"
address = "\"Linde House\", Near Nilamber Circle, Vasna Gotri Road, Vasna, Vadodara- 391 410, Gujarat, India"

# creare a string to store data in url as query string
data = "fname="+fname+"&lname="+lname+"&designation="+designation+"&company="+company+"&phone="+phone+"&email="+email+"&address="+address

# encode it with pybase64
import pybase64
data = pybase64.b64encode(data.encode("ascii")).decode("ascii")

# create a QR code
qrCode=qrcode.make('https://nisarg01-01.github.io/QR-based-Business-Card/?data='+data,
                   box_size=10, # size of each box in pixels
                   border=5, # thickness of border in box
                   error_correction=qrcode.constants.ERROR_CORRECT_M # error correction level of QR code M = 15% error correction
                   )

# save the QR code in png format
qrCode.save('D:\\Codes\\Projects\\QR-based-Business-Card\\MyLink.png')
