"""Password hashing helpers.

Passwords are stored as bcrypt hashes. verify_password also accepts a legacy
plaintext row so accounts created before hashing was introduced still work; the
caller can then re-save the password to upgrade it.
"""

import bcrypt


def hash_password(plain):
    """Return a bcrypt hash (str) for a plaintext password."""
    return bcrypt.hashpw(plain.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def is_hashed(stored):
    """True if the stored value looks like a bcrypt hash rather than plaintext."""
    return isinstance(stored, str) and stored.startswith(("$2a$", "$2b$", "$2y$"))


def verify_password(plain, stored):
    """Check a plaintext password against the stored value."""
    if stored is None:
        return False
    if is_hashed(stored):
        try:
            return bcrypt.checkpw(plain.encode("utf-8"), stored.encode("utf-8"))
        except ValueError:
            return False
    # Legacy plaintext row.
    return plain == stored
