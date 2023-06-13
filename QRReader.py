import cv2

# Decode same img and open link in browser
img=cv2.imread('D:\\Codes\\Projects\\Business-Card\\MyLink.png')
cv2.waitKey(0)
detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# open link in browser
import webbrowser
webbrowser.open(data)