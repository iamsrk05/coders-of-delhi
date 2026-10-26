import json

with open("coders-of-delhi/data/raw/codebook_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    data["users"][0]["friends"].append(3)

print("Total User:", len(data["users"]))

for user in data["users"]:
    print(f"User: {user["name"]}\nFriends: {user["friends"]} \nLiked Page: {user["liked_pages"]}")

    original_friends = len(user["friends"])
    unique_friends = len(set(user["friends"]))

    if original_friends != unique_friends:
        cleaned_friends = list(dict.fromkeys(user["friends"]))
        user["friends"] = cleaned_friends
        print(f"Duplicate detected for {user['name']} and cleaned as: {cleaned_friends}")
        print(cleaned_friends)

    original_pages = len(user["liked_pages"])
    unique_pages = len(set(user["liked_pages"]))
    data["users"][0]["liked_pages"].append(101)

    if original_pages != unique_pages:
        cleaned_pages = list(dict.fromkeys(user["liked_pages"]))
        user["liked_pages"] = cleaned_pages
        print(f"Duplicate detected for {user['name']} and cleaned as: {cleaned_pages}")
        print(cleaned_pages)
