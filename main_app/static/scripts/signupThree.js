let genders = [];
let bodyType = [];
let relationshipStatus = [];
let education = [];
let religion = [];
let race = [];

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
    document.getElementById('relationship_status_input').value = relationshipStatus.join();
}

const changeEducation = function(id) {
    const level = id.value;
    const present = education.includes(level);
    if (present) {
        const index = education.indexOf(level);
        education.splice(index, 1);
    } else {
        education.push(id.value);
    }
    console.log(education);
    document.getElementById('education_input').value = education.join();
}

const changeReligion = function(id) {
    const kind = id.value;
    const present = religion.includes(kind);
    if (present) {
        const index = religion.indexOf(kind);
        religion.splice(index, 1);
    } else {
        religion.push(id.value);
    }
    console.log(religion);
    document.getElementById('religion_input').value = religion.join();
}

const changeRace = function(id) {
    const ethnicity = id.value;
    const present = race.includes(ethnicity);
    if (present) {
        const index = race.indexOf(ethnicity);
        race.splice(index, 1);
    } else {
        race.push(id.value);
    }
    console.log(race);
    document.getElementById('race_input').value = race.join();
}