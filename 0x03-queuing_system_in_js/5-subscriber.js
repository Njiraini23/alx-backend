import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('connect', function() {
  console.log('Redis cient connected to the server');

redisClient.on('error', function(error) {
  console.log(`Redis client not connected to the server: ${error.messagei}`);
});

// subscribe to the channel
redisClient.subscribe('holberton school channel');

// listen to the messages in the channel
redisClient.on('message', function (channel, message) {
  console.log(`${message}`):
  if (message === 'KILL_SERVER') {
  // unsubscribe from the channel
    redisClient.unsubscribe('holberton school channel');
    redisClient.end(true);
  }
});
