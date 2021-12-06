import numpy as np
import pyautogui
import rtmidi2
import Key_module as m_key

def Clear():
    pattern.clear()
    pre_word.clear()
    key_count = 0
    
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
#全パターン用リスト
pattern = []
#単語予測結果リスト,表示リスト
pre_word = []
display_list = []
#文リスト
sen_list = []
#キーボード打鍵リスト
key_message = []
#選択用リスト
select_list = []
#キーボード押した回数
key_count = 0
select = 0
try:
    while True:        
        message = midi_in.get_message()
        #message[状態(押した144/離した128), 押したキーの場所, 押した強さ]
        #message[1]== 0->C,1->C#,.....11->B,13->C
        if message:   
            if message[0]==144:
                if len(key_message) < 2:
                    key_count+=1
                    key_num = m_key.Return_Scale_Num2(scale_list,message[1])
                    key_press = m_key.Key_Schange(key_num)
                    if key_num == 22:
                        pattern.clear()
                        pre_word.clear()
                        key_count = 0
                        print("clear")
                    else:
                        pattern += m_key.Cartesian_list(pattern,key_press)
                        for i in pattern:
                            if len(i) == key_count:
                                pre_word += m_key.Text_Enchant(i)
                                display_list += m_key.Text_Enchant(i)
                        key_message.append(message[1])
                        print(display_list)
                        display_list = []
                if len(key_message) >= 2:
                    for i in pre_word:
                        if len(i) == key_count-len(key_message):
                            select_list.append(i)
                    select += m_key.Roll_CandG(sum(key_message))
                    print('\033[31m'+select_list[select]+'\033[0m')
                    if sum(key_message) == 9+14:
                        sen_list.append(select_list[select])       
                    print(sen_list)
                    key_count = 0
                #pyautogui.keyDown(key_press)
            if message[0]==128:
                if key_message:
                    key_message.pop()
                    #pyautogui.keyUp(key_press)
except KeyboardInterrupt:
    print('\nmidi入力終了')
