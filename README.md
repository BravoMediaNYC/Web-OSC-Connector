# OSC REST Proxy

This project provides a way to connect an HTML page with an OSC (Open Sound Control) application like Touch Designer. It consists of a Python script (`OSCRestProxy.py`) that sets up a REST API using Flask and a simple HTML page (`index.html`) that interacts with the API to send OSC messages.

## Prerequisites

* Python 3.x
* Flask
* Flask-Cors
* python-osc

## Installation

1. Install the required Python packages:

   **pip** **install** **python-osc** **Flask** **Flask-Cors**
2. Save the [OSCRestProxy.py](vscode-file://vscode-app/c:/Users/Porthos/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) and [index.html](vscode-file://vscode-app/c:/Users/Porthos/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) files in your project directory.

## Usage

### Running the OSC REST Proxy

1. Start the Flask server by running the [OSCRestProxy.py](vscode-file://vscode-app/c:/Users/Porthos/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) script:

   **python** **OSCRestProxy.py**
2. The server will be running on `http://127.0.0.1:5000`.

### HTML Page

Open [index.html](vscode-file://vscode-app/c:/Users/Porthos/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) in a web browser. This page contains sliders and a text box that allow you to send data to the OSC application.

### OSC Receiver
We are using `Touch Designer` as the OSC receiver. You can set up Touch Designer to listen for OSC messages on the same port (e.g., `7287`) and process them accordingly.

The example file is provided at `OSCReciever.toe`.


### API Endpoints

#### `/sayHi`

* **Method:** POST
* **Description:** Sends a "sayHi" message to the OSC client.
* **Request Body:**
```json
  {
      "message": "Hello"
  }
  ```

#### `/sendData`

* **Method:** POST
* **Description:** Sends generic data to the OSC client.
* **Request Body:**

```json
  {

      "data": "Some data"

  }
  ```


#### `/sendOSCMessage`

* **Method:** POST
* **Description:** Sends a custom OSC message to the OSC client.
* **Request Body:**


```json
  {

      "address": "/customAddress",
      "data": "Some data"

  }
  ```


## HTML Page Functionality

### Sliders

The HTML page contains two sliders. When the slider value changes, it sends the value to the OSC client using the `/sendOSCMessage` endpoint with the address `/slider1` or `/slider2`.

### Text Box

The HTML page contains a text box. When the "Send Text Box Data" button is clicked, it sends the text box value to the OSC client using the `/sendOSCMessage` endpoint with the address `/textBox`.

## Example

1. Move the sliders or enter text in the text box on the HTML page.
2. The corresponding data will be sent to the OSC client (e.g., Touch Designer) via the Flask server.

This setup allows for a flexible and generic way to send data from a web interface to an OSC application.
