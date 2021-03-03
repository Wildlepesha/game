import random
import sys
import os
import time
from races import race_list, items

isGoing = True

class player():
	life = 100
	race = ''
	crit = 5
	crit_mp = 1.5
	base_atk_min = 10
	base_atk_max = 15  
	
	
def title():
	print("#"*50)
	print("#                      play                      #")
	print("#"*50)

def crit_deal():
	r = random.randint(0,100)
	if r <= player.crit:
		return True
	else:
		return False

def body_part():
	bp = random.randint(0, 2)
	part = ""
	if bp == 0:
		part = 'head'
	elif bp == 1:
		part = 'body'
	elif bp == 2:
		part = 'legs'
	print(part)
	
	if part == 'head':
		h = random.randint(int(player.base_atk_min * 1.5), int(player.base_atk_max * 1.5))
		return h
	
	elif part == 'body':
		b = random.randint(int(player.base_atk_min), int(player.base_atk_max))
		return b

	elif part == 'legs':
		l = random.randint(int(player.base_atk_min * 0.8), int(player.base_atk_max * 0.8))
		return l
		
def crit_dmg():
	if crit_deal() == True:
		dealt = int(body_part() * 1.5)
		print('Crit!',dealt)
	else:
		print('No crit (', body_part())

def item_drop():
	index = random.randint(0, 2)
	item = items[index]
	print('Вам выпал', item)
	if index == 0:
		mn = int(player.base_atk_min + 3)
		mx = int(player.base_atk_max + 3)
		dmg_mid = (mn + mx)//2
		print(dmg_mid)
	elif index == 1:
		if player.crit >= 100:
			player.crit_mp += 0.1
		else:
			player.crit += 6
		print(player.crit)
	elif index == 2:
		player.life += 6
		print(player.life)
		
def race_choice():
		print('Выберите рассу: ')
		count = 0
		for i in race_list:
			print(count, i)
			count += 1