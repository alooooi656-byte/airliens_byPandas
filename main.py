import pandas as pd
from sqlalchemy import create_engine
from db_config import DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE


connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
engine = create_engine(connection_string)

query="select * from Flights"

df_Flights = pd.read_sql(query, con=engine)
print("========================================================")
print(df_Flights.info)
print("========================================================")
print(df_Flights.head())
print("========================================================")

cheap_flights = df_Flights[df_Flights['ticket_price'] < 1000]
print(cheap_flights[['flight_id', 'destination', 'ticket_price']])
print("========================================================")


df_airlines = pd.read_sql("SELECT * FROM airlines", con=engine)
print(f"\n=== Airlines ({len(df_airlines)} Airlines) ===")
print(df_airlines.head(3))
print("========================================================")
df_airplanes = pd.read_sql("SELECT * FROM airplanes", con=engine)
print(f"\n=== Airplanes ({len(df_airplanes)} Plan) ===")
print(df_airplanes.head(3))
print("========================================================")
df_passengers = pd.read_sql("SELECT * FROM passengers", con=engine)
print(f"\n=== Passengers ({len(df_passengers)}Passenger) ===")
print(df_passengers.head(3))
print("========================================================")
df_bookings = pd.read_sql("SELECT * FROM bookings", con=engine)
print(f"\n=== Bookings ({len(df_bookings)} Book) ===")
print(df_bookings.head(3))
print("========================================================")
print(df_bookings.info)

print("========================================================")
df_payments = pd.read_sql("SELECT * FROM payments", con=engine)
print(f"\n=== Payments (Total: {df_payments['amount'].sum() if 'amount' in df_payments.columns else 'N/A'}) ===")
print(df_payments.info)

print("========================================================")
