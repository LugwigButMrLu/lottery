import json
import os
from pathlib import Path

from qfluentwidgets import QConfig, ConfigItem, OptionsValidator, OptionsConfigItem, BoolValidator, FolderValidator


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class GlobalValue:
    def __init__(self):
        self.font_color = ["black", "black", "black", "black"]
        self.awards_name_list = ["友情奖", "三等奖", "二等奖", "一等奖"]
        self.prize_name_list = ["万事利日用礼盒", "奥迪车模型", "万事利蚕丝被", "海蓝宝 裸石 1颗"]
        self.prize_name_list_2 = ["价值 298元", "价值 458元", "价值 600元", "价值 2000元"]
        self.prize_pic_list = ["./p4.jpg", "./p3.jpg", "./p2.jpg", "./p1.jpg"]
        self.background_pic_list = ["./b4.jpg", "./b3.jpg", "./b2.jpg", "./b1.jpg"]
        self.path = ""
        self.start_number = 1
        self.end_number = 111

    def get_all(self):
        for k, v in self.__dict__.items():
            print(f"{k}:{v}")

    def filtered_dict(self, exclude_keys=None):
        if exclude_keys is None:
            exclude_keys = []
        return {k: v for k, v in self.__dict__.items() if k not in exclude_keys}

    def save_to_file(self, filename):
        """
        将所有属性存储为json文件
        """
        with open(filename, 'w') as f:
            r = self.filtered_dict([self.path])
            json.dump(self.filtered_dict(['path']), f, ensure_ascii=False, indent=4)

    def import_from_file(self, filename):
        """
        从json文件中解析文件，并修改GlobalValue的各个属性
        """
        with open(filename, 'r') as f:
            data = json.load(f)
            self.__dict__.update(data)

    def init(self):
        if os.path.isfile(Path(self.path) / "config.txt"):
            self.import_from_file(Path(self.path) / "config.txt")
        else:
            pass


gv = GlobalValue()
