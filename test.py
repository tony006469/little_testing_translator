from googletrans import Translator
from PIL import Image
import cv2
import pytesseract


# def recorder():
#     r = sr.Recognizer
#     with sr.Microphone() as source:
#         print('Speak:')
#         audio = r.listen(source)
#         abc=r.recognize.google(audio)
#         print('You said:{}'.format(abc))

# def make_photo():
#     """使用opencv拍照"""
#     cap = cv2.VideoCapture(0)  # 默认的摄像头
#     while True:
#         ret, frame = cap.read()
#         if ret:
#             cv2.imshow("capture", frame)  # 弹窗口
#             # 等待按键q操作关闭摄像头
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 file_name = "xieyang.jpeg"
#                 cv2.imwrite(file_name, frame)
#                 break
#         else:
#             break
 
#     cap.release()
#     cv2.destroyAllWindows()


def main():
        # Get File Name from Command Line
    #recorder()
    path = input("Enter the file path : ").strip()
    
    # Load the required image
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    preprocess = False
    temp = input(
        "Do you want to pre-process the image ?\nThreshold : 1\nGrey : 2\nNone : 0\nEnter your choice : ").strip()

    # If user enters 1, Process Threshold. Else if user enters 2, Process Median Blur. Else, do nothing
    if temp == "1":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif temp == "2":
        gray = cv2.medianBlur(gray, 3)

    # Store grayscale image as a temporary file to apply OCR
    filename = "{}.png".format("temp")
    cv2.imwrite(filename, gray)

    # Load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(Image.open(filename))

    print("OCR Text is " + text)
    translator = Translator()
    a=translator.translate(text, dest='zh-tw')
    print (a)

    b=translator.translate('我很帥,牛肉麵,滷肉飯,饅頭,臭豆腐,定哥,蕭祺恩,宜蘭沈玉琳', dest='en')
    print (b)
    

try:
    main()
except Exception as e:
    print(e.args)
    print(e.__cause__)
    
    

# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
    #a=translator.translate('我長得比雞帥很多,牛肉麵,滷肉飯,饅頭,臭豆腐,吳佳定', dest='en')
# <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
#translator.translate('veritas lux mea', src='la')
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
    #print (a)

