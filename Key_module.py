#音階の位置を探索する関数(リスト,音階位置を引数)ドレミファを返す
import random
import itertools
def return_scale_num(list_s,search_num):
    return_num = 0
    for i in range(12):
        for n in range(11):
            if list_s[i][n]==search_num:
                return_num = i
    return return_num
#2オクターブ用
def return_scale_num2(list_s,search_num):
    return_num = 0
    for i in range(24):
        for n in range(6):
            if list_s[i][n]==search_num:
                return_num = i
    return return_num

#スケールから指配置を指定する関数
def key_schange(key_num):
    key_text = [['q','a','z'],['w','s','x'],['e','d','c'],['r','f','v','t','g','b'],['y','h','n','u','j','m'],['i','k'],['o','l'],['p'],['']]
    scale_name = ['C','C#','D','Eb','E','F','F#','G','G#','A','Bb','B','C2','C2#','D2','E2b','E2','F2','F2#','G2','G2#','A2','B2b','B2']
    scale_press = scale_name[key_num]
    if scale_press == 'C':
        return key_text[0]
    if scale_press == 'D':
        return key_text[1]
    if scale_press == 'E':
        return key_text[2]
    if scale_press == 'F':
        return key_text[3]
    if scale_press == 'F2':
        return key_text[4]
    if scale_press == 'G2':
        return key_text[5]
    if scale_press == 'A2':
        return key_text[6]
    if scale_press == 'B2':
        return key_text[7]
    else:
        return key_text[8]
        print('ポジションが違う')

#リストの直積（全通り組み合わせ）
def Cartesian_list(product,add):
    p = []
    if product == []:
        for i in add:
            p.append(i)
    else:
        p = itertools.product(product,add)
    return p
#def suggestion(all_list):