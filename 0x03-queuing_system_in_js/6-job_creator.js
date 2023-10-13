import { createQueue } from 'kue';

const queue = createQueue();

const notification = {
  'phoneNumber': '123123123'
  'message': 'please verify your email'
}

const job = queue.create('push_notification_code', notification).save( function(err) {
  if (!err)
    console.log(`Notification job completed: ${job.id}`);
  }
});
   
job.on('complete', function() {
  console.log('Notification job completed');
}).on('failed', function() {
  console.log('Notification job failed');
});
