document.addEventListener('DOMContentLoaded', initSnakeGame);

function initSnakeGame() {
    // Definicion variables
    const canvas = document.getElementById('juegoSerpiente');
    const ctx = canvas.getContext('2d');
    const botonSt = document.getElementById('botonStart');
    const puntosDisplay = document.getElementById('output');
    const cuadrado = 20;
    let serpiente = [{x: canvas.width/2, y: canvas.height/2}];
    let dx = cuadrado;
    let dy = 0;
    let manzana = {x: Math.floor(Math.random() * 20) * cuadrado, y: Math.floor(Math.random() * 20) * cuadrado};
    let juego;
    let puntos = 0;
    let nombreJugador = '';

    ctx.fillStyle = "rgba(125,255,90,1.0)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    let selectorVeloz = document.getElementById('veloz');

    // Eventos listener para boton Start del juego y flechas teclado
    botonSt.addEventListener('click', empiezoJ);
    document.addEventListener('keydown', cambioDireccion);

    function empiezoJ() {
        nombreJugador = prompt("Por favor, introduce tu nombre:");
        if (!nombreJugador) {
            alert("Nombre de jugador es requerido para jugar.");
            return;
        }

        // Reset juego
        serpiente = [{x: canvas.width/2, y: canvas.height/2}];
        dx = cuadrado;
        dy = 0;
        manzana = {x: Math.floor(Math.random() * 20) * cuadrado, y: Math.floor(Math.random() * 20) * cuadrado};
        puntos = 0;

        // Detener el intervalo del juego
        if (juego) {
            clearInterval(juego);
        }

        // Velocidad juego
        let velo = parseInt(selectorVeloz.value);
        let combo = document.getElementById('veloz');
        let nivel = combo.options[combo.selectedIndex].text;
        salida = ("Puntuación de: " + puntos + " Manzanas - Nivel Juego: " + nivel);
        document.getElementById("output").innerHTML = salida;

        if (velo >= 50 && velo <= 200) {
            juego = setInterval(dibujo, velo);
        }
    }

    function cambioDireccion(e) {
        if (e.keyCode === 37 && dx !== cuadrado) { // flecha izquierda
            dx = -cuadrado;
            dy = 0;
        } else if (e.keyCode === 38 && dy !== cuadrado) { // flecha arriba
            dx = 0;
            dy = -cuadrado;
        } else if (e.keyCode === 39 && dx !== -cuadrado) { // flecha derecha
            dx = cuadrado;
            dy = 0;
        } else if (e.keyCode === 40 && dy !== -cuadrado) { // flecha abajo
            dx = 0;
            dy = cuadrado;
        }
    }

    function dibujo() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = "rgba(125,255,90,1.0)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = 'red';
        ctx.fillRect(manzana.x, manzana.y, cuadrado, cuadrado);
        ctx.strokeStyle = 'black';
        ctx.strokeRect(manzana.x, manzana.y, cuadrado, cuadrado);
        ctx.fillStyle = 'white';
        serpiente.forEach((segment) => {
            ctx.fillRect(segment.x, segment.y, cuadrado, cuadrado);
            ctx.strokeStyle = 'black';
            ctx.strokeRect(segment.x, segment.y, cuadrado, cuadrado);
        });

        const cabeza = {x: serpiente[0].x + dx, y: serpiente[0].y + dy};
        serpiente.unshift(cabeza);

        if (cabeza.x === manzana.x && cabeza.y === manzana.y) {
            manzana = {x: Math.floor(Math.random() * 20) * cuadrado, y: Math.floor(Math.random() * 20) * cuadrado};
            puntos++;
            salida = ("Puntuación de: " + puntos + " Manzanas - Nivel Juego: " + nivel);
            document.getElementById("output").innerHTML = salida;
            if (puntos % 10 === 0) {
                levelUp();
            }
        } else {
            serpiente.pop();
        }

        if (cabeza.x < 0 || cabeza.x >= canvas.width || cabeza.y < 0 || cabeza.y >= canvas.height || colision()) {
            clearInterval(juego);
            alert("Fin del Juego !!! ");
            saveScore(nombreJugador, puntos);
        }
    }

    function levelUp() {
        clearInterval(juego);
        juego = setInterval(dibujo, velo);
        velo = Math.max(velo - 50, 50);
        if (velo === 200) {
            nivel = "Facil";
        } else if (velo === 150) {
            nivel = "Medio";
        } else if (velo === 100) {
            nivel = "Difícil";
        } else {
            nivel = "Muy Difícil";
        }
        output = ("Puntuación de: " + puntos + " Manzanas - Nivel Juego: " + nivel);
        document.getElementById("output").innerHTML = output;
    }

    function colision() {
        return serpiente.slice(1).some(segment => segment.x === serpiente[0].x && segment.y === serpiente[0].y);
    }

    function saveScore(name, score) {
        fetch('/save_score/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({name: name, score: score})
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                fetchTopScores();
            }
        });
    }

    function fetchTopScores() {
        fetch('/top_scores/')
            .then(response => response.json())
            .then(data => {
                let message = "Top 10 Jugadores:\n";
                data.forEach((player, index) => {
                    message += `${index + 1}. ${player.name} - ${player.score}\n`;
                });
                alert(message);
            });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}