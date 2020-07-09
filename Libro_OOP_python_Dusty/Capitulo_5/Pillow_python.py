from zip_processor import ZipProcessor
import sys
from PIL import Image
class ScaleZip(ZipProcessor):
    def process_zip(self):
        for filename in self.temp_directory.iterdir():
            ima = Image.open(str(filename))
            scale = ima.resize((640,480))
            scale.save(str(filename))

if __name__=="__main__":
    ScaleZip(*sys.argv[1:4]).process_file()