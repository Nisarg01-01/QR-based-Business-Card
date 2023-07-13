function generateQRCode() {
    // Import the necessary libraries
    const QRCode = require('qrcode');
    const fs = require('fs');
  
    // Define the data for the QR code
    const fname = "Tejas";
    const lname = "Mehta";
    const designation = "Dy. Manager Digitalization";
    const company = "Linde Enigneering India Pvt. Ltd.";
    const phone = "8306206161";
    const email = "tejas.mehta@linde.com";
    const address = "\"Linde House\", Near Nilamber Circle, Vasna Gotri Road, Vasna, Vadodara- 391 410, Gujarat, India";
  
    // Create a string to store data in URL format
    const data = `fname=${fname}&lname=${lname}&designation=${designation}&company=${company}&phone=${phone}&email=${email}&address=${address}`;
    // const data = `fname=${fname}&lname=${lname}&designation=${designation}&company=${company}&phone=${phone}&email=${email}`;
      
    // Generate the QR code
    QRCode.toFile('MyLinkJS2.png', `https://nisarg01-01.github.io/QR-based-Business-Card/?data=${encodeURIComponent(data)}`, {
      errorCorrectionLevel: 'M',
      scale: 10,
      margin: 5
    }, function (err) {
      if (err) throw err;
      console.log('QR code generated successfully!');
    });
  }
  
  // Call the function to generate the QR code
  generateQRCode();
  
