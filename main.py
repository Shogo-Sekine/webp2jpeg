from PIL import Image
import os

webps_path = "webps/"
outputs_path = 'outputs/'

webps = os.listdir(webps_path)

for webp in webps:
    file_name = webp.split('.')[0]
    im = Image.open(f'{webps_path}{webp}').convert('RGB')
    im.save(f'{outputs_path}{file_name}.jpg', 'jpeg')