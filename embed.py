from PIL import Image
import random

# Shared configuration
key = 2026
colour_plane = 1       # 0 = red, 1 = green, 2 = blue
bit_position = 7       # 7 = least significant bit

cover_image = 'img/flowers.bmp'
secret_file = 'secret.txt'
output_image = 'stego-image.bmp'


# Modify selected pixel bit
def modify_pixel(pixel, plane, bit_position, direction):
    change = direction * (2 ** (7 - bit_position))

    red = pixel[0] + change if plane == 0 else pixel[0]
    green = pixel[1] + change if plane == 1 else pixel[1]
    blue = pixel[2] + change if plane == 2 else pixel[2]

    return (red, green, blue)


# Open image
img = Image.open(cover_image).convert("RGB")
pixels = img.load()

width, height = img.size
total_pixels = width * height

# Create shuffled pixel order
indexes = list(range(total_pixels))

random.seed(key)
random.shuffle(indexes)

# Read secret message
with open(secret_file, 'r') as file:
    secret_message = file.read()

message_length = len(secret_message)

# Convert length to 14-bit binary
length_bits = format(message_length, '014b')

# Convert message to 7-bit ASCII
message_bits = ''

for char in secret_message:
    message_bits += format(ord(char), '07b')

# Full bit stream
all_bits = length_bits + message_bits

# Capacity check
if len(all_bits) > total_pixels:
    raise ValueError("Message is too large for this image.")

# Embed bits
for i, bit in enumerate(all_bits):

    pixel_index = indexes[i]

    x = pixel_index % width
    y = pixel_index // width

    pixel = pixels[x, y]

    # Select colour channel
    channel_value = pixel[colour_plane]

    # Convert to binary
    binary_value = format(channel_value, '08b')

    # Current bit in selected position
    current_bit = binary_value[bit_position]

    # If bit already correct, continue
    if current_bit == bit:
        continue

    # Decide direction
    if bit == '1':
        direction = 1
    else:
        direction = -1

    # Prevent overflow
    if channel_value == 255:
        direction = -1

    if channel_value == 0:
        direction = 1

    # Modify pixel
    new_pixel = modify_pixel(pixel, colour_plane, bit_position, direction)

    pixels[x, y] = new_pixel

# Save stego image
img.save(output_image)

print("Message embedded successfully!")
print("Saved as:", output_image)