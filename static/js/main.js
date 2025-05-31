
<!-- static/js/main.js -->
// WebSocket for real-time meal logs
const mealLogSocket = new WebSocket((location.protocol === 'https:' ? 'wss://' : 'ws://') + window.location.host + '/ws/meal-log/');
mealLogSocket.onmessage = function(e) {
  const data = JSON.parse(e.data);
  console.log('Meal log:', data);
  // Optionally update a live log section
};