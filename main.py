from gtts import  gTTS
from pathlib import Path
from art import tprint
import pdfplumber


def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[+] Original file: {Path(file_path).name}')
        print(f'[+] Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            text = ''.join(pages)
            text = text.replace('\n', '')

            my_audio = gTTS(text=text, lang=language)
            file_name = Path(file_path).stem
            my_audio.save(f'{file_name}.mp3')
            return f'[+] {file_name}.mp3 saved successfully!'
    else:
        return 'File does not exist, check the file path!'


def main():
    tprint('PDF to MP3')
    file_path = input('\n Enter file\'s path: ')
    lang = input('\n Choose the language, for example "en" or "ru": ')
    print(pdf_to_mp3(file_path, lang))


if __name__ == '__main__':
    main()