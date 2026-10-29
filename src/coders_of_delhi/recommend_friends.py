"""Friend recommendation work belongs here. Add your own implementation."""
import json

with open("coders-of-delhi/data/processed/processed_data.json", "r", encoding="utf-8") as file:
	data = json.load(file)

print("Total users:", len(data["users"]))

user_lookup = {}

for user in data["users"]:
    user_lookup[user["id"]] = user

target_user_id = 1

direct_friends = user_lookup[target_user_id]["friends"]

for friend_id in direct_friends:
    friends_of_friends = user_lookup[friend_id]["friends"]

    for candidate_id in friends_of_friends:
        # Check whether candidate_id is not the target
        # Check whether candidate_id is not already a direct friend
        # Print only eligible candidate IDs





# for user in user_lookup:
#     for friend_id in direct_friends:
#         friend = user_lookup[friend_id]
#         print(f"Friend {friend_id} knows: {friend['friends']}")