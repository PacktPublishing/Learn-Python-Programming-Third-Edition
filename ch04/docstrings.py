# docstrings.py
def square(n):
    """Return the square of a number n. """
    return n ** 2


def get_username(userid):
    """Return the username of a user given their id. """
    return db.get(user_id=userid).username


def connect(host, port, user, password):
    """Connect to a database.

    Connect to a PostgreSQL database directly, using the given
    parameters.

    :param host: The host IP.
    :param port: The desired port.
    :param user: The connection username.
    :param password: The connection password.
    :return: The connection object.
    """
    # body of the function here...
    return connection
