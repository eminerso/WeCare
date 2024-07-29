
document.querySelector(".open-book-an-appointment-button1").addEventListener("click", function() {
    document.querySelector(".section-book-an-appointment").style.display = "block";
    window.scrollTo({ top: 0, behavior: 'smooth' });
    
   
});
document.querySelector(".open-book-an-appointment-button2").addEventListener("click", function() {
    document.querySelector(".section-book-an-appointment").style.display = "block";
   
    window.scrollTo({ top: 0, behavior: 'smooth' });
   
});
document.querySelector(".open-book-an-appointment-button3").addEventListener("click", function() {
    document.querySelector(".section-book-an-appointment").style.display = "block";
    window.scrollTo({ top: 0, behavior: 'smooth' });
   
});
document.querySelector(".open-book-an-appointment-button4").addEventListener("click", function() {
    document.querySelector(".section-book-an-appointment").style.display = "block";
    window.scrollTo({ top: 0, behavior: 'smooth' });
   
});

document.querySelector(".close-button i").addEventListener("click", function() {
    document.querySelector(".section-book-an-appointment").style.display = "none";
   
});

document.querySelector(".button-book-appoinment-confirmed").addEventListener("click", function() {
    var name = document.getElementById("name_").value;
    var email = document.getElementById("email_").value;
    var phone = document.getElementById("phone").value;
    var gender = document.getElementById("gender").value;
    var message = document.getElementById("message").value;
    


    if (name && email && phone && gender && message) {
        document.querySelector(".section-book-an-appointment").style.display = "none";
        document.querySelector(".section-book-an-appointment-confirmed").style.display = "block"; 
        
    } else {
        alert("Please fill out all fields before submitting the form.");
    }
    
});

document.querySelector(".button-done").addEventListener("click", function() {
    document.querySelector(".section-book-an-appointment-confirmed").style.display = "none"; 
    document.querySelector(".section-book-an-appointment").style.display = "none";
    window.location.href = window.location.href

   
});
