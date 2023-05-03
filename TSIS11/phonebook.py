import psycopg

conn = psycopg.connect(dbname = "phones", user = 'postgres', password = 's09112001')
cur = conn.cursor()
conn.autocommit = True
cur.execute(''' CREATE OR REPLACE FUNCTION get_pagination(
                    _limit INT,
                    _offset INT)
                RETURNS TABLE(
                    name TEXT,
                    phone TEXT
                )
                LANGUAGE SQL
                AS $$
                    SELECT * FROM phonebook
                    LIMIT _limit
                    OFFSET _offset;
                $$''')
cur.execute(""" CREATE OR REPLACE PROCEDURE add_update_user(
                    _name TEXT,
                    _phone TEXT)
            LANGUAGE plpgsql
            AS $$
            BEGIN
                UPDATE phonebook SET phone = _phone WHERE name = _name;
                IF NOT FOUND THEN
                    INSERT INTO phonebook (name, phone) VALUES (_name, _phone);
                END IF;
            END
            $$
            """)
cur.execute(""" CREATE OR REPLACE PROCEDURE delete_user(
                _n TEXT,
                _m TEXT)
                LANGUAGE plpgsql
                AS $$
                BEGIN
                    IF _m = 'p' THEN
                        DELETE FROM phonebook WHERE phone = _n;
                    ELSE
                        DELETE FROM phonebook WHERE name = _n;
                    END IF;
                END
                $$""")

check = True
while check:
    print("[0] to exit\n[1] to print data with pattern\n[2] to insert/update user\n[3] insert many\n[4] pagination\n[5] delete by name/phone")

    choice = int(input("number:"))
    if choice == 0:
        check = False
    if choice == 1:
        pattern = input("what pattern?")
        cur.execute("SELECT * FROM phonebook WHERE CONCAT(name, phone) LIKE '%"+pattern+"%'")
        result = cur.fetchall()
        for i in result:
            print(i)
    if choice == 2:
        user = input("user_name:")
        phone = input("phone:")
        cur.execute("CALL add_update_user(%s,%s)",(user,phone))
    if choice == 3:
            print('insert name phone and so on')
            values = input()
            values = values.split(" ")
            inc_v = {}
            a = {}
            i = 0
            while i != len(values):
                n, p = values[i], values[i + 1]
                try:
                    if type(int(p)) is int:
                        a[n] = p
                        cur.execute("CALL add_update_user(%s, %s)", (n, p))
                except:
                    inc_v[n] = p
                i += 2
    if choice == 4:
        offset = input("offset")
        limit = input("limit:")
        cur.execute('SELECT * FROM get_pagination(%s,%s)',(limit,offset))
        result = cur.fetchall()
        for i in result:
            print(i)
    if choice == 5:
        what_to_delete = input('p/n:')
        nameORphone = input('input name/phone to delete:')
        cur.execute("CALL delete_user(%s,%s)",(nameORphone,what_to_delete))
        

