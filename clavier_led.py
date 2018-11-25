# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 08:02:05 2018

@author: timothy
"""
from logipy import logi_led
import time
import ctypes
import math
import random

class clavier_led():
    def __init(self):
        self.dic_keys = {"a":30, "b":48, "c":46, "d":32, "e":18, "f":33, "g":34, "h":35, "i":23, "j":36, "k":37, "l":38, "m":50,
            "n":49, "o":24, "p":25, "q":16, "r":19, "s":31, "t":20, "u":22, "v":47, "w":17, "x":45, "y":21, "z":44,
            "0":11, "1":2, "2":3, "3":4, "4":5, "5":6, "6":7, "7":8, "8":9, "9":10,
            ",":51, ".":52, ";":39, "/":53, " ":57, "'":40, "`":41, "-":12, "=":13, "backsp":14, "ins":338, "home":327, "paup":329,
            "numlo":69, "n/":309, "n*":55, "n-":74, "n+":78, "nenter":284, "ndel":83, "n0":82, "n1":79, "n2":80, "n3":81, "n4":75, "n5":76, "n6":77, "n7":71, "n8":72, "n9":73,
            "capslo":58, "backsla":43, "shiftr":54, "shiftl":42, "ctrlr":285, "ctrll":29, "winr":348, "winl":347, "alt":56, "altgr":312, "text":349, "arrup":328, "arrdo":336, "arrl":331, "arrr":333,
            "tab":15, "[":26, "]":27, "enter":28, "delete":339, "end":335, "padown":337,
            "g1":65521, "g2":65522, "g3":65523, "g4":65524, "g5":65525, "g6":65526, "g7":65527, "g8":65528, "g9":65529,
            "esc":1, "priscr":311, "scrlo":70, "pau":325,
            "f1":59, "f2":60, "f3":61, "f4":62, "f5":63, "f6":64, "f7":65, "f8":66, "f9":67, "f10":68, "f11":87, "f12":88}
        self.all_keys_array = [["+",  "+",      "+",      "g6",  "g7",  "g8", "g9", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
                  ["+",  "esc",    "+",      "f1",  "f2",  "f3", "f4", "f5", "f6", "f7", "f8", "+", "f9", "f10", "f11", "f12", "priscr", "scrlo", "pau", "+", "+", "+", "+"],
                  ["g1", "`",      "1",      "2",   "3",   "4", "5", "6", "7", "8", "9", "0", "-", "=", "backsp", "ins", "home", "paup", "numlo", "n/", "n*", "n-"],
                  ["g2", "tab",    "q",      "w",   "e",   "r", "t", "y", "u", "i", "o", "p", "[", "]", "enter", "delete", "end", "padown", "n7", "n8", "n9", "n+"],
                  ["g3", "capslo", "a",      "s",   "d",   "f", "g", "h", "j", "k", "l", ";", "'", "backsla", "enter", "+", "+", "+", "n4", "n5", "n6", "n+"],
                  ["g4", "shiftl", "+", "z",   "x",   "c", "v", "b", "n", "m", ",", ".", "/", "+", "shiftr", "+", "arrup", "+", "n1", "n2", "n3", "nenter"],
                  ["g5", "ctrll",  "winl",   "+", "alt", "+", "+", " ", "+", "+", "+", "altgr", "winr", "text", "ctrlr", "arrl", "arrdo", "arrr", "n0", "n0", "ndel", "nenter"]]
        
    def health_bar(self, lives, delay_time=1/200, color_life=[0, 100, 0], color_dead=[100, 0, 0], life_keys=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
        """give it the number of lives and it displays it"""
        dic_keys = {"a":30, "b":48, "c":46, "d":32, "e":18, "f":33, "g":34, "h":35, "i":23, "j":36, "k":37, "l":38, "m":50,
            "n":49, "o":24, "p":25, "q":16, "r":19, "s":31, "t":20, "u":22, "v":47, "w":17, "x":45, "y":21, "z":44,
            "0":11, "1":2, "2":3, "3":4, "4":5, "5":6, "6":7, "7":8, "8":9, "9":10,
            ",":51, ".":52, ";":39, "/":53, " ":57, "'":40, "`":41, "-":12, "=":13, "backsp":14, "ins":338, "home":327, "paup":329,
            "numlo":69, "n/":309, "n*":55, "n-":74, "n+":78, "nenter":284, "ndel":83, "n0":82, "n1":79, "n2":80, "n3":81, "n4":75, "n5":76, "n6":77, "n7":71, "n8":72, "n9":73,
            "capslo":58, "backsla":43, "shiftr":54, "shiftl":42, "ctrlr":285, "ctrll":29, "winr":348, "winl":347, "alt":56, "altgr":312, "text":349, "arrup":328, "arrdo":336, "arrl":331, "arrr":333,
            "tab":15, "[":26, "]":27, "enter":28, "delete":339, "end":335, "padown":337,
            "g1":65521, "g2":65522, "g3":65523, "g4":65524, "g5":65525, "g6":65526, "g7":65527, "g8":65528, "g9":65529,
            "esc":1, "priscr":311, "scrlo":70, "pau":325,
            "f1":59, "f2":60, "f3":61, "f4":62, "f5":63, "f6":64, "f7":65, "f8":66, "f9":67, "f10":68, "f11":87, "f12":88}
        logi_led.logi_led_init()
        for i in range(lives):
            logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[life_keys[i]], color_life[0] , color_life[1], color_life[2])
        for i in range(len(life_keys)-lives):
            logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[life_keys[i+lives]], color_dead[0] , color_dead[1], color_dead[2])
        time.sleep(delay_time)
    def delay(delay_time):
        time.sleep(delay_time)
    def led_init():
        logi_led.logi_led_init()