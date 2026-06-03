import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="codesentinel"
    )

    return conn


def save_scan(filename, issue_count):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO scans
    (filename, issue_count)
    VALUES (%s,%s)
    """

    values = (filename, issue_count)

    cursor.execute(query, values)

    conn.commit()

    cursor.close()
    conn.close()


def get_scans():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scans")

    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records