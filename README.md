# Azure's Inn — Hotel Management System

A desktop hotel-management application built with Python, Tkinter and MySQL. It
covers the day-to-day desk work of a small hotel: registering guests, booking
rooms, maintaining the room inventory and producing a bill at checkout.

Written as an OOP + file-handling + GUI project: each screen is a class, all
state lives in MySQL, and a shared theme module keeps the look consistent.

---

## Features

- **Staff accounts** — register, log in, and reset a forgotten password via a
  security question. Passwords are stored as bcrypt hashes, never plaintext.
- **Customer management** — add, update, delete and search guest records
  (contact details, nationality, ID proof). Search by mobile number or
  reference.
- **Room inventory** — add rooms with floor, room number and room type.
- **Room booking** — look up a guest by mobile, pick check-in/check-out dates
  from a calendar, choose room and meal plan, and generate a bill with tax.
- **Live table views** — every screen lists current records in a sortable,
  scrollable table that refreshes after each change.

---

## Requirements

- **Python 3.10+** (developed on 3.12.3)
- **MySQL Server 8.0+**, running locally
- Tkinter — bundled with the standard Python installer on Windows

Install the Python packages:

```bash
pip install pillow mysql-connector-python bcrypt pycountry tkcalendar
```

Versions this was verified against:

| Package | Version |
| --- | --- |
| pillow | 11.0.0 |
| mysql-connector-python | 9.1.0 |
| bcrypt | 4.2.1 |
| pycountry | 24.6.1 |
| tkcalendar | 1.5.0 |

---

## Setup

### 1. Create the database

The database is named `bank_management` (a leftover name from an earlier
project — the app reads it from config, so you can rename it if you prefer).

```sql
CREATE DATABASE IF NOT EXISTS bank_management;
USE bank_management;

CREATE TABLE register (
    fname     VARCHAR(45),
    lname     VARCHAR(45),
    contact   VARCHAR(45),
    email     VARCHAR(45),
    securityQ VARCHAR(45),
    securityA VARCHAR(45),
    password  VARCHAR(255)      -- must fit a 60-char bcrypt hash
);

CREATE TABLE customer (
    Ref         INT,
    Name        VARCHAR(45),
    Mother      VARCHAR(45),
    Gender      VARCHAR(45),
    PostCode    VARCHAR(45),
    Mobile      VARCHAR(45),
    Email       VARCHAR(45),
    Nationality VARCHAR(45),
    Idproof     VARCHAR(45),
    Idnumber    VARCHAR(45),
    Address     VARCHAR(45)
);

CREATE TABLE details (
    Floor    VARCHAR(45),
    RoomNo   VARCHAR(45),
    RoomType VARCHAR(45)
);

CREATE TABLE room (
    Contact   VARCHAR(45),
    check_in  VARCHAR(45),
    check_out VARCHAR(45),
    roomtype  VARCHAR(45),
    Room      VARCHAR(45),
    meal      VARCHAR(45),
    noOfdays  VARCHAR(45)
);
```

### 2. Configure the connection

Credentials are kept out of the source. Copy the template and fill in your own:

```bash
cp config.ini.example config.ini
```

```ini
[mysql]
host = localhost
user = root
password = your_mysql_password
database = bank_management
```

`config.ini` is listed in `.gitignore` — **do not commit it.** Environment
variables override the file if you would rather not keep one on disk:

```bash
HOTEL_DB_HOST  HOTEL_DB_USER  HOTEL_DB_PASSWORD  HOTEL_DB_NAME
```

### 3. Migrate existing passwords (upgrades only)

If you have an older copy of this database where passwords were stored as
plaintext, run this once. It widens the `password` column and hashes every
existing row. It is safe to re-run — already-hashed rows are skipped.

```bash
python migrate_passwords.py
```

### 4. Run

```bash
python login.py
```

`login.py` is the entry point — not `hotel.py`. Log in with an account from the
`register` table; the **Username** field matches on **email address**, not on
the first name. If the table is empty, use *Register new user* first.

---

## Project structure

| File | Purpose |
| --- | --- |
| `login.py` | Entry point: login, registration and password-reset windows |
| `hotel.py` | Main dashboard with the menu sidebar |
| `customer.py` | Add / update / delete / search guest records |
| `room.py` | Room booking and billing |
| `details.py` | Room inventory (add new rooms) |
| `theme.py` | Shared palette, fonts, ttk styles and window sizing |
| `db_config.py` | Single `get_connection()` used by every screen |
| `security.py` | bcrypt password hashing and verification |
| `migrate_passwords.py` | One-time plaintext → bcrypt migration |
| `config.ini` | Your DB credentials (git-ignored) |
| `config.ini.example` | Template to copy |
| `images/` | Backgrounds, logo and icons |

All screens size themselves to the actual display via `theme.fit_window()`, so
the layout adapts instead of being cut off on smaller monitors.

---

## Notes and known issues

- The `bank_management` database also contains `account` and `amount` tables
  left over from an earlier banking project. Nothing here uses them.
- In `room.py` the **Room Type** dropdown writes to `var_roomavailable` while
  **Available Rooms** writes to `var_roomtype` — the two variables look
  swapped. Worth reviewing before relying on booking records.
- Guest and booking data is not validated beyond basic format checks, and
  `register` has no unique constraint on `email`, so duplicate accounts are
  possible.
- If you ever publish this repository, rotate your MySQL password: earlier
  commits contain the old hardcoded `root` credentials in the source history.
