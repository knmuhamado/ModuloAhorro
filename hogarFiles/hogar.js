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

            if (data.gastos['Otros'].length >= 2) {
                document.getElementById('divOtro1').style.display = "block";
                document.getElementById('divOtro2').style.display = "block";
                document.getElementById('Otros1').textContent = "Otros: $" + data.gastos['Otros'][data.gastos['Otros'].length - 1];
                document.getElementById('Otros2').textContent = "Otros: $" + data.gastos['Otros'][data.gastos['Otros'].length - 2];
            } else if (data.gastos['Otros'].length == 1) {
                document.getElementById('divOtro1').style.display = "block";
                document.getElementById('Otros1').textContent = "Otros: $" + data.gastos['Otros'][data.gastos['Otros'].length - 1];
                document.getElementById('divOtro2').style.display = "none";
            } else {
                document.getElementById('divOtro1').style.display = "none";
                document.getElementById('divOtro2').style.display = "none";
            }

            if (data.gastos['Alimentacion'].length >= 2) {
                document.getElementById('divAlimentacion1').style.display = "block";
                document.getElementById('divAlimentacion2').style.display = "block";
                document.getElementById('Alimentacion1').textContent = "Alimentacion: $" + data.gastos['Alimentacion'][data.gastos['Alimentacion'].length - 1];
                document.getElementById('Alimentacion2').textContent = "Alimentacion: $" + data.gastos['Alimentacion'][data.gastos['Alimentacion'].length - 2];
            } else if (data.gastos['Alimentacion'].length == 1) {
                document.getElementById('divAlimentacion1').style.display = "block";
                document.getElementById('Alimentacion1').textContent = "Alimentacion: $" + data.gastos['Alimentacion'][data.gastos['Alimentacion'].length - 1];
                document.getElementById('divAlimentacion2').style.display = "none";
            } else {
                document.getElementById('divAlimentacion1').style.display = "none";
                document.getElementById('divAlimentacion2').style.display = "none";
            }

            new ApexCharts(document.querySelector("#reportsChart"), {


                series: [{
                    name: 'Presupuestos',
                    data: [parseInt(data.presupuestos['Alimentacion']), parseInt(data.presupuestos['Vivienda']), parseInt(data.presupuestos['Servicios']), parseInt(data.presupuestos['Otros'])],
                }, {
                    name: 'Gastos',
                    data: [parseInt(data.gastosS['Alimentacion']), parseInt(data.gastosS['Vivienda']), parseInt(data.gastosS['Servicios']), parseInt(data.gastosS['Otros'])],
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
                    categories: ["Alimentacion", "Vivienda", "Servicios", "Otros"]
                },
                tooltip: {
                    x: {
                        format: 'dd/MM/yy HH:mm'
                    },
                }
            }).render();

            console.log("Hola")
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
