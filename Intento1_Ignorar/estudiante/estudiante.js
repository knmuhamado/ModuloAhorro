document.addEventListener("DOMContentLoaded", function() {
    fetch('http://127.0.0.1:5000/presupuesto')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('presupuesto_usuario').textContent = `$${data.presupuesto_total}`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});