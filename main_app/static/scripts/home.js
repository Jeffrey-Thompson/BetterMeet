const openModal = function() {
    document.getElementById('modal-id').classList.add('active');
}

const closeModel = function() {
    document.getElementById('modal-id').classList.remove('active');
}

document.getElementById('learn').addEventListener('click', openModal);
document.querySelector('.btn-clear').addEventListener('click', closeModel);
