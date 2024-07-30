document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('juegoSerpiente');
    const ctx = canvas.getContext('2d');
    const botonSt = document.getElementById('botonStart');
    const nombreInput = document.getElementById('nombre');
    const puntosDisplay = document.getElementById('output');
    const cuadrado = 20;
    let serpiente = [{x: canvas.width / 2, y: canvas.height / 2}];
    let dx = cuadrado;
    let dy = 0;
    let manzana = {
        x: Math.floor(Math.random() * 20) * cuadrado,
        y: Math.floor(Math.random() * 20) * cuadrado
    };
    let juego;
    let puntos = 0;


    let selectorVeloz = document.getElementById('veloz');

    botonSt.addEventListener('click', empiezoJ);
    document.addEventListener('keydown', cambioDireccion);

    function empiezoJ() {
        // Validar nombre del jugador
        if (!nombreInput.value) {
            alert('Por favor, ingresa tu nombre.');
            return;
        }

        // Reset juego
        serpiente = [{x: canvas.width / 2, y: canvas.height / 2}];
        dx = cuadrado;
        dy = 0;
        manzana = {
            x: Math.floor(Math.random() * 20) * cuadrado,
            y: Math.floor(Math.random() * 20) * cuadrado
        };
        puntos = 0;

        // Detener el intervalo del juego
        if (juego) {
            clearInterval(juego);
        }

        // Velocidad juego
        let velo = parseInt(selectorVeloz.value);
        if (velo >= 50 && velo <= 200) {
            juego = setInterval(dibujo, velo);
        }
    }

    function cambioDireccion(e) {
        if (e.keyCode === 37 && dx !== cuadrado) {
            dx = -cuadrado;
            dy = 0;
        } else if (e.keyCode === 38 && dy !== cuadrado) {
            dx = 0;
            dy = -cuadrado;
        } else if (e.keyCode === 39 && dx !== -cuadrado) {
            dx = cuadrado;
            dy = 0;
        } else if (e.keyCode === 40 && dy !== -cuadrado) {
            dx = 0;
            dy = cuadrado;
        }
    }

    function dibujo() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'rgba(125,255,90,0.9)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // Cuadrado manzana
        ctx.fillStyle = 'red';
        ctx.fillRect(manzana.x, manzana.y, cuadrado, cuadrado);

        // Contorno cuadrado manzana
        ctx.strokeStyle = 'black';
        ctx.strokeRect(manzana.x, manzana.y, cuadrado, cuadrado);

        // Cuadrado serpiente
        ctx.fillStyle = 'white';
        serpiente.forEach((segment) => {
            ctx.fillRect(segment.x, segment.y, cuadrado, cuadrado);
            ctx.strokeStyle = 'black';
            ctx.strokeRect(segment.x, segment.y, cuadrado, cuadrado);
        });

        // Agrega una coordenada al array serpiente
        const cabeza = {x: serpiente[0].x + dx, y: serpiente[0].y + dy};
       

 serpiente.unshift(cabeza);

        if (cabeza.x === manzana.x && cabeza.y === manzana.y) {
            manzana = {
                x: Math.floor(Math.random() * 20) * cuadrado,
                y: Math.floor(Math.random() * 20) * cuadrado
            };
            puntos++;
            puntosDisplay.textContent = `Puntuación: ${puntos}`;
        } else {
            serpiente.pop();
        }

        if (cabeza.x < 0 || cabeza.x >= canvas.width || cabeza.y < 0 || cabeza.y >= canvas.height || colision()) {
            clearInterval(juego);
            alert("Fin del Juego !!!");
            guardarPuntuacion();
        }
    }

    function colision() {
        return serpiente.slice(1).some(segment => segment.x === serpiente[0].x && segment.y === serpiente[0].y);
    }

    function guardarPuntuacion() {
        const inputNombre = document.getElementById('inputNombre');
        const inputPuntos = document.getElementById('inputPuntos');
        inputNombre.value = nombreInput.value;
        inputPuntos.value = puntos;
        document.getElementById('saveScoreForm').submit();
    }
});