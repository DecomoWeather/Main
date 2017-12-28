import time

class DM_CLOCK():
    def __init__(self):
        pass
    def response(self, state):
        if 'clock' in state['request_slots']:
            clock = time.strftime('%H:%M:%S', time.localtime(time.time()))
            sys_action = {'request_slots': {}, 'inform_slots': {'clock': clock}, 'diaact': 'inform'}
        return sys_action