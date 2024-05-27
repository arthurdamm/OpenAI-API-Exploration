from openai import OpenAI
import DANGER_API_KEYS.keys

API_KEY = DANGER_API_KEYS.keys.API_KEY
print("KEYS ARE", API_KEY)


client = OpenAI(
  organization='YOUR_ORG_ID',
  project='$PROJECT_ID',
)