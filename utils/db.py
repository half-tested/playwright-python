import sqlite3


class Database:
    def __init__(self, path: str):
        self.connection = sqlite3.connect(path)

    def create_test_case(self, name: str, description: str, author_name: str):
        c = self.connection.cursor()
        c.execute(f'SELECT id FROM auth_user WHERE username = "{author_name}"')
        author_id = str(c.fetchall()[0][0])
        c.execute('INSERT INTO tcm_testcase (name, description, author_id) VALUES (?, ?, ?)',
                  (name, description, author_id))
        self.connection.commit()

    def delete_test_case(self, test_name: str):
        c = self.connection.cursor()
        c.execute('DELETE FROM tcm_testcase WHERE name=?', (test_name,))
        self.connection.commit()

    def close(self):
        self.connection.close()
