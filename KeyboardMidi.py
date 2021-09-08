import rtmidi2
import pyautogui
import numpy as np

#特殊キーボードの操作リスト
key_action = ['space','enter','return','backspace','esc','command','shift','ctrl']
#キーボードの文字リスト
key_text = [['q','a','z'],['w','s','x'],['e','d','c'],['r','f','v','t','g','b'],['y','h','n','u','j','m'],['i','k',','],['o','l','.'],['p',';','/']]
#音階の名前リスト
scale_name = ['c','c#','d','eb','d','f','f#','g','g#','a','a#','b']
#音階の位置リスト
scale_list_mold = np.zeros((11,12))
for i in range(12):
    for n in range(11):
        scale_list_mold[n][i]=i+12*n
scale_list = scale_list_mold.T

#音階の位置を探索する関数(リスト,音階位置を引数)ドレミファを返す
def return_scale_num(list_s,search_num):
    return_num = 0
    for i in range(12):
        for n in range(11):
            if list_s[i][n]==search_num:
                return_num = i
    return return_num

midi_in = rtmidi2.MidiIn()
print(midi_in.ports)

device_name = "microKEY-25"
#device_name = "KOMPLETE KONTROL A49"
# midiがデバイスで検知されているかどうかのエラー処理
try:
    index = midi_in.ports_matching(device_name+"*")[0]
    input_port = midi_in.open_port(index)
except IndexError:
    raise(IOError("Input port not found."))

try:
    while True:
        message = input_port.get_message()
        #message[状態(押した144/離した128), 押したキーの場所, 押した強さ]
        #message[1]== 0->C,1->C#,.....11->B,13->C
        if message:
            if message[0]==144:
                key_num = return_scale_num(scale_list,message[1])
                key_press = scale_name[key_num]
                pyautogui.keyDown(key_press)
            elif message[0]==128:
                key_num = return_scale_num(scale_list,message[1])
                key_press = scale_name[key_num]
                pyautogui.keyUp(key_press)
except KeyboardInterrupt:
    print('\nmidi入力終了')