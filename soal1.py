def converts_temperature (value, unit):
    if unit == 'C' :
        return value *9/5 + 32

    elif unit == 'F' :
        return (value - 32)* 9/5

    else:
        return None
    
input_value = float(input("Masukkan value: "))
input_unit =    input("Masukkan unit (c/f): ")

konversi = converts_temperature(input_value, input_unit)
if (input_unit == 'c'):
    print(f"{input_value} derajat Celsius = {konversi} derajat Fahrenheit")
elif (input_unit == 'f'):
    print(f"{input_value} derajat Fahrenheit = {konversi} derajat Celsius")