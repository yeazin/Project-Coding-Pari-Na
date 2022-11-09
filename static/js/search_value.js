
// Search logics for Input list 
// User will input a search value 
// functions will return True if search value found 
// else functions will return False 

function searchlist(){
    localStorage.removeItem('search_value');
    const input_values = document.getElementById('input_value').innerHTML;
    const convert_to_arrays = input_values.split(',')
    let search_value = document.getElementById('search_value').value;

    if (convert_to_arrays.includes(search_value)){
        console.log("found");
        console.log(convert_to_arrays);
        document.getElementById('result').innerHTML = "True"
    }else{
        console.log("Not found");
        console.log(convert_to_arrays);
        document.getElementById('result').innerHTML = "False"
    }
}

function add_value_after_post(){
    document.getElementById('search_value').value = localStorage.getItem('search_value');
    const input_values = document.getElementById('input_value').innerHTML;
    const convert_to_arrays = input_values.split(',')
    let search_value = document.getElementById('search_value').value;

    if (convert_to_arrays.includes(search_value)){
        console.log("found");
        console.log(convert_to_arrays);
        document.getElementById('result').innerHTML = "True"
    }else{
        console.log("Not found");
        console.log(convert_to_arrays);
        document.getElementById('result').innerHTML = "False"
    }
}



if (localStorage.getItem('search_value')=== null){
    // window.onload = heii();
    console.log('')
    
}else{
    add_value_after_post();
}
