# API Documentation for Social Meet Backend

## Endpoints

### Authentication
#### POST /api/signup/
This endpoint allows a user to create a new account in the system.

**Request Body**
| Parameter | Type | Required | Description |
|:-----|:--------:|------:|------:|
| name | string | Yes | The desired full name for the new user |
| email | string | Yes | The email address for the new user |
| password1 | string | Yes | The desired password for the new user |
| password2 | string | Yes | Confirm desired password for the new user |

**Response**
* 201 Created: The account was successfully created.
* 400 Bad Request: The request body was invalid or incomplete.
* 409 Conflict: An account with the given username or email already exists.

#### POST /api/login/
This endpoint allows a user to log in to their account.

**Request Body**
| Parameter | Type | Required | Description |
|:-----|:--------:|------:|------:|
| email | string | Yes | The email address for the user |
| password | string | Yes | The password of the user |

**Response**
* 200 OK: The user was successfully authenticated.
* 400 Bad Request: The request body was invalid or incomplete.
* 401 Unauthorized: The provided credentials were incorrect.


#### POST /api/logout/
This endpoint allows a user to log out of their account.

**Request Body**
None.

**Response**
* 204 No Content: The user was successfully logged out.
* 401 Unauthorized: The user is not authenticated.

😭😭 I'm tired of this documentation i'll continue later!! 🥺🥺
