from config import LOCATION, TIME_NOW, TOMORROW, DAY_AFTER_TOMORROW
class StateTracker():
    def __init__(self):
        self.state_w = {'intent': 'weather', 'diaact': 'request', 'request_slots': {'weather_action': {}},
                        'inform_slots': {'time': TIME_NOW, 'location': LOCATION}}
        self.state_c = {'intent': 'clock', 'diaact': 'request', 'request_slots': {'time':'UNK'},
                        'inform_slots': {'location': LOCATION}}
        self.current_state = {'intent': 'weather', 'diaact': 'request', 'request_slots': {'weather_action': {}},
                        'inform_slots': {'time': TIME_NOW, 'location': LOCATION}}
        self.history = []  # 存储每一句话的action
        self.turn_count = 0
        self.weather_slot_set = set(["weather", "weather_action", "natural_phenomenon"])
        self.clock_slot_set = set(['clock'])

    def update_history_state(self, user_action={}, sys_action={}):
        if user_action != {}:
            user_action['speaker'] = 'user'
            user_action['turn'] = self.turn_count
            self.history.append(user_action)
            intent = user_action['intent'].split('+')[0]
            slot = user_action['intent'].split('+')[1]
            if slot in self.weather_slot_set:
                self.state_w['request_slots'] = user_action['request_slots']
                self.state_w['inform_slots'].update(user_action['inform_slots'])
                self.current_state = self.state_w
            elif slot in self.clock_slot_set:
                self.state_c['request_slots'] = user_action['request_slots']
                self.state_c['inform_slots'].update(user_action['inform_slots'])
                self.current_state = self.state_c
            elif intent == 'inform':
                if self.current_state['intent'] == 'weather':
                    self.state_w['inform_slots'].update(user_action['inform_slots'])
                    self.current_state = self.state_w
                elif self.current_state['intent'] == 'clock':
                    self.state_c['inform_slots'].update(user_action['inform_slots'])
                    self.current_state = self.state_c
                else:
                    print('current state is false !!!')
            else:
                self.current_state['intent'] = 'other'
        elif sys_action != {}:
            sys_action['speaker'] = 'sys'
            sys_action['turn'] = self.turn_count
            self.history.append(sys_action)
        self.turn_count += 1

    def get_state(self):
        return self.current_state

# if __name__ == '__main__':
#     state_tracker = StateTracker()
#     user_action = {"intent": "request+weather", "request_slots": {"weather": "UNK"}, "inform_slots": {"location": "北京"}}
#     state_tracker.update_history_state(user_action=user_action)
#     state = state_tracker.get_state()
#     print(state)
#     user_action = {"intent": "inform+time", "request_slots": {}, "inform_slots": {"time": TOMORROW}}
#     state_tracker.update_history_state(user_action=user_action)
#     state = state_tracker.get_state()
#     print(state)
#     user_action = {"intent": "request+clock", "request_slots": {'clock': 'UNK'}, "inform_slots": {}}
#     state_tracker.update_history_state(user_action=user_action)
#     state = state_tracker.get_state()
#     print(state)
