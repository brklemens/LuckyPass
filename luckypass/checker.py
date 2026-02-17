import os
import zipfile

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
ROCKYOU_ZIP = os.path.join(DATA_DIR, 'rockyou.txt.zip')
ROCKYOU_PATH = os.path.join(DATA_DIR, 'rockyou.txt')

def ensure_rockyou_extracted():
    if not os.path.exists(ROCKYOU_PATH) and os.path.exists(ROCKYOU_ZIP):
        print("Extracting rockyou.txt... (one-time setup)")
        with zipfile.ZipFile(ROCKYOU_ZIP, 'r') as zip_ref:
            zip_ref.extractall(DATA_DIR)
        print("Done!")

def check_common_password(password):
    ensure_rockyou_extracted()

    try:
        with open(ROCKYOU_PATH, 'r', encoding='latin-1') as f:
            for line in f:
                if line.strip() == password:
                    return True
        return False
    except FileNotFoundError:
        return None

def analysis(password):

        length = len(password)

        unique_chars = len(set(password))

        has_special = any(not char.isalnum() for char in password)

        has_capital = any(char.isupper() for char in password)

        has_lower = any(char.islower() for char in password)

        in_rockyou = check_common_password(password)

        return {
                'length': length,
                'unique_characters': unique_chars,
                'special_character': has_special,
                'capital_character': has_capital,
                'lower_character': has_lower,
                'in_common_list': in_rockyou
        }