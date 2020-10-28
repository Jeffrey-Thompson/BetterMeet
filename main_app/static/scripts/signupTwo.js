let interests = []

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

