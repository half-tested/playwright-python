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

    def get_test_case_id_by_name(self, test_name: str):
        c = self.connection.cursor()
        c.execute('SELECT id FROM tcm_testcase WHERE name=? limit 1', (test_name,))
        result = c.fetchall()
        return result[0][0] if len(result) > 0 else -1

    def get_authors_rating(self) -> list:
        sql_query = """
        select u.username, count(1) as "cnt"
        from tcm_testcase t  join auth_user u on t.author_id = u.id
        group by u.username
        order by count(1) desc
        limit 3
        """
        c = self.connection.cursor()
        c.execute(sql_query)
        result = c.fetchall()
        empty = ["", ""]
        top_1_author = [result[0][0], result[0][1]] if len(result) > 0 else empty
        top_2_author = [result[1][0], result[1][1]] if len(result) > 1 else empty
        top_3_author = [result[2][0], result[2][1]] if len(result) > 2 else empty
        processed_data = [top_1_author, top_2_author, top_3_author]
        return processed_data

    def delete_user(self, username: str):
        c = self.connection.cursor()
        c.execute('DELETE FROM auth_user WHERE username=?', (username,))
        self.connection.commit()

    def close(self):
        self.connection.close()
