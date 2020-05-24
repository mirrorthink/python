import pytesseract
from PIL import Image
from urllib import request
import time


def main():
    pytesseract.pytesseract.tesseract_cmd = r'E:\data_Learn\tesseract\tesseract.exe'
    url = "验证码链接"
    while True:
        request.urlretrieve(url, 'captoha.png')
        image = Image.open('')
        text = pytesseract.image_to_string(image)
        print(text)
        time.sleep(2)


if __name__ == '__main__':
    main()