import speech_recognition as sr
from gtts import gTTS
import os
import pygame
import datetime

# Atur threshold untuk mendeteksi suara masuk
recognizer = sr.Recognizer()

def record_audio():
    # Merekam audio dari mikrofon
    with sr.Microphone() as source:
        print("Mendengarkan...")
        audio = recognizer.listen(source)
        
    try:
        # Menggunakan Google Speech Recognition untuk mengenali teks
        text = recognizer.recognize_google(audio, language="id-ID")
        print("Anda: ", text)
        return text
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print("Maaf, terjadi kesalahan pada layanan pengenalan suara.")
    
    return ""

def speak(text):
    # Membuat objek gTTS dengan teks yang diberikan
    tts = gTTS(text=text, lang="id")

    # Simpan file audio sebagai "output.mp3"
    tts.save("output.mp3")

    # Putar file audio menggunakan pygame
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.quit()
    os.remove("output.mp3")

def get_greeting():
    current_hour = datetime.datetime.now().hour

    if 5 <= current_hour < 12:
        greeting = "Selamat pagi!"
    elif 12 <= current_hour < 18:
        greeting = "Selamat siang!"
    else:
        greeting = "Selamat sore!"
    
    return greeting

def translate_javanese_word(word):
    # Kamus Bahasa Jawa
    kamus = {
        "siji": "satu",
        "loro": "dua",
        "telu": "tiga",
        "papat": "empat",
        "limo": "lima",
        # Tambahkan kata-kata Bahasa Jawa dan terjemahannya lainnya di sini
    }

    translated_word = kamus.get(word.lower())
    return translated_word

def virtual_assistant():
    # Inisialisasi pygame
    pygame.init()

    greeting = get_greeting()
    speak(greeting)
    
    print("Virtual Assistant aktif...")
    
    while True:
        input_text = record_audio()
        if input_text:
            print("Diterima")

            if "halo" in input_text:
                response = "Halo, ada yang bisa saya bantu?"
                speak(response)

            elif "Siapa kamu" in input_text:
                response = "Nama saya Airi. Saya adalah kecerdasan buatan sebagai virtual asistant yang dibuat oleh Richal Fajril."
                speak(response)

            elif "Tolong terjemahkan" in input_text:
                response = "Baik, coba katakan suatu kata dalam Bahasa Jawa"
                speak(response)

            elif "terima kasih" in input_text:
                response = "Sama-sama. Terima kasih kembali, senang bisa membantu"
                speak(response)

            elif "keluar" in input_text:
                response = "Terima kasih. Senang bertemu denganmu, Sampai jumpa lagi!"
                speak(response)
                break

            else:
                translated_word = translate_javanese_word(input_text)
                if translated_word:
                    response = f"Arti dari '{input_text}' dalam Bahasa Jawa adalah '{translated_word}'"
                else:
                    response = f"Maaf, kata '{input_text}' tidak ditemukan dalam kamus"
                speak(response)

virtual_assistant()
