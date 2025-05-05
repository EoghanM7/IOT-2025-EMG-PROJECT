#The Imports needed for the projects.
import RPi.GPIO as GPIO
import time
import json
from azure.iot.device import IoTHubDeviceClient, Message

# Declaring the connection ports for the modules
MOTION_SENSOR_PIN = 5
LED_PIN = 18

#The connection string for my Azure IOT HUB
CONNECTION_STRING = "HostName=Weather-StationEMCG2025.azure-devices.net;DeviceId=Motion-Sensor;SharedAccessKey=/QxXMJ8wIVyZuIqhrzyKu26X8B5XL9c56jdOZnlwtfQ="

#This line of code ensures there is no delay between the motion state changing and sending the message. 
MSG_SEND_INTERVAL = 0

def main():
    try:

#Sets the mode for the GPIO pins to broadcom and then setups the pins for the sensor for in and out signals
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)
        GPIO.setup(LED_PIN, GPIO.OUT)
#The connection string for the IOTHub creating an instance usedt to communicate with the Hub
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
        print("IoT Hub Device Client created")

        print("Monitoring motion sensor. LED will light up when motion is detected. Sending status to Azure...")
#Variable for the state of the motion detector
        motion_detected_prev = False

#the loop to continuously  monitor the motion sensor
        while True:
            motion_detected = GPIO.input(MOTION_SENSOR_PIN)
#the logic for handling the  led light and tracking the motion sensor. And sending the JSON format to the IOTHUB
            if motion_detected and not motion_detected_prev:
                GPIO.output(LED_PIN, GPIO.HIGH)
                motion_status = "motion_detected"
                print(f"Motion detected! LED on. Sending '{motion_status}' to Azure.")
                telemetry_data = {
                    "motion_status": motion_status,
                    "timestamp": time.time()
                }
                msg = Message(json.dumps(telemetry_data))
                msg.custom_properties["event_type"] = "motion_detection"
                client.send_message(msg)
                print("Message sent!")
# Logic for when the motion sensor has not detected motion and switches off the LED and then sends the message to the  IOTHUB
            elif not motion_detected and motion_detected_prev:
                GPIO.output(LED_PIN, GPIO.LOW)
                motion_status = "no_motion"
                print(f"Motion stopped. LED off. Sending '{motion_status}' to Azure.")
                telemetry_data = {
                    "motion_status": motion_status,
                    "timestamp": time.time()
                }
                msg = Message(json.dumps(telemetry_data))
                msg.custom_properties["event_type"] = "motion_detection"
                client.send_message(msg)
                print("Message sent!")

            motion_detected_prev = motion_detected

            time.sleep(0.1)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        GPIO.cleanup()
        if 'client' in locals() and client:
            client.shutdown()
            print("IoT Hub Device Client shut down")

if __name__ == "__main__":
    main()