scale = ['C','C#','D','Eb','E','F','F#','G','G#','A','Bb','B']
scale_dic = {}
for i in range(12):
    for n in range(11):
        scale_dic.setdefault(scale[i],[]).append(i+12*n)
    

print(scale_dic)