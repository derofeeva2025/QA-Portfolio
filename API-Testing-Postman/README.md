# REST API Testing with Postman

A Postman collection for the public demo API [Restful-Booker](https://restful-booker.herokuapp.com/apidoc/index.html) (a hotel booking service).
It covers token authentication and the full lifecycle of a booking: create, read, update (PUT and PATCH), delete and verify the deletion.

## What is in the collection

| Folder | Request | Purpose |
|---|---|---|
| `01 Auth` | Get token | `POST /auth`, saves the token to an environment variable |
| `02 Bookings` | Get all bookings | `GET /booking`, lists booking ids |
| | Create booking | `POST /booking`, saves the new `bookingId` |
| | Get booking by id | `GET /booking/{{bookingId}}` |
| | Update booking (PUT) | Replaces the whole booking, uses the token |
| | Update booking (PATCH) | Changes only the sent fields, uses the token |
| | Delete booking | `DELETE /booking/{{bookingId}}`, uses the token |
| | Get deleted booking | Verifies the booking is gone (404) |

## Techniques used

- Collection, folders and an environment (`baseUrl`, `username`, `password`, `token`, `bookingId`)
- Chained requests: values from one response are stored as variables and used in the next request
- Test scripts (`pm.test`, `pm.expect`) in the post-response tab: status code, body fields, saved token
- Running the whole collection with the Collection Runner or Newman

## How to run

**Postman:** import both files from `postman/` (collection and environment), select the `booker` environment, then run the collection with the Collection Runner.

**Newman (command line):**

```bash
npx newman run postman/booker.postman_collection.json -e postman/booker.postman_environment.json
```

Last run: 8 requests, 7 assertions, 0 failed.

## Notes

- Restful-Booker is a shared public sandbox: data is reset periodically and the first response after idle time can be slow.
- The credentials in the environment file are the public demo credentials from the official API documentation.
- Observed behavior worth reporting: a successful `DELETE` returns `201 Created` instead of `200` or `204`.

## Next steps

- Assertions for PATCH, DELETE and the get-all request
- Negative cases: missing or invalid token (403), non-existent id (404), wrong password
- The same checks in Python (`requests` and `pytest`)
