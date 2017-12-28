# Created by Helic on 2017/7/21
import json

class NLG:

    def __init__(self):
        # 读取dataset
        with open('nlg_template.json', encoding='utf-8') as f:
            value = json.load(f)
            self.request = value['request']  # list
            self.inform = value['inform']
        self.weather_inform = set(['date', 'text_day', 'text_night', 'high', 'low', 'wind_direction', 'wind_scale'])

    def get_sentence(self, diaact):
        request_slots = []
        inform_slots = []
        s = ''
        for i in diaact['request_slots']:
            request_slots.append(i)
        for i in diaact['inform_slots']:
            inform_slots.append(i)
        if diaact["diaact"] == 'inform':
            if 'weather' in inform_slots:
                s += self.inform['weather']
                for i in self.weather_inform:
                    r1 = '$'+str(i)+'$'
                    s = s.replace(r1, diaact['inform_slots']['weather'][i])
                    # print(s)
            if 'weather_action' in inform_slots:
                for slot in diaact['inform_slots']['weather_action'].keys():
                    r2 = str(slot)+'-'+str(diaact['inform_slots']['weather_action'][slot])
                    s += self.inform['weather_action'][r2]
                    # print(s)
            if 'natural_phenomenon' in inform_slots:
                for slot in diaact['inform_slots']['natural_phenomenon'].keys():
                    r3 = str(slot)+'-'+str(diaact['inform_slots']['natural_phenomenon'][slot])
                    s += self.inform['natural_phenomenon'][r3]
                    # print(s)
            if 'clock' in inform_slots:
                return diaact['inform_slots']['clock']
            return s
        else:
            print('NLG模板缺失')
            return diaact

# sys_action = {'diaact': 'inform',
#            'request_slots': {},
#            'inform_slots': {
#                             'location': 'beijing',
#                             'time': 1,
#                             'weather_action': {'打伞': '需要'},
#                             'weather': {
#                                         'wind_scale': '2',
#                                         'precip': '',
#                                         'date': '2017-12-28',
#                                         'wind_direction': '无持续风向',
#                                         'text_night': '晴',
#                                         'low': '-5',
#                                         'wind_direction_degree': '',
#                                         'code_day': '0',
#                                         'text_day': '晴',
#                                         'high': '5',
#                                         'code_night': '1',
#                                         'wind_speed': '10'},
#                             'weather_action': {
#                                         '打伞': False,
#                                         '洗车': True},
#                             'natural_phenomenon': {
#                                         '下雨': False}}}
# nlg = NLG()
# s = nlg.get_sentence(sys_action)
# print(s)
