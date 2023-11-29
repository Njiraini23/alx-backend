import { createClient } from 'redis';

const redisClient = createClient();

//create connection to server
redisClient.on('connect', function () {
  console.log('Redis client connected to the server');
});

redisClient.on('error', function (error) {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

//subscribing to the channel
redisClient.subscribe('holberton school channel');

//listen for any messages on channel
redisClient.on('message', function (channel, message) {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
  // unsubscribe form the channel
    redisClient.unsubscribe('holberton school channel');
    redisClient.end(true);
  }
});
