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

# ============================================================
# 3. KONTROLLO KAPACITETIN
# ============================================================

total_pixels = dimensions[0] * dimensions[1]

# 7 bit për çdo karakter (ASCII)
sbits = ''.join(format(ord(char), 'b').zfill(7) for char in secret)

# 14 bit për gjatësinë e mesazhit (max 16383 karaktere)
lbits = format(len(secret), 'b').zfill(14)

# Bashko bitat
bits = lbits + sbits

if len(bits) > total_pixels:
    print(f"Gabim: Nevojiten {len(bits)} bit, por kemi vetëm {total_pixels} piksela.")
    exit(1)

print(f"Po fshehim {len(bits)} bit ({len(secret)} karaktere) në {total_pixels} piksela...")



# 4. RENDITJA E RASTËSISHME E PIKELAVE


shuffledIndices = list(range(total_pixels))
random.seed(key)
random.shuffle(shuffledIndices)



# 5. FUNKSIONI PËR MODIFIKIMIN E PIKSELEVE


def modify_pixel(pixel, plane, bit, modifier):
    """
    Ndryshon një plan ngjyre të një pikseli.
    
    pixel: tuple (R, G, B)
    plane: 0=kuqe, 1=gjelbër, 2=blu
    bit: pozita e bitit (7=LSB)
    modifier: +1 ose -1 (rrit ose ul vlerën)
    """
    m = modifier * (2 ** (7 - bit))
    
    r = pixel[0] + m if plane == 0 else pixel[0]
    g = pixel[1] + m if plane == 1 else pixel[1]
    b = pixel[2] + m if plane == 2 else pixel[2]
    
    return (r, g, b)



# 6. FSHIH BITAT NË IMAZH

for i in range(len(bits)):
    x = shuffledIndices[i] % dimensions[0]
    y = shuffledIndices[i] // dimensions[0]
    
    p = format(pixels[x, y][colourPlane], 'b').zfill(8)
    
    if p[significantBit] == '0' and bits[i] == '1':
        pixels[x, y] = modify_pixel(pixels[x, y], colourPlane, significantBit, 1)
    elif p[significantBit] == '1' and bits[i] == '0':
        pixels[x, y] = modify_pixel(pixels[x, y], colourPlane, significantBit, -1)



# 7. RUAJ IMAZHIN


image.save(outputImage)
print(f"Fshehja u krye. Imazhi u ruajt si: {outputImage}")

