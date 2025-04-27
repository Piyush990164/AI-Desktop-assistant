import webbrowser
import os


def open_facebook():

    url = "https://www.facebook.com"
    webbrowser.open(url)

def open_google():
    url = "https://www.google.com"
    webbrowser.open(url)    

def open_youtube():
    url = "https://www.youtube.com"
    webbrowser.open(url)

def open_instagram():
    url = "https://www.instagram.com"
    webbrowser.open(url)

def open_linkedin():
    url = "https://www.linkedin.com"
    webbrowser.open(url)

def open_discord():
    url = "https://www.discord.com"
    webbrowser.open(url)

def open_google_drive():
    url = "https://drive.google.com"
    webbrowser.open(url)


def close_browser():
    browsers = ["chrome.exe", "msedge.exe", "firefox.exe", "brave.exe", "opera.exe"]
    for browser in browsers:
        os.system(f"taskkill /im {browser} /f")
    print("All browsers closed.")
