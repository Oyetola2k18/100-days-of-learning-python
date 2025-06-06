#learning about a concept called slicing 

piano_keys = ["a","b", "c", "d", "e", "f", "g"]

#ok lets say i want "c" to "e"
#i could just do 

# for k in piano_keys[2:5]:
#     print(k)

#the syntax is (starting:ending:interval)
# print(piano_keys[::-1])

#works for tuples also

piano_tupples = ("do","re","mi","fa","so","la","ti","do")

for p in piano_tupples[:3:1]:
    print(p)