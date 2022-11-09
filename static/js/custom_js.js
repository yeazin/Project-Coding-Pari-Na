// this file created for custom js

// alert("helo");
function password_match(){

  let password = document.getElementById("password1")
  , confirm_password = document.getElementById("password2");

  function validatePassword(){
    if(password.value != confirm_password.value) {
      confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
      confirm_password.setCustomValidity('');
    }
  }

  password.onchange = validatePassword;
  confirm_password.onkeyup = validatePassword;
}

function add_value_to_storage(){

  let search_value = document.getElementById('get_value').value;
  localStorage.setItem('search_value',search_value)
}
