import jieba
import config
import json
import jieba.posseg as pseg


class NLU:
    def __init__(self, semantic="semantic.json", dic="dic.txt"):
        """构造函数"""
        self.slot_set = config.weather_slot_set
        self.sys_request_slot = config.weather_sys_request_slot
        self.sys_inform_slot = config.weather_sys_inform_slot
        self.weather_action_set = config.weather_action_set
        self.natural_phenomenon_set = config.natural_phenomenon_set
        self.stopwords = ['，', '。', '？', '“', '”', '‘', '’', '；', '：', '！', '、', '（', '）', '-', '=',
                          '【', '】', ' ', '{', '}', ',', '.', '/', '\\', '(', ')', '?', '!', ';', ':', '\'',
                          '"', '[', ']', '~', '\n', '\t']
        with open(semantic, 'r', encoding="utf-8") as f:
            self.value = json.load(f)
            # jieba.load_userdict(dic)

    def participle(self, raw_sentence):
        """对原始语句分词，去标点，返回两个列表，第一个为分词结果，第二个为词性列表"""
        m, n = [], []
        for i, j in pseg.lcut(raw_sentence):  # 去标点
            if i not in self.stopwords:
                m.append(i)
                n.append(j)
        return m, n

    def get_iob(self, m, n):
        """Input:
                m为分词后的列表,n为词性列表
           Output:
                return iob list, ['B-time', 'B-location', 'O', 'B-weather', 'O']"""
        iob = []
        i = 0
        while i < len(m):
            if n[i] == 'ns':
                iob.append('B-location')
            else:
                if m[i] in self.value['weather']:
                    iob.append('B-weather')
                elif m[i] in self.value['time']:
                    iob.append('B-time')
                elif m[i] in self.value['location']:
                    iob.append('B-location')
                else:
                    for j in self.value["weather_action"]:
                        if m[i] in self.value["weather_action"][j]:
                            iob.append("B-{}".format(j))
                            continue
                    for j in self.value["natural_phenomenon"]:
                        if m[i] in self.value["natural_phenomenon"][j]:
                            iob.append("B-{}".format(j))
                            continue
                    iob.append("O")
            i += 1
        return iob

    def iob_to_diaact(self, iob, string):
        """将iob转化为diaact,string是一个分词后列表"""
        diaact = {"intent": "", "request_slot": {}, "inform_slot": {}}
        for index, value in enumerate(iob):
            if value == "O":
                continue
            else:
                slot = value.split('-')[1]
                if slot in self.sys_request_slot:
                    diaact["inform_slot"][slot] = string[index]
                else:
                    if slot == "weather":
                        diaact["request_slot"][slot] = 'UNK'
                    elif slot in self.weather_action_set:
                        diaact["request_slot"]["weather_action"][slot] = 'UNK'
                    elif slot in self.natural_phenomenon_set:
                        diaact["request_slot"]["natural_phenomenon"][slot] = 'UNK'
                    else:
                        pass

        if diaact["request_slot"]:
            diaact["intent"] = "request"
            for i in diaact["request_slot"]:
                 diaact["intent"] += "+{}".format(i)
        else:
            diaact["intent"] = "inform"
            for i in diaact["inform_slot"]:
                diaact["intent"] += "+{}".format(i)
        return diaact

    def get_diaact(self, raw_sentence):
        m, n = self.participle(raw_sentence)
        iob = self.get_iob(m, n)
        diaact = self.iob_to_diaact(iob, m)
        return diaact

# for test
# nlu = NLU()
# s = "今天北京的天气怎么样？"
# m, n = nlu.participle(s)
# print(m, n)
# iob = nlu.get_iob(m, n)
# print(iob)
# print(nlu.get_diaact(s))
