import requests
import gmail  # You may need to install the gmail library using pip
import time

# ThingSpeak channel and API key
channel_id = 2373887
read_api_key = "QSFKKBCECY1FIDUQ"

api_url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?results=2&api_key={read_api_key}"

# Create a MailClient object to send email alerts (assuming gmail library is configured)
mclient = gmail.MailClient()

# Track the last time an alert was sent for each sensor (temperature, humidity, gas)
last_temp_alert_time = time.time()
last_hum_alert_time = time.time()
last_gas_alert_time = time.time()

while True:
  current_time = time.time()

  try:
    # Send a GET request to the ThingSpeak API to get the latest sensor readings
    response = requests.get(api_url)

    if response.status_code == 200:
      # Parse the JSON response
      data = response.json()

      # Extract the temperature, humidity, and gas readings from the latest feed entry
      temp = float([entry['field1'] for entry in data['feeds']][-1])
      hum = float([entry['field2'] for entry in data['feeds']][-1])
      gas = float([entry['field3'] for entry in data['feeds']][-1])

        

      # Check if temperature is high and send an email alert 
        if temp >= 23 and current_time - last_temp_alert_time >= 30:  # Send alert only if 30 seconds have passed since the last alert
        mclient.subject = "!!! Alert Temperature High"
        mclient.body = f"Warning! Your room temperature is {temp} degrees Celsius."
        mclient.send()
        print("Temperature alert sent.")
        last_temp_alert_time = current_time  # Update last alert time

        

      # Check if humidity is high and send an email alert
      if hum >= 55 and current_time - last_hum_alert_time >= 10:  # Send alert only if 10 seconds have passed since the last alert
        mclient.subject = "!!! Alert Humidity is High"
        mclient.body = f"Warning! Your room humidity is {hum} percent."
        mclient.send()
        print("Humidity alert sent.")
        last_hum_alert_time = current_time  # Update last alert time

        

      # Check if gas level is high and send an email alert 
      if gas >= 80 and current_time - last_gas_alert_time >= 10:  # Send alert only if 10 seconds have passed since the last alert
        mclient.subject = "!!! Alert Gas PPM is High"
        mclient.body = f"Warning! Your room gas level is {gas} PPM."
        mclient.send()
        print("Gas alert sent.")
        last_gas_alert_time = current_time  # Update last alert time


    else:
      print("Error:", response.status_code, response.text)

  except Exception as e:
    print("An error occurred:", str(e))

  # Wait for 1 second before checking again
  time.sleep(1)
