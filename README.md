## Project Update: Motion Sensor Project

**Date:** May 5, 2025

**Previous Project:** Weather Station

**Current Project:** IoT Motion Sensor with Azure Data Explorer Visualization

### Project Description and Changes

The project has shifted its focus from a weather station to an IoT motion sensor project with data visualization in Azure Data Explorer. The core idea remains the same - to collect data from a sensor and send it to the cloud - but the specific application and the cloud service used for visualization have changed.

**Key Changes:**

* **Sensor:** Instead of collecting temperature and humidity data, the project now uses a motion sensor to detect movement.
* **Data:** The data being collected is the motion status (motion detected or no motion) and a timestamp.
* **Actuation:** An LED is used to indicate when motion is detected.
* **Cloud Visualization:** Instead of initially using a general-purpose visualization, the project now uses Azure Data Explorer, a fast and fully managed data analytics service for exploration.
* **Focus:** The project now focuses on detecting and logging motion events and visualizing these events in near real-time.

### Reasons for the Change:

* **Data Visualization with Azure Data Explorer:** This allows for a more robust and interactive data visualization.
* **Real-time Analysis:** Motion data can be effectively visualized in near real-time, providing a clear demonstration of how quickly data can be ingested and analyzed in a cloud environment.

### Current Status:

* The motion sensor is set up and connected to a Raspberry Pi.
* The Python script to read data from the motion sensor and send it to Azure IoT Hub is functional.
* Data is being ingested into Azure Data Explorer.
* A time series chart has been created in Azure Data Explorer to visualize the motion data.

