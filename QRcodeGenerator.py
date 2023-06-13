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

# Add data to qrcode
qrCode=qrcode.make('http://127.0.0.1:5500/index.html?data='+data, version=1, box_size=10, border=5)
qrCode.save('D:\\Codes\\Projects\\Business-Card\\MyLink.png')