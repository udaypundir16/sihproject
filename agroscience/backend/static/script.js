// Initialize charts when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeCharts();
    fetchWeather();
    loadMarketPrices();
});

// Initialize all charts
function initializeCharts() {
    // Fertilizer composition chart
    const fertilizerCtx = document.getElementById('fertilizerChart').getContext('2d');
    window.fertilizerChart = new Chart(fertilizerCtx, {
        type: 'doughnut',
        data: {
            labels: ['Nitrogen', 'Phosphorus', 'Potassium', 'Other'],
            datasets: [{
                data: [40, 25, 25, 10],
                backgroundColor: [
                    '#4CAF50',
                    '#8BC34A',
                    '#CDDC39',
                    '#FFC107'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });

    // Market trends chart
    const marketCtx = document.getElementById('marketTrendsChart').getContext('2d');
    window.marketTrendsChart = new Chart(marketCtx, {
        type: 'line',
        data: {
            labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4'],
            datasets: [
                {
                    label: 'Wheat',
                    data: [2050, 2080, 2100, 2100],
                    borderColor: '#4CAF50',
                    tension: 0.1,
                    fill: false
                },
                {
                    label: 'Rice',
                    data: [2450, 2480, 2500, 2500],
                    borderColor: '#2196F3',
                    tension: 0.1,
                    fill: false
                },
                {
                    label: 'Corn',
                    data: [1820, 1810, 1800, 1800],
                    borderColor: '#FFC107',
                    tension: 0.1,
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: false,
                    title: {
                        display: true,
                        text: 'Price (₹/quintal)'
                    }
                }
            }
        }
    });

    // Rainfall prediction chart
    const rainfallCtx = document.getElementById('rainfallChart').getContext('2d');
    window.rainfallChart = new Chart(rainfallCtx, {
        type: 'bar',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Rainfall (mm)',
                data: [2, 5, 12, 8, 3, 0, 0],
                backgroundColor: '#2196F3',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Rainfall (mm)'
                    }
                }
            }
        }
    });

    // Crop yield prediction chart
    const yieldCtx = document.getElementById('yieldPredictionChart').getContext('2d');
    window.yieldChart = new Chart(yieldCtx, {
        type: 'radar',
        data: {
            labels: ['Soil Quality', 'Water Availability', 'Temperature', 'Sunlight', 'Pest Control'],
            datasets: [{
                label: 'Current Conditions',
                data: [75, 60, 80, 70, 65],
                backgroundColor: 'rgba(76, 175, 80, 0.2)',
                borderColor: '#4CAF50',
                pointBackgroundColor: '#4CAF50'
            }, {
                label: 'Optimal Conditions',
                data: [90, 85, 75, 80, 90],
                backgroundColor: 'rgba(33, 150, 243, 0.2)',
                borderColor: '#2196F3',
                pointBackgroundColor: '#2196F3'
            }]
        },
        options: {
            responsive: true,
            scales: {
                r: {
                    angleLines: {
                        display: true
                    },
                    suggestedMin: 0,
                    suggestedMax: 100
                }
            }
        }
    });
}

// Fertilizer calculator function
function calculateFertilizer() {
    const crop = document.getElementById('crop').value;
    const area = document.getElementById('area').value;
    const soil = document.getElementById('soil').value;
    
    if (!area || area <= 0) {
        alert('Please enter a valid land area');
        return;
    }
    
    // Simple calculation based on crop type
    let nitrogen, phosphorus, potassium;
    
    switch(crop) {
        case 'wheat':
            nitrogen = 120 * area;
            phosphorus = 60 * area;
            potassium = 40 * area;
            break;
        case 'rice':
            nitrogen = 100 * area;
            phosphorus = 50 * area;
            potassium = 50 * area;
            break;
        case 'corn':
            nitrogen = 150 * area;
            phosphorus = 70 * area;
            potassium = 70 * area;
            break;
        case 'sugarcane':
            nitrogen = 200 * area;
            phosphorus = 80 * area;
            potassium = 100 * area;
            break;
        case 'cotton':
            nitrogen = 80 * area;
            phosphorus = 40 * area;
            potassium = 30 * area;
            break;
        default:
            nitrogen = 100 * area;
            phosphorus = 50 * area;
            potassium = 50 * area;
    }
    
    // Adjust based on soil type
    if (soil === 'sandy') {
        nitrogen *= 1.2;
        phosphorus *= 1.1;
        potassium *= 1.1;
    } else if (soil === 'clay') {
        nitrogen *= 0.9;
        phosphorus *= 0.9;
        potassium *= 0.9;
    } else if (soil === 'silt') {
        nitrogen *= 1.0;
        phosphorus *= 1.0;
        potassium *= 1.0;
    }
    
    const resultDiv = document.getElementById('fertilizer-result');
    resultDiv.innerHTML = `
        <h3>Recommended Fertilizer for ${area} acres of ${crop} (${soil} soil):</h3>
        <p>Nitrogen: ${nitrogen.toFixed(2)} kg</p>
        <p>Phosphorus: ${phosphorus.toFixed(2)} kg</p>
        <p>Potassium: ${potassium.toFixed(2)} kg</p>
    `;
    
    // Update the chart
    window.fertilizerChart.data.datasets[0].data = [
        nitrogen, phosphorus, potassium, (nitrogen * 0.1)
    ];
    window.fertilizerChart.update();
}

// Fetch weather data (simulated)
function fetchWeather() {
    const weatherDiv = document.getElementById('weather-info');
    
    // In a real application, you would fetch this from a weather API
    const weatherData = {
        temperature: 28,
        condition: 'Sunny',
        humidity: 65,
        wind: 12,
        forecast: [
            { day: 'Today', temp: 28, icon: 'fa-sun', condition: 'Sunny' },
            { day: 'Tomorrow', temp: 27, icon: 'fa-cloud-sun', condition: 'Partly cloudy' },
            { day: 'Next Day', temp: 25, icon: 'fa-cloud-rain', condition: 'Light showers' }
        ]
    };
    
    let forecastHTML = '<div class="weather-container">';
    weatherData.forecast.forEach(day => {
        forecastHTML += `
            <div class="weather-card">
                <h3>${day.day}</h3>
                <div class="weather-icon"><i class="fas ${day.icon}"></i></div>
                <div class="temperature">${day.temp}°C</div>
                <p>${day.condition}</p>
            </div>
        `;
    });
    forecastHTML += '</div>';
    
    weatherDiv.innerHTML = forecastHTML;
}

// Load market prices (simulated)
function loadMarketPrices() {
    // In a real application, you would fetch this from an API
    const prices = [
        { crop: 'Wheat', price: '₹2100 / quintal', trend: 'up', change: '2.5%' },
        { crop: 'Rice', price: '₹2500 / quintal', trend: 'up', change: '1.8%' },
        { crop: 'Corn', price: '₹1800 / quintal', trend: 'down', change: '0.8%' }
    ];
    
    const pricesList = document.querySelector('#market-prices ul');
    pricesList.innerHTML = '';
    
    prices.forEach(item => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            ${item.crop}: ${item.price} 
            <span class="trend ${item.trend}">${item.trend === 'up' ? '↑' : '↓'} ${item.change} from last week</span>
        `;
        pricesList.appendChild(listItem);
    });
}

// Chatbot functions
function toggleChat() {
    const chatWindow = document.getElementById('chat-window');
    chatWindow.style.display = chatWindow.style.display === 'flex' ? 'none' : 'flex';
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function sendMessage() {
    const input = document.getElementById('chat-input');
    const message = input.value.trim();
    
    if (message === '') return;
    
    // Add user message
    addMessage(message, 'user');
    input.value = '';
    
    // Generate bot response after a short delay
    setTimeout(() => {
        generateBotResponse(message);
    }, 500);
}

function addMessage(text, sender) {
    const messagesContainer = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
    messageDiv.textContent = text;
    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function generateBotResponse(userMessage) {
    const lowerMessage = userMessage.toLowerCase();
    let response = '';
    
    if (lowerMessage.includes('fertilizer') || lowerMessage.includes('nutrient')) {
        response = 'For fertilizer recommendations, use our calculator tool above. It considers your crop type, land area, and soil type to give personalized suggestions.';
    } else if (lowerMessage.includes('weather') || lowerMessage.includes('rain')) {
        response = 'Check the weather section for detailed forecasts and rainfall predictions. This can help you plan your irrigation and harvesting activities.';
    } else if (lowerMessage.includes('price') || lowerMessage.includes('market')) {
        response = 'Current market prices are available in the Market Prices section. You can see trends for wheat, rice, corn and other crops.';
    } else if (lowerMessage.includes('hello') || lowerMessage.includes('hi')) {
        response = 'Hello! How can I assist with your farming needs today?';
    } else if (lowerMessage.includes('bye') || lowerMessage.includes('thank')) {
        response = 'You\'re welcome! Feel free to ask if you have more questions.';
    } else if (lowerMessage.includes('pest') || lowerMessage.includes('disease')) {
        response = 'For pest and disease management, I recommend consulting with local agricultural experts. You can also visit the pesticides section for recommended treatments.';
    } else if (lowerMessage.includes('crop') || lowerMessage.includes('plant')) {
        response = 'The best crops to plant depend on your soil type, climate, and market demand. Our crop prediction tool can help you make informed decisions.';
    } else {
        response = 'I\'m here to help with farming-related questions. You can ask me about fertilizers, weather, market prices, or other agricultural topics.';
    }
    
    addMessage(response, 'bot');
}

// Smooth scrolling for navigation links
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);
        
        window.scrollTo({
            top: targetElement.offsetTop - 80,
            behavior: 'smooth'
        });
    });
});

// Lazy loading for images
if ('IntersectionObserver' in window) {
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    lazyImages.forEach(img => {
        imageObserver.observe(img);
    });
}