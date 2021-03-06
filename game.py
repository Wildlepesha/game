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
	skill = 3
	dmg_mid = (base_atk_min + base_atk_max)//2

class dummie():
	life = 150
	
def title():
	print("#" * 50)
	print("#                      play?                     #")
	print("#" * 50)
	print('Type y - for start, n - for exit')
	print('#' * 50)
	p = input('> ').lower()
	if p == 'y':
		return True
	else:
		return False

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
	
	if part == 'head':
		dmg = random.randint(int(player.base_atk_min * 1.5), int(player.base_atk_max * 1.5))
		if crit_deal() == True:
			dmg = dmg * player.crit_mp
			return dmg, 'Крит! Голова'
		else:
			return dmg, 'Голова'
	
	elif part == 'body':
		dmg = random.randint(int(player.base_atk_min), int(player.base_atk_max))
		if crit_deal() == True:
			dmg = dmg * player.crit_mp
			return dmg, 'Крит! Тело'
		else:
			return dmg, 'Тело'

	elif part == 'legs':
		dmg = random.randint(int(player.base_atk_min * 0.8), int(player.base_atk_max * 0.8))
		if crit_deal() == True:
			dmg = dmg * player.crit_mp
			return dmg, 'Крит! Ноги'
		else:
			return dmg, 'Ноги'
		
# def damage():
# 	if crit_deal() == True:
# 		dealt = int(body_part() * player.crit_mp)
# 		return dealt
# 	else:
# 		return body_part()

def item_drop():
	index = random.randint(0, 2)
	item = items[index]
	print('Вам выпал предмет - ', item)
	if index == 0:
		sword = random.randint(1, 3)
		player.base_atk_min += sword
		player.base_atk_max += sword
		print(f'Он дает: {sword} атаки!')
	elif index == 1:
		if player.crit >= 100:
			player.crit_mp += 0.1
		else:
			glove = random.randint(1, 6)
			player.crit += glove
			print(f'Он дает: {glove} % шанса крита, но если у вас больше 100% он дает 0.1 мультипликатора урона!')
	elif index == 2:
		ring = random.randint(1, 6)
		player.life += ring
		print(f'Он дает {ring} здоровья!')
		
def race_choice():
	print('Выберите рассу: ')
	count = 0
	for i in race_list:
		print(count, i)
		count += 1
	r = int(input('> '))
	if r in [0, 1, 2, 3]:
		player.race = race_list[r]
		if r == 1:
			player.crit += 10
		print('Поздравляю! Вы -', player.race)
		stats()
	else:
		race_choice()

def stats():
	print('Ваши статистики: ')
	print('Здоровье:', player.life)
	print('Шанс крита:', player.crit, '%')
	print('Крит мультипликатор:', player.crit_mp)
	print('Урон атаки:', player.base_atk_min, '-', player.base_atk_max)

def skill_choice():
	while player.skill != 0:
		print(f'\nУ вас есть свободные очки навыкв({player.skill}), куда их распределить? \n')
		for char in range(3):
			if char == 0:
				print(char, 'Здоровье')
			elif char == 1:
				print(char, 'Шанс крита')
			elif char == 2:
				print(char, 'Атака \n')
		sk = int(input('> '))
		if sk == 0:
			print('Здоровье увеличено на 5! \n')
			player.life += 5
		elif sk == 1:
			print('Шанс крита увеличен на 2! \n')
			player.crit += 2
		elif sk == 2:
			print('Базовая атака увеличена на 2! \n')
			player.base_atk_min += 2
			player.base_atk_max += 2
		player.skill -= 1
		stats()
def chest():
	for i in range(random.randint(0, 4)):
		item_drop()

def beat():
	# print(body_part())
	# print(dummie.life - round(body_part()))
	while dummie.life > 0:
		dummie.life -= round(body_part()[0])
		if dummie.life < 0:
			print('Oh no(')
		else:
			print(dummie.life, body_part()[1])