import { createClient } from 'redis';

function redisConnect() {
  const client = createClient();

  client.on('connect', function() {
  
})
