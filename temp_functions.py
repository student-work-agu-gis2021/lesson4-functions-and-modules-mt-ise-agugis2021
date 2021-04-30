def fahr_to_celsius(temp_fahrenheit):
  return(temp_fahrenheit-32)/1.8

def temp_classifier(temp_celsius):
  #The purpose of function : Separate the Temperatures
  #Paramater: temp_celsius
  #4 classes from 0 to 3
  if temp_celsius<-2:
   return 0
  elif temp_celsius<2:
    return 1
  elif temp_celsius<15:
    return 2
  elif temp_celsius>=15:
    return 3