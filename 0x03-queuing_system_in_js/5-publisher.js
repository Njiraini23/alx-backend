import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('connect', function() {
  console.log('Redis client connected to the server');
});

redisClient.on('error', function(error) {
  console.log(`Redis client to the server: ${error.message}`);
});

function publishMessage(message, time) {
  // the message to be published
  setTimeout(function () {
    console.log(`About to send ${message}`);
    redisClient.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton student #1 starts course", 100);
publishMessage("Holberton student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton student #3 starts course", 400);
