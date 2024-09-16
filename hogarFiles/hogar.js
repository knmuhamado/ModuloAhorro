document.addEventListener("DOMContentLoaded", function () {
    fetch('http://127.0.0.1:5000/datosH')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log("Hola")
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
            document.getElementById('alimentacion').textContent = data.presupuestos['Alimentacion'];
            document.getElementById('vivienda').textContent = data.presupuestos['Vivienda'];
            document.getElementById('servicios').textContent = data.presupuestos['Servicios'];
            document.getElementById('otros').textContent = data.presupuestos['Otros'];

            document.getElementById('alimentacionGasto').textContent = data.gastosS['Alimentacion'];
            document.getElementById('viviendaGasto').textContent = data.gastosS['Vivienda'];
            document.getElementById('serviciosGasto').textContent = data.gastosS['Servicios'];
            document.getElementById('otrosGasto').textContent = data.gastosS['Otros'];


            var porcentajeA = 0;
            if (data.Meta > 0) {
                porcentajeA = (data.gastosS['Ahorro'] / data.Meta) * 100;
            }

            document.getElementById('porcentajeA').textContent = porcentajeA.toFixed(2) + '%';
            document.getElementById('alimentacion').textContent = data.presupuestos['Alimentacion'];
            document.getElementById('otros').textContent = data.presupuestos['Otros'];
            document.getElementById('transporte').textContent = data.presupuestos['Transporte'];

            document.getElementById('alimentacionGasto').textContent = data.gastosS['Alimentacion'];
            document.getElementById('otrosGasto').textContent = data.gastosS['Otros'];
            document.getElementById('transporteGasto').textContent = data.gastosS['Transporte'];





        })
        .catch(error => {
            console.error('Error:', error);
        });
});

console.log("Hola")
