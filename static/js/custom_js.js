
// Function for checking password and confirm password matching 

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


//  This function will save the Search value to Localstorage 
function add_value_to_storage(){

  let search_value = document.getElementById('get_value').value;
  localStorage.setItem('search_value',search_value)
}


// Functions for checking given input in list input fields 

function list_given_checker(){

  let check_input = document.getElementById('list_checker').value.replaceAll(' ', '');
  const list_input_format = /^[0-9 ,]+$/g;
  const double_comma = /(,{2,})/g;


  if (!list_input_format.test(check_input)){
      // checking if given input has anyting except Number
      document.getElementById('error_show').style.color = "red";
      document.getElementById('error_show').innerHTML = "Please Type Number only";

  }else if(double_comma.test(check_input)){
      // checking if given input has double comma in it
      document.getElementById('error_show').style.color = "red";
      document.getElementById('error_show').innerHTML = "Please return a list with single seprated comma.For example ( 23,32,545 )";
      
  }else if (check_input[0] == ',' || check_input.slice(-1) == ','){
      // checking if given input has comman in first or last character
      document.getElementById('error_show').style.color = "red";
      document.getElementById('error_show').innerHTML = "Please Remove First or Last Comma";
      
  }else{
      // if above condition pass then return given input removing all space 
      document.getElementById('error_show').style.color = "green";
      document.getElementById('error_show').innerHTML = "Looking Good !!";
      document.getElementById('list_checker').value = check_input;
  }
}