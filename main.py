import os
import time
import random
import sys
import math


#our game is Golden egg. The main rule is to find golden egg and survive from aliens.
#Try to not die, gain gold and beat score to achieve victory.

#here is our small created maps for the game. 
#As it is not allowed to use drawing libraries, we try to create ASCII arts by symbols
# Thanks Iman for creating wonderfull ascii arts
forest_art = r""" # here is forest ascii art
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣀⣠⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣶⡶⠶⣿⣿⣿⣿⣛⣓⠦⠝⢿⡿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⠷⢏⣄⣤⣌⣣⣄⣄⡹⣿⣿⣽⠖⠻⣷⣟⣷⢆⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠈⠷⣠⣲⣾⣿⢿⣿⡿⠿⢏⣹⣿⣿⣿⣿⡖⢿⠛⠻⣦⣿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⣃⣲⣦⣽⡿⠋⣉⢻⣷⣦⣤⣁⣉⣋⣻⠛⠻⣾⣼⣿⣻⣯⣭⣿⣄⡀⠀⠀⠀⠀                   
⠀⠀⢀⣴⣿⠋⠩⣿⢿⣿⡿⣝⣟⢧⣤⣌⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⠿⣾⣿⣅⠀⣿⣿⣦⡀⠀⠀
⠀⣰⣿⡿⠋⣡⣶⠀⠿⣿⡷⠿⢻⣿⣿⡟⢻⣿⢿⣿⣿⣾⣿⣶⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⠿⡀⠀
⠀⢹⣿⣿⠟⠛⣛⣀⣶⣾⣷⣎⣿⣷⣿⠹⣿⣿⣤⠞⢩⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⠟⠻⣿⣷⣷⠀
⠀⠎⠽⣿⣶⣾⡿⢟⣿⣿⣿⡿⠿⣿⡟⠳⣿⣿⣯⣤⡾⠃⣩⣿⡿⠿⣿⣿⣿⡟⢿⠷⣦⣼⣿⣿⣦
⢰⣦⡖⠚⢿⣽⣿⡾⣛⣿⣷⣿⣦⣨⣿⣦⣈⣿⣿⣿⣠⣾⡿⠟⢻⡿⡯⠽⢭⣽⣿⡟⡿⣿⣿⡿⠛
⠈⢻⣤⣶⣿⣭⣭⠿⢿⠏⠁⠉⠀⠉⠉⠻⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠈⠁⠀⠀
⠀⠀⠈⠉⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠾⠿⣿⡿⠿⣿⠿⡿⣦⡤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                       
"""

thicket_art = r""" # here is thicket ascii art
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣧⣾⣿⣯⢿⣷⠤⢼⡀⠶⢋⠹⡟⡛⣛⠛⠛⠚⠤⠄⣀⠘⣤⠀⢢⠀⡆⠀⠈⢂⣠⡀⠀⠀⠀⢀⢠⠔⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠓⢿⣦⣸⠁⡸⠁⡜⢠⠤⠓⢰⠠⠀⣀⡌⠀⡣⢥⣀⠀⠂⠘⢎⠉⠓⡗⢸⠥⠤⢵⢓⠂⠂⠀⣀⡀⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⡴⡃⠀⣵⡂⠀⠀⠀⠔⢉⠄⣧⢈⡌⠄⠚⢻⠪⠄⠀⠑⢤⠓⠌⡆⣠⡮⠄⢄⠀⠀⠀⠀⡃⢠⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠐⢄⠀⢸⣿⣯⣿⣿⣿⣿⣦⣾⣿⢻⠀⠀⠹⢀⠉⠳⣦⠊⢀⠌⡠⠛⡄⠂⠂⡀⢸⠖⢛⡉⠟⢦⡗⡖⠣⡵⡀⠀⠠⠑⠂⠀⡀⠑⡀⠁⠢⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⢠⠜⡤⢚⣿⣯⣿⣟⣿⣿⣿⠋⢀⣾⣄⠴⠛⠋⠱⠂⣹⣤⠼⠭⢤⠀⣈⠤⢀⠆⢎⣥⣠⠀⠁⢹⣟⠒⢼⠁⠈⠢⠄⡐⠊⠀⣸⠀⠘⠀⠀⡄⠀⠀
⠀⠀⠀⠀⠈⠀⠀⠀⢀⠀⡠⡍⡜⢠⣿⣿⣿⣿⣿⣿⣿⣿⣴⠿⠋⠁⠀⠀⠀⠄⣴⣿⣧⢤⣤⣗⠌⠀⠔⠍⠀⣾⠿⣿⣧⣄⣸⡜⣦⣾⠄⡉⠀⠀⠃⢀⡔⡇⠀⡈⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠆⡞⠀⠀⠀⢂⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⠃⠂⠀⠀⠐⠐⠁⢀⣾⡟⠁⠀⠀⠈⠉⠂⢀⡴⢾⠿⡶⠬⠿⡟⢿⣷⡄⣧⠁⡀⠀⠅⠋⢨⠀⠑⢆⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡼⠀⠈⠦⡀⢠⣴⠺⡸⣟⣿⣿⣿⣿⣿⣿⡇⠀⢠⣶⣾⣷⣶⣶⣿⠟⠀⠀⡀⣠⣠⣦⣴⣿⣶⣽⣮⣤⣾⡀⠙⣿⢿⢳⣻⡈⠐⡆⠘⠀⠀⠀⠀⠐⠀⢀⠀⡀⠀⠠
⢀⠀⠀⠀⠀⡁⠀⡄⢠⣾⣿⣽⠂⣧⣿⣯⣿⣿⣿⣿⣿⣷⣴⣿⡿⠋⠀⠉⢏⢀⡾⣽⣾⣾⣿⣿⣽⣿⣾⣿⣿⣽⣿⣿⣿⠳⣿⣼⣯⣙⣿⣄⠨⠆⠀⠀⠀⠀⠘⠄⠈⠀⠀⠀⠀
⠀⠀⠀⠂⢄⢨⠊⠀⢴⢿⣭⡵⡔⠁⢿⡟⢿⣿⣿⣿⣿⣿⣿⠛⢱⠀⠄⠀⢀⣼⡿⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣾⢻⣿⣿⣿⣿⠀⠨⠐⠀⢠⠀⠂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⡼⠀⠶⠉⠀⠀⣧⡇⠐⣿⣿⣿⣿⣿⣿⣿⣿⣱⡋⣰⠃⣤⣾⣟⢵⣾⣿⡿⠛⢹⢣⢠⣿⡇⠀⠃⠶⠟⣿⡻⢿⣿⣿⢿⣝⢿⣿⣷⠀⢈⠀⠘⢄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢸⠆⣸⡆⣇⡰⠾⣿⣇⢰⣿⣿⣿⣿⣿⣿⣿⣿⠏⢰⣷⣾⣿⣿⣿⣿⡿⠉⠀⣰⡏⡉⣿⠏⢱⠀⠀⠇⠀⡸⣷⣾⠉⣿⣿⣿⡏⡇⣿⣆⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀
⠀⠀⠠⠀⡀⡧⠈⢠⠑⠁⠀⠓⢽⣿⣿⣿⣿⣧⣿⣿⣿⣟⢲⣬⢾⣿⢹⣿⡿⠋⠀⢀⠊⢸⠁⠢⠅⢂⡀⠡⡀⠀⢰⠁⠹⣿⣴⡈⢿⢻⣿⣿⣎⣻⣦⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀
⠀⠀⠠⠉⠛⠂⠲⢄⠀⡀⠀⠄⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢠⣾⣿⣾⣿⣧⠀⠀⠊⠀⠊⠁⠁⠸⡜⢀⠠⠘⢦⠀⠀⠀⠹⡻⣿⡄⢷⣿⣿⣻⣯⢿⣧⠀⠄⠂⠁⠀⠤⠀⠂⠀
⠐⠁⢀⡀⠈⠀⠀⠂⢠⠈⠤⠀⢨⣿⣿⣿⢿⣯⣿⣿⣿⣿⣮⣩⠝⢻⣿⣿⢮⢧⠀⠠⠀⠂⡀⠄⠄⢸⢮⣀⠀⢨⢐⠀⠐⢠⢜⣼⣿⣾⣿⡿⣿⣿⡌⣯⣧⠀⢀⠐⠾⠂⠈⠀⠀
⡵⠈⢰⣒⣶⡰⠆⠀⠀⢨⠑⢺⣿⣿⣿⣷⣟⣼⣿⣜⢿⣿⣿⣿⣿⣿⣶⣿⣿⣾⠁⠁⠉⠡⠀⠀⠤⠄⡛⠴⠿⡀⠀⡧⠀⢠⣽⢚⡿⡟⣿⣿⣝⢼⣏⠙⣮⡻⣿⣕⢤⣭⠤⢐⠈⠀
⣶⡾⣭⣻⣛⡯⠞⠳⠾⣾⣷⣿⣿⣿⣷⣿⡛⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡷⡾⣶⣌⠀⠀⡉⠁⢄⠃⡀⢨⠀⢹⣄⠈⢸⡾⣶⣙⣺⣿⣿⣿⣿⣇⢸⡷⢵⡿⣆⠁⠀⠃⠀⠀
⠘⣯⣿⣤⣝⡒⢙⣿⣿⣿⣿⣿⣿⣽⣿⡻⣿⣾⣿⢿⣿⣿⣿⣿⣿⣎⣿⣿⠏⠓⠀⢰⠚⠯⠶⢌⣇⢒⠂⠐⡀⠀⡈⠞⢣⣼⡳⡧⠛⣘⣿⣿⣿⣿⣇⣾⣥⣾⣿⡿⣵⣦⣄⠔⠁
⢸⣷⣿⢿⣯⣴⣿⣿⣿⣘⣦⣿⣿⣿⣿⣿⣿⣫⣿⡷⣿⣿⢿⣿⣿⣿⣿⣿⣦⠘⠒⠀⠀⢀⠒⠀⠋⢓⢶⣘⡒⢖⠂⢒⣿⣿⣿⣿⣴⣿⣿⣿⣿⣿⣿⢿⣾⣿⣿⣿⣾⡿⣽⢾⣷
⣾⣿⣿⣿⣟⣽⣿⣻⣿⢿⣽⣿⣿⣿⣿⣿⣾⣿⣿⣿⣟⣵⣿⡧⣿⣿⣷⣆⣻⣆⠀⠀⠀⠀⠀⠀⠀⠐⠀⠈⠙⠲⠳⠤⢶⣽⣿⣿⢛⣿⣿⣷⣷⣝⠩⣿⣿⣿⣿⢻⣿⣳⣿⣿⣿
⢿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣽⣸⣿⣿⠿⠙⠉⠉⠉⠁⠀⠉⠁⠘⠙⠛⠁⠉⠉⠒⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠛⠛⠛⠻⠿⠿⠚⠓⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠓⠀⠀
"""


# so here is bank stream arrt
stream_bank_art =r"""
⣿⣿⣿⣿⣾⣽⣿⣿⣿⣿⣿⡿⣿⣿⣿⢿⡯⢟⡿⣿⢿⡿⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⢿⣿⢿⡿⣿⣻⢿⣟⡿⢯⠿⣟⠿⡹⢯⠽⡡⢏⠿⠻⡟⠿⡛
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠶⡙⠤⢊⠜⡠⠑⡄⢂⠘⡀⠊⠱⠘⣿⣿⣿⣿⣿⣽⣿⠻⠞⡿⣻⣟⣿⣽⣷⣿⣿⣿⣿⣿⣿⣽⡿⣞⣯⣳⠹⣌⢳⡙⢦⠣⣑⠊⡔⢡⠘⡐⠠
⣿⣞⣿⣻⣿⣿⣿⠿⣙⣿⣿⣄⡐⢠⡈⢄⠂⠠⠑⢠⢂⡰⣠⢆⠧⡳⣌⠿⣟⢿⡻⠗⢋⡨⢩⣷⣦⣽⣏⡱⢬⣝⡲⡽⠿⠟⠿⡿⡿⣿⢯⣷⢓⡌⠦⡉⠆⡑⢠⠃⢌⠂⡔⠠⢁
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣬⣣⣛⣽⡽⣏⢷⢣⡓⢮⣳⡱⢯⡜⡜⢪⡙⢣⠎⡔⢫⠝⣿⣛⣶⣽⣿⣞⣥⣳⡭⢎⡵⣢⢵⣮⣧⣽⠇⡜⢂⡱⣈⢔⡣⠜⡠⠃⠄⡁⢂
⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣽⣶⣻⣗⡾⣹⣷⣿⣷⣾⣼⣣⣛⡴⣋⢞⣯⢻⣿⡽⣯⣽⣫⣾⣿⣿⣿⣿⣟⣫⣴⣧⠶⠿⠾⣷⣻⣴⣋⣶⠵⠟
⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣝⢾⣙⣞⡲⣏⡾⣵⣏⡷⣿⠿⣿⠟⣿⣿⡿⠟⠋⠁⠠⢒⢂⠌⠛⠛⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⣻⣿⣿⣵⣎⣷⣻⣜⣷⣻⣟⣷⢾⣽⣭⣭⣵⡿⠛⠁⠀⠄⣱⠃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⡀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠻⠿⠿⠿⠿⣿⣿⣿⣿⣿⡿⠃⠀⠀⡠⠤⠃⠘⠠⠀⠀⣀⣀⢀⡄⡄⢇⡘⠃⠀⡀⠠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠉⠛⠻⠛⣩⣉⠄⣤⣤⢤⡶⢚⠡⠄⠄⠀⠉⠉⠁⠀⠀⢀⣠⢄⣰⢢⠵⢢⠍⠝⡠⢋⡌⢐⠠⡄⠔⡂⠌⡑⠃
⠒⠶⣲⢲⣚⢖⣂⠒⠒⡒⢦⠤⡐⢦⡑⣦⠆⢲⣄⠂⢰⡤⣀⠀⣀⣀⣄⡀⠀⠀⠀⠀⠀⠂⠤⠃⠜⠠⢉⠂⣅⡠⠤⣖⠞⡉⡈⠈⠀⡡⡐⠄⢎⠲⢍⠂⠬⠂⠃⠘⠀⠀⠀⠀⠀
⡍⡙⠦⣯⣭⣭⣤⣭⢽⡽⣯⢯⡿⡿⣮⢭⡸⣗⣲⣶⠶⣮⣝⣩⣽⣿⡿⣍⣅⣽⣿⣃⣥⣴⠒⠚⠀⠶⠟⠛⠮⣕⣞⠨⢋⡑⠀⠀⡀⠆⡑⢢⠀⠀⢀⡈⠤⠄⠠⠂⠀⠂⠠⠀⠀
⠁⠀⠀⠨⣙⠎⡿⠁⠈⠀⠀⠀⠀⠀⠁⠀⠀⠉⠛⢯⡤⢿⢿⣿⣾⡿⠟⢉⠉⠀⠈⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠀⠀⢰⡶⠖⠷⠧⠈⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣄⠦⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠀⠈⠀⡀⢀⡠⢈⠈⠁⢦⣢⢤⣄⢀⣀⣀⣄⣤⣠⣤⡴⡄⡀⠀⢀⠀⠁⠀⠀⠂⠈⠀⠈⠀⠀⠠⠤⠄⠀⠀⠀⠀⠀⢀⠀
⠁⠀⠂⡐⡀⢀⣢⢤⢀⡆⠆⠀⠂⠂⠀⠀⠀⠀⠀⠀⠙⠲⠲⠉⠯⠹⠖⠊⠙⠂⢉⡁⠤⠰⠚⠁⢬⠤⠭⢘⣳⠶⠆⠫⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢲⢩⡘⠤⢀⣋⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣴⣶⡶⢏⡹⡱⠛⣷⢀⡛⢒⣮⣰⣦⣼⣮⣡⠂⢈⠔⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠄⠀⠀⠀⠐⠀
⠀⠀⠀⣠⣤⣶⣾⣶⣷⣤⣤⡄⠀⢀⣼⣶⣿⣿⣿⢞⣻⣿⣿⣟⣟⣮⡍⠠⠇⠮⠿⣥⡒⢿⡟⢟⢿⢯⣀⣍⠙⣋⡙⠭⢌⡗⡞⡳⣉⢃⡁⣀⢁⢂⠁⠀⠀⠉⠀⠀⠀⠂⠀⠀⠀
⠀⠀⠀⠛⠿⢿⣿⣿⣿⣿⣿⣾⣷⣾⣭⣭⣕⣠⡉⠛⡋⠙⣋⡉⣹⣿⣧⠀⠀⠀⠀⠀⠈⠀⠠⢚⢺⣶⣻⣧⡼⠧⠛⡬⢃⠙⠓⠁⠈⠃⠒⠡⠞⠠⠀⠔⠂⠠⣀⠠⡀⠄⠀⠀⠀
⠀⠀⠀⡀⣀⣀⣠⡀⠙⠛⠿⠿⣿⣿⣿⣿⣿⣿⣯⣿⣷⣾⣿⣿⣭⣭⣤⣀⣀⣀⠀⠀⠀⠀⠀⠘⠉⠀⠑⠃⠐⠈⠓⠁⠒⠠⠀⠈⡀⠄⠐⠀⠀⠀⠉⠀⠑⠂⠀⠂⠁⠂⠀⠈⠀
⠀⠀⠂⡱⢄⠓⣈⡒⢍⡱⡢⠄⠄⠉⠙⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠁⠌⠀⠁⠃⠈⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

#small camp art
campsite_art= r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⠌⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⠀⠂⠚⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡍⠁⠀⠀⠄⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⠀⡀⠀⠙⠃⠀⠀⣼⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣷⣤⠄⢃⠀⢀⡀⡀⠀⢠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⢹⣿⣯⣄⡄⠀⠀⠈⣠⠠⡀⠀⠚⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠠⠀⢙⣿⡛⠁⢠⣶⠌⠙⣤⠀⠐⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡀⠀⠀⢀⣹⡷⠿⠀⠁⠒⠲⠏⠁⡀⠟⠻⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⡀⠀⠀⢀⡙⣷⣦⡀⠀⢀⣤⡌⠉⠡⣤⣦⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⠀⠀⢰⠀⣹⣿⣿⣿⠀⢙⠋⢁⠀⢠⣈⠉⢉⡹⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅⠀⢀⢀⠀⢈⣿⣿⣿⡆⣿⡿⠖⢂⡀⠉⠲⣾⡃⠈⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣙⠻⢿⣿⣿⣿⣿⣿⡇⠀⠠⣸⣾⠀⠀⢻⣿⣿⠀⣿⣿⣷⡄⢡⣶⣿⣏⠀⠃⠙⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠘⣿⣄⠠⡉⢛⠛⠋⠰⠂⠀⡎⢇⠑⠠⢈⣿⣿⠀⣿⣿⣿⡇⠘⣿⣿⡟⠘⠂⠘⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠏⠘⣿⣿⣿⣿⣿⣿⠏⣼⠀⠀⠘⠿⣷⡔⣶⡢⠳⡴⡐⣶⡀⠠⣄⢀⠚⠛⡛⠀⠛⠛⠃⢷⠀⣿⡿⠁⢰⡆⠀⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠋⣰⣾⢘⣿⣿⣿⣿⣿⠏⡄⣿⠀⠀⢰⣌⢾⣿⣿⣿⣄⣙⢷⣌⠻⣌⠊⠳⣄⡀⠘⡄⠤⣄⠀⠈⠀⣿⡷⠂⣴⣤⡀⢶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⡏⣤⡜⠛⣿⣿⣿⢏⡜⠁⡇⠀⠀⢸⣿⠠⠻⣿⡟⣿⣿⣧⣉⠓⠨⡠⣔⢏⡨⣆⠈⢕⠀⠁⠐⠀⢿⠷⠨⣿⡃⠠⣴⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠛⠟⠘⢣⡙⢇⢁⠿⡿⢣⣾⠇⡀⡇⠀⠀⠀⣿⠀⠱⣌⠻⠹⡿⣿⣽⣿⣿⡈⠪⡷⣝⠮⡳⣤⡑⠢⡃⠀⠀⡙⢠⣟⡉⢂⣛⣿⣿⣿⣿⣿
⣿⣿⠿⡟⣴⣶⣦⡾⠳⣄⢀⣆⢱⠿⠃⠀⢀⠀⠀⠀⠀⢸⠀⢂⠘⣷⣄⠠⠀⠉⠉⠛⠻⠛⠪⠙⠷⢌⢒⢝⠂⡈⠀⠀⠀⠀⠙⢿⡈⢿⣿⣿⣿⣿⣿
⣿⣿⢁⠙⣼⠠⢿⣼⣶⠈⢀⣏⣰⣀⡔⢁⣿⠀⠀⠀⠀⢸⠀⠈⢦⠘⢻⣷⣌⠊⠀⠀⠀⠀⠈⠂⠄⠀⠑⠀⠈⠀⠄⠠⡀⠀⢄⠀⠀⠲⢿⣿⣿⣿⣿
⣿⡏⠜⢷⡟⠘⢟⠛⠋⠋⠃⢻⡿⠈⠀⢀⠋⠀⠀⠀⠀⢸⣆⠠⡄⠓⢀⠉⠛⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠐⠘⠂⠀⢀⣈⣙⣋⣸
⣿⣿⣦⡘⢰⢀⠈⠁⣠⣌⢆⡆⠁⡄⠀⢀⣶⠀⠀⠀⠀⠘⠈⠀⡈⠢⠈⠀⠀⠉⠻⢿⡖⠄⡀⢀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿
⡏⠉⠀⠀⣠⡉⠀⠼⠛⠟⠘⠀⠤⡀⢤⣭⣝⣠⣶⣤⣤⣤⣥⣄⣙⠆⠀⠀⠀⠠⠿⠬⠀⠀⠹⠦⠄⠀⢀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⡇⠈⠛⠁⠀⢂⠰⠧⠂⠀⠚⠓⠈⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣷⣶⣤⣴⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""
#alien pod
alien_pod_art=r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⢉⡁⠄⠠⢤⡀⠈⠱⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⠁⣠⣾⣿⡀⠀⠀⠸⣷⠀⠀⡟⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠃⠀⢠⣿⢻⡇⢿⠀⣀⢀⢸⡄⢠⠀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠾⠁⣦⠀⣰⣿⢃⠞⠀⢈⣷⣽⡿⡛⠀⡜⠀⣾⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠐⣿⠠⢩⣧⡞⢀⡴⢊⡽⠫⠘⠀⢰⣧⣴⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣀⣀⣀⣀⣹⡄⢻⠫⢴⠯⠚⠉⢀⡀⠀⢠⣾⣿⣿⣿⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠒⣛⣹⣏⣩⣭⣤⣴⣿⣏⠙⠲⣄⠈⠴⢶⢶⠿⢿⡒⣼⣿⢿⣿⢳⣟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠋⣡⣴⡶⠿⡿⠏⠉⠉⣿⠟⠙⠉⠑⠙⠆⢸⣧⡀⠀⢸⣲⠂⢰⣿⣿⣾⢃⣺⡯⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⢁⡴⠊⠉⠀⢠⡼⠇⠀⢦⡾⠁⠀⠀⠀⠀⠀⠀⣼⡞⢙⡟⠻⠟⢃⣿⣿⣿⡏⢸⡏⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⢃⡴⠋⢠⡀⠀⢠⡞⠁⠀⣠⠏⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⣼⡇⠀⠀⣼⣿⣿⣿⡉⡹⢼⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡞⢁⣾⠃⠀⣩⣟⣶⣿⣀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⢀⣼⡏⣰⣿⠃⠀⣸⣿⣿⣿⢛⣿⢚⡞⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⡞⠀⠘⠿⠶⠷⠾⢿⣿⠿⠘⣶⡃⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⣰⣿⠏⠀⣸⢿⣿⣿⠏⢤⠏⣸⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡿⠁⠀⠀⠀⠀⠀⢠⣿⠁⠀⡰⢁⣼⣷⣶⣾⣧⣼⣟⡀⣼⡿⣵⣿⡟⠀⢠⢿⣿⣿⠿⠾⠏⢡⢿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⢠⠎⢧⣀⡼⢁⣾⣿⣿⣿⣿⣿⣿⡟⣻⡿⣹⣿⡿⠁⢈⣯⣿⣿⡿⣗⠀⢀⡎⢸⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⢠⡎⠀⠀⡼⢧⣾⣫⣿⣿⣿⣿⣿⣿⣽⡟⣽⣿⣿⡿⢘⣿⣿⣿⣿⣁⡟⠂⡼⠁⡞⠀⠀⠀⠀⠀⠀⠀
⠸⠚⠋⠙⠛⠲⢄⡀⠀⢠⠏⠀⠀⡼⢁⣾⣿⣿⣷⣾⣿⣿⢿⣿⠟⣼⣿⣿⡟⢀⣾⣿⣿⣿⠏⡿⠀⢠⠃⣸⠁⠀⠀⠀⢀⣴⡞⠟
⠀⠀⠀⠀⠀⠀⠀⠙⠢⠮⠴⠒⠚⠒⠼⣿⣇⣿⣔⣭⣿⣫⣯⠎⣼⣿⣿⠏⢀⠾⣿⣿⣿⣟⣫⣤⠤⠯⠴⠧⠤⠤⠤⠜⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣶⡶⠶⠒⣶⠶⣿⣌⣠⠟⠋⢉⢉⢓⠻⡿⠧⠤⠾⠤⠼⢛⠋⠉⠀⠀⠀⠀⣄⣤⡤⣖⠒⢦⣤⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠉⠑⣦⣾⡏⠋⣼⣿⠀⢰⣽⣿⡟⣿⣷⣶⣶⠀⠒⠀⠀⠁⣤⣤⣤⠀⠀⠀⠘⡟⠋⠈⠉⠛⠛⠃⠀
⠀⠀⠀⠀⠀⢀⣀⣤⡤⣦⣄⣀⣀⣀⣀⡿⠞⠉⠀⠀⠺⣥⣀⣐⣿⣿⣿⣿⠂⠄⢠⡶⠛⢻⣽⣿⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠑⠦⢼⣿⡿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

golden_nest_art=r"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢉⣤⣽⣿⣶⣤⣍⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⡵⢟⣤⣾⣿⣿⣿⣿⣿⡻⣿⣷⡜⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡡⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡜⣿⡿⡞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⡞⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⡼⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⡞⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣇⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⣿⣟⢋⡞⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣻⣿⡸⣿⣿⡿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣛⣛⠃⠈⠁⣸⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠫⢠⡿⢹⡇⠀⠙⠃⢿⣿⣿⣿⣿
⣿⣿⣬⡛⠋⠑⠀⠀⠀⣿⢠⣿⠋⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡅⠀⡼⢡⢿⠇⠀⠀⠀⠄⠩⠻⣿⣿
⣿⣿⠟⡀⠀⠀⠀⠀⠀⢻⣾⣿⣷⣬⡛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣯⠖⡱⢣⢏⣾⠁⠀⠀⡀⡈⠀⢀⢹⣿
⣟⣁⠀⡇⡄⠐⠀⠠⠀⠘⢿⢿⡛⠷⣽⣷⣝⣿⣿⣿⣿⣿⣿⣛⠉⣴⣴⣧⠾⠃⢀⠤⠂⣠⠁⠄⠈⢦⣿
⣿⡏⠀⠑⢃⡈⠦⣀⠀⠀⠀⠑⢷⣀⠐⠻⣿⣟⢋⠽⠛⠛⠉⡶⢟⠿⠏⠁⠀⠀⠀⠀⠔⠁⠀⠀⠀⠀⢿
⣿⣷⠀⠀⠀⠠⡁⠘⠒⠲⣄⠂⠀⠈⠂⠀⠤⠥⠄⠤⠁⠂⠬⠭⠥⠤⠄⠒⠒⣒⡠⠄⢊⣀⢀⡄⢀⣼⣿
⣿⣿⡆⠄⠀⠑⠀⠀⠀⢀⠈⠑⠀⠀⠀⢂⠂⠬⠭⣥⣭⣍⣙⣛⣤⠤⠐⠈⣁⣀⡀⠂⢀⠄⠀⠀⢸⣿⣿
⣿⣿⣿⣦⡀⠀⠐⠂⠀⠠⠀⠀⠀⠀⠀⠀⠨⠄⠠⠶⠒⠪⠤⠬⢉⠉⠉⠀⠀⠀⠀⠊⢁⠀⢈⣤⣿⣿⣿
⣿⣿⣿⣿⣧⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⡀⠀⣐⣩⠤⠄⠒⠂⠁⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣦⡀⠉⠁⠒⠒⠀⠀⠈⠈⠽⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣶⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣤⣤⣤⣤⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""

# we stored created arts into dictionary to get access them when game runs
ART_GALLERY = {
    "forest": forest_art,
    "thicket": thicket_art,
    "crashed_pod": alien_pod_art,
    "golden_nest": golden_nest_art,
    "stream_bank": stream_bank_art,
    "abandoned_campsite": campsite_art
}

# Alien Classes
# so we created 4 types of aliens and all of them have common attributes and methods

class Alien:
    def __init__(self, name, description, health, damage, defense, behavior, drops):
        self.name = name
        self.description = description
        self.health = health
        self.damage = damage
        self.defense = defense
        self.behavior = behavior  # guard, chase, ranged, ambush
        self.drops = drops # its items that alien drop when they die

    def is_alive(self):
        return self.health > 0 #check alien is alive or dir

    def attack_player(self, player): # function to calculate how much damage it deals to game players
        damage_dealt = max(0, self.damage - (player.stats[4] // 2))  #just calculation
        player.health = player.health - damage_dealt
        return damage_dealt

    def drop_item(self):
        if self.drops:
            return random.choice(self.drops) # Return a random item drop when dies
        
        return "Not any items" #maybe not any items drop

# ==========================================
# Alien Types


class Gronk(Alien):
    """Slow, armored guardian"""
    def __init__(self):
        super().__init__( # here is its attributes and features #super() calls Alien class constructor
            name="Gronk",
            description="A massive armored alien stands guard, unmoving.",
            health=80, 
            damage=6,
            defense=12,
            behavior="guard",
            drops=["Armor Plating", "Med Pack"]
        )

class Zorvath(Alien):
    """Fast hunter that chases players"""
    def __init__(self):
        super().__init__(
            name="Zorvath",
            description="A sleek predator stalks you from the shadows.",
            health=50,
            damage=12,
            defense=6,
            behavior="chase",
            drops=["Energy Blade", "Stimulant"]
        )

    def dodge_chance(self):
        return 0.35

class Xexu(Alien):
    """Ranged aerial attacker"""
    def __init__(self):
        super().__init__(
            name="Xexu",
            description="A floating alien hums as energy builds around it.",
            health=40,
            damage=18,
            defense=8,
            behavior="ranged",
            drops=["Plasma Cell", "Cloaking Shard"]
        )

class Mireling(Alien):
    """Weak ambush swarm enemy"""
    def __init__(self):
        super().__init__(
            name="Mireling",
            description="Small, vicious creatures swarm toward you.",
            health=25,
            damage=8,
            defense=4,
            behavior="ambush",
            drops=["Alien Claw", "Smoke Bomb"]
        )

def create_alien(alien_type): # alien factory method when we need to create alien
    """Factory method for creating aliens"""
    aliens = alien_type.lower()
    if aliens == "gronk":
        return Gronk()
    elif aliens == "zorvath":
        return Zorvath()
    elif aliens == "xexu":
        return Xexu()
    elif aliens == "mireling":
        return Mireling()
    else:
        raise ValueError("Unknown alien type") # maybe for some errors 


# ==========================================
# 3. WORLD DATA
# ==========================================

WORLD_ROOMS = {
    "forest": {
        "name": "Forest",
        "description": (
            "Standing within a dense forest where trees crowd the pathway "
            "and branches weave themselves over and above you, disrupting any "
            "signs of light. The air feels heavy and still."
        ),
        "look": (
            "Due to the thick vegetation, it remains hard to see what’s out there. "
            "Shadows move between the trees. "
            "Openings reveal themselves: East or South"
        ),
        "exits": {
            "south": "thicket",
            "east": "crashed_pod"
        },
        "items": [],
        "alien": None,
        "art_key": "forest", 
        "effects": []
    },
    "thicket": {
        "name": "Thicket",
        "description": (
            "Past the bushes entangled and intertwined and overgrown. "
            "Here, thick brambles and vines reach out to you in every direction. "
        ),
        "look": (
            "Through the gaps in the branches you see there are two possible pathways: "
            "North or West."
        ),
        "exits": {
            "north": "forest",
            "west": "abandoned_campsite"
        },
        "items": [],
        "alien": None,
        "art_key": "thicket",
        "effects": []
    },
    "abandoned_campsite": {
        "name": "Abandoned Campsite",
        "description": (
            "You finally reach an open stretch of land. "
            "Torn apart tents lay haphazardly on the grass. "
            "Old fire pits stand abandoned."
        ),
        "look": (
            "The campsite looks recently deserted. Near an empty fire pit, "
            "you spot supplies."
        ),
        "exits": {
            "east": "thicket",
            "north": "stream_bank",
            "south": "golden_nest"
        },
        "items": ["medkit"],
        "alien": "zorvath", 
        "art_key": "abandoned_campsite",
        "effects": []
    },
    "crashed_pod": {
        "name": "Crashed Alien Pod",
        "description" : (
            "Strobing lights pierce behind the bushes. "
            "A low hum fills the air."
        ),
        "look": (
           "In front of you - a crashed alien spaceship. "
            "You are filled with fear."
        ),
        "exits": {
            "south": "stream_bank",
            "west": "forest"
        },
        "items": ["plasma cell", "cloaking shard"],
        "alien": "xexu",
        "art_key": "crashed_pod",
        "effects": []
    },
    "golden_nest": {
        "name": "Golden Nest",
        "description": ("Stepping out into an open clearing, "
        "the trees beckon you into a circular open space bathed "
        "in golden sunlight. Lies a glowing nest."
        ),
        "look": ("It is beautiful, but guarded."),
        "items":["golden egg"],
        "alien": "gronk",
        "art_key": "golden_nest",
        "exits": { "north": "abandoned_campsite" }, 
        "effects": []
    },
    "stream_bank": {
        "name": "Stream Bank",
        "description": (
            "You come upon a shallow stream. Clear water flows calmly. "
            "The sound of the gentle stream briefly calms your nerves."
        ),
        "look": (
            "Beyond the stream, flickering lights probe through the trees. "
            "Something metallic lies ahead."
        ),
        "exits": {
            "north": "crashed_pod",
            "east": "abandoned_campsite"
        },
        "items": [],
        "alien": None,
        "art_key": "stream_bank",
        "effects": []
    }
}

# ==========================================
# 4. GAME ENGINE & MAIN
# ==========================================
# Hee
CLASS_TYPES = ["Lyra Stormwhisper", "Rowan Ironbrand", "Elowen Brightquill"]
STAT_NAMES = ["Strength:", "Agility:", "Intelligence:", "Perception:", "Endurance:"]
CLASS_STATS = [[4,8,3,8,5], [8,3,2,5,8], [2,3,9,7,4]]

# Shop Data
SHOP_ITEMS = {
    "potion": 50,
    "burnHeal": 50,
    "iceHeal": 50,
    "statBoost": 200
}

class User: #created User class to store players data
    def __init__(self, name, characters_index):
        self.name = name
        self.stats = CLASS_STATS[characters_index]
        self.hero_class = CLASS_TYPES[characters_index] 
        self.max_health = self.stats[4] * 5 + 100 #here is max health of hero at starting point
        self.health = self.max_health
        self.money = 250
        self.score = 0 
        self.inventory = ["potion"] #its just have potion
        self.Map = "forest" #game starts from forest map

#to record high score in the game, we need read and write to txt file name highscore
def record_score():
    """Reads the high score (points) from file"""
    try:
        with open("highscore.txt", "r") as f:
            score = int(f.read().strip())
            return score
    except FileNotFoundError and ValueError:
         0  # If file doesn't exist, return 0 as high score

def save_score(users_score):
    record = record_score()
    if users_score > record: # if current users score high than in txt, so it will rewrite it again
        with open("highscore.txt", "w") as f:
            f.write(str(users_score))
        print(f"\n[NEW HIGH SCORE: {users_score}!]")

def clear_sys():
    os.system('cls' if os.name == 'nt' else 'clear') # need for clear console 

def create_character():
    clear_sys()
    high_score = record_score()
    print("\n Hi. Welcome to Golden Egg Game created by UEA Students. Main rule of the game to survive and find golden egg.\n")
    print(f"=== Creating character === (Current High Score: {high_score})")
    
    for i in range(len(CLASS_TYPES)):
        print(f"{i}) {CLASS_TYPES[i]} | Stats: {CLASS_STATS[i]}")
    
    while True:
        try:
            choice = int(input("\nPlease choose your character by enter numbers from 0 to 2: "))
            if 0 <= choice < len(CLASS_TYPES):
                break
            print("Wrong number. Please enter number between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 2.")
            
    name = input("What is your name? ")
    if not name:
        name = CLASS_TYPES[choice]
        
    print(f"Good luck, {name}!")
    return User(name, choice)

def battle_alien(user, aliens_type):
    print(f"\nBe care. {aliens_type.name} attacks you!")
    
    while aliens_type.is_alive() and user.health > 0:
        print(f"\nUser: {user.health}/{user.max_health} HP | Alien: {aliens_type.health} HP")
        option = input("`What are you gonna do? Action` (1-Attack, 2-Potion, 3-Run): ")

        if option == "1":
            damage = random.randint(5, 10) + user.stats[0]
            aliens_type.health = aliens_type.health - damage
            print(f"> You dealt {damage} damage!")
            
        elif option == "2":
            if "potion" in user.inventory:
                user.inventory.remove("potion")
                user.health = min(user.health + 50, user.max_health)
                print("> Your health increased up to 50 HP!")
            else:
                print("> So sad( No potions left!")
                
        elif option == "3":
            if random.randint(0, 10) + user.stats[1] > 10:
                print("> You successfully escaped! You fast)")
                return "escaped"
            print("> Failed to escape. Alien damages you! Take action quickly")
        
        if aliens_type.is_alive():
            try:
                dmg = aliens_type.attack_player(user)
                print(f"> {aliens_type.name} damaged you {dmg}.")
                time.sleep(1)
            except Exception as e:
                print(f"Battle Error with {aliens_type.name}: {e}")
                break

    if user.health < 1:
        return "dead"
    
    else:
        print(f"\nVICTORY!")
        item = aliens_type.drop_item()
        user.inventory.append(item)
        user.money = user.money + 30 # Give gold
        
        # NEW: ADD SCORE POINTS
        score_gain = 100
        print(f"You gained {score_gain} score points by killing {aliens_type.name}!")
        user.score = user.score + score_gain
        
        print(f"Obtained: {item}, 20 gold and {score_gain} score points!")
        return "won"


# SHOP Menu to buy items
def shops(user):
    while True:
        print("\n--- SHOP ---")
        print(f"Your Gold: {user.money}")
        print("0. Exit Shop")
        
        items_list = list(SHOP_ITEMS.keys())
        for i, item in enumerate(items_list): # display items in shop
            print(f"{i+1}. {item} ({SHOP_ITEMS[item]} gold)")
            
        choice = input(" Please select item that you want to buy: ")
        
        if choice == "0":
            break # exits shop menu
            
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(items_list):
                item_name = items_list[idx]
                price = SHOP_ITEMS[item_name]
                
                if user.money >= price: # if player has enough money to buy items
                    user.money = user.money - price

                    user.inventory.append(item_name) # items will add to user inventory

                    print(f"Bought {item_name}! You can use it from invertory")

                    print(f"Your remaining Gold: {user.money}")
                else:
                    print("Not enough gold to buy)")
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Please enter a number.") # if user enter invalid input

def main(): # main game fucntion
    try:
        user = create_character()
        launch_game = True
        
        while launch_game:
            clear_sys()
            current_key = user.Map
            
            # Error handling for broken map links
            if current_key not in WORLD_ROOMS:
                print(f"Sorry: Map {current_key} not found in world data.")
                break
                
            game_map = WORLD_ROOMS[current_key]
            
            # Display Art if its available
            if "art_key" in game_map and game_map["art_key"] in ART_GALLERY:
                print(ART_GALLERY[game_map["art_key"]])

            print(f"--- {game_map['name']} ---")
            print(game_map['description'])
            print(f"Exits: {list(game_map['exits'].keys())}")  # each map has own exits
            
            # Alien Encounter Logic
            if game_map.get('alien'):
                # Create alien instance
                current_alien = create_alien(game_map['alien'])
                if current_alien:
                    result = battle_alien(user, current_alien)
                    
                    if result == "dead":
                        print("\n=== GAME OVER ===")
                        save_score(user.score) # Saves Score 
                        break
                    elif result == "won":
                        # Remove alien from game if it s die
                        game_map['alien'] = None 

            print("-" * 40)
            print(f"Health: {user.health}/{user.max_health} | Gold: {user.money} | Score: {user.score}") # user stats
            print(f"Inventory: {user.inventory}")
            print("-" * 40)

            command = input("Type commands (go [direction], shop, look, quit): ").lower().split()
            if not command: continue
            
            action = command[0]
            
            if action == "quit":
                save_score(user.score) 
                launch_game = False
                
            elif action == "look":
                print(f"\n{game_map['look']}")
                if game_map.get('items'):
                    print(f"Here lies: {game_map['items']}")
                    if input("Take it? (yes/no): ").lower() == 'yes':
                        user.inventory.extend(game_map['items'])
                        game_map['items'] = [] # Remove items from room

                        if "golden egg" in user.inventory:
                            user.score = user.score + 500
                            print("\n You found Golden Egg! You win this game")
                            save_score(user.score)
                            launch_game = False

                input("Press Enter to continue...")
                
            elif action == "shop":
                shops(user)
                
            elif action == "go":
                if len(command) > 1:
                    direction = command[1]
                    if direction in game_map['exits']:
                        user.Map = game_map['exits'][direction]
                    else:
                        print("You can't go that way! No map there")
                        time.sleep(1)
                else:
                    print("Go where? (e.g., 'go north')")
                    time.sleep(1)
            else:
                print("Unknown command. Please try 1 more time.")
                time.sleep(1)

    except KeyboardInterrupt: # ctrl + c to close game
        print("\nGame closed.")
    except Exception as e:
        print(f"Sorry. Error: {e}") # its for debugging
        import traceback
        traceback.print_exc()
    finally:
        print("Thanks for playing! Bye and see you again!")

if __name__ == "__main__":
    main()
