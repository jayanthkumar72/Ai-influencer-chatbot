async function sendMessage() {
    const messageInput = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");

    const userMessage = messageInput.value.trim();

    if (!userMessage) return;

    // Show user message
    chatBox.innerHTML += `<div class="message-user">${userMessage}</div>`;

    messageInput.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userMessage })
        });

        const data = await response.json();

        // Show bot response
        chatBox.innerHTML += `<div class="message-bot">${data.response}</div>`;

        // Auto scroll
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        console.error("Error:", error);
    }
}

// Allow Enter key
document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("message");

    input.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});