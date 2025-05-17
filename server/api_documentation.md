# Drug Trafficking Detection API Documentation

This API provides endpoints for managing detected messages, Telegram users, and fetching detailed Telegram user information using the Telethon library.

---

## Base URL

```
http://<your-domain-or-ip>/api/
```

---

## Endpoints Overview

| Endpoint                                 | Methods           | Description                                  |
|-------------------------------------------|-------------------|----------------------------------------------|
| `/detectedmessage/`                      | GET, POST         | List or create detected messages             |
| `/detectedmessage/<id>/`                  | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a detected message |
| `/telegramusers/`                        | GET, POST         | List or create Telegram users                |
| `/telegramusers/<id>/`                    | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a Telegram user   |
| `/username_details?user_id=<id>`<br>`/username_details?username=<username>` | GET | Get full Telegram user details by user ID or username |

---

## 1. Detected Messages

### List All Detected Messages

**GET** `/detectedmessage/`

**Response:**
```json
[
  {
    "id": 1,
    "user": 2,
    "message": "Suspicious message",
    "detected_at": "2025-05-18T12:34:56Z"
  }
]
```

### Create a Detected Message

**POST** `/detectedmessage/`

**Request:**
```json
{
  "user": 2,
  "message": "Suspicious message"
}
```

**Response:**
```json
{
  "id": 2,
  "user": 2,
  "message": "Suspicious message",
  "detected_at": "2025-05-18T13:00:00Z"
}
```

### Retrieve/Update/Delete a Detected Message

**GET/PUT/PATCH/DELETE** `/detectedmessage/<id>/`

---

## 2. Telegram Users

### List All Telegram Users

**GET** `/telegramusers/`

**Response:**
```json
[
  {
    "id": 2,
    "username": "john_doe",
    "first_name": "John",
    "last_name": "Doe"
  }
]
```

### Create a Telegram User

**POST** `/telegramusers/`

**Request:**
```json
{
  "username": "jane_doe",
  "first_name": "Jane",
  "last_name": "Doe"
}
```

**Response:**
```json
{
  "id": 3,
  "username": "jane_doe",
  "first_name": "Jane",
  "last_name": "Doe"
}
```

### Retrieve/Update/Delete a Telegram User

**GET/PUT/PATCH/DELETE** `/telegramusers/<id>/`

---

## 3. Telegram User Details

### Get User Details by Username or User ID

**GET** `/username_details?username=john_doe`  
or  
**GET** `/username_details?user_id=123456789`

**Response:**
```json
{
  "id": 123456789,
  "username": "john_doe",
  "first_name": "John",
  "last_name": "Doe",
  "phone": "+1234567890",
  "bio": "Hello, I'm John!",
  "is_bot": false,
  "is_premium": false,
  "restricted": false,
  "scam": false,
  "verified": true,
  "status": "UserStatusOnline",
  "profile_photo": 9876543210
}
```

**Error Example:**
```json
{
  "error": "Either user_id or username parameter is required"
}
```

---

## How to Use in React

### Fetch All Telegram Users

```javascript
fetch('/api/telegramusers/')
  .then(res => res.json())
  .then(data => console.log(data));
```

### Create a Detected Message

```javascript
fetch('/api/detectedmessage/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    user: 2,
    message: 'Suspicious message'
  })
})
  .then(res => res.json())
  .then(data => console.log(data));
```

### Update a Telegram User

```javascript
fetch('/api/telegramusers/3/', {
  method: 'PUT',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    username: 'jane_doe',
    first_name: 'Jane',
    last_name: 'Smith'
  })
})
  .then(res => res.json())
  .then(data => console.log(data));
```

### Delete a Detected Message

```javascript
fetch('/api/detectedmessage/2/', {
  method: 'DELETE'
})
  .then(res => {
    if (res.status === 204) {
      alert('Deleted!');
    }
  });
```

### Get Telegram User Details

```javascript
fetch('/api/username_details?username=john_doe')
  .then(res => res.json())
  .then(data => console.log(data));
```

---

## Notes

- All endpoints return JSON.
- Use the correct HTTP method (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) for each operation.
- For `POST`, `PUT`, and `PATCH`, set `Content-Type: application/json` and send data as JSON.
- For detail endpoints, append the object’s ID (e.g., `/api/telegramusers/3/`).
- For `/username_details`, provide either `user_id` or `username` as a query parameter.
- The `/username_details` endpoint requires the Telegram client to be authorized and may return an error if not.

---

**Contact Hardik for authentication or advanced usage.**