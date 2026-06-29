window.addEventListener('load', () => {

    document.getElementById('loader').style.display = 'none';

});


const menuBtn = document.getElementById('menuBtn');
const navLinks = document.getElementById('nav-links');

menuBtn.addEventListener('click', () => {

    navLinks.classList.toggle('active');

});


const darkBtn = document.getElementById('darkBtn');

darkBtn.addEventListener('click', () => {

    document.body.classList.toggle('dark');

});


function updateClock() {

    const now = new Date();

    document.getElementById('clock').innerHTML =
        now.toLocaleTimeString();

    document.getElementById('date').innerHTML =
        now.toLocaleDateString();

}

setInterval(updateClock, 1000);


const searchInput = document.getElementById('searchInput');
const cards = document.querySelectorAll('.book-card');

const filterSubject = document.getElementById('filterSubject');
const filterYear = document.getElementById('filterYear');


function filterBooks() {

    const search = searchInput.value.toLowerCase();
    const subject = filterSubject.value.toLowerCase();
    const year = filterYear.value.toLowerCase();

    cards.forEach(card => {

        const title = card.dataset.title.toLowerCase();
        const cardSubject = card.dataset.subject.toLowerCase();
        const cardYear = card.dataset.year.toLowerCase();

        const matchSearch = title.includes(search);
        const matchSubject = subject === '' || cardSubject.includes(subject);
        const matchYear = year === '' || cardYear.includes(year);

        if (matchSearch && matchSubject && matchYear) {

            card.style.display = 'block';

        } else {

            card.style.display = 'none';

        }

    });

}

searchInput.addEventListener('keyup', filterBooks);
filterSubject.addEventListener('change', filterBooks);
filterYear.addEventListener('change', filterBooks);


const suggestForm = document.getElementById('suggestForm');

suggestForm.addEventListener('submit', async (e) => {

    e.preventDefault();

    const data = {

        nombre: document.getElementById('nombre').value,
        libro: document.getElementById('libro').value,
        comentario: document.getElementById('comentario').value

    }

    const response = await fetch('/sugerir', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify(data)

    });

    const result = await response.json();

    alert(result.mensaje);

    suggestForm.reset();

});