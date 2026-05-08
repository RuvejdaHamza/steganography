"""
embed.py — Fsheh një mesazh tekst brenda një imazhi bitmap.
"""

from PIL import Image
import random


# 1. KONFIGURIMI


key = 12345                    # Çelësi për randomizim
colourPlane = 0                # 0=kuqe, 1=gjelbër, 2=blu
significantBit = 7             # 7=biti më pak i rëndësishëm (LSB)
coverImage = "cover.bmp"       # Imazhi origjinal
secretFile = "secret.txt"      # Mesazhi sekret
outputImage = "stego-image.bmp" # Imazhi me mesazh të fshehur



# 2. LEXO IMAZHIN DHE MESAZHIN


image = Image.open(coverImage).convert("RGB")
dimensions = image.size
pixels = image.load()

with open(secretFile, "r", encoding="utf-8") as f:
    secret = f.read()


