import jieba
import config
import json


class NLU:
    def __init__(self, semantic="semantic.json"):
        """构造函数"""
        self.slot_set = config.weather_slot_set
        self.sys_request_slot = config.weather_sys_request_slot
        self.sys_inform_slot = config.weather_sys_inform_slot
        with open(semantic, 'r', encoding="utf-8") as f:
            self.value = json.load(f)
