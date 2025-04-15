# HTTP File Upload using Flask & Requests

## Project Overview

This project demonstrates how to implement file uploads using HTTP **POST** requests. It consists of two parts:

- **Client-side**: A Python script that sends the file to the server using the `requests` library.
- **Server-side**: A Flask application that listens for the file upload and saves it to a directory.

---

## Workflow

### Client-Side (File Upload Request):

- The client sends a **POST** request to the server with the file as part of the request body.
- The `requests` library in Python is used to open the file and send it to the server. The file is sent as a part of the `multipart/form-data` content type, which is suitable for file uploads.
- The request includes the file in a dictionary (e.g., `{'file': open('example.txt', 'rb')}`) where the key is the field name that the server expects (in this case, `'file'`).

### Server-Side (File Handling):

- The server is a Flask application that listens for incoming **POST** requests at the `/upload` route.
- Upon receiving the file, the server checks if the file exists in the request, if the file has a name, and if it is valid. If any of these checks fail, it returns an error message.
- If the file passes validation, it is saved to the `uploads/` folder with its original filename.

### Communication:

- The **HTTP POST** request is used by the client to send the file to the server.
- The server receives the request, extracts the file from the request body, and saves it locally.
- Once the file is saved, the server responds to the client with a success message.

---

## Process Flow:

### Client:

- Prepares a file (e.g., `example.txt`) to be uploaded.
- Sends the file to the server using an **HTTP POST** request.

### Server:

- Accepts the incoming request and retrieves the file.
- Validates the file (checks if it's present and non-empty).
- Saves the file to a local directory (`uploads/`).
- Returns a response indicating the file was successfully uploaded.

### Result:

- After the client successfully uploads the file, the server confirms by sending a message like "File example.txt uploaded successfully."
- The uploaded file is saved in the `uploads/` directory, which is a part of the project folder.

---

## Key Concepts:

- **HTTP POST**: This is the method used to send data to the server. In this case, it's used to send the file.
- **Multipart/Form-Data**: This is the encoding type used when sending files in a POST request. It allows the file to be split into parts and transmitted.
- **Flask**: A lightweight Python framework used to build the web server. It listens for incoming requests, processes them, and responds to the client.
- **Requests Library**: A simple HTTP library for Python, used to send HTTP requests, including file uploads.

---

## Error Handling:

- **No File Found**: If the client does not include a file in the request, the server will respond with an error message like **"No file part."**
- **Empty File Name**: If the file has no name (e.g., it's not selected), the server will respond with **"No selected file."**

---

## Server Setup and Execution:

1. **Start the Server**: The Flask server runs locally on `localhost:5000`. The client sends a request to this server.
2. **Client Upload**: Once the client sends the request with the file, the server processes it and saves the file in the `uploads/` folder.
3. **Confirm Upload**: The server responds with a success message, and the file is saved on the server.

---

## Requirements:

To run this project, you need to install the following Python packages:

- **Flask**: Web framework to handle HTTP requests.
- **Requests**: Library to make HTTP requests from the client side.

You can install these dependencies using the following commands:

```bash
pip install Flask
pip install requests
```
