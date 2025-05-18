#learning how to nest lists and dictionaries inside a dictionary
# 
# nesting

capitals = {
    "France":"paris",
    "Germany":"Berlin",
} 
# {#nesting lists
#     "France":{
#         "cities_visited":["Paris","lille"],
#     }
# }
#nesting a list in a dictionary
#each key can only have 1 value
travel_log ={
    "Francce": ["Paris","LiLle","Dijon"],
    "Germany": ["Berlin","Hamburg", "Stuttgart"]
}
#nesting a list in a list

# random_chars = ["A","B","C","D",[1,2,3,4,5],"E"]\

# print(random_chars[4])

#nesting a dictionary in a dictionary(with lists)

# travel_log2 ={
#     "France":{
#         "Cities_visited":["Paris","LiLle","Dijon"],
#         "total_num_of_visits":12
#     },
#     "Germany":{
#         "cities_visited":["abuja","onatario","Lagos"],
#         "times_vistied":[1,2,3,54],
#     },
# }

#nesting a dictionary in a list 
travel_log2 =[
    {   "country":"France",
        "Cities_visited":["Paris","LiLle","Dijon"],
        "total_num_of_visits":12
    },
    {   "countries":"Germany",
        "cities_visited":["abuja","onatario","Lagos"],
        "times_vistied":2,
    },
]
print(travel_log2[0])