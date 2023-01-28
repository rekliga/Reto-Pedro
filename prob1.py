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
for index, row in df.iterrows():
    #print(row[1])
    
    try:
        var1= (f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{cuenta}","{row[1]}","{row.company_id}",{row.amount},"{row.status}","{row.created_at}","{row.paid_at}")')
        cursor.execute(var1)
    except:

        #row.amount = round(row.amount,2)
        #print(row.amount)
        #print(f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{row.id}","{row[1]}","{row.company_id}",{row.amount},"{row.status}","{row.created_at}",null)')
        try:
            cursor.execute(f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{cuenta}","{row[1]}","{row.company_id}",{row.amount},"{row.status}","{row.created_at}",null)')
        except:
            if len(str(row.amount))>15:
                cursor.execute(f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{cuenta}","{row[1]}","{row.company_id}",{str(row.amount)[:4]},"{row.status}","{row.created_at}",null)')
                print("funciono XD")
            elif str(row.id) == "nan":
                cursor.execute(f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{cuenta}","{row[1]}","{row.company_id}",{str(row.amount)[:4]},"{row.status}","{row.created_at}",null)')
            
            #print(str(row.amount)[:4])
            #print(f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{row.id}","{row[1]}","{row.company_id}",{row.amount},"{row.status}","{row.created_at}",null)')
    cuenta +=1
    
#cursor.commit()
#cursor.close()
#print(len(valor_max))
estados = cursor.execute("SELECT * FROM Cargo")
#for i in (cursor.fetchall()):
#    print(i)
#print("valores quitados",valores_quitados)
connection.commit()