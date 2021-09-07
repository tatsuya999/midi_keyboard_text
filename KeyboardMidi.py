import rtmidi2
import pyautogui

midi_in = rtmidi2.MidiIn()
print(midi_in.ports)

device_name = "microKEY-25"
# midiがデバイスで検知されているかどうかのエラー処理
try:
    index = midi_in.ports_matching(device_name+"*")[0]
    input_port = midi_in.open_port(index)
except IndexError:
    raise(IOError("Input port not found."))

while True:
    # [状態(押した/離した), 押したキーの場所, 押した強さ]
    message = input_port.get_message()
    if message:
        if message[0]==144:
            pyautogui.press('a')
#音階の辞書
scale = ['C','C#','D','Eb','E','F','F#','G','G#','A','Bb','B']
scale_dic = {}
for i in range(12):
    for n in range(11):
        scale_dic.setdefault(scale[i],[]).append(i+12*n)
    
def get_key()