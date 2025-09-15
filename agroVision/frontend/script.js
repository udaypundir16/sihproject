async function calculateFertilizer() {
  const crop = document.getElementById("crop").value;
  const area = document.getElementById("area").value;
  const soil = document.getElementById("soil").value;

  const res = await fetch("http://127.0.0.1:5000/fertilizer", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({crop, area, soil})
  });
  const data = await res.json();
  document.getElementById("fertilizer-result").innerHTML = 
    `N: ${data.N.toFixed(2)} kg, P: ${data.P.toFixed(2)} kg, K: ${data.K.toFixed(2)} kg`;
}

function toggleChat(){
  document.getElementById("chat-window").style.display =
    document.getElementById("chat-window").style.display === "flex" ? "none" : "flex";
}

async function sendMessage() {
  const input = document.getElementById("chat-input");
  const msg = input.value;
  if(!msg) return;

  const messages = document.getElementById("chat-messages");
  messages.innerHTML += `<div class='user'>${msg}</div>`;
  input.value = "";

  const res = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({message: msg})
  });
  const data = await res.json();
  messages.innerHTML += `<div class='bot'>${data.reply}</div>`;
  messages.scrollTop = messages.scrollHeight;
}
