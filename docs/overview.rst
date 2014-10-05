Overview
=======================

Response construction
~~~~~~~~~~~~~~~~~~~~~~~~

All API endpoints return a top level object with various children. The data
requested is always a child object called 'payload'. 

An example would be::

    {
        payload: [
            {
                id: 123,
                name: "John Smith"
            },
            {
                id: 245,
                name: "Jane Doe"
            }
        ],
        perms: [
            "read",
            "write",
            "delete"
        ],
        errors: {
            code: 401
            messages: [ "must supply XXX for YYYY resource", ]
        }
    }

If present the 'payload' contains the requested data. Permissions the user has
set to true will be present in the 'perms' list. 

If present, the 'errors' object will contain details on what went wrong. The
code variable should match the http status code returned. The messages list
will contain any appropriate details.

Endpoints may optionally supply other top level members to the returned 
object. These will be detailed on appropriate documentation pages.

Site Identification
~~~~~~~~~~~~~~~~~~~~~

All requests should provide an api_key in the 'SiteKey' header.

Requests that require authorization should provide an auth token in the 
'Authorization' header.

