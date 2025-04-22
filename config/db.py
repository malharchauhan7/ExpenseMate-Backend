from motor.motor_asyncio import AsyncIOMotorClient
import os

uri = "mongodb+srv://malharchauhan7777:Malhar7777@expensemate.mpzoetd.mongodb.net/?retryWrites=true&w=majority&appName=expensemate"
# uri = os.getenv("MONGODB_URI")
client = AsyncIOMotorClient(uri)

db = client["expense-tracker-db"]

users_collection = db["users"]
category_collection = db["category"]
transaction_collection = db["transactions"]
budget_collection = db["budgets"]