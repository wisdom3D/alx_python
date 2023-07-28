def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*(5/9)
    return print("{:.2f}".format(celsius))
convert_to_celsius(-459.67)