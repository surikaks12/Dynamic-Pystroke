import psycopg2
def CreateTable():
    DB_NAME = 'ixvgfxto'
    DB_USER = 'ixvgfxto'
    DB_PASS = 'Lg71aU_InBQ2vDUcmq19KuHCYIhWJAm0'
    DB_HOST = 'salt.db.elephantsql.com'
    DB_PORT = '5432'
    try:
        conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
        print ('Databse connected successfully')
    except:
        print ('unable to connect to database')

        ##########Creating columns in the dababase########

    cur = conn.cursor()
    try:
        cur.execute("""

        DROP TABLE NewTable

        """)
        print('Dropped table')
    except:
        print('unable to drop the table')
    conn.commit()
    conn.close()
    cur.close()

CreateTable()
