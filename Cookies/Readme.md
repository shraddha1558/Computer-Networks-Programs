# 🍪 Understanding Cookies using Flask and Python

This simple project helps you **understand the concept of HTTP Cookies** by observing how they behave in a basic web interaction between a Flask server and a Python client.

---

## What Are Cookies?

- **Cookies** are small data pieces stored in the **user’s browser** or HTTP client.
- They are used to:
  - Remember user identity (e.g., login session)
  - Track user activity across sessions
  - Store temporary preferences

---

## Key Concepts Demonstrated

### 1. **Setting a Cookie**

- A cookie is assigned when a user visits a specific route (like `/set_cookie/<username>`).
- The server sends the cookie to the client, storing it in the browser or HTTP session.

### 2. **Retrieving a Cookie**

- Once stored, cookies are automatically included in subsequent requests to the server.
- The server reads the cookie and uses its value (like showing a personalized greeting).

### 3. **Deleting a Cookie**

- The server can instruct the client to delete the cookie.
- Once deleted, the user is treated as a new or guest visitor.

---

##  How the Code Works

###  1. Server Side – Flask App

- The Flask app provides three endpoints:
  - `/` — Displays a greeting.
  - `/set_cookie/<username>` — Sets a cookie for the given username.
  - `/delete_cookie` — Deletes the existing username cookie.

- **Cookie Logic**:
  - When a user visits `/set_cookie/Shraddha`, a cookie is set with:
    - Key: `username`
    - Value: `Shraddha`
  - On accessing `/`, the server checks for this cookie.
    - If present → Greets: `Hello, Shraddha!`
    - If not → Greets: `Hello, guest!`

- When `/delete_cookie` is called:
  - The server tells the browser/client to delete the `username` cookie.

---

###  2. Client Side – Python Requests

- Uses a **`requests.Session()`** object to maintain cookie state across requests.
- Performs 4 actions:
  1. Set cookie for `Shraddha`
  2. Access `/` — Receives personalized greeting
  3. Delete the cookie
  4. Access `/` again — Receives default guest message

---

## Real-World Applications

- **Login systems** (Remember me)
- **Shopping carts**
- **User preferences/themes**
- **Session tracking**

---

Cookies = Tiny memory snacks for the web 🍪
