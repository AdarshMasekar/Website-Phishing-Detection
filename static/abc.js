
let x = '{{xx}}';
// let a = '{website_details}';
// let country = a[country];
// let city =  a[city];
// let zipcode = a[zipcode];
// let timezone = a[timezone];

// document.getElementById("country").innerHTML = "country :" + country;
// document.getElementById("city").innerHTML = "city :" + city;
// document.getElementById("zipcode").innerHTML = "zipcode :" + zipcode;
// document.getElementById("timezone").innerHTML = "timezone :" + timezone;

let num = x*100;
if (0<=x && x<0.50){
    num = 100-num;z
}
let txtx = num.toString();

// Get the prediction element
var predictionElement = document.getElementById('prediction');

// Get the prediction value
var predictionValue = txtx;
if(x<=1 && x>=0.50){
    var label = "Website is "+txtx +"% safe to use...";
    document.getElementById("prediction").innerHTML = label;
    document.getElementById("prediction").style.color = "green";
    document.getElementById("button1").style.display="block";
}
else if (0<=x && x<0.50){
    var label = "Website is "+txtx +"% unsafe to use..."

    document.getElementById("prediction").innerHTML = label ;
    document.getElementById("prediction").style.color = "red";


    // document.getElementById("button1").style.display="block";
}
