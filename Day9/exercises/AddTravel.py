#Basically a program that improves our knowledge on Nesting of Lists and Dictionarires
travel_log =[
{
    "country": "France",
    "Visits": 112,
    "cities": ["Paris","Lille","Dijion"]
},
{
    "country": "France",
    "Visits": 112,
    "cities": ["Paris","Lille","Dijion"]
},
] 

def add_new_country(Country_list,Vist_times,cityList):
    new_entry = {
        "country": Country_list,
        "Visits": Vist_times,
        "cities": cityList,
    }
    travel_log.append(new_entry)

    print(f"You've visited {new_entry['country']} {new_entry['Visits']}times")

    print(f"you have been to {new_entry['cities'][0]} and {new_entry['cities'][1]}")


add_new_country("Russia", 2, ["Moscow","Saint petersburg"])
print(travel_log)