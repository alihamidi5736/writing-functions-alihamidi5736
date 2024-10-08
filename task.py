# You will define and write each function for the task in this file

def tempeture_conventor(tempture, unit):
    if unit == "C" :
        fahrenheit = (tempture * 9/5) + 32:
        return f"{fahrenheit} F"
      elif unit == "F":

        celsius = (tempture - 32) * 5/9:
        return f"{celsius} C"
        else return "invalid unit"
