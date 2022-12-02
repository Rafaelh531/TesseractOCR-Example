#precisa de poppler  conda install -c conda-forge poppler  e tessseractt-ocr
# C:\Users\rafa6899\Miniconda3\envs\pythonAMB
from pdf2image import convert_from_path
import cv2
import pytesseract
from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image, ImageEnhance, ImageFilter
import re

#inputpdf = PdfFileReader(open("C:\\Users\\rafa6899\\Downloads\\teste\eddff.pdf", "rb"))

#for i in range(inputpdf.numPages):
  #  output = PdfFileWriter()
  #  output.addPage(inputpdf.getPage(i))
  #  document_page = "document-page" + (str)(i+1) + ".pdf"
  #  with open(document_page, "wb") as outputStream:
  #      output.write(outputStream)
  #  images  = convert_from_path(document_page,500)

  #  for j, image in enumerate(images):
  #      fname = 'image'+str(i+1)+'.png'
  #      image.save(fname, "PNG")
    
  #  croped = "croped"+str(i+1)+'.png' 
  #  w=200
  #  h = 200
  #  img = cv2.imread(fname)
  #  crop_img = img[0:1000,0:4132]
  #  imageout = fname
  #  cv2.imwrite(croped, crop_img)
    #cv2.imshow("cropped", crop_img)
    
    #cv2.waitKey(0)
    
    #
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rafa6899\AppData\Local\Programs\Tesseract-OCR\tesseract'
str1 = pytesseract.image_to_string(Image.open("C:\\Users\\rafa6899\\Downloads\\teste.jpg"))
    #
print(str1)
    #if "RNC"  in str1 or "Relatorio de Conformidade" in str1 or "relatorio de cno Conformidad" in str1:
    #    print("pagina " + (str)(i+1) + " É um relatorio de não conformidade")
    #    try:
    #        found = re.search('d{2}', str1).group(1)
    #        print(found)
    #    except AttributeError:
            # AAA, ZZZ not found in the original string
    #        found = '' # apply your error handling

  #  else:
  #      print("pagina " + (str)(i+1) + " Não é um relatório de não conformidade")
   # print(str1)
