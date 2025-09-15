async function sendMessage() {
  const inputField = document.getElementById("user-input");
  const message = inputField.value.trim();
  if (!message) return;

  const chatBox = document.getElementById("chat-box");

  // Display user message
  const userMsg = document.createElement("div");
  userMsg.classList.add("message", "user");
  userMsg.textContent = "👤 You: " + message;
  chatBox.appendChild(userMsg);

  inputField.value = "";

  // Send to backend
  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();

    const botMsg = document.createElement("div");
    botMsg.classList.add("message", "bot");
    botMsg.textContent = "🤖 Bot: " + (data.response || data.error);
    chatBox.appendChild(botMsg);

    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (err) {
    const errorMsg = document.createElement("div");
    errorMsg.classList.add("message", "bot");
    errorMsg.textContent = "⚠️ Error connecting to server.";
    chatBox.appendChild(errorMsg);
  }
}
