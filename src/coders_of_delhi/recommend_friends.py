"""Friend recommendation work belongs here. Add your own implementation."""
import json

with open("coders-of-delhi/data/processed/processed_data.json", "r", encoding="utf-8") as file:
	data = json.load(file)

print("Total users:", len(data["users"]))