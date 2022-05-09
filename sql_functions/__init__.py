import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
)

cursor = conexao.cursor()

def EndSqlConnection():
    conexao.close()
    cursor.close()

##Check/Select or create methods
def CheckOrCreateDatabase():
    cursor.execute("CREATE DATABASE IF NOT EXISTS doggos;")


def SelectDatabase():
    cursor.execute("use doggos;")


def CheckOrCreateTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS doggo_list(id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(30) NOT NULL, borned date, sex enum('M','F'), color varchar(20), fluffyness decimal(4.2));")

##Data show and manipulation methods
def AddDog(name, borned, sex, color, fluffyness):
    cursor.execute('INSERT INTO doggo_list values (DEFAULT, "{}", "{}", "{}", "{}", {})'.format(name, borned, sex, color, fluffyness))
    conexao.commit()

def DeleteDog(id):
    cursor.execute("DELETE FROM doggo_list where id={}".format(id))
    conexao.commit()
    
def ShowAllDogs():
    cursor.execute("SELECT * FROM doggo_list")

    myresults = cursor.fetchall()

    for result in myresults:
        print("="*40)
        print("Id: {} - Name: {} - Borned at: {} - Sex: {} - Color: {} - Fluffiness: {}".format(result[0],result[1],result[2],result[3],result[4],result[5]))
        print("="*40)
    input("Press any key to continue...")