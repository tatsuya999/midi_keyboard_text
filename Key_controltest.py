import numpy as np
import pyautogui
import rtmidi2
import Key_module as m_key

midi_in = rtmidi2.MidiIn()
print(midi_in.ports)

#device_name = "microKEY-25"
device_name = "KOMPLETE KONTROL A49"
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
#全パターン用リスト
pattern = []
#単語予測結果リスト
pre_word = []
try:
    while True:        
        message = midi_in.get_message()
        #message[状態(押した144/離した128), 押したキーの場所, 押した強さ]
        #message[1]== 0->C,1->C#,.....11->B,13->C
        if message:
            if message[0]==144:
                key_num = m_key.Return_Scale_Num2(scale_list,message[1])
                key_press = m_key.Key_Schange(key_num)
                pattern += m_key.Cartesian_list(pattern,key_press)
                for i in pattern:
                    pre_word += m_key.Text_Enchant(i)
                #pyautogui.keyDown(key_press)
                print(pre_word)
                pre_word = []
            elif message[0]==128:
                key_num = m_key.Return_Scale_Num2(scale_list,message[1])
                key_press = m_key.Key_Schange(key_num)
                #pyautogui.keyUp(key_press)
except KeyboardInterrupt:
    print('\nmidi入力終了')
