#Create a function that converts Fahrenheit temperatures to Celsius 
#Start with prompting the user for a temperature in Fahrenheit. Then call your function and pass in the user input as a parameter.

#Your function should:

#have one parameter: the temperature in Fahrenheit
#do the conversion with this formula: C = (F - 32) x 5/9
#ensure that the parameter you pass in is a number by converting it with int()
#Output the result in a full sentence using string interpolation.

def Fahrenheitconvert(f_conversion):
    celcius = ((int(f_conversion)-32)*5/9)
    print("{}F converted to Celcius is {}C".format(f_conversion,celcius))


Fahrenheitconvert(32)
Fahrenheitconvert(-32)
Fahrenheitconvert(212)
