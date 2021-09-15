import numpy as np
import pyautogui
import rtmidi2
import Key_module as m_key
#キーボードの文字リスト
key_text = [['q','a','z'],['w','s','x'],['e','d','c'],['r','f','v','t','g','b'],['y','h','n','u','j','m'],['i','k'],['o','l'],['p']]
scale_name = ['C','C#','D','Eb','E','F','F#','G','G#','A','Bb','B','C2','C2#','D2','E2b','E2','F2','F2#','G2','G2#','A2','B2b','B2']
midi_in = rtmidi2.MidiIn()
print(midi_in.ports)

device_name = "microKEY-25"
#device_name = "KOMPLETE KONTROL A49"
try:
    index = midi_in.ports_matching(device_name+"*")[0]
    input_port = midi_in.open_port(index)
except IndexError:
    raise(IOError("Input port not found."))

#音階の位置リスト
scale_list_mold = np.zeros((6,24))
for i in range(24):
    for n in range(6):
        scale_list_mold[n][i]=i+24*n

scale_list = scale_list_mold.T

try:
    while True:
        message = input_port.get_message()
        #message[状態(押した144/離した128), 押したキーの場所, 押した強さ]
        #message[1]== 0->C,1->C#,.....11->B,13->C
        if message:
            if message[0]==144:
                key_num = m_key.return_scale_num(scale_list,message[1])
                key_press = m_key.key_schange(scale_name[key_num],key_text)
                pyautogui.keyDown(key_press)
            elif message[0]==128:
                key_num = m_key.return_scale_num(scale_list,message[1])
                key_press = m_key.key_schange(scale_name[key_num],key_text)
                pyautogui.keyUp(key_press)
except KeyboardInterrupt:
    print('\nmidi入力終了')
"""
message_list = []
message_con_list = []
chord_list = [0]
list_number = 0
try:
    while True:
        message = input_port.get_message()
        if message:
            print(message)
except KeyboardInterrupt:
    print('\nmidi入力終了')


#音階の辞書

scale_dic={}
for i in range(24):
    for n in range(6):
        scale_dic.setdefault(scale_name[i],[]).append(i+24*n)
print(scale_dic)
#音階の位置リスト
scale_list_mold = np.zeros((6,24))
for i in range(24):
    for n in range(6):
        scale_list_mold[n][i]=i+24*n

scale_list = scale_list_mold.T


#音階の位置を探索する関数
def return_scale_num(list_s,search_num):
    return_num = 0
    for i in range(24):
        for n in range(6):
            if list_s[i][n]==search_num:
                return_num = i
    return return_num
print(scale_list)
print(return_scale_num(scale_list,32))
"""