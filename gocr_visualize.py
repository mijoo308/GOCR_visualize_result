from xml.etree.ElementTree import parse
import PIL
from PIL import Image, ImageDraw, ImageFont

tree = parse('./sample_img.xml')  # xml path 입력

user = tree.find('./block')

boxes = user.findall("line")

new_img1 = Image.new("RGB", (1229, 836), "white") # 원하는 크기로 지정
new_img2 = Image.open('./sample_img.jpg').convert('RGB')  #img path입력
draw1 = ImageDraw.Draw(new_img1)
draw2 = ImageDraw.Draw(new_img2)
font1 = ImageFont.truetype("arial", 36)
font2 = ImageFont.truetype("arial", 25)
for box in boxes:
    chars = box.findall("box")
    for char in chars:
        x = int(char.get("x"))
        y = int(char.get("y"))
        ch = char.get("value")

        print(char.attrib)
        s = char.get("value")
        if len(s) == 1:
            draw2.text((x, y+25), s, (255,0,0), font=font2)
            draw1.text((x, y), s, (255,0,0), font=font1)

new_img1.save("sample_result1.jpg")
new_img2.save("sample_result2.jpg")


