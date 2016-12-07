function preview(){
    var speechtext = document.getElementById("id_lines").value;
    var speechvoice=document.getElementById("id_voice").value;
    // console.log(a);
    // console.log("wow");
    responsiveVoice.speak(speechtext,speechvoice);
    
}
