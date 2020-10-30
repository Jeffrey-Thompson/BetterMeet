console.log('profile edit js');

let interests = [];

const getInterests = function() {
    console.log('get interests running');
    const allInterests = document.getElementsByClassName('interests');
    for (let index = 0; index < allInterests.length; index++) {
        if (allInterests[index].checked) {
            const value = allInterests[index].value;
            interests.push(value);
        }
        console.log(interests);
    }
    document.getElementById('interests_input').value = interests.join()
}

const changeInterests = function(id) {
    const interest = id.value
    const present = interests.includes(interest);
    if (present) {
        const index = interests.indexOf(interest);
        interests.splice(index, 1);
    } else {
        interests.push(id.value);
    }
    console.log(interests);
    document.getElementById('interests_input').value = interests.join()
}