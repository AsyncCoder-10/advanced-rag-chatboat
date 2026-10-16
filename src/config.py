import os
from dotenv import load_dotenv

# 1. Print the current working directory to see where Python is looking
print(f"Current Working Directory: {os.getcwd()}")

# 2. Load the .env file
load_dotenv()

# 3. Print the entire environment dictionary to see if it loaded (Don't worry, this is temporary)
# print("Environment Variables loaded:", os.environ)

# 4. Try to get the key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# 5. Check if it worked
if not GROQ_API_KEY:
    print("❌ ERROR: Could not find GROQ_API_KEY. Please check your .env file.")
    raise ValueError("GROQ_API_KEY is missing from .env file")
else:
    print("✅ SUCCESS: GROQ_API_KEY loaded successfully!")
