import numpy as np
"""
#音階の辞書
scale_name = ['C','C#','D','Eb','E','F','F#','G','G#','A','Bb','B']
scale_dic={}
for i in range(12):
    for n in range(11):
        scale_dic.setdefault(scale_name[i],[]).append(i+12*n)
"""
#音階の位置リスト
scale_list_mold = np.zeros((11,12))
for i in range(12):
    for n in range(11):
        scale_list_mold[n][i]=i+12*n

scale_list = scale_list_mold.T


#音階の位置を探索する関数
def return_scale_num(list_s,search_num):
    return_num = 0
    for i in range(12):
        for n in range(11):
            if list_s[i][n]==search_num:
                return_num = i
    return return_num

print(return_scale_num(scale_list,119))