# Mail-Sending-code
---

This Python code monitors sensor readings from a ThingSpeak channel and sends email alerts when certain threshold values are exceeded.

Key functionalities:

**Data Fetching:<br/>**
        Retrieves sensor data (temperature, humidity, gas) from a specified ThingSpeak channel using the requests library.
        Parses the JSON response from the ThingSpeak API to extract the latest readings.

**Alert Logic:<br/>**
        Compares the current sensor readings with predefined threshold values.
        If a threshold is exceeded:
            Sends an email alert using the gmail library.
            Includes the sensor reading and a warning message in the email body.
            Prevents rapid alert spamming by introducing a time delay (e.g., 30 seconds for temperature, 10 seconds for humidity and gas) before sending another alert for the same sensor.

**Error Handling:<br/>**
        Includes try-except blocks to handle potential errors during API requests, data parsing, or email sending.
        Prints informative error messages to the console.

**Continuous Monitoring:<br/>**
        Runs in an infinite loop (while True) to continuously monitor sensor readings and send alerts as needed.
        Includes a time.sleep(1) to avoid overloading the system.

**Note:**

> **This code assumes the gmail library is installed and configured correctly.<br/>**
> **Storing API keys and passwords directly in the code is generally not recommended for security reasons.<br/>**
> **It's crucial to replace the placeholder values for channel_id, read_api_key, and email credentials with your actual values.<br/>**



This code provides a basic framework for monitoring sensor data and sending alerts.

![Screenshot 2025-01-27 193439](https://github.com/user-attachments/assets/86cf31de-02e8-41ad-a774-53463c835ab9)


