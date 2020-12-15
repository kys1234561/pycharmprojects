def check_length(dict):
    for key in dict:
        if len(dict[key]) > 2:
            dict[key] = dict[key][0:2]
        else:
            continue
    print(dict)
check_length({'k1':'34','k5':'67','h6':[676,'gfd','sdfs']})