import pytesseract
from PIL import Image, ImageEnhance

# 1.引入Tesseract程序
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
# 2.使用Image模块下的Open()函数打开图片
im = Image.open('ocr1.png', mode='r')
# print(image)
# 调色
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
# 把图片调成只有黑白两个颜色，处理后每个像素色用8位表示
im = im.convert('1')
#im.show() #测试查看

xsize, ysize = im.size  # 长、宽
#对照片里的所有像素点：如果像素色不是白色并且右边的一个像素点像素色是白色（RGB（255，255,255））或者像素色不是白色并且下方的一个像素点是白色的，统一变成白色
for i in range(ysize-1):
  for j in range(xsize-1):
    if (im.getpixel((j, i)) !=255&im.getpixel((j+1,i))==255):
      im.putpixel((j, i), 255)
    if(im.getpixel((j,i)) != 255&im.getpixel((j,i+1))==255):
      im.putpixel((j, i), 255)
#im.show()  #再看看效果

# 把上面我们变成白色的小黑点给他补一点回来- -
for i in range(ysize - 1):
  for j in range(xsize - 1):
    if (im.getpixel((j, i))!=255&im.getpixel((j+1,i)) !=255):
      im.putpixel((j, i), 0)
    if (im.getpixel((j, i))!=255&im.getpixel((j,i+1)) !=255):
      im.putpixel((j, i), 0)
#im.show()  # 再看看效果

# 3.识别图片文字
print(im)
code = pytesseract.image_to_string(im)
print(code)