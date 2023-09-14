import sqlite3
import matplotlib.pyplot as plt
        
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

years = []
co2 = []
temp = []

cursor.execute('SELECT Year, CO2, Temperature FROM ClimateData')
data = cursor.fetchall()

for row in data:
    year, co2_value, temp_value = row
    years.append(year)
    co2.append(co2_value)
    temp.append(temp_value)

conn.close()



plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

plt.show() 
plt.savefig("co2_temp_1.png") 