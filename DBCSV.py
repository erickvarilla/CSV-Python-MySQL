import mysql.connector
import csv
##========================================
# conexion ala base de datos
#========================================
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()
##========================================
# creo la tabla para almacenar la informacion 
# del archivo .csv
##========================================
mycursor.execute("CREATE TABLE csv (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), second_name VARCHAR(255),Grade VARCHAR(255))")
 


##========================================
# informacion que contendra el archivo.csv
##========================================
# myData = [["first_name", "second_name", "Grade"],
#           ['Alex', 'Brian', 'A'],
#           ['Tom', 'Smith', 'B']]

##========================================
# escribimos la informacion en el archivo .csv
##========================================
# myFile = open('example2.csv', 'w')
# with myFile:
#     writer = csv.writer(myFile)
#     writer.writerows(myData)


##========================================
# abrimos y leemos el archivo .csv
##========================================
with open('example2.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    data= list()
    ##========================================
    # muestro la informacion por consola
    ##========================================
    for row in reader:
       #print(row['first_name'], row['second_name'],row['Grade'])
        tupla = (row['first_name'], row['second_name'],row['Grade'])
        data.append(tupla)
##========================================
# capturo la informacion en data
# y la organizo para meter toda la informacion 
# ala base de datos 
##========================================
print(data)

##========================================
# guardado de la informacion 
# en la base de datos
##========================================
sql = "INSERT INTO csv (first_name, second_name,Grade) VALUES (%s, %s,%s)"
##==============================
# executemany => es para guardar 
# muchos registros al mismo tiempo
##==============================
mycursor.executemany(sql, data)
mydb.commit()
## mycursor.rowcount => contar cuantos registros se introducieron
print(mycursor.rowcount, "was inserted.")