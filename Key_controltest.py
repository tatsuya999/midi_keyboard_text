import numpy as np
import rtmidi2
import datetime
"""
midi_in = rtmidi2.MidiIn()
print(midi_in.ports)

device_name = "microKEY-25"
try:
    index = midi_in.ports_matching(device_name+"*")[0]
    input_port = midi_in.open_port(index)
except IndexError:
    raise(IOError("Input port not found."))

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


"""
#音階の辞書
scale_name = ['C','C#','D','Eb','E','F','F#','G','G#','A','Bb','B','C2','C2#','D2','E2b','E2','F2','F2#','G2','G2#','A2','B2b','B2']
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
