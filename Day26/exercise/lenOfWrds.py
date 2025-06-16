sentence = "What is the airspeed velocity of an unladen swallow?"
split_sentence = sentence.split()

result = {word:len(word) for word in split_sentence}

print(result)