# great idea using dictionaries for that country game

"""
Use a dictionary to enumerate all possible personalities then when
creating extra countries (in a for loop, etc.) use something like:
num = random.randint(a,b)
countryXpersonality = personalities[num]
"""
personalities = {
    1: "Friendly"
    2: "Short Tempered"
    3: "Cautious"
    4: "Quiet"
    5: "Angry"
}

# Then do this for the other string-related info about countries