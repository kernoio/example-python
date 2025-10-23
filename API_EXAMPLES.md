# API Usage Examples

This document provides practical examples of how to use the FastAPI User & Games API with pure JWT authentication.

## Prerequisites

Make sure the API is running on `http://localhost:8000`

**Note:** This API uses pure JWT authentication (not OAuth2), so login accepts JSON payloads instead of form data.

## 1. Register a New User

**Request:**
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepass123"
  }'
```

**Response:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "id": 1,
  "created_at": "2025-10-23T10:30:00.000000"
}
```

## 2. Login

**Request:**
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepass123"
  }'
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huX2RvZSIsImV4cCI6MTYzNDk4NzY1MH0.abc123...",
  "token_type": "bearer"
}
```

**Save the access token for subsequent requests!**

## 3. Get Current User Info

**Request:**
```bash
curl -X GET "http://localhost:8000/users/me" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "id": 1,
  "created_at": "2025-10-23T10:30:00.000000"
}
```

## 4. Create a Game

**Request:**
```bash
curl -X POST "http://localhost:8000/games/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Legend of Zelda: Breath of the Wild",
    "description": "An open-world action-adventure game",
    "genre": "Action-Adventure"
  }'
```

**Response:**
```json
{
  "title": "The Legend of Zelda: Breath of the Wild",
  "description": "An open-world action-adventure game",
  "genre": "Action-Adventure",
  "id": 1,
  "owner_id": 1,
  "created_at": "2025-10-23T10:35:00.000000"
}
```

## 5. Create More Games

**Request:**
```bash
curl -X POST "http://localhost:8000/games/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Super Mario Odyssey",
    "description": "A 3D platform game",
    "genre": "Platform"
  }'
```

## 6. Get All Games

**Request:**
```bash
curl -X GET "http://localhost:8000/games/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
[
  {
    "title": "The Legend of Zelda: Breath of the Wild",
    "description": "An open-world action-adventure game",
    "genre": "Action-Adventure",
    "id": 1,
    "owner_id": 1,
    "created_at": "2025-10-23T10:35:00.000000"
  },
  {
    "title": "Super Mario Odyssey",
    "description": "A 3D platform game",
    "genre": "Platform",
    "id": 2,
    "owner_id": 1,
    "created_at": "2025-10-23T10:36:00.000000"
  }
]
```

## 7. Get Games by Specific User

**Request:**
```bash
curl -X GET "http://localhost:8000/games/user/1" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
[
  {
    "title": "The Legend of Zelda: Breath of the Wild",
    "description": "An open-world action-adventure game",
    "genre": "Action-Adventure",
    "id": 1,
    "owner_id": 1,
    "created_at": "2025-10-23T10:35:00.000000"
  },
  {
    "title": "Super Mario Odyssey",
    "description": "A 3D platform game",
    "genre": "Platform",
    "id": 2,
    "owner_id": 1,
    "created_at": "2025-10-23T10:36:00.000000"
  }
]
```

## 8. Get Current User with All Their Games

**Request:**
```bash
curl -X GET "http://localhost:8000/users/me/games" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
{
  "username": "john_doe",
  "email": "john@example.com",
  "id": 1,
  "created_at": "2025-10-23T10:30:00.000000",
  "games": [
    {
      "title": "The Legend of Zelda: Breath of the Wild",
      "description": "An open-world action-adventure game",
      "genre": "Action-Adventure",
      "id": 1,
      "owner_id": 1,
      "created_at": "2025-10-23T10:35:00.000000"
    },
    {
      "title": "Super Mario Odyssey",
      "description": "A 3D platform game",
      "genre": "Platform",
      "id": 2,
      "owner_id": 1,
      "created_at": "2025-10-23T10:36:00.000000"
    }
  ]
}
```

## 9. Update a Game

**Request:**
```bash
curl -X PUT "http://localhost:8000/games/1" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "An epic open-world adventure game - Game of the Year!",
    "genre": "Open-World Adventure"
  }'
```

**Response:**
```json
{
  "title": "The Legend of Zelda: Breath of the Wild",
  "description": "An epic open-world adventure game - Game of the Year!",
  "genre": "Open-World Adventure",
  "id": 1,
  "owner_id": 1,
  "created_at": "2025-10-23T10:35:00.000000"
}
```

## 10. Get a Specific Game

**Request:**
```bash
curl -X GET "http://localhost:8000/games/1" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
{
  "title": "The Legend of Zelda: Breath of the Wild",
  "description": "An epic open-world adventure game - Game of the Year!",
  "genre": "Open-World Adventure",
  "id": 1,
  "owner_id": 1,
  "created_at": "2025-10-23T10:35:00.000000"
}
```

## 11. Update User Profile

**Request:**
```bash
curl -X PUT "http://localhost:8000/users/1" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@newdomain.com"
  }'
```

**Response:**
```json
{
  "username": "john_doe",
  "email": "john.doe@newdomain.com",
  "id": 1,
  "created_at": "2025-10-23T10:30:00.000000"
}
```

## 12. Delete a Game

**Request:**
```bash
curl -X DELETE "http://localhost:8000/games/2" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:** `204 No Content`

## 13. Get All Users

**Request:**
```bash
curl -X GET "http://localhost:8000/users/" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

**Response:**
```json
[
  {
    "username": "john_doe",
    "email": "john.doe@newdomain.com",
    "id": 1,
    "created_at": "2025-10-23T10:30:00.000000"
  }
]
```

## Using Python Requests

If you prefer using Python:

```python
import requests

BASE_URL = "http://localhost:8000"

# Register
response = requests.post(
    f"{BASE_URL}/auth/register",
    json={
        "username": "jane_doe",
        "email": "jane@example.com",
        "password": "password123"
    }
)
print(response.json())

# Login
response = requests.post(
    f"{BASE_URL}/auth/login",
    json={
        "username": "jane_doe",
        "password": "password123"
    }
)
token = response.json()["access_token"]

# Create game
headers = {"Authorization": f"Bearer {token}"}
response = requests.post(
    f"{BASE_URL}/games/",
    headers=headers,
    json={
        "title": "Pokemon Red",
        "description": "Classic Pokemon game",
        "genre": "RPG"
    }
)
print(response.json())

# Get my games
response = requests.get(f"{BASE_URL}/users/me/games", headers=headers)
print(response.json())
```

## Error Responses

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 403 Forbidden
```json
{
  "detail": "Not authorized to update this game"
}
```

### 404 Not Found
```json
{
  "detail": "Game not found"
}
```

### 400 Bad Request
```json
{
  "detail": "Username already registered"
}
```

## Tips

1. **Token Expiration**: Access tokens expire after 30 minutes (configurable). If you get a 401 error, login again to get a new token.

2. **Pagination**: Use `skip` and `limit` query parameters for pagination:
   ```bash
   curl -X GET "http://localhost:8000/games/?skip=10&limit=20" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
   ```

3. **Interactive Documentation**: Visit `http://localhost:8000/docs` to try the API interactively through Swagger UI.

4. **Authorization**: Only the owner of a game can update or delete it. Only users can update/delete their own profile.

