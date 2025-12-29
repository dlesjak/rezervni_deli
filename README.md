# Rezervni deli

An example of Django web application to store spare parts.

Example SQLite database is at https://www-f9.ijs.si/~lesi/rd/db.sqlite3

## CRUD REST API

### CREATE
POST method on http://127.0.0.1:8000/rd/api/spareparts/
Necessary fields:
- name
- type
- dop (date of purchase in form YYYY-MM-DD)
- location (location id)
- owner (owner id)

### READ
GET method
All entries: http://127.0.0.1:8000/rd/api/spareparts/
Specific entry (by part id): http://127.0.0.1:8000/rd/api/spareparts/<id>/

### UPDATE
URL: http://127.0.0.1:8000/rd/api/spareparts/<id>/
PUT method (needs all fields)
PATCH method (only changed fields)

### DELETE
DELETE method
URL: http://127.0.0.1:8000/rd/api/spareparts/<id>/
