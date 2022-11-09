
// Search Function for searching list with given search value
// User will input a search value 
// functions will return True if search value found 
// else functions will return False 

function searchlist(){
    localStorage.removeItem('search_value');
    const input_values = document.getElementById('input_value').innerHTML;
    const convert_to_arrays = input_values.split(',')
    let search_value = document.getElementById('search_value').value;

    if (!search_value){
        // checking if user doesn`t input a search value
        document.getElementById('search_value').style.borderColor = "red";
        document.getElementById('result_not_found').hidden = true;
        document.getElementById('result_found').hidden = true;
    }
    
    else if (convert_to_arrays.includes(search_value)){
        document.getElementById('search_value').style.borderColor = "";
        document.getElementById('result_not_found').hidden = true;
        document.getElementById('result_found').hidden = false;

    }else{
        document.getElementById('search_value').style.borderColor = "";
        document.getElementById('result_found').hidden = true;
        document.getElementById('result_not_found').hidden = false;
    }
}


// When a User create a list with search fields 
// this function will help the user to see the result right after the POST
// functions will return True if search value found 
// else functions will return False 

function add_value_after_post(){
    document.getElementById('search_value').value = localStorage.getItem('search_value');
    const input_values = document.getElementById('input_value').innerHTML;
    const convert_to_arrays = input_values.split(',')
    let search_value = document.getElementById('search_value').value;

    if (convert_to_arrays.includes(search_value)){
        document.getElementById('result_not_found').hidden = true;
        document.getElementById('result_found').hidden = false;

    }else{
        document.getElementById('result_found').hidden = true;
        document.getElementById('result_not_found').hidden = false;

    }
    // deleting the localstorage search value
    localStorage.removeItem('search_value');    
}

// function for reseting values 
function reset(){
    document.getElementById('search_value').value = "";
    document.getElementById('result_not_found').hidden = true;
    document.getElementById('result_found').hidden = true;
}


if (localStorage.getItem('search_value') === null){
    // checking if window is loaded and there is no localstorage variable named Search Value
    console.log('')
    
}else{
    // returning  the function 
    add_value_after_post();
}
