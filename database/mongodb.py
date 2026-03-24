from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://hishammon:hishammon@cluster0.2g7bqyf.mongodb.net/?appName=Cluster0"
client = AsyncIOMotorClient(MONGO_URL)
db = client['Dark-H-Filter']
col = db['files']

async def save_file(file_data):
    await col.insert_one(file_data)

async def search_file(query):
    # സിമ്പിൾ സെർച്ച് ലോജിക്
    files = col.find({"file_name": {"$regex": query, "$options": "i"}})
    return await files.to_list(length=10)
