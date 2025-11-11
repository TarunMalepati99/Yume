# 🧩 Smart Collage Maker (Sequential Upload + Auto Color Borders)
from PIL import Image, ImageOps
from google.colab import files
import numpy as np

def get_dominant_color(image):
    """Return dominant color from an image (as RGB tuple)."""
    img = image.copy().resize((50, 50))
    pixels = np.array(img).reshape(-1, 3)
    avg_color = tuple(np.mean(pixels, axis=0).astype(int))
    return avg_color

def add_border(image, border_size=15):
    """Add border using image's dominant color."""
    color = get_dominant_color(image)
    return ImageOps.expand(image, border=border_size, fill=color)

def create_collage(image_paths, collage_path="collage_output.jpg"):
    n = len(image_paths)
    if n == 0 or n > 5:
        raise ValueError("Please upload between 1 and 5 images.")

    # Load and process all images
    images = [Image.open(p).convert("RGB") for p in image_paths]
    target_size = (400, 400)
    images = [add_border(img.resize(target_size)) for img in images]

    # Define collage layout
    if n == 1:
        collage = images[0]
    elif n == 2:
        collage = Image.new("RGB", (830, 430))
        collage.paste(images[0], (15, 15))
        collage.paste(images[1], (415, 15))
    elif n == 3:
        collage = Image.new("RGB", (830, 830), (255, 255, 255))
        collage.paste(images[0], (215, 15))
        collage.paste(images[1], (15, 415))
        collage.paste(images[2], (415, 415))
    elif n == 4:
        collage = Image.new("RGB", (830, 830))
        collage.paste(images[0], (15, 15))
        collage.paste(images[1], (415, 15))
        collage.paste(images[2], (15, 415))
        collage.paste(images[3], (415, 415))
    elif n == 5:
        collage = Image.new("RGB", (830, 1030), (255, 255, 255))
        collage.paste(images[0], (215, 15))
        collage.paste(images[1], (15, 415))
        collage.paste(images[2], (415, 415))
        collage.paste(images[3], (15, 815))
        collage.paste(images[4], (415, 815))

    collage.save(collage_path)
    collage.show()
    print(f"✅ Collage saved as {collage_path}")

# --- Sequential Upload Section ---
image_files = []
print("📸 Upload your images one by one (max 5). Type 'done' to finish early.\n")

for i in range(5):
    ans = input(f"Upload image {i+1}? (y/n or 'done'): ").strip().lower()
    if ans == 'done' or ans == 'n':
        break
    print(f"➡️ Please upload image {i+1}:")
    uploaded = files.upload()
    new_files = list(uploaded.keys())
    if new_files:
        image_files.append(new_files[0])
    else:
        print("⚠️ No file uploaded, skipping.")

if image_files:
    create_collage(image_files, "final_collage.jpg")
else:
    print("❌ No images uploaded. Collage not created.")
