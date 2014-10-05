Authentication (/auth)
=======================

When making a API request that requires authentication, you must pass a token 
in the request. The token must be specified on the header: 'Authorization'. 
Passwords are expected to be a minimum of 8 characters long. There is no upper
limit. 

/get-token
--------------
Retrieve a token for the user

post
~~~~

+-------------+----------+---------------------------------------------------+
| Property    | Required | Description                                       |
+-------------+----------+---------------------------------------------------+
| username    | Yes      | The user's username. This should almost always be |
|             |          | a valid email address                             |
+-------------+----------+---------------------------------------------------+
| password    | Yes      | The user's password                               |
|             |          |                                                   |
+-------------+----------+---------------------------------------------------+

Example results::

    {
        payload: {
            "token":"378a4e24-8ea0-48b7-b23b-ac1aaeda41ae"
        }
    }

Returns a 401 error on a failed login.

/check-token
----------------
Checks the validity of a token. Returns the token owner's basic info on 
success.

get
~~~~~~~
There are no parameters on this method. The only guaranteed result properties 
on the payload results are 'email' and 'expires'.

Example results::

    {
        Payload: {
            "id":"378a4e24-8ea0-48b7-b23b-ac1aaeda41ae",
            "slug":"eric-hutchinson",
            "full_name":"Eric Hutchinson",
            "display_name":"Hutch",
            "email":"email@example.com",
            "expires":1403023354
        }
    }

Returns a 404 response on an expired token.

/renew-token
---------------
Checks a token and returns a fresh one with it's expiration reset. The token 
id number may or may not be the same.

post
~~~~~~
There are no parameters on this method

Example Results::

    {
        payload: {
            "token":"378a4e24-8ea0-48b7-b23b-ac1aaeda41ae"
        }
    }

Returns a 404 response on an expired token.

/change-password
----------------------
Changes the current users password.

post
~~~~~~~~~

+-------------+----------+---------------------------------------------------+
| Property    | Required | Description                                       |
+-------------+----------+---------------------------------------------------+
| password    | Yes      | The user's new password                           |
|             |          |                                                   |
+-------------+----------+---------------------------------------------------+

Returns a 400 BAD REQUEST on an invalid password.

Returns the user's info on a successful password change, as per check-token.

/forgotten-password
----------------------

post
~~~~~~~
When passed the email parameter, we send an email to the user with a reset 
token. This will include a url based on information provided for the app.

When the token parameter is passed, we email the user a new password. We also 
include a link based on the information provided for the app.
