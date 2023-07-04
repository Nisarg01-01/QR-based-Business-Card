import qrcode
import cv2

fname = "Tejas"
lname = "Mehta"
designation = "Dy. Manager Digitalization"
company = "Linde Enigneering India Pvt. Ltd."
phone = "8306206161"
email = "tejas.mehta@linde.com"
address = "\"Linde House\", Near Nilamber Circle, Vasna Gotri Road, Vasna, Vadodara- 391 410, Gujarat, India"

# creare a string to store data in url format with first name, last name, fullname, designation, company, phone, email, address
data = "fname="+fname+"&lname="+lname+"&designation="+designation+"&company="+company+"&phone="+phone+"&email="+email+"&address="+address

# encode it with pybase64
import pybase64
data = pybase64.b64encode(data.encode("ascii")).decode("ascii")

qrCode=qrcode.make('https://nisarg01-01.github.io/QR-based-Business-Card/?data='+data, version=1, box_size=10, border=5, error_correction=qrcode.constants.ERROR_CORRECT_M)
qrCode.save('D:\\Codes\\Projects\\QR-based-Business-Card\\MyLink.png')
# save the qrcode in svg format
# qrCode.save('D:\\Codes\\Projects\\QR-based-Business-Card\\MyLink.svg')
