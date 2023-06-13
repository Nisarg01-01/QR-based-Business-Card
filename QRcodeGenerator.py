import qrcode
import cv2

name = "Nisarg"
designation = "Intern at digitalization"
phone = "8849904363"
email = "nisargshah@gmail.com"
address = "Vadodara,Gujarat"

# creare a string to store data in url format
data = "name="+name+"&designation="+designation+"&phone="+phone+"&email="+email+"&address="+address

# encode it with pybase64
import pybase64
data = pybase64.b64encode(data.encode("ascii")).decode("ascii")

qrCode=qrcode.make('https://nisarg01-01.github.io/QR-based-Business-Card/?data='+data, version=1, box_size=10, border=5)
qrCode.save('D:\\Codes\\Projects\\QR-based-Business-Card\\MyLink.png')