def to_celsius(x):
    if x < 0:
      raise ValueError ("Temperature can not be negative.")
    if type(x) not in [int, float]:
      raise TypeError ("Temperature should be Integer or Float number")
    return (x-32)*5/9

# converting 0 to 100 farenheit into celcius in steps of 10

for temp_f in range(1, 100, 1):
    print("Farenheit = %3.1f, Celsius: %3.1f" % (temp_f, to_celsius(temp_f)))
    celsius = to_celsius(temp_f)
 
#print("Farenheit = %3.1f, Celsius: %3.1f" % (3+5j, to_celsius(3+5j))) 
#print("Farenheit = %3.1f, Celsius: %3.1f" % (True, to_celsius(True))) 
#print("Farenheit = %3.1f, Celsius: %3.1f" % ("temp", to_celsius("temp"))) 


