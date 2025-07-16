
const ws = new WebSocket("wss://heroku-chat.up.railway.app/ws");


const input = document.getElementById("input");
const messages = document.getElementById("messages");


window.onload = () => input.focus();


input.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    sendMessage();
  }
});


ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  displayMessage(data.reply, "bot");
};


function sendMessage() {
  const message = input.value.trim();
  if (message === "") return;

  displayMessage(message, "user");
  ws.send(message);
  input.value = "";
}


function displayMessage(text, type) {
  const msg = document.createElement("div");
  msg.className = `message ${type}`;
  msg.textContent = text;
  messages.appendChild(msg);

  messages.scrollTop = messages.scrollHeight;
}
