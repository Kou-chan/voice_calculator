import recognition as r
import subprocess as sps
import MorphologicalAnalysis as ma

#softalkのpathの設定
path_voice = "C:/free_tool/softalk/SofTalk.exe"

if __name__ == "__main__":
    text = r.rec()
    text = str(ma.changevoice(text))
    sps.call("start " + path_voice + " /X1: /W:" + text, shell=True)