import os
from wand.image import Image
import base64

SCRIPT_DIR = os.path.dirname(__file__)
resume = "resume_workspace"
PDF_FILENAME = "resume_workspace\main_template.pdf"

pdf_file = open(os.path.join(SCRIPT_DIR, os.pardir, PDF_FILENAME), "rb")
encoded_string = base64.b64encode(pdf_file.read())

from PIL import Image
from pdf2image import convert_from_path
pages = convert_from_path(os.path.join(SCRIPT_DIR, os.pardir, PDF_FILENAME), 500)
count = 0
for page in pages:
    count = count + 1
    name = "".join(["page", str(count)])
    page.save("".join([name, '.jpg']), 'JPEG')


# Converting first page into JPG
with Image(filename=os.path.join(SCRIPT_DIR, os.pardir, PDF_FILENAME)) as img:
     img.save(filename="/temp.jpg")