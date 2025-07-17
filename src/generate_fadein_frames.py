from PIL import Image, ImageEnhance
import os

# Path to the input logo image
logo_path = "./images/1080.png"

# Output directory for generated frames
output_dir = "part0"
os.makedirs(output_dir, exist_ok=True)

# Open the original image and ensure RGBA mode
img = Image.open(logo_path).convert("RGBA")

# Total number of frames to generate
total_frames = 60

for i in range(total_frames):
    # Brightness factor: from 0.0 (black) to 1.0 (original brightness)
    brightness_factor = i / (total_frames - 1)
    
    # Adjust brightness
    enhancer = ImageEnhance.Brightness(img)
    new_img = enhancer.enhance(brightness_factor)
    
    # Frame name: 00000.png ~ 00059.png
    filename = f"{i:05d}.png"
    new_img.save(os.path.join(output_dir, filename))

print("✅ 60 fade-in frames generated in", output_dir)
