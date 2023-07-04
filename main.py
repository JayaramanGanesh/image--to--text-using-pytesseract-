import pytesseract
import nltk
from PIL import Image
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
image_path = 'C:\\Users\\Admin\\3D Objects\\1.jpg'

def image_to_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def collect_keywords(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    freq_dist = nltk.FreqDist(filtered_tokens)
    keywords = freq_dist.most_common(1000)
    return keywords


result = image_to_text(image_path)
text = result
keywords = collect_keywords(text)

for ii in keywords:
    print(ii)
