import psycopg


check = True

with psycopg.connect(dbname="phones", user="postgres", password="s09112001") as con:
    cur = con.cursor()
    con.autocommit = True

    # function for get paginated data
    cur.execute("""CREATE OR REPLACE FUNCTION get_paginated_data(
        _limit INTEGER,
        _offset INTEGER
    )
    RETURNS TABLE (
        name TEXT,
        phone TEXT
    )
    LANGUAGE plpgsql
    AS $$
    BEGIN
        RETURN QUERY SELECT *
        FROM phonebook
        LIMIT _limit
        OFFSET _offset;
    END;
    $$;""")

    # procedure for delete user
    cur.execute("""create or replace procedure delete_phone(v text)
    LANGUAGE plpgsql
    as $$ 
    begin
        delete from phonebook where name = v or phone = v;
    end;
    $$;""")

    # function  for print all data
    cur.execute("""CREATE OR REPLACE FUNCTION print_data()
RETURNS TABLE(name text, phone text) AS $$
BEGIN
    RETURN QUERY SELECT * FROM phonebook;
END;
$$ LANGUAGE plpgsql;""")

    # procedure for update all insert user
    cur.execute("""CREATE OR REPLACE PROCEDURE add_new(n text, p text)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE phonebook SET phone = p WHERE name = n;
    IF NOT FOUND THEN
        INSERT INTO phonebook(name, phone) VALUES(n, p);
    END IF;
END;
$$;
""")

    while check:
        print(
            "[0] to exit\n[1] to update or insert phone\n[2] to delete phone\n[3] print data\n[4] insert many values\n[5] get pagination")
        n = int(input())
        if n == 0:
            check = False
        if n == 1:
            print("write the new user name or phone which you want to update or insert:")
            new_name = input()
            print("write the new phone which you want to update:")
            new_phone = input()
            cur.execute("CALL add_new(%s, %s)", (new_name, new_phone))
        if n == 2:
            print("Write the user name or phone number which you want to delete:")
            np = input()
            try:
                a = int(np)
                if type(a) is int:
                    cur.execute(f"SELECT * FROM phonebook WHERE phone = '{np}'")
                    cnt = cur.fetchall()
                    if len(cnt) > 1:
                        cur.execute(f"SELECT * FROM phonebook WHERE phone = '{np}'")
                        print('Insert which one you want to delete')
                        print(cnt)
                        np = input()
                        cur.execute(f"CALL delete_phone('{np}')")  # Use CALL statement and cur.execute()

                    if len(cnt) == 1:
                        cur.execute(f"CALL delete_phone('{np}')")  # Use CALL statement and cur.execute()

            except ValueError:
                cur.execute(f"CALL delete_phone('{np}')")  # Use CALL statement and cur.execute()

        if n == 3:
            cur.execute("SELECT * FROM print_data()")
            result = cur.fetchall()
            for i in result:
                print(i)
        if n == 4:
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
                        cur.execute("CALL add_new(%s, %s)", (n, p))
                except:
                    inc_v[n] = p
                i += 2
            print(inc_v)
        con.commit()
        if n == 5:
            print('insert page')
            page = int(input())
            print('insert start p')
            start_p = int(input())
            cur.execute("SELECT * FROM get_paginated_data(%s, %s)", (page, start_p))
            result = cur.fetchall()
            for i in result:
                print(i)