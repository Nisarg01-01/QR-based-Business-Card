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

# encode it with pybase64
import pybase64
data = pybase64.b64encode(data.encode("ascii")).decode("ascii")

qrCode=qrcode.make('https://nisarg01-01.github.io/QR-based-Business-Card/?data='+data, version=1, box_size=10, border=5)
print("https://nisarg01-01.github.io/QR-based-Business-Card/?data="+data)
qrCode.save('D:\\Codes\\Projects\\QR-based-Business-Card\\MyLink.png')