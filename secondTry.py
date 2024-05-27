from openai import OpenAI
import DANGER_API_KEYS.keys



query="""
Can you find any of these on costo website:
Acer	CP7271K
Acer	Predator X32
Acer	X27
Acer	X32
Acer	X35
Acer	X38S
ASUS	PG65
ASUS	PG27UQ
ASUS	PG32UQX
ASUS	PG35VQ
ASUS	PG32UQXE
AGON by AOC	AG353UCG
AGON by AOC	AGON PRO AG274QGM
AGON by AOC	AGON PRO AG274QG
Alienware	AW2721D
Alienware	AW3821DW
Alienware	AW3423DW
HP	OMEN X Emperium 65
LG	34GP950G
MSI	MEG 271Q Mini LED
MSI	MEG381CQR
ViewSonic	ELITE XG272G
ViewSonic	XG321UG
"""

print("SecondTry!", query)

API_KEY = DANGER_API_KEYS.keys.API_KEY
client = OpenAI(api_key=API_KEY)


completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": query}
  ]
)

print(completion.choices[0].message)
