# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 14:39:13 2018

@author: timothy
"""
from logipy import logi_led
import time
import ctypes
import pygame
import math
import random

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

# Creates a list containing 4 lists, each of 10 items, all set to 0
keys_array = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"], ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
              ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";"], ["z", "x", "c", "v", "b", "n", "m", ",", ".", "/"]]

all_keys_array = [["+",  "+",      "+",      "g6",  "g7",  "g8", "g9", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+", "+"],
                  ["+",  "esc",    "+",      "f1",  "f2",  "f3", "f4", "f5", "f6", "f7", "f8", "+", "f9", "f10", "f11", "f12", "priscr", "scrlo", "pau", "+", "+", "+", "+"],
                  ["g1", "`",      "1",      "2",   "3",   "4", "5", "6", "7", "8", "9", "0", "-", "=", "backsp", "ins", "home", "paup", "numlo", "n/", "n*", "n-"],
                  ["g2", "tab",    "q",      "w",   "e",   "r", "t", "y", "u", "i", "o", "p", "[", "]", "enter", "delete", "end", "padown", "n7", "n8", "n9", "n+"],
                  ["g3", "capslo", "a",      "s",   "d",   "f", "g", "h", "j", "k", "l", ";", "'", "backsla", "enter", "+", "+", "+", "n4", "n5", "n6", "n+"],
                  ["g4", "shiftl", "+", "z",   "x",   "c", "v", "b", "n", "m", ",", ".", "/", "+", "shiftr", "+", "arrup", "+", "n1", "n2", "n3", "nenter"],
                  ["g5", "ctrll",  "winl",   "+", "alt", "+", "+", " ", "+", "+", "+", "altgr", "winr", "text", "ctrlr", "arrl", "arrdo", "arrr", "n0", "n0", "ndel", "nenter"]]
#print(keys_array[0][4]) gives 5

def fade_key_color(dic_keys, key, display_time, color_display, color_normal):
    """dic_keys is dic, key is chart, displ is int, color_display and color_normal is [0-100, 0-100, 0-100]"""
    
def health_bar(lives, color_life, color_dead, life_keys=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]):
    """"""
    for i in range(lives):
        logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[life_keys[i]], color_life[0] , color_life[1], color_life[2])
    for i in range(len(life_keys)-lives):
        logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[life_keys[i+lives]], color_dead[0] , color_dead[1], color_dead[2])
    

def scanning_all(dic_keys, all_keys_array, display_time, direction, color_display, color_normal):
    """do a scanning of the whole keyboard in a difinite time"""
    if direction == "x":
        for i in range(22):
            for j in range(7):
                if all_keys_array[j][i] != "+":
                    logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[all_keys_array[j][i]], color_display[0] , color_display[1], color_display[2])
            time.sleep(display_time*9/10)
            for j in range(7):
                if all_keys_array[j][i] != "+":
                    logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[all_keys_array[j][i]], color_normal[0] , color_normal[1], color_normal[2])
            time.sleep(display_time/10)
    if direction == "y":
        for i in range(7):
            for j in range(22):
                if all_keys_array[i][j] != "+":
                    logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[all_keys_array[i][j]], color_display[0] , color_display[1], color_display[2])
            time.sleep(display_time*9/10)
            for j in range(22):
                if all_keys_array[i][j] != "+":
                    logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[all_keys_array[i][j]], color_normal[0] , color_normal[1], color_normal[2])
            time.sleep(display_time/10)
            
def scanning(dic_keys, keys_array, display_time, direction, color_display, color_normal):
    """do a scanning of the keyboard in a difinite time"""
    if direction == "x":
        for i in range(10):
            for j in range(4):
                logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[keys_array[j][i]], color_display[0] , color_display[1], color_display[2])
            time.sleep(display_time*9/10)
            for j in range(4):
                logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[keys_array[j][i]], color_normal[0] , color_normal[1], color_normal[2])
            time.sleep(display_time/10)
    if direction == "y":
        for i in range(4):
            for j in range(10):
                logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[keys_array[i][j]], color_display[0] , color_display[1], color_display[2])
            time.sleep(display_time*9/10)
            for j in range(10):
                logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[keys_array[i][j]], color_normal[0] , color_normal[1], color_normal[2])
            time.sleep(display_time/10)

def display_string(dic_keys, string, display_time, color_display, color_normal):
    """dic_keys is dic, string is str, displ is int, color_display and color_normal is [0-100, 0-100, 0-100]"""
    for i in string:
        logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[i], color_display[0] , color_display[1], color_display[2])
        time.sleep(display_time*9/10)
        logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[i], color_normal[0] , color_normal[1], color_normal[2])
        time.sleep(display_time/10)

def wave(dic_keys, all_keys_array, display_time):
    count = 0
    rand1 = 0.95 + random.random()/10
    rand2 = 0.95 + random.random()/10
    rand3 = 0.95 + random.random()/10
    reset_time = 350
    while(True):
        if count > display_time/0.02:
            break
        for i in range(reset_time+100):
            count = count+1
            if count > display_time/0.02:
                break
            time.sleep(0.02)
            for j in range(7):
                for k in range(22):
                    if all_keys_array[j][k] != "+":
                        if i < reset_time:
                            logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[all_keys_array[j][k]],
                                                                                 int(abs(100*math.sin(rand1*i*(0.0134765+(j+k)/3000)))),
                                                                                 int(abs(100*math.sin(rand2*i*(0.0144754+(j+k)/3000)))),
                                                                                 int(abs(100*math.sin(rand3*i*(0.0174723+(j+k)/3000)))))
                        elif i%reset_time < 100:
                            logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[all_keys_array[j][k]],
                                                                                 int(abs(100*math.sin(rand1*i*(0.0134765+(j+k)/3000)))*(100-i%reset_time-1)/100 + i%reset_time),
                                                                                 int(abs(100*math.sin(rand2*i*(0.0144754+(j+k)/3000)))*(100-i%reset_time-1)/100 + i%reset_time),
                                                                                 int(abs(100*math.sin(rand3*i*(0.0174723+(j+k)/3000)))*(100-i%reset_time-1)/100 + i%reset_time))
                        
        
"""def wave(dic_keys, all_keys_array, start_key_coord, display_time, color_display, color_normal):
    logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[all_keys_array[start_key_coord[0]][start_key_coord[1]]], color_display[0] , color_display[1], color_display[2])
    time.sleep(0.02)
    for i in range(int(display_time/0.02)):
        time.sleep(0.02)
        logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[all_keys_array[start_key_coord[0]][start_key_coord[1]]],
                                                            int((color_display[0]*(100-i))/100+(color_normal[0]*(i))/100),
                                                            int((color_display[1]*(100-i))/100+(color_normal[1]*(i))/100),
                                                            int((color_display[2]*(100-i))/100+(color_normal[2]*(i))/100))
        for j in range(7):
            for k in range(22):
                if j != start_key_coord[0] and k != start_key_coord[1] and all_keys_array[j][k] != "+":
                    logi_led.logi_led_set_lighting_for_key_with_key_name(dic_keys[all_keys_array[j][k]],
                                                                        int((color_display[0]*(i-abs(((j-start_key_coord[0])+(k-start_key_coord[1]))/60)))/100+(color_normal[0]*(100-(i-abs(((j-start_key_coord[0])+(k-start_key_coord[1]))/60))))/100),
                                                                        int((color_display[1]*(i-abs(((j-start_key_coord[0])+(k-start_key_coord[1]))/60)))/100+(color_normal[1]*(100-(i-abs(((j-start_key_coord[0])+(k-start_key_coord[1]))/60))))/100),
                                                                        int((color_display[2]*(i-abs(((j-start_key_coord[0])+(k-start_key_coord[1]))/60)))/100+(color_normal[2]*(100-(i-abs(((j-start_key_coord[0])+(k-start_key_coord[1]))/60))))/100))
                
"""             
        
        

logi_led.logi_led_init()
time.sleep(1) # Give the SDK a second to initialize

logi_led.logi_led_set_lighting(100, 100, 100)

#display_string(dic_keys, "#", 0.7, [100, 0, 0], [0, 100, 0])

#for i in range(10):
#    scanning(dic_keys, keys_array, 0.1, "x", [100, 0, 0], [0, 100, 0])
#    scanning(dic_keys, keys_array, 0.1, "y", [100, 0, 0], [0, 100, 0])

#health_bar(2, [0, 100, 0], [100, 0, 0])

#logi_led.logi_led_set_lighting_for_key_with_key_name(43, 100, 0, 0)
#for i in range(10):
#    scanning_all(dic_keys, all_keys_array, 0.1, "x", [100, 0, 0], [0, 100, 0])
#    scanning_all(dic_keys, all_keys_array, 0.1, "y", [100, 0, 0], [0, 100, 0])
wave(dic_keys, all_keys_array, 20)

#while(True):
    
time.sleep(0.02)
logi_led.logi_led_shutdown()

#help(logi_led)