#convert a dictionary that has different days of the week with the temperature in celsius to farenheit


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {day:round(((temp *(9/5)) + 32),1) for (day,temp) in weather_c.items()}

print(weather_f)