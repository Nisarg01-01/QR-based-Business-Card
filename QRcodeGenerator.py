import qrcode
import cv2

name = "Nisarg"
designation = "Intern at digitalization"
company = "Linde Enigneering India Pvt. Ltd."
phone = "8849904363"
email = "nisargshah@gmail.com"
address = "Linde House, Near Nilamber Circle, Vasna Gotri Road, Vasna, Vadodara- 391 410, Gujarat, India"

# creare a string to store data in url format
data = "name="+name+"&designation="+designation+"&company="+company+"&phone="+phone+"&email="+email+"&address="+address
print(data)

# encode it with pybase64
import pybase64
data = pybase64.b64encode(data.encode("ascii")).decode("ascii")

qrCode=qrcode.make('https://nisarg01-01.github.io/QR-based-Business-Card/?data='+data, version=1, box_size=10, border=5)
qrCode.save('D:\\Codes\\Projects\\QR-based-Business-Card\\MyLink.png')
# print with local host url
print('http://127.0.0.1:5500/index.html?data='+data)