# 天气模块
weather_slot_set = ["weather", "time", "location", "weather_action", "natural_phenomenon"]
weather_sys_request_slot = ["time", "location"]
weather_sys_inform_slot = ["weather", "weather_action", "natural_phenomenon"]
weather_action_set = ["打伞","口罩","感冒","旅游","紫外线指数","洗车","运动","晾晒"]  #在不添加注释的情况下，True值均指适宜进行某行为，易出现某现象
natural_phenomenon_set = ["下雨","下雪","有雾","冰雹","刮风","沙尘暴","干燥","潮"]

weather_kb = {
    "晴": {
        "weather_action": {
            "打伞": False,
            "口罩": False,
            "感冒": False,
            "旅游": True,
            "紫外线指数": True,#Ture值指紫外线指数高，False值指紫外线指数低
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
            "刮风":False
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
            "刮风":False
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
            "刮风":False
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
            "刮风":True
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
            "刮风":False
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
            "刮风":True
        }
    },
}

