console.log('profile edit js');


const addChecks = function(){
    interests = document.getElementById('interests_input').value
    console.log(interests);
}

document.getElementById('interests_input').addEventListener('load', addChecks())