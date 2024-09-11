document.getElementById('form-login').addEventListener('submit', function (e) {
    e.preventDefault();  // Evita que el formulario se envíe de la manera tradicional

    const nombre = document.getElementById('nombre').value;
    const contrasena = document.getElementById('contrasena').value;

    // Enviar los datos a Flask usando Fetch API
    fetch('http://127.0.0.1:5000/procesar_datos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nombre: nombre, contrasena: contrasena }),
    })
        .then(response => response.json())
        .then(data => {
            // Mostrar el mensaje recibido del servidor
            document.getElementById('mensaje').innerText = data.mensaje;
            // Redireccionar a la página relacionada
            setTimeout(function () {
                if (data.perfil) {
                    const url = data.perfil === 'Estudiante' ? '../estudiante.html' : '../hogar.html';
                    console.log(url);
                    window.location.href = url;
                }
            }, 1000)

        })
        .catch((error) => {
            console.error('Error:', error);
        });
});