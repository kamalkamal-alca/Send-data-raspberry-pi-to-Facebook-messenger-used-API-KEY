# Send-data-raspberry-pi-to-Facebook-messenger-used-API-KEY
send data to facebook messenger used raspberry pi &amp; python
1- go to https://m.me/api.callmebot
2- connect with your messenger account
3- Send "create apikey" to @api.callmebot (using Facebook Messenger of course)
4- The bot will generate a secure apikey for you.
5- The bot will answer you with your personal apikey .
6- You can now start sending notifications to yourself through Facebook Messenger

How to send a Text notification through Facebook Messenger
https://api.callmebot.com/facebook/send.php?apikey=[your_apikey]&text=[message]
[your_apikey]: The apikey that you received during the activation process (step 4-5 above)
[text]: Message to send (urlencoded). You can use this online converter to encode the message. (i.e. %20 for space, %0A for new lines). Facebook Messenger formatting characters are allowed (i.e "*" for bold, etc.  but it will be only visible in the Web Client). Check here how to include emoticons in the message 👍.

Example:
https://api.callmebot.com/facebook/send.php?apikey=1234567890&text=This+is+a+test+from+my+appliance+%F0%9F%98%84
How to send an Image through Facebook Messenger
https://api.callmebot.com/facebook/send.php?apikey=[your_apikey]&image=[image_url]
[your_apikey]: The apikey that you received during the activation process (step 4-5 above)
[image_url]: URL of the image to send. The URL has to be urlencoded. You can use this online converter to encode the message. (i.e. %20 for space).

Example:

https://api.callmebot.com/facebook/send.php?apikey=1234567890&image=https://d17fnq9dkz9hgj.cloudfront.net/breed-uploads/2018/08/beagle-card-medium.jpg
