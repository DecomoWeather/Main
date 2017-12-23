# Main

## 天气
```
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
```

#### NLU
`return format`
```python
# for "weather", "time", "location"
diaact = {"intent": "request+weather", "request_slot": {"weather": "UNK"}, "inform_slot": {"location": "北京"}}
diaact = {"intent": "inform+location", "request_slot": {}, "inform_slot": {"location": "北京"}}

# for "weather_action", "natural_phenomenon"
diaact = {"intent": "request+weather_action", "request_slot": {"weather_action": {"打伞": "UNK", "others": "UNK"}}}
```