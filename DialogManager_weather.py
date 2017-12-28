import json, requests
from config import weather_kb, weather_map, KEY, LANGUAGE, UNIT, API_now, API_days, API_life


class DM_WEATHER:
    def __init__(self):
        pass

    def fetchWeather(self, location, time):
        result = requests.get(API_days, params={
            'key': KEY,
            'location': location,
            'language': LANGUAGE,
            'unit': UNIT,
            'start': 0,
            'days': 3
        }, timeout=1)
        return result.text

    def lookup(self, weather_action=None, natural_phenomenon=None, weather=''):
        result = {'weather_action':{}, 'natural_phenomenon':{}}
        if weather_action == None and natural_phenomenon == None:
            print('不能查询空值！')
        if weather == '':
            print('查询天气为空！')
        if weather_action != None:  # 'weather_action': {'打伞': 'UNK', '洗车': 'UNK'}
            for slot in weather_action.keys():
                result['weather_action'][slot] = weather_kb[weather]['weather_action'][slot]
        else:
            del result['weather_action']
        if natural_phenomenon != None:
            for slot in natural_phenomenon.keys():
                result['natural_phenomenon'][slot] = weather_kb[weather]['natural_phenomenon'][slot]
        else:
            del result['natural_phenomenon']
        return result

    def weather_map(self, text):
        for i in weather_map.keys():
            if text in weather_map[i]:
                return i

    def response(self, state):
        sys_action = {'diaact': 'inform', 'inform_slots': {}, 'request_slots':{}}
        code_day = state['inform_slots']['time']
        location = state['inform_slots']['location']
        weather_action = None
        natural_phenomenon = None
        if 'weather_action' in state['request_slots'].keys():
            weather_action = state['request_slots']['weather_action']
        if 'natural_phenomenon' in state['request_slots'].keys():
            natural_phenomenon = state['request_slots']['natural_phenomenon']
        result = self.fetchWeather(location, code_day)
        re = json.loads(result)
        weather_reault = re['results'][0]['daily'][code_day]
        weather = self.weather_map(weather_reault['text_day'])
        if weather_action != None or natural_phenomenon != None:
            lookup_result = self.lookup(weather_action=weather_action, natural_phenomenon=natural_phenomenon, weather=weather)
            sys_action['inform_slots'].update(lookup_result)
        return sys_action

# if __name__ == '__main__':
    # dd = {'inform_slots': {'location': 'beijing', 'time': 0}, 'intent': 'weather', 'diaact': 'request', 'request_slots': {'weather_action': {'打伞': 'UNK', '洗车': 'UNK'}}}
    # dmw = DM_WEATHER()
    # ne = dmw.response(dd)
    # print(ne)

    # test weather_map
    # dm = DM_WEATHER()
    # text = '晴间多云'
    # print(dm.weather_map(text))