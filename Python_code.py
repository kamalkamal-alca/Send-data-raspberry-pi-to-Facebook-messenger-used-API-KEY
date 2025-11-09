import Adafruit_DHT,time
import requests

DHT = 'P9_11'
#https://api.callmebot.com/facebook/send.php?apikey=xaX1lqjWlKiNmQ1C&text=This+is+a+test
# Facebook API URL
apiKey = "xxxxxxxxxxxxxxxx"
#url = "https://api.callmebot.com/facebook/send.php?apikey=[your_apikey]&text=[message] # send textdirect to facebook messenger, change apikey and text
url = "https://api.callmebot.com/facebook/send.php"

def send_message(message):
    """Sends a message to Signal."""
    params = {
        'apikey': apiKey,
        'text': message
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print("Message sent successfully.")
        else:
            print(f"Error sending message. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")
    except Exception as e:
        print(f"Exception occurred: {e}")

def get_temperature():
    """Read the temperature and humidity from the DHT11 sensor."""
    humidity, temperature = Adafruit_DHT.read_retry(11, DHT)
    
    if temperature is not None and humidity is not None:
        return temperature, humidity
    else:
        print("Failed to get reading from the DHT sensor.")
        return None, None

# Main loop: send temperature and humidity every minute
try:
    print("Monitoring temperature and sending data every minute.")
    while True:
        temperature, humidity = get_temperature()
        if temperature is not None and humidity is not None:
            message = f"Temperature: {temperature}*C -- Humidity: {humidity}%"
            print(f"Sending message: {message}")
            send_message(message)
        time.sleep(60)  # Wait for 1 minute before sending the next reading

except KeyboardInterrupt:
    print("Program interrupted")
