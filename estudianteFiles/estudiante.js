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

            document.getElementById('alimentacion').textContent = data.presupuestos['Alimentacion'];
            document.getElementById('otros').textContent = data.presupuestos['Otros'];
            document.getElementById('transporte').textContent = data.presupuestos['Transporte'];

            document.getElementById('alimentacionGasto').textContent = data.gastosS['Alimentacion'];
            document.getElementById('otrosGasto').textContent = data.gastosS['Otros'];
            document.getElementById('transporteGasto').textContent = data.gastosS['Transporte'];

            if (data.gastos['Otros'].length >= 2) {
                document.getElementById('divOtro1').style.display = "block";
                document.getElementById('divOtro2').style.display = "block";
                document.getElementById('Otros1').textContent = "Otros: $" + data.gastos['Otros'][data.gastos['Otros'].length - 1];
                document.getElementById('Otros2').textContent = "Otros: $" + data.gastos['Otros'][data.gastos['Otros'].length - 2];
            }
            else if (data.gastos['Otros'].length == 1) {
                document.getElementById('divOtro1').style.display = "block";
                document.getElementById('Otros1').textContent = "Otros: $" + data.gastos['Otros'][data.gastos['Otros'].length - 1];
                document.getElementById('divOtro2').style.display = "none";
            }
            else {
                document.getElementById('divOtro1').style.display = "none";
                document.getElementById('divOtro2').style.display = "none";
            }


            //Mostrar gastos Alimentacion
            if (data.gastos['Alimentacion'].length >= 2) {
                document.getElementById('divAlimentacion1').style.display = "block";
                document.getElementById('divAlimentacion2').style.display = "block";
                document.getElementById('Alimentacion1').textContent = "Alimentacion: $" + data.gastos['Alimentacion'][data.gastos['Alimentacion'].length - 1];
                document.getElementById('Alimentacion2').textContent = "Alimentacion: $" + data.gastos['Alimentacion'][data.gastos['Alimentacion'].length - 2];
            }
            else if (data.gastos['Alimientacion'].length == 1) {
                document.getElementById('divAlimentacion1').style.display = "block";
                document.getElementById('Alimentacion1').textContent = "Alimentacion: $" + data.gastos['Alimentacion'][data.gastos['Alimentacion'].length - 1];
                document.getElementById('divAlimentacion2').style.display = "none";
            }
            else {
                document.getElementById('divAlimentacion1').style.display = "none";
                document.getElementById('divAlimentacion2').style.display = "none";
            }

            //Mostras gastos Transporte
            if (data.gastos['Transporte'].length >= 2) {
                document.getElementById('divTransporte1').style.display = "block";
                document.getElementById('divTransporte2').style.display = "block";
                document.getElementById('Transporte1').textContent = "Transporte: $" + data.gastos['Transporte'][data.gastos['Transporte'].length - 1];
                document.getElementById('Transporte2').textContent = "Transporte: $" + data.gastos['Transporte'][data.gastos['Transporte'].length - 2];
            }
            else if (data.gastos['Alimientacion'].length == 1) {
                document.getElementById('divTransporte1').style.display = "block";
                document.getElementById('Transporte1').textContent = "Transporte: $" + data.gastos['Transporte'][data.gastos['Transporte'].length - 1];
                document.getElementById('divTransporte2').style.display = "none";
            }
            else {
                document.getElementById('divTransporte1').style.display = "none";
                document.getElementById('divTransporte2').style.display = "none";
            }


            new ApexCharts(document.querySelector("#reportsChart"), {


                series: [{
                    name: 'Presupuestos',
                    data: [parseInt(data.presupuestos['Alimentacion']), parseInt(data.presupuestos['Transporte']), parseInt(data.presupuestos['Otros'])],
                }, {
                    name: 'Gastos',
                    data: [parseInt(data.gastosS['Alimentacion']), parseInt(data.gastosS['Transporte']), parseInt(data.gastosS['Otros'])],
                },],
                chart: {
                    height: 350,
                    type: 'area',
                    toolbar: {
                        show: false
                    },
                },
                markers: {
                    size: 4
                },
                colors: ['#4154f1', '#2eca6a'],
                fill: {
                    type: "gradient",
                    gradient: {
                        shadeIntensity: 1,
                        opacityFrom: 0.3,
                        opacityTo: 0.4,
                        stops: [0, 90, 100]
                    }
                },
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    curve: 'smooth',
                    width: 2
                },
                xaxis: {
                    type: 'text',
                    categories: ["Alimentacion", "Transporte", "Otros"]
                },
                tooltip: {
                    x: {
                        format: 'dd/MM/yy HH:mm'
                    },
                }
            }).render();

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


