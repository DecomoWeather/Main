from nlu import NLU
from DialogManager_weather import DM_WEATHER
from DialogManager_clock import DM_CLOCK
from Global_State_Tracker import StateTracker
from nlg import NLG

class Weather_or_Clock():
    def __init__(self):
        # 初始化
        self.nlu = NLU()
        self.nlg = NLG()
        self.dm_w = DM_WEATHER()
        self.dm_c = DM_CLOCK()
        self.global_state_tracker = StateTracker()
        self.episode_over = False

    def response(self, user_sentence):
        # 对话过程
        if self.episode_over == False:
            user_action = self.nlu.get_diaact(user_sentence)  # user_action = {'diaact':'request+weather_action', 'request_slots':{ 'weather_action':['打伞', '洗车']}, 'inform_slots':{}, 'intent':'weather\clock\other'}
                                                # 只有时间和地点的可以分类放在other里，比如‘明天呢’
            print('user_action:', user_action)
            self.global_state_tracker.update_history_state(user_action=user_action)
            user_state = self.global_state_tracker.get_state()
            print('user_state:', user_state)
            if user_state['intent'] == 'weather':
                sys_action = self.dm_w.response(user_state)
            elif user_state['intent'] == 'clock':
                sys_action = self.dm_c.response(user_state)
            else:
                sys_action = self.other_response(raw_sentence)
            self.global_state_tracker.update_history_state(sys_action=sys_action)
            print('sys_action:', sys_action)
            sys_nl = self.nlg.get_sentence(sys_action)
        return sys_nl
            # 对话结束的判断

if __name__ == '__main__':
    weather_clock = Weather_or_Clock()
    raw_sentence = '今天需要带伞么？适合洗车么？有雨么？'
    print(weather_clock.response(raw_sentence))   # 比较适合洗车。不需要带伞。没有雨。
    raw_sentence = '明天呢？'
    print(weather_clock.response(raw_sentence))  # 不需要带伞。比较适合洗车。没有雨。
    raw_sentence = '下雪吗？'
    print(weather_clock.response(raw_sentence))
    raw_sentence = '今天有雪吗？'  # 不会下雪
    print(weather_clock.response(raw_sentence))
    raw_sentence = '现在几点了？'
    print(weather_clock.response(raw_sentence))