// app.js
document.addEventListener('DOMContentLoaded', function() {
    // Initialize Chart.js for market prices
    const priceCtx = document.getElementById('priceChart').getContext('2d');
    const priceChart = new Chart(priceCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'],
            datasets: [
                {
                    label: 'Wheat',
                    data: [20, 21, 22, 21, 22, 23, 22, 21, 22, 22.5],
                    borderColor: '#4caf50',
                    tension: 0.1
                },
                {
                    label: 'Rice',
                    data: [30, 32, 31, 33, 34, 35, 34, 33, 34, 35.75],
                    borderColor: '#ff9800',
                    tension: 0.1
                },
                {
                    label: 'Corn',
                    data: [17, 17.5, 18, 18.5, 18, 18.5, 19, 18.5, 19, 19.2],
                    borderColor: '#795548',
                    tension: 0.1
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Price Trends (₹/kg)',
                    color: '#2e7d32'
                }
            }
        }
    });

    // Crop prediction functionality
    const predictBtn = document.querySelector('.btn-predict');
    if (predictBtn) {
        predictBtn.addEventListener('click', function() {
            const soilType = document.getElementById('soil-type').value;
            const rainfall = document.getElementById('rainfall').value;
            const temperature = document.getElementById('temperature').value;
            const ph = document.getElementById('ph').value;
            
            // Mock prediction logic
            let crop = "Rice";
            let yieldEstimate = "4.2";
            
            if (soilType === "sandy" && rainfall < 600) {
                crop = "Millets";
                yieldEstimate = "3.5";
            } else if (soilType === "clay" && temperature > 30) {
                crop = "Cotton";
                yieldEstimate = "2.8";
            }
            
            document.querySelector('.prediction-result h3').textContent = `Recommended: ${crop}`;
            document.querySelector('.prediction-result p').textContent = `Expected Yield: ${yieldEstimate} tons/acre`;
        });
    }

    // Fertilizer calculator
    const calculateBtn = document.querySelector('.btn-calculate');
    if (calculateBtn) {
        calculateBtn.addEventListener('click', function() {
            const cropType = document.getElementById('crop-type').value;
            const area = document.getElementById('area').value;
            
            // Mock calculation
            let recommendation = "50-40-30 kg/acre";
            
            if (cropType === "rice") {
                recommendation = "60-50-40 kg/acre";
            } else if (cropType === "corn") {
                recommendation = "45-35-30 kg/acre";
            }
            
            document.querySelector('.calculation-result p').textContent = `N-P-K Recommendation: ${recommendation}`;
        });
    }

    // Add to cart functionality
    const addButtons = document.querySelectorAll('.btn-add');
    addButtons.forEach(button => {
        button.addEventListener('click', function() {
            const product = this.closest('.product-card').querySelector('h4').textContent;
            alert(`${product} added to cart!`);
        });
    });

    // Chat functionality
    const chatInput = document.querySelector('.chat-input input');
    const chatSend = document.querySelector('.chat-input button');
    
    if (chatSend) {
        chatSend.addEventListener('click', function() {
            if (chatInput.value.trim() !== '') {
                const messageContainer = document.querySelector('.chat-messages');
                const newMessage = document.createElement('div');
                newMessage.classList.add('message', 'my-message');
                newMessage.innerHTML = `<span class="sender">You:</span> <span class="text">${chatInput.value}</span>`;
                messageContainer.appendChild(newMessage);
                chatInput.value = '';
                messageContainer.scrollTop = messageContainer.scrollHeight;
                
                // Mock reply after a short delay
                setTimeout(() => {
                    const reply = document.createElement('div');
                    reply.classList.add('message');
                    reply.innerHTML = `<span class="sender">Rajesh Kumar:</span> <span class="text">Thanks for the information!</span>`;
                    messageContainer.appendChild(reply);
                    messageContainer.scrollTop = messageContainer.scrollHeight;
                }, 1000);
            }
        });
    }
});