let genders = [];
let bodyType = [];
let relationshipStatus = [];

const changeGenders = function(id) {
    const gender = id.value;
    const present = genders.includes(gender);
    if (present) {
        const index = genders.indexOf(gender);
        genders.splice(index, 1);
    } else {
        genders.push(id.value);
    }
    console.log(genders);
    document.getElementById('genders_input').value = genders.join();
}

const changeBody = function(id) {
    const body = id.value;
    const present = bodyType.includes(body);
    if (present) {
        const index = bodyType.indexOf(body);
        bodyType.splice(index, 1);
    } else {
        bodyType.push(id.value);
    }
    console.log(bodyType);
    document.getElementById('body_type_input').value = bodyType.join();
}

const changeRelationship = function(id) {
    const relationship = id.value;
    const present = relationshipStatus.includes(relationship);
    if (present) {
        const index = relationshipStatus.indexOf(relationship);
        relationshipStatus.splice(index, 1);
    } else {
        relationshipStatus.push(id.value);
    }
    console.log(relationshipStatus);
    document.getElementById('body_type_input').value = bodyType.join();
}