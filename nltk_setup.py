import nltk
import os
nltk_data_path = os.path.join(os.getcwd(), "nltk_data")
nltk.data.path.append(nltk_data_path)
nltk.download("punkt_tab", download_dir=nltk_data_path)
nltk.download("stopwords", download_dir=nltk_data_path)
