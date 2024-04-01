import hashlib

def save_image(image):
    image_hash = hashlib.sha256(image.tobytes()).hexdigest()
    image_path = f"static/images/{image_hash}.png"
    image.save(image_path)

    image_name = f"{image_hash}.png"
    return image_name
