# Authenication Endpoints

## Authentication

### /auth/login/ (POST)

-   username
-   email
-   password

Returns Token key

### /auth/logout/ (POST)

### /auth/password/reset/ (POST)

-   email

### /auth/password/reset/confirm/ (POST)

-   uid
-   token
-   new_password1
-   new_password2

Note

uid and token are sent in email after calling /dj-rest-auth/password/reset/

### /auth/password/change/ (POST)

-   new_password1
-   new_password2
-   old_password

Note
OLD_PASSWORD_FIELD_ENABLED = True to use old_password.
Note
LOGOUT_ON_PASSWORD_CHANGE = False to keep the user logged in after password change

### /auth/user/ (GET, PUT, PATCH)

-   username
-   first_name
-   last_name

Returns pk, username, email, first_name, last_name

### /auth/registration/ (POST)

-   username
-   password1
-   password2
-   email

### /auth/registration/verify-email/ (POST)

-   key
