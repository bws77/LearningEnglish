# -*- coding: utf-8 -*-

class GlobalStatistic:
	def __init__(self, min_percent, min_success_cnt):
		self.stat_en_ru = []
		self.stat_ru_en = []
		self.min_percent     = min_percent
		self.min_success_cnt = min_success_cnt

	def calc_stat(self, word, stat_info):
		en_word, transcription, ru_word = word.get_show_info()
		total       = stat_info.get_total_answer()
		success_cnt = stat_info.get_success_answer()
		error_cnt   = total - success_cnt
		pers        = stat_info.get_success_persent()

		if pers >= self.min_percent and total >= self.min_success_cnt:
			state = 0
		elif total > 0:
			state = 1
		else:
			state = 2
		return (en_word, transcription, ru_word, str(success_cnt), str(error_cnt), str(round(pers, 2))+'%', state)

	def add_word(self, word, stat_en_ru, stat_ru_en):	
		self.stat_en_ru.append(self.calc_stat(word, stat_en_ru))
		self.stat_ru_en.append(self.calc_stat(word, stat_ru_en))

	def get_en_ru(self):
		return sorted(self.stat_en_ru, key=lambda x : (x[6], x[0].lower()))

	def get_ru_en(self):
		return sorted(self.stat_ru_en, key=lambda x : (x[6], x[0].lower()))