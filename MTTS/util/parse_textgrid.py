import textgrid

def parse_Interval(IntervalObject):
    start_time = ""
    end_time = ""
    P_name = ""

    ind = 0
    str_interval = str(IntervalObject)
    # print(str_interval)
    for ele in str_interval:
        if ele == "(":
            ind = 1
        if ele == " " and ind == 1:
            ind = 2
        if ele == "," and ind == 2:
            ind = 3
        if ele == " " and ind == 3:
            ind = 4

        if ind == 1:
            if ele != "(" and ele != ",":
                start_time = start_time + ele
        if ind == 2:
            end_time = end_time + ele
        if ind == 4:
            if ele != " " and ele != ")":
                P_name = P_name + ele

    st = float(start_time)
    et = float(end_time)
    pn = P_name

    return pn, et
    # return {pn: (st, et)}


def parse_textgrid(filename):
    tg = textgrid.TextGrid.fromFile(filename)
    list_words = tg.getList("words")
    words_list = list_words[0]

    w = ""
    e_time = ""
    for ele in words_list:
        pn, et = parse_Interval(ele)
        print(pn)
        if pn == "None":
            w += ","
        else:
            w += "," + pn
        e_time += "," + str(et)
    # w += e_time
    print(w[1:])
    print(e_time[1:])


if __name__ == "__main__":
    # d = parse_Interval('Interval(13.63000, 13.78000, ah0)')
    # print(d)
    # parse_textgrid("data/thchs30_250_demo/output/textgrid/mandarin_voice/A11_0.TextGrid")
    parse_textgrid("testdata/output/textgrid/mandarin_voice/38_5845_20170916163148.TextGrid")