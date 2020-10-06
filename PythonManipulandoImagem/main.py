from PIL import Image, ImageDraw, ImageFont
import os
from openpyxl import Workbook
from openpyxl import load_workbook

book = load_workbook('Imagens/planilha.xlsx')

sheet = book['Plan1']

d = sheet.dimensions
i = 1

for c1, c2 in sheet[d]:
    print(c1.value+" "+str(c2.value))

# for item in d:
#     nomei = sheet['A{}'.format(str(i+1))].value
#     print(nomei)
#     i = i + 1


# img = Image.open("Imagens/certificado.jpg")

# fnt = ImageFont.truetype(font='arial.ttf', size=24)

# d = ImageDraw.Draw(img)
# d.text((65, 358), "Reval", font=fnt, fill=(30, 30, 30))
# d.text((455, 358), "Estevão Garcia Junior", font=fnt, fill=(30, 30, 30))

# img.show()