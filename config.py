# 天气模块
weather_slot_set = ["weather", "time", "location", "weather_action", "natural_phenomenon"]
weather_sys_request_slot = ["time", "location"]
weather_sys_inform_slot = ["weather", "weather_action", "natural_phenomenon"]
weather_action_set = ["打伞", "口罩", "感冒", "旅游", "紫外线指数", "洗车", "运动", "晾晒"]  # 在不添加注释的情况下，True值均指适宜进行某行为，易出现某现象
natural_phenomenon_set = ["下雨", "下雪", "有雾", "冰雹", "刮风", "沙尘暴", "干燥", "潮"]

# 时钟模块
clock_set = ['clock']

weather_kb = {
    "晴": {
        "weather_action": {
            "打伞": False,
            "口罩": False,
            "感冒": False,
            "旅游": True,
            "紫外线指数": True,  # Ture值指紫外线指数高，False值指紫外线指数低
            "洗车": True,
            "运动": True,
            "晾晒": True
        },
        "natural_phenomenon": {
            "下雨": False,
            "下雪": False,
            "有雾": False,
            "冰雹": False,
            "沙尘暴": False,
            "干燥": True,
            "潮": False,
            "刮风":False
        }
    },
    "阴": {
        "weather_action": {
            "打伞": False,
            "口罩": False,
            "感冒": False,
            "旅游": True,
            "紫外线指数": False,
            "洗车": True,
            "运动": True,
            "晾晒": False
        },
        "natural_phenomenon": {
            "下雨": False,
            "下雪": False,
            "有雾": False,
            "冰雹": False,
            "沙尘暴": False,
            "干燥": False,
            "潮": True,
            "刮风":False
        }
    },
    "雨": {
        "weather_action": {
            "打伞": True,
            "口罩": False,
            "感冒": True,
            "旅游": False,
            "紫外线指数": False,
            "洗车": False,
            "运动": False,
            "晾晒": False
        },
        "natural_phenomenon": {
            "下雨": True,
            "下雪": False,
            "有雾": False,
            "冰雹": False,
            "沙尘暴": False,
            "干燥": False,
            "潮": True,
            "刮风": False
        }
    },
    "冰雹": {
        "weather_action": {
            "打伞": True,
            "口罩": False,
            "感冒": False,
            "旅游": False,
            "紫外线指数": False,
            "洗车": False,
            "运动": False,
            "晾晒": False
        },
        "natural_phenomenon": {
            "下雨": False,
            "下雪": False,
            "有雾": False,
            "冰雹": True,
            "沙尘暴": False,
            "干燥": False,
            "潮": True,
            "刮风": False
        }
    },
    "雪": {
        "weather_action": {
            "打伞": False,
            "口罩": False,
            "感冒": True,
            "旅游": False,
            "紫外线指数": False,
            "洗车": False,
            "运动": False,
            "晾晒": False
        },
        "natural_phenomenon": {
            "下雨": False,
            "下雪": True,
            "有雾": False,
            "冰雹": False,
            "沙尘暴": False,
            "干燥": False,
            "潮": True,
            "刮风": False
        }
    },
    "沙尘暴": {
        "weather_action": {
            "打伞": False,
            "口罩": True,
            "感冒": False,
            "旅游": False,
            "紫外线指数": False,
            "洗车": False,
            "运动": False,
            "晾晒": False
        },
        "natural_phenomenon": {
            "下雨": False,
            "下雪": False,
            "有雾": False,
            "冰雹": False,
            "沙尘暴": True,
            "干燥": True,
            "潮": False,
            "刮风": True
        }
    },
    "雾霾": {
        "weather_action": {
            "打伞": False,
            "口罩": True,
            "感冒": False,
            "旅游": False,
            "紫外线指数": False,
            "洗车": False,
            "运动": False,
            "晾晒": False
        },
        "natural_phenomenon": {
            "下雨": False,
            "下雪": False,
            "有雾": True,
            "冰雹": False,
            "沙尘暴": False,
            "干燥": False,
            "潮": True,
            "刮风": False
        }
    },
    "大风": {
        "weather_action": {
            "打伞": False,
            "口罩": False,
            "感冒": True,
            "旅游": False,
            "紫外线指数": False,
            "洗车": False,
            "运动": False,
            "晾晒": True
        },
        "natural_phenomenon": {
            "下雨": False,
            "下雪": False,
            "有雾": True,
            "冰雹": False,
            "沙尘暴": False,
            "干燥": False,
            "潮": True,
            "刮风": True
        }
    },
}
weather_map = {'晴': set(['晴', '晴间多云', '热']), "阴": set(['多云', '大部多云', '阴']),
               "雨": set(['小雨', '中雨', '大雨', '暴雨', '大暴雨', '特大暴雨', '阵雨', '雷阵雨', '冻雨', '雨夹雪', '冷']),
               "冰雹": set(['雷阵雨伴有冰雹']), "雪": set(['阵雪', '小雪', '中雪', '大雪', '暴雪']),
               "沙尘暴": set(['浮尘', '扬沙', '沙尘暴', '强沙尘暴']), "雾霾": set(['雾', '霾']),
               "大风": set(['风', '大风', '飓风', '热带风暴', '龙卷风'])}

# 天气API参数
KEY = 'aiqwln0k57pigeay'  # API key
UID = "U7D56E6A69"  # 用户ID
LOCATION = 'beijing'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等
API_now = 'https://api.seniverse.com/v3/weather/now.json'  # API 获取实况天气
API_days = 'https://api.seniverse.com/v3/weather/daily.json'  # 获取未来三天的天气
API_life = 'https://api.seniverse.com/v3/life/suggestion.json'  # 获取生活指数
UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言

# 时间
TIME_NOW = 0
TOMORROW = 1
DAY_AFTER_TOMORROW = 2
