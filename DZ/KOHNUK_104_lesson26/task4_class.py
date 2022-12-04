class DB:

    def __init__(self, cursor):
        self.cursor = cursor

    def base_maker(self, base, one, two=None, three=None):
        if two is None and three is None:
            self.cursor.execute('''INSERT INTO ''' + base + '''(num) VALUES (3)''')
        elif two is not None and three is None:
            if isinstance(two, int):
                self.cursor.execute('''DELETE FROM ''' + base + ''' WHERE id=1''')
        else:
            if two is not None and isinstance(three, int):
                self.cursor.execute('''UPDATE ''' + base + '''SET num = 77 WHERE id=3''')
