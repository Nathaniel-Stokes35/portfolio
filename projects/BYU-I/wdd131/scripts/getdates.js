const year_container = document.getElementById('currentYear');
const modified_container = document.getElementById('lastModified');
const today = new Date();
const modified_date = document.lastModified;

year_container.innerHTML = today.getFullYear();
modified_container.innerHTML = `Last Modified: ${modified_date}`;