from PIL import Image

# Open the image
image = Image.open("input.jpg")

# Resize the image
resized_image = image.resize((2500,1500))  # (width, height)

# Save the cropped and resized image
resized_image.save("imgCroppingAndResizing/resized_image3.jpg")









""" in case the image should maintain proportainallty 
    
    k= image.width/image.height
    new_height=(new_width/k)
    new_width=1000
"""