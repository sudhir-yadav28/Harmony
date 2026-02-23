from PIL import Image
import os

filepath = '/Users/sudhiryadav/Downloads/harmony-replica/images/icons/image.png'

try:
    img = Image.open(filepath)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    
    # We want to remove pure white or very light colors (background)
    # The logo has black text and an orange icon. We must be careful not to remove the inside of letters if they are white, wait, letters usually don't have white inside them, they are transparent when background is removed.
    # Actually, a simpler approach is preserving everything that is not nearly white.
    for item in datas:
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            # Replace white with transparent
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(filepath, "PNG")
    print("Background removed successfully.")
except Exception as e:
    print(f"Error: {e}")

