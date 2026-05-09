from PIL import Image
import random

# Shared configuration
key = 2026
colour_plane = 1
bit_position = 7

stego_image = 'stego-image.bmp'

# Open image
img = Image.open(stego_image)
pixels = img.load()

width, height = img.size
total_pixels = width * height

# Rebuild shuffled index list
indexes = list(range(total_pixels))

random.seed(key)
random.shuffle(indexes)

# Extract bits
extracted_bits = []

for i in range(total_pixels):

    pixel_index = indexes[i]

    x = pixel_index % width
    y = pixel_index // width

    pixel = pixels[x, y]

    channel_value = pixel[colour_plane]

    binary_value = format(channel_value, '08b')

    extracted_bits.append(binary_value[bit_position])

# Recover message length
length_bits = ''.join(extracted_bits[:14])

message_length = int(length_bits, 2)

# Recover message bits
message_bits = extracted_bits[14:14 + (message_length * 7)]

# Decode message
message = ''

for i in range(0, len(message_bits), 7):

    char_bits = ''.join(message_bits[i:i+7])

    ascii_value = int(char_bits, 2)

    message += chr(ascii_value)

print("Recovered message:")
print(message)