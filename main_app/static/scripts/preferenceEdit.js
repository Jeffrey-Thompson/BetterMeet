console.log('preference edit js');

let genders = [];
let race = [];
let bodyType = [];
let relationshipStatus = [];
let education = [];
let religion = [];

const getGenders = function() {
    console.log('getting genders');
    const allGenders = document.getElementsByClassName('genders');
    for (let index = 0; index < allGenders.length; index++) {
        if (allGenders[index].checked) {
            const value = allGenders[index].value;
            genders.push(value);
        }
    }
    document.getElementById('genders_input').value = genders.join()
}

const getRace = function() {
    console.log('getting races');
    const allRaces = document.getElementsByClassName('races');
    for (let index = 0; index < allRaces.length; index++) {
        if (allRaces[index].checked) {
            const value = allRaces[index].value;
            race.push(value);
        }
    }
    document.getElementById('race_input').value = race.join()
}

const getBodyTypes = function() {
    console.log('getting body_types');
    const bodyTypes = document.getElementsByClassName('body_types');
    for (let index = 0; index < bodyTypes.length; index++) {
        if (bodyTypes[index].checked) {
            const value = bodyTypes[index].value;
            bodyType.push(value);
        }
    }
    document.getElementById('body_type_input').value = bodyType.join()
}

const getRelationships = function() {
    console.log('getting relationship_statuses');
    const allRelationships = document.getElementsByClassName('relationship_statuses');
    for (let index = 0; index < allRelationships.length; index++) {
        if (allRelationships[index].checked) {
            const value = allRelationships[index].value;
            relationshipStatus.push(value);
        }
    }
    document.getElementById('relationship_status_input').value = relationshipStatus.join()
}

const getEducation = function() {
    console.log('getting educations');
    const allEducation = document.getElementsByClassName('educations');
    for (let index = 0; index < allEducation.length; index++) {
        if (allEducation[index].checked) {
            const value = allEducation[index].value;
            education.push(value);
        }
    }
    document.getElementById('education_input').value = education.join()
}

const getReligion = function() {
    console.log('getting religions');
    const allReligions = document.getElementsByClassName('religions');
    for (let index = 0; index < allReligions.length; index++) {
        if (allReligions[index].checked) {
            const value = allReligions[index].value;
            religion.push(value);
        }
    }
    document.getElementById('religion_input').value = religion.join()
}

const getData = function() {
    console.log('getting data');
    getGenders();
    getRace();
    getBodyTypes();
    getRelationships();
    getEducation();
    getReligion();
}

const changeGenders = function(id) {
    const gender = id.value;
    const present = genders.includes(gender);
    if (present) {
        const index = genders.indexOf(gender);
        genders.splice(index, 1);
    } else {
        genders.push(id.value);
    }
    document.getElementById('genders_input').value = genders.join();
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
    document.getElementById('race_input').value = race.join();
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
