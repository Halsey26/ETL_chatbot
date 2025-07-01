import os
from dotenv import load_dotenv
from supabase import create_client, Client
import pandas as pd

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_apikey=os.getenv('SUPABASE_SERVICE_ROLE_KEY')

# verificar carga de keys
# print(f'SUPABASE_URL: {supabase_url}')
# print(f'SUPABASE_SERVICE_ROL: {supabase_apikey}')

cliente_supa= create_client(supabase_url, supabase_apikey)
response= ( 
    cliente_supa.table("logs_chat")
    .select("*")
    .execute()
)

data = response.data

data_df = pd.DataFrame(data)

print(data_df[0])


# if data:
#     print('Yeii conexión correcta con supabase')
#     print(type(data)) # lista
#     print(data[0])
#     print(type(data[0])) # dicionario


# else:
#     print('Ups ERROR :c')

# podemos tratarlo como lista de diccionario
# pero vamos a evaluar como dataframe 


