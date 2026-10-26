
import json

with open("coders-of-delhi/data/raw/codebook_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Total User:", len(data["users"]))

for user in data["users"]:
    print(f"User: {user["name"]}\nFriends: {user["friends"]} \nLiked Page: {user["liked_pages"]}")
    
