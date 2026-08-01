"""One-time migration: widen the password column and hash existing passwords.

Safe to run more than once -- rows that are already hashed are skipped.
Run with:  python migrate_passwords.py
"""

from db_config import get_connection
from security import hash_password, is_hashed


def main():
    conn = get_connection()
    cursor = conn.cursor()

    # A bcrypt hash is 60 chars and will not fit the original varchar(45).
    cursor.execute("show columns from register like 'password'")
    column_type = cursor.fetchone()[1]
    if "varchar(255)" not in column_type.lower():
        cursor.execute("alter table register modify password varchar(255)")
        conn.commit()
        print("password column widened: %s -> varchar(255)" % column_type)
    else:
        print("password column already varchar(255)")

    cursor.execute("select email, password from register")
    rows = cursor.fetchall()

    migrated = 0
    for email, stored in rows:
        if is_hashed(stored):
            continue
        cursor.execute(
            "update register set password=%s where email=%s",
            (hash_password(stored), email),
        )
        migrated += 1

    conn.commit()
    conn.close()
    print("hashed %d of %d rows (%d already hashed)"
          % (migrated, len(rows), len(rows) - migrated))


if __name__ == "__main__":
    main()
