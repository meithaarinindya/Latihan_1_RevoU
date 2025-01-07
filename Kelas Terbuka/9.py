#pertemuan 9 = aplikasi aritmetika

#program konversi suhu
print("\n===PROGRAM KONVERSI TEMPERATUR===\n")

#suhu dalam celcius
print("---SUHU DALAM CELCIUS---")
c = float(input("masukan suhu dalam celcius : "))
print("jika suhu dalam celcius adalah", c,"celcius")
#ubah ke reamur
reamur = (4/5)*c
print("maka suhu dalam reamur adalah",reamur,"reamur")
#ubah ke fahrenheit
fahrenheit = ((9/5) * c) + 32
print("maka suhu dalam fahrenheit",fahrenheit,"fahrenheit")
#ubah ke kelvin
kelvin = c + 273
print("maka suhu dalam kelvin adalah",kelvin,"kelvin")

#suhu dalam reamur
print("\n---SUHU DALAM REAMUR---")
r = float(input("masukan suhu dalam reamur : "))
print("jika suhu dalam reamur adalah",r,"reamur")
#ubah ke celcius
celcius = (5/4) * r
print("maka suhu dalam celcius adalah",celcius,"celcius")
#ubah ke fahrenheit
fahrenheit = ((9/4) * r) + 32
print("maka suhu dalam fahrenheit adalah",fahrenheit,"fahrenheit")
#ubah ke kelvin
kelvin = ((5/4)*r)+273
print("maka suhu dalam kelvin adalah",kelvin,"kelvin")

#suhu dalam fahrenheit
print("\n---SUHU DALAM FAHRENHEIT---")
f = float(input("masukan suhu dalam fahrenheit : "))
print("jika suhu dalam fahrenheit adalah",f,"fahrenheit")
#ubah ke celcius
celcius = (f-32)/9*5
print("maka suhu dalam celcius adalah",celcius,"celcius")
#ubah ke reamur
reamur = (f-32)/9*4
print("maka suhu dalam reamur adalah",reamur,"reamur")
#ubah ke kelvin
kelvin = ((f-32)/9*5)+273
print("maka suhu dalam kelvin adalah",kelvin,"kelvin")

#suhu dalam kelvin
print("\n---SUHU DALAM KELVIN---")
k = float(input("suhu dalam kelvin adalah : "))
print("jika suhu dalam kelvin adalah", k)
#ubah ke celcius
celcius = (k-273)
print("maka suhu dalam celcius adalah",celcius,"celcius")
#ubah ke reamur
reamur = (k-273)/5*4
print("maka suhu dalam reamur adalah",reamur,"reamur")
#ubah ke fahrenheiit
fahrenheit = ((k-273)/5*9)+32
print("maka suhu dalam fahrenheit adalah",fahrenheit,"fahrenheit")