document.addEventListener("DOMContentLoaded", function () {
    fetch('http://127.0.0.1:5000/datos')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Actualizar el total de presupuesto
            document.getElementById('presupuesto_usuario').textContent = `$${data.presupuesto_total}`;

            // Actualizar el total de gastos
            document.getElementById('total_gastos').textContent = `$${data.gastado}`;

            // Calcular y mostrar el porcentaje de gastos sobre el presupuesto
            var porcentaje = 0;
            if (data.presupuesto_total > 0) {
                porcentaje = (data.gastado / data.presupuesto_total) * 100;
            }
            document.getElementById('porcentaje').textContent = porcentaje.toFixed(2) + '%';
        })
        .catch(error => {
            console.error('Error:', error);
        });
});

document.getElementById('formEditarPresupuesto').addEventListener('submit', function (event) {
    event.preventDefault();

    var categoria = document.getElementById('categoria').value;
    var nuevoPresupuesto = document.getElementById('nuevoPresupuesto').value;

    // Enviar los datos al servidor
    fetch('http://127.0.0.1:5000/editar_presupuesto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            categoria: categoria,
            nuevoPresupuesto: nuevoPresupuesto
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Presupuesto actualizado correctamente');
                location.reload();
            } else {
                alert('Error al actualizar el presupuesto');
            }
        })
        .catch(error => console.error('Error:', error));
});


document.getElementById('formEditarGasto').addEventListener('submit', function (event) {
    event.preventDefault();

    var categoria = document.getElementById('categoriaGasto').value;
    var nuevoGasto = document.getElementById('nuevoGasto').value;

    // Enviar los datos al servidor
    fetch('http://127.0.0.1:5000/editar_gasto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            categoria: categoria,
            nuevoGasto: nuevoGasto
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Gasto actualizado correctamente');
                location.reload();
            } else {
                alert('Error al actualizar el presupuesto');
            }
        })
        .catch(error => console.error('Error:', error));
});


