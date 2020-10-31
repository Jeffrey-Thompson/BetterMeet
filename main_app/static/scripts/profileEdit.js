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

const openModal = function() {
    document.getElementById('modal-id').classList.add('active');
}

const closeModel = function() {
    document.getElementById('modal-id').classList.remove('active');
}

document.getElementById('delete-btn').addEventListener('click', openModal);
document.querySelector('.btn-clear').addEventListener('click', closeModel);
document.getElementById('close_modal').addEventListener('click', closeModel);