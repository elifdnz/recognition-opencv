from PIL import Image
import pytesseract

img = Image.open("C://Documents//text.png")


text = pytesseract.image_to_string(img, lang="eng")

print(text)