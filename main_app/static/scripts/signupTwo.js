let interests = []

const changeInterests = function(id) {
    interests.push(id.value)
    console.log(interests);
    document.getElementById('interests_input').value = interests.join()
}

