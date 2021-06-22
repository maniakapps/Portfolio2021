import mysql.connector

"""
    Database example
"""
def get_rows():
    try:
        connection = mysql.connector.connect(host='127.0.0.1', user='root', password='Maniak12'
                                             , database='world_x')
        cursor = connection.cursor()
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        print("Connected")
        sql_data_grab = 'SELECT ID json_extract'
        sql_city = "SELECT * FROM city"
        cursor.execute(sql_city)
        records = cursor.fetchall()
        print("Total rows")
        for row in records:
            cursor1.execute(sql_data_grab)
            print("ID: ",row[0])
            id = row[0]
            print("Name:", row[1])
            print("CC:", row[2])
            print("Distritic: ", row[3])
            print("Original population: ", row[4])
            population = int(''.join(map(str, cursor1.fetchone())))
            population = int(population + (population*0.1))
            update = (population, id)
            sql_update = "UPDATE city SET Population = %s where id= %s"
            print(update)
            cursor2.execute(sql_update, update)
            print("New population: ", row[5])
            connection.commit()
    except mysql.connector.Error as error:
        print('Error: ', error)


get_rows()
