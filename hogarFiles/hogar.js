document.addEventListener("DOMContentLoaded", function () {
    fetch('http://127.0.0.1:5000/datosH')
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

            // Actualizar Meta
            document.getElementById('meta').textContent = `$${data.Meta}`;

            // Actualizar ahorro
            document.getElementById('ahorroTotal').textContent = `$${data.gastosS['Ahorro']}`;

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
            console.log(data);
            if (data.success) {
                alert('Gasto añadido correctamente');
                location.reload();
            } else {
                alert('Error al añadir el gasto');
            }
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('formDefinirMeta').addEventListener('submit', function (event) {
    event.preventDefault();

    var nuevaMeta = document.getElementById('ahorro').value;

    // Enviar los datos al servidor
    fetch('http://127.0.0.1:5000/definir_meta', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            meta: nuevaMeta
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Meta de ahorro actualizada correctamente');
                location.reload();
            } else {
                alert('Error al actualizar la meta: ' + data.message);
            }
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('formEditarAhorro').addEventListener('submit', function (event) {
    event.preventDefault();  // Evitar que el formulario se envíe de forma tradicional

    // Obtener los valores seleccionados
    var ahorro = document.getElementById('montoAhorro').value;
    var opcion = document.getElementById('opcionAhorro').value;

    // Validar que ambos campos tengan valores
    if (!ahorro || !opcion) {
        alert('Por favor completa ambos campos.');
        return;
    }


    // Enviar los datos al servidor usando Fetch API
    fetch('http://127.0.0.1:5000/ahorro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            ahorro: ahorro,
            opcion: opcion
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Ahorro actualizado correctamente');
                location.reload();
            } else {
                alert('Error al actualizar el ahorro: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error en el fetch:', error);
            alert('Hubo un problema al conectarse con el servidor.');
        });
});
document.getElementById('formAñadirPendiente').addEventListener('submit', function (e) {
    e.preventDefault();

    // Recoger datos del formulario
    const formData = new FormData(this);
    const data = {
        fecha: formData.get('fechaPendiente'),
        id_pendiente: Date.now(), // Generar un ID único
        monto: formData.get('montoPendiente'),
        nombre: formData.get('nombrePendiente')
    };

    // Enviar datos al servidor
    fetch('http://127.0.0.1:5000/añadir_pendiente', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(result => {
            if (result.success) {
                alert('Pendiente añadido correctamente');
                cargarPendientes();
                document.getElementById('formAñadirPendiente').reset();
                $('#modalAñadirPendientes').modal('hide');
            } else {
                alert('Error al añadir el pendiente: ' + result.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Hubo un problema al conectarse con el servidor.');
        });
});
function cargarPendientes() {
    fetch('http://127.0.0.1:5000/pendientes')
        .then(response => response.json())
        .then(data => {
            console.log('Datos de pendientes:', data);  // Agrega esto para depuración
            const container = document.getElementById('actividad-container');
            container.innerHTML = ''; // Limpiar el contenedor

            data.pendientes.forEach(pendiente => {
                // Asegúrate de que la estructura coincide con los datos JSON
                const [fecha, id, monto, nombre, usuario] = pendiente;

                const item = document.createElement('div');
                item.className = 'activity-item d-flex';
                item.innerHTML = `
                    <div class="activite-label">
                        <b><p>$${monto}</p></b>
                        <b><p>${fecha}</p></b>
                    </div>
                    <i class='bi bi-circle-fill activity-badge text-danger align-self-start'></i>
                    <div class="activity-content flex-grow-1">
                        ${nombre}
                        <button class="btn btn-sm btn-outline-danger btn-delete m-3" onclick="eliminarPendiente(${id})">
                            <i class="bi bi-trash"></i>
                        </button>
                    </div>
                `;
                container.appendChild(item);
            });
        })
        .catch(error => console.error('Error:', error));
}



function eliminarPendiente(idPendiente) {
    if (confirm('¿Estás seguro de que deseas eliminar este pendiente?')) {
        fetch('http://127.0.0.1:5000/eliminar_pendiente', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id_pendiente: idPendiente })
        })
            .then(response => response.json())
            .then(result => {
                if (result.success) {
                    alert('Pendiente eliminado correctamente');
                    cargarPendientes();
                } else {
                    alert('Error al eliminar el pendiente: ' + result.message);
                }
            })
            .catch(error => console.error('Error:', error));
    }
}
