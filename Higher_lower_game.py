
data = [{"name": "Instagram",
        "follower_count": 346,
        "description": "Social media platform",
        "country": "United States"},
        {"name": "Cristiano Ronaldo",
        "follower_count": 310,
        "description": "Footballer",
        "country": "Portugal"},
        {"name": "Selina Gomez",
        "follower_count": 418,
        "description": "Musician",
        "country": "United States"},
        {"name": "Khloe` Kardashian",
        "follower_count": 306,
        "description": "businesswomen",
        "country": "US"},
        {"name": "Leonel Messi",
        "follower_count": 83,
        "description": "Footballer",
        "country": "Argentina"},
        {"name": "Kylie Jenner",
        "follower_count": 396,
        "description": "businesswomen",
        "country": "US"},
        {"name": "Neymar Jr.",
        "follower_count": 108,
        "description": "Footballer",
        "country": "Brazil"},
        {"name": "Justin Bieber",
        "follower_count": 289,
        "description": "Musician",
        "country": "US"},
        {"name": "Virat Kohli",
        "follower_count": 270,
        "description": "Cricketer",
        "country": "India"},
        {"name": "Dwayne Johnson",
        "follower_count": 126,
        "description": "Actor",
        "country": "US"},
        ]


import random

random.shuffle(data)
print("******************************")
print("WELLCOME TO HIGHER LOWER GAME!")
print("******************************\n")

def higher_lower():
    score = 0
    i = 0
    while i < len(data)-1:
        j = i + 1
        person1 = data[i]
        person2 = data[j]
        print(f"Compare A: {person1["name"]}, a {person1["description"]}, from {person1["country"]}")
        print("""
          _    __
         | |  / /_____
         | | / / ____/
         | |/ (____)
         |___/_____(-)
         """)
        print(f"Compare B: {person2["name"]}, a {person2["description"]}, from {person2["country"]}")
        print("-------------------------------------------------------------------------------------")
        user_guess = input("Who has more followers?  Type A or B: ").upper()
        if user_guess == "A":
            if person1["follower_count"] > person2["follower_count"]:
                score += 1
            else:
                return (f"Sorry! that's wrong. Final score: {score}")

        if user_guess == "B":
            if person2["follower_count"] > person1["follower_count"]:
                score += 1
            else:
                return (f"Sorry! that's wrong. Final score: {score}")
        i += 1
    return f"You have passed this level with a score of {score}"

print(higher_lower())




