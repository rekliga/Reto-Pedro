import pandas as pd
import pymysql

df = pd.read_csv("data_prueba_tecnica.csv")


print(df.dtypes)

#df["created_at"] = pd.to_date(df["created_at"])
#df["paid_at"] = pd.to_date(df["paid_at"])

print(df[["created_at","paid_at"]].head(n=5))

connection = pymysql.connect(
            host = "localhost",#aqui va la ip
            port =33080,
            user = "root",
            password = "ilker",
            db = "prueba")
cursor = connection.cursor()

df.fillna(' ')


#valor_max = str()
for index, row in df.iterrows():
    try:
        var1= (f'INSERT INTO Cargo (id,company_name,company_id,amount,status,created_at,update_at ) values("{row.id}","{row.name}","{row.company_id}",{row.amount},"{row.status}","{row.created_at}","{row.paid_at}")')
        cursor.execute(var1)
    except:
        pass
    #valor_max = row.id
    #print(var1)
    
#cursor.commit()
#cursor.close()
#print(len(valor_max))
estados = cursor.execute("SELECT * FROM Cargo")
for i in (cursor.fetchall()):
    print(i)

connection.commit()