import speech_recognition as sr
import subprocess as sps
import time

#softalkのpathの設定
path_voice = "C:/free_tool/softalk/SofTalk.exe"

def rec():
    re = sr.Recognizer()
    with sr.Microphone() as source:
        re.adjust_for_ambient_noise(source)
        sps.call("start " + path_voice + " /X1: /W:計算したい式を言ってください", shell=True)
        time.sleep(2)
        print("録音開始")
        audio = re.listen(source)
        print("録音終了")

    try:
        text = re.recognize_google(audio, language='ja-JP')
    except:
        print('error')
        text = '音声入力に失敗しました'
    return text
