import pandas as pd
import pymysql

df = pd.read_csv("data_prueba_tecnica.csv")


print(df.dtypes)

#df["amount"] = pd.to_numeric(df["amount"])
df["amount"] = pd.Series([round(val,2) for val in df["amount"]])
print(df["amount"])
#df["paid_at"] = pd.to_date(df["paid_at"])

print(df[["name","created_at","paid_at"]].head(n=5))

connection = pymysql.connect(
            host = "localhost",#aqui va la ip
            port =33080,
            user = "root",
            password = "ilker",
            db = "prueba")
cursor = connection.cursor()

valores_quitados = int()
cuenta = 0
def cargaSQL():
    for index, row in df.iterrows():
        try:
            var1= (f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{cuenta}","{row[1]}","{row.company_id}",{row.amount},"{row.status}","{row.created_at}","{row.paid_at}")')
            cursor.execute(var1)
        except:
            try:
                cursor.execute(f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{cuenta}","{row[1]}","{row.company_id}",{row.amount},"{row.status}","{row.created_at}",null)')
            except:
                if len(str(row.amount))>15:
                    cursor.execute(f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{cuenta}","{row[1]}","{row.company_id}",{str(row.amount)[:4]},"{row.status}","{row.created_at}",null)') 
                elif str(row.id) == "nan":
                    cursor.execute(f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{cuenta}","{row[1]}","{row.company_id}",{str(row.amount)[:4]},"{row.status}","{row.created_at}",null)')
                
                
        cuenta +=1
    connection.commit()
try:
    cargaSQL()
except:
    pass
import openpyxl
def generaexcel():
    wb = openpyxl.Workbook()
    hoja = wb.active
    linea = int()
    estados = cursor.execute("SELECT * FROM Cargo order by id")
    for i in (cursor.fetchall()):
        hoja.append(i)

    wb.save('datos.xlsx')
    
generaexcel()
