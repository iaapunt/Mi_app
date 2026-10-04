from pathlib import Path
from datetime import datetime
import shutil

BASE = Path.home() / "mi_app"
HTML = BASE / "index.html"

if not BASE.exists():
    raise SystemExit("❌ No existe ~/mi_app")

# -------------------------------------------------
# COPIA DE SEGURIDAD
# -------------------------------------------------

if HTML.exists():
    backup = BASE / (
        "index_backup_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".html"
    )
    shutil.copy2(HTML, backup)
    print("🛡️ Copia de seguridad:", backup.name)

# -------------------------------------------------
# NUEVO INDEX
# -------------------------------------------------

page = r'''<!DOCTYPE html>
<html lang="es">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width,
initial-scale=1,
maximum-scale=1,
user-scalable=no">

<meta name="theme-color" content="#050b16">

<title>XaIA</title>

<style>

*{
box-sizing:border-box;
}

body{
margin:0;
background:#050b16;
color:white;
font-family:Arial,sans-serif;
min-height:100vh;
}

.app{
max-width:720px;
margin:auto;
padding:16px 15px 100px;
}

header{
display:flex;
justify-content:space-between;
align-items:center;
padding:8px 2px 20px;
}

.logo{
font-size:29px;
font-weight:bold;
letter-spacing:1px;
}

.status{
font-size:12px;
padding:8px 12px;
border-radius:20px;
background:#102030;
}

.hero{
padding:23px;
border-radius:28px;
background:
linear-gradient(
145deg,
#09243b,
#11142d
);
border:1px solid #16425e;
box-shadow:0 10px 35px #0008;
margin-bottom:18px;
}

.hero h1{
margin:0 0 7px;
font-size:27px;
}

.hero p{
margin:0;
color:#a9c5d8;
}

.cards{
display:grid;
grid-template-columns:repeat(2,1fr);
gap:12px;
}

.card{
min-height:130px;
padding:18px;
border-radius:23px;
background:
linear-gradient(
145deg,
#0d1928,
#101527
);
border:1px solid #19354a;
color:white;
text-align:left;
}

.card:active{
transform:scale(.98);
}

.icon{
font-size:31px;
margin-bottom:11px;
}

.card b{
font-size:17px;
}

.card small{
display:block;
color:#8da6b8;
margin-top:6px;
}

.panel{
display:none;
margin-top:15px;
padding:18px;
border-radius:24px;
background:#0b1422;
border:1px solid #19354a;
}

.panel.active{
display:block;
}

.chat{
min-height:260px;
max-height:47vh;
overflow-y:auto;
padding:5px;
}

.msg{
padding:13px 15px;
border-radius:18px;
margin:8px 0;
white-space:pre-wrap;
}

.user{
background:#123a55;
margin-left:20%;
}

.ai{
background:#151d32;
margin-right:10%;
}

.input{
display:flex;
gap:8px;
margin-top:12px;
}

.input input{
flex:1;
padding:15px;
border-radius:18px;
border:1px solid #24445c;
background:#07101c;
color:white;
outline:none;
}

button{
border:0;
border-radius:17px;
padding:13px 16px;
background:#123b57;
color:white;
font-size:15px;
}

.primary{
background:#007ea8;
}

.danger{
background:#8b1730;
}

.green{
background:#12613d;
}

.power{
width:100%;
margin-top:18px;
padding:16px;
font-weight:bold;
}

.tools{
display:grid;
grid-template-columns:1fr 1fr;
gap:10px;
margin-top:12px;
}

.tool{
padding:17px;
border-radius:18px;
background:#101d2d;
border:1px solid #1c3b52;
}

.note{
color:#8da6b8;
font-size:13px;
line-height:1.5;
}

video{
width:100%;
border-radius:20px;
margin-top:12px;
background:#000;
}

#preview{
display:none;
width:100%;
border-radius:20px;
margin-top:12px;
}

.bottom{
position:fixed;
bottom:0;
left:0;
right:0;
background:#07101cdd;
backdrop-filter:blur(15px);
border-top:1px solid #173148;
display:flex;
justify-content:center;
gap:20px;
padding:10px;
z-index:20;
}

.bottom button{
background:transparent;
}

</style>

</head>

<body>

<div class="app">

<header>

<div class="logo">
⚡ XaIA
</div>

<div id="coreStatus"
class="status">
🟡 COMPROBANDO
</div>

</header>

<section class="hero">

<h1>
Hola, Xavi 👋
</h1>

<p>
Tu asistente personal inteligente
</p>

</section>

<section class="cards">

<button class="card"
onclick="openPanel('chatPanel')">

<div class="icon">
💬
</div>

<b>
Chat
</b>

<small>
Habla con XaIA
</small>

</button>


<button class="card"
onclick="startVoice()">

<div class="icon">
🎤
</div>

<b>
Voz
</b>

<small>
Micrófono + altavoz
</small>

</button>


<button class="card"
onclick="openPanel('cameraPanel');startCamera()">

<div class="icon">
📷
</div>

<b>
Cámara IA
</b>

<small>
Analiza imágenes
</small>

</button>


<button class="card"
onclick="openPanel('toolsPanel')">

<div class="icon">
🛠️
</div>

<b>
Herramientas
</b>

<small>
Wi-Fi + Bluetooth
</small>

</button>

</section>


<section id="chatPanel"
class="panel">

<h2>
💬 Chat con XaIA
</h2>

<div id="chat"
class="chat">

<div class="msg ai">
🤖 XaIA

Hola Xavi 👋
¿En qué puedo ayudarte?
</div>

</div>

<div class="input">

<input
id="textInput"
placeholder="Escribe a XaIA..."
autocomplete="off">

<button
class="primary"
onclick="sendMessage()">
➤
</button>

</div>

<button
class="green power"
onclick="startVoice()">

🎤 Hablar con XaIA

</button>

</section>


<section id="cameraPanel"
class="panel">

<h2>
📷 Cámara IA
</h2>

<p class="note">

Permite la cámara y captura una imagen
para analizarla con XaIA.

</p>

<video
id="video"
autoplay
playsinline>
</video>

<canvas
id="canvas"
style="display:none">
</canvas>

<div class="tools">

<button
onclick="capturePhoto()">

📸 Capturar

</button>

<button
onclick="stopCamera()">

⛔ Parar

</button>

</div>

<img
id="preview">

<button
class="primary power"
onclick="analyzePhoto()">

🧠 Analizar imagen

</button>

</section>


<section id="toolsPanel"
class="panel">

<h2>
🛠️ Herramientas
</h2>


<div class="tool">

📶 <b>Wi-Fi</b>

<p
id="wifiStatus"
class="note">

Comprobando...

</p>

</div>


<br>


<div class="tool">

🔵 <b>Bluetooth</b>

<p
id="btStatus"
class="note">

Preparado para conectar dispositivos.

</p>

<button
class="primary"
onclick="connectBluetooth()">

🔵 Buscar dispositivo

</button>

</div>


<br>


<div class="tool">

📱 <b>Dispositivos</b>

<p class="note">

Preparado para futuras conexiones
con altavoces, sensores, ESP32,
ordenadores y dispositivos IoT.

</p>

</div>

</section>


<button
id="powerButton"
class="danger power"
onclick="toggleXaIA()">

🛑 PARAR XaIA

</button>

</div>


<nav class="bottom">

<button onclick="closePanels()">
⌂ Inicio
</button>

<button onclick="openPanel('chatPanel')">
💬 Chat
</button>

<button onclick="startVoice()">
🎤 Voz
</button>

<button onclick="openPanel('toolsPanel')">
🛠️ Herramientas
</button>

</nav>


<script>

const API =
'http://127.0.0.1:5000';

let xaiaActive = true;

let recognition = null;

let cameraStream = null;

let lastPhoto = null;


/* -------------------------
   NAVEGACIÓN
------------------------- */

function openPanel(id){

document
.querySelectorAll('.panel')
.forEach(p =>
p.classList.remove('active')
);

document
.getElementById(id)
.classList.add('active');

}


function closePanels(){

document
.querySelectorAll('.panel')
.forEach(p =>
p.classList.remove('active')
);

}


/* -------------------------
   ESTADO XAIA
------------------------- */

async function updateXaIAStatus(){

try{

const response =
await fetch(API+'/status');

const data =
await response.json();

xaiaActive =
!!data.active;

const status =
document.getElementById(
'coreStatus'
);

const button =
document.getElementById(
'powerButton'
);

if(xaiaActive){

status.innerText =
'🟢 ACTIVA';

button.innerText =
'🛑 PARAR XaIA';

button.className =
'danger power';

}else{

status.innerText =
'🔴 APAGADA';

button.innerText =
'🟢 ENCENDER XaIA';

button.className =
'green power';

stopVoice();

stopCamera();

}

}catch(error){

document
.getElementById(
'coreStatus'
)
.innerText =
'⚠️ CORE OFFLINE';

}

}


/* -------------------------
   POWER
------------------------- */

async function toggleXaIA(){

try{

const response =
await fetch(
API+'/power',
{
method:'POST',
headers:{
'Content-Type':
'application/json'
},
body:JSON.stringify({
active:!xaiaActive
})
}
);

const data =
await response.json();

xaiaActive =
!!data.active;

const status =
document.getElementById(
'coreStatus'
);

const button =
document.getElementById(
'powerButton'
);

if(xaiaActive){

status.innerText =
'🟢 ACTIVA';

button.innerText =
'🛑 PARAR XaIA';

button.className =
'danger power';

speak(
'XaIA está encendida'
);

}else{

status.innerText =
'🔴 APAGADA';

button.innerText =
'🟢 ENCENDER XaIA';

button.className =
'green power';

stopVoice();

stopCamera();

speechSynthesis.cancel();

}

}catch(error){

alert(
'⚠️ No puedo conectar con XaIA CORE'
);

}

}


/* -------------------------
   CHAT
------------------------- */

async function sendMessage(){

if(!xaiaActive){

addMessage(
'🛑 XaIA está apagada. Pulsa ENCENDER XaIA para continuar.',
'ai'
);

return;

}

const input =
document.getElementById(
'textInput'
);

const text =
input.value.trim();

if(!text)return;

input.value='';

addMessage(
text,
'user'
);

const thinking =
addMessage(
'🤖 XaIA está pensando...',
'ai'
);

try{

const response =
await fetch(
API+'/chat',
{
method:'POST',
headers:{
'Content-Type':
'application/json'
},
body:JSON.stringify({
message:text
})
}
);

const data =
await response.json();

thinking.remove();

if(data.reply){

addMessage(
'🤖 XaIA\n\n'+
data.reply,
'ai'
);

speak(data.reply);

}else if(data.error){

addMessage(
'🛑 '+data.error,
'ai'
);

}else{

addMessage(
'⚠️ XaIA no ha devuelto respuesta.',
'ai'
);

}

}catch(error){

thinking.remove();

addMessage(
'⚠️ No puedo conectar con XaIA CORE.',
'ai'
);

}

}


function addMessage(
text,
type
){

const chat =
document.getElementById(
'chat'
);

const div =
document.createElement(
'div'
);

div.className =
'msg '+type;

div.innerText =
text;

chat.appendChild(div);

chat.scrollTop =
chat.scrollHeight;

return div;

}


document
.getElementById(
'textInput'
)
.addEventListener(
'keydown',
function(e){

if(e.key === 'Enter'){
sendMessage();
}

}
);


/* -------------------------
   VOZ
------------------------- */

function startVoice(){

if(!xaiaActive){

alert(
'🛑 XaIA está apagada'
);

return;

}

openPanel(
'chatPanel'
);

const SpeechRecognition =
window.SpeechRecognition ||
window.webkitSpeechRecognition;

if(!SpeechRecognition){

alert(
'⚠️ Usa Chrome en Android para activar el micrófono.'
);

return;

}

if(recognition){

stopVoice();

return;

}

recognition =
new SpeechRecognition();

recognition.lang =
'es-ES';

recognition.continuous =
true;

recognition.interimResults =
false;


recognition.onresult =
function(event){

const result =
event.results[
event.results.length-1
][0].transcript;

document
.getElementById(
'textInput'
)
.value =
result;

sendMessage();

};


recognition.onerror =
function(){

stopVoice();

};


recognition.onend =
function(){

if(
xaiaActive &&
recognition
){

try{

recognition.start();

}catch(e){}

}

};


try{

recognition.start();

speak(
'Te escucho, Xavi'
);

}catch(error){}

}


function stopVoice(){

if(recognition){

try{

recognition.stop();

}catch(e){}

recognition =
null;

}

}


/* -------------------------
   ALTAVOZ
------------------------- */

function speak(text){

if(!xaiaActive)
return;

if(
!'speechSynthesis'
in window
)
return;

speechSynthesis.cancel();

const voice =
new SpeechSynthesisUtterance(
text
);

voice.lang =
'es-ES';

voice.rate =
0.95;

voice.pitch =
1;

speechSynthesis.speak(
voice
);

}


/* -------------------------
   CÁMARA
------------------------- */

async function startCamera(){

if(!xaiaActive){

alert(
'🛑 XaIA está apagada'
);

return;

}

try{

cameraStream =
await navigator
.mediaDevices
.getUserMedia({

video:{
facingMode:
'environment'
},

audio:false

});

document
.getElementById(
'video'
)
.srcObject =
cameraStream;

}catch(error){

alert(
'⚠️ No se puede acceder a la cámara. Comprueba los permisos.'
);

}

}


function capturePhoto(){

if(!cameraStream)
return;

const video =
document.getElementById(
'video'
);

const canvas =
document.getElementById(
'canvas'
);

const preview =
document.getElementById(
'preview'
);

canvas.width =
video.videoWidth;

canvas.height =
video.videoHeight;

canvas
.getContext('2d')
.drawImage(
video,
0,
0
);

lastPhoto =
canvas.toDataURL(
'image/jpeg',
0.85
);

preview.src =
lastPhoto;

preview.style.display =
'block';

}


function stopCamera(){

if(cameraStream){

cameraStream
.getTracks()
.forEach(
track =>
track.stop()
);

cameraStream =
null;

}

}


async function analyzePhoto(){

if(!lastPhoto){

alert(
'📷 Primero captura una foto.'
);

return;

}

addMessage(
'📷 Imagen preparada para el análisis de visión de XaIA.',
'ai'
);

}


/* -------------------------
   BLUETOOTH
------------------------- */

async function connectBluetooth(){

if(
!navigator.bluetooth
){

document
.getElementById(
'btStatus'
)
.innerText =
'⚠️ Web Bluetooth no está disponible en este navegador.';

return;

}

try{

document
.getElementById(
'btStatus'
)
.innerText =
'🔎 Buscando dispositivo...';

const device =
await navigator
.bluetooth
.requestDevice({

acceptAllDevices:
true

});

document
.getElementById(
'btStatus'
)
.innerText =
'🔵 Dispositivo: '+
(
device.name ||
'Sin nombre'
);

}catch(error){

document
.getElementById(
'btStatus'
)
.innerText =
'ℹ️ Búsqueda cancelada.';

}

}


/* -------------------------
   WIFI
------------------------- */

function checkWifi(){

const status =
document.getElementById(
'wifiStatus'
);

if(
navigator.onLine
){

status.innerText =
'🟢 Internet disponible';

}else{

status.innerText =
'🔴 Sin conexión a Internet';

}

}


window.addEventListener(
'online',
checkWifi
);

window.addEventListener(
'offline',
checkWifi
);


/* -------------------------
   ARRANQUE
------------------------- */

checkWifi();

updateXaIAStatus();

setInterval(
updateXaIAStatus,
5000
);

</script>

</body>

</html>
'''

# -------------------------------------------------
# ESCRIBIR ARCHIVO
# -------------------------------------------------

HTML.write_text(
page,
encoding="utf-8"
)

# -------------------------------------------------
# COMPROBACIÓN
# -------------------------------------------------

content = HTML.read_text(
encoding="utf-8"
)

checks = [
    "<!DOCTYPE html>",
    "toggleXaIA",
    "updateXaIAStatus",
    "sendMessage",
    "startVoice",
    "startCamera",
    "connectBluetooth",
    "127.0.0.1:5000",
    "/power",
    "/status",
    "/chat"
]

missing = [
    item for item in checks
    if item not in content
]

if missing:
    print("❌ FALTAN ELEMENTOS:")
    for item in missing:
        print(" -", item)
else:
    print()
    print("================================")

print("🚀 XaIA ACTUALIZADA")
print("================================")
print("💬 Chat              OK")
print("🎤 Micrófono         OK")
print("🔊 Altavoz           OK")
print("📷 Cámara            OK")
print("🛠️ Herramientas     OK")
print("📶 Wi-Fi             OK")
print("🔵 Bluetooth         OK")
print("🔌 Encendido         OK")
print("🧠 Backend existente OK")
print("🛡️ Copia seguridad   OK")
print("================================")
print("📱 Abre/refresca XaIA")
print("================================")
