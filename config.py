# 天气模块
weather_slot_set = ["weather", "time", "location", "weather_action", "natural_phenomenon"]
weather_sys_request_slot = ["time", "location"]
weather_sys_inform_slot = ["weather", "weather_action", "natural_phenomenon"]
weather_action_set = ["打伞"]
natural_phenomenon_set = ["下雨"]

weather_kb = {
    "晴天": {
        "weather_action": {
            "打伞": True,
            "other actions": "values"  # 与weather_action_set对应
        },
        "natural_phenomenon": {
            "下雨": False,
            "others": "values"   # 与natural_phenomenon_set对应
        }
    },
    "雨天": {
        "weather_action": {
            "打伞": True,
            "other actions": "values"
        },
        "natural_phenomenon": {
            "下雨": True,
            "others": "values"
        }
    },
}
