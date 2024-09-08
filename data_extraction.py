import requests
import gmail
import time

channel_id = 2373887
read_api_key = "QSFKKBCECY1FIDUQ"

api_url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?results=2&api_key={read_api_key}"

mclient = gmail.MailClient()

last_temp_alert_time = time.time()
last_hum_alert_time = time.time()
last_gas_alert_time = time.time()

while True:
    current_time = time.time()
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            
            # Extracting values from fields
            temp = float([entry['field1'] for entry in data['feeds']][-1])
            hum = float([entry['field2'] for entry in data['feeds']][-1])
            gas = float([entry['field3'] for entry in data['feeds']][-1])

            if temp >= 23:
                mclient.subject = "!!! Alert Temperature High"
                mclient.body = f"Warrning your room temperature is {temp}"
                mclient.send()
                print("temperature high")
                time.sleep(30)
            
            if hum >= 55:
                mclient.subject = "!!! ALert Humidity is High"
                mclient.body = f"Warrning your room humidity is {hum}"
                mclient.send()
                print("humidity high")
                time.sleep(10)


            if gas >= 80:
                mclient.subject = "!!! ALert gas ppm is High"
                mclient.body = f"Warrning your room gas ppm is {gas}"
                mclient.send()
                print("gas ppm high")
                time.sleep(10)
            


        else:
            print("Error:", response.status_code, response.text)

    except Exception as e:
        print("An error occurred:", str(e))

    time.sleep(1)

