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

## What's Happening in This Example?

- A username (like **Shraddha**) is stored as a cookie.
- When revisiting the site, the server reads this cookie and greets the user.
- After deleting the cookie, the server no longer recognizes the user.

---

## Real-World Applications

- **Login systems** (Remember me)
- **Shopping carts**
- **User preferences/themes**
- **Session tracking**

---

Cookies = Tiny memory snacks for the web 🍪
