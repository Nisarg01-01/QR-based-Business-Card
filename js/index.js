// onload function to call the display data function
window.onload = function() { 
    DisplayData();  
}

// variables to store the data
let fullname;
let designation;
let company;
let phone;
let email;
let address;

// encode the data to be passed in the url

function GetCurrentUrl() {
    var url = window.location.href;
    console.log(url);

    // get url parameters
    var urlParams = new URLSearchParams(window.location.search);
    console.log(urlParams);

    // decode the data
    data = urlParams.get('data');
    data = atob(data);

    // assign the data to the variables 
    fname = data.split('&')[0].split('=')[1];
    lname = data.split('&')[1].split('=')[1];
    fullname = fname+" "+lname;
    designation = data.split('&')[2].split('=')[1];
    company = data.split('&')[3].split('=')[1];
    phone = data.split('&')[4].split('=')[1];
    email = data.split('&')[5].split('=')[1];
    address = data.split('&')[6].split('=')[1];
}

//  function to display the data
function DisplayData(){
    GetCurrentUrl();
    document.getElementById("name").innerHTML = fullname;
    document.getElementById("designation").innerHTML = designation;
    document.getElementById("company").innerHTML = company;
    document.getElementById("address").innerHTML = address;
    document.getElementById("phone").innerHTML = phone;
    document.getElementById("email").innerHTML = email;
}

// function on click uses phone and prompts to call
function ToCall(){
    window.open("tel:"+phone);
}

// function on click uses email and prompts to send email
function ToEmail(){
    window.open("mailto:"+email);
}

// function on click uses address and prompts to open in maps
function GoToLocation(){
    window.open("https://www.google.com/maps/search/?api=1&query="+address);
}

// function to create vcard and save it
function CreateVcard(){
    var vcard = "BEGIN:VCARD\nVERSION:3.0\nN:"+lname+";"+fname+"\nFN:"+fullname+"\nORG:"+company+"\nTITLE:"+designation+"\nTEL;TYPE=WORK,VOICE:"+phone+"\nADR;TYPE=WORK:;;"+address+"\nEMAIL:"+email+"\nEND:VCARD";
    var blob = new Blob([vcard], {type: "text/vcard"}); //Covert to Blob to save
    var link = document.createElement('a');  // Create a link to download
    link.href = window.URL.createObjectURL(blob); // Create a link to the file
    link.download = fullname+".vcf"; // Set the file name
    link.click(); // Download the file
}