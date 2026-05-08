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



# 4. LEXO 14 BITAT E PARË (GJATËSIA E MESAZHIT)

length_bits = []
for i in range(14):
    x = shuffledIndices[i] % dimensions[0]
    y = shuffledIndices[i] // dimensions[0]
    
    colour_value = pixels[x, y][colourPlane]
    p = format(colour_value, 'b').zfill(8)
    length_bits.append(p[significantBit])

length_bits_str = ''.join(length_bits)
message_length = int(length_bits_str, 2)

print(f"Gjatësia e mesazhit: {message_length} karaktere")


# 5. LEXO BITAT E MESAZHIT

message_bits = []
start_index = 14
num_bits_needed = message_length * 7

for i in range(start_index, start_index + num_bits_needed):
    x = shuffledIndices[i] % dimensions[0]
    y = shuffledIndices[i] // dimensions[0]
    
    colour_value = pixels[x, y][colourPlane]
    p = format(colour_value, 'b').zfill(8)
    message_bits.append(p[significantBit])



# 6. DEKODONO MESAZHIN


message = ""
for i in range(0, len(message_bits), 7):
    byte_bits = ''.join(message_bits[i:i+7])
    char_code = int(byte_bits, 2)
    message += chr(char_code)



# 7. SHFAQO DHE RUAJ MESAZHIN


print("\n" + "="*50)
print("MESAZHI I FSHUR:")
print("="*50)
print(message)
print("="*50)

with open("extracted_secret.txt", "w", encoding="utf-8") as f:
    f.write(message)
    
print("\nMesazhi u ruajt edhe në 'extracted_secret.txt'")print("\nMesazhi u ruajt edhe në 'extracted_secret.txt'")
