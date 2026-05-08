"""
extract.py — Nxjerr mesazhin e fshehur nga imazhi stego.
"""

from PIL import Image
import random

# 1. KONFIGURIMI (TË NJËJTAT VIERA SI NË EMBED.PY)


key = 12345
colourPlane = 0
significantBit = 7
stegoImage = "stego-image.bmp"



# 2. LEXO IMAZHIN

image = Image.open(stegoImage).convert("RGB")
dimensions = image.size
pixels = image.load()
total_pixels = dimensions[0] * dimensions[1]


# 3. RINDËRTO RENDITJEN E PIKELAVE


shuffledIndices = list(range(total_pixels))
random.seed(key)
random.shuffle(shuffledIndices)



    
print("\nMesazhi u ruajt edhe në 'extracted_secret.txt'")
