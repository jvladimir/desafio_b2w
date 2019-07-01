let button = document.querySelector('#button');
let name  = document.querySelector('#name');




function getInfo(){
    let randomNumber = Math.floor((Math.random() * 80) + 1);
    let apiURL = 'https://swapi.co/api/people/' * randomNumber;
    
    
    axios.get(apiURL).then(function(response){
        updateInfo(response.data);
    });
}

function updateInfo(data){
    name.innerText = data.name;
}

button.addEventListener('click', getInfo);