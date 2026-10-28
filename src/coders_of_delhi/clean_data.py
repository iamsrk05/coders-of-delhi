import json

with open("coders-of-delhi/data/raw/codebook_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

data["users"][0]["friends"].append(3)
data["users"][0]["liked_pages"].append(101)

print("Total User:", len(data["users"]))

for user in data["users"]:
    original_friends = len(user["friends"])
    unique_friends = len(set(user["friends"]))

    if original_friends != unique_friends:
        cleaned_friends = list(dict.fromkeys(user["friends"]))
        user["friends"] = cleaned_friends

    original_pages = len(user["liked_pages"])
    unique_pages = len(set(user["liked_pages"]))

    if original_pages != unique_pages:
        cleaned_pages = list(dict.fromkeys(user["liked_pages"]))
        user["liked_pages"] = cleaned_pages
        print(f"Duplicate detected for {user['name']} and cleaned as: {cleaned_pages}")
        print(cleaned_pages)

    print(f"User: {user['name']}\nFriends: {user['friends']}\nLiked Page: {user['liked_pages']}")

valid_user_ids = set()

for user in data["users"]:
    valid_user_ids.add(user["id"])
    
print(valid_user_ids)

for user in data["users"]:
    if user["id"] in user["friends"]:
        print(f"Error found: {user['name']} (ID {user['id']}) is in their own friends list")
        user["friends"].remove(user["id"])
        print(f"Removed self-friendship for {user['name']}")
        print(user["friends"])

    for friend_id in user["friends"]:
        print('friend_id =>', friend_id, 'valid_user_ids =>', valid_user_ids )
        if friend_id not in valid_user_ids:
            print(f"Invalid friend ID: {friend_id} for {user['name']}")

valid_page_id = set()

for page in data["pages"]:
    valid_page_id.add(page["id"])

print(valid_page_id)

for user in data["users"]:
    for liked_page in user["liked_pages"][:]:
        if liked_page not in valid_page_id:
            print(f"Invalid page ID: {liked_page} for {user['name']}")
            user["liked_pages"].remove(liked_page)

print("\nFinal Cleaned Data:")

for user in data["users"]:
    print(f"User: {user['name']}")
    print(f"Friends: {user['friends']}")
    print(f"Liked Pages: {user['liked_pages']}")
    print()

