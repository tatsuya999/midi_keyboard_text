#音階の位置を探索する関数(リスト,音階位置を引数)ドレミファを返す
import random
def return_scale_num(list_s,search_num):
    return_num = 0
    for i in range(12):
        for n in range(11):
            if list_s[i][n]==search_num:
                return_num = i
    return return_num

#スケールから指配置を指定する関数
def key_schange(scale_name,key_text):
    if scale_name == 'C':
        return random.choice(key_text[0])
    if scale_name == 'D':
        return random.choice(key_text[1])
    if scale_name == 'E':
        return random.choice(key_text[2])
    if scale_name == 'F':
        return random.choice(key_text[3])
    if scale_name == 'F2':
        return random.choice(key_text[4])
    if scale_name == 'G2':
        return random.choice(key_text[5])
    if scale_name == 'A2':
        return random.choice(key_text[6])
    if scale_name == 'B2':
        return random.choice(key_text[7])
    else:
        print('ポジションが違う')
