###################################################
###################################################
#    ALL STUFF HERE ARE MADE BY HN (ImNoobb)      #
#    PLEASE ASK ME IF YOU WANT TO USE IN YOUR     #
#    PROGRAM(S), TY!                              #
###################################################
###################################################
import pygame,random,time,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption('MathWithMe! v2')
pygame.display.set_icon(pygame.image.load('data/icon.png').convert_alpha())

# Button Classes ==============================================================
class N_Button():
	def __init__(self,btn_img,btn_img_hover,pos,cmd):
		self.button = [btn_img,btn_img_hover]
		self.rect = self.button[0].get_rect(topleft=pos)
		self.cmd = cmd
		self.index = 0
		self.col = False
		self.get_pressed = None

	def run(self,scr,click,s_m_o_f):
		mouse_pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(mouse_pos):
			self.col = True
			self.index = 1
			if click and pygame.mouse.get_pressed()[0]:
				self.cmd()
				s_m_o_f()
				self.get_pressed = True
		else:
			self.index = 0
			self.col = False

		scr.blit(self.button[self.index],self.rect)

	def change_cmd(self,cmd):
		self.cmd = cmd

	def isCollide(self):
		return self.col

	def set_pos(self,pos):
		self.rect = self.button[0].get_rect(topleft=pos)

class T_Button():
	def __init__(self,btn_img,btn_img_hover,pos,cmd,font,text,color1,color2):
		self.button = [btn_img,btn_img_hover]
		self.rect = self.button[0].get_rect(topleft=pos)
		self.cmd = cmd
		self.index = 0
		self.col = False
		self.get_pressed = None
		self.color1 = color1
		self.color2 = color2
		self.font = font
		self.t = text
		self.text = font.render(text, True, self.color1)
		self.text_rect = self.text.get_rect(center = self.rect.center)

	def run(self,scr,click,s_m_o_f):
		mouse_pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(mouse_pos):
			self.col = True
			self.index = 1
			self.text = self.font.render(self.t, True, self.color2)
			if click and pygame.mouse.get_pressed()[0]:
				self.cmd()
				s_m_o_f()
				self.get_pressed = True
		else:
			self.index = 0
			self.col = False
			self.text = self.font.render(self.t, True, self.color1)

		scr.blit(self.button[self.index],self.rect)
		scr.blit(self.text,self.text_rect)

	def change_cmd(self,cmd):
		self.cmd = cmd

	def isCollide(self):
		return self.col

	def set_pos(self,pos):
		self.rect = self.button[0].get_rect(topleft=pos)
		self.text_rect = self.text.get_rect(center = self.rect.center)


def show_label(scr,text,font,color,center_pos):
	img = font.render(text, True, color)
	rect = img.get_rect(center = center_pos)
	scr.blit(img,rect)


mainClock = pygame.time.Clock()
# Pages ===========================================
start_page = True
choose_class_page = False
settings_page = False
info_page = False

l6_page = False
l7_page = False
l8_page = False
l9_page = False



# Definds ==========================================
class bg():
    def __init__(self,img):
        self.img = img
    def change_img(self,img):
        self.img = img
    def get_img(self):
        return self.img

def load_img(path,alpha = False):
    if alpha:
        return pygame.image.load('data/'+path).convert_alpha()
    else:
        return pygame.image.load('data/'+path).convert()

def _startcmd():
    global start_page,choose_class_page
    start_page = not start_page
    choose_class_page = not choose_class_page

def _settingscmd():
    global start_page,settings_page
    start_page = not start_page
    settings_page = not settings_page

def _infocmd():
    global start_page,info_page
    start_page = not start_page
    info_page = not info_page

def l6cmd():
	global choose_class_page,l6_page
	choose_class_page = not choose_class_page
	l6_page = not l6_page

def l7cmd():
	global choose_class_page,l7_page
	choose_class_page = not choose_class_page
	l7_page = not l7_page

def l8cmd():
	global choose_class_page,l8_page
	choose_class_page = not choose_class_page
	l8_page = not l8_page

def l9cmd():
	global choose_class_page,l9_page
	choose_class_page = not choose_class_page
	l9_page = not l9_page
# Varibles =========================================
_background = bg(load_img('backgrounds/start.png'))

start_button = N_Button(load_img('buttons/start.png',alpha=True),load_img('buttons/start1.png',alpha=True),(707,194),_startcmd)


settings_button = N_Button(load_img('buttons/settings.png',alpha=True),load_img('buttons/settings1.png',alpha=True),(689,267),_settingscmd)


info_button = N_Button(load_img('buttons/info.png',alpha=True),load_img('buttons/info1.png',alpha=True),(710,340),_infocmd)

back_button = N_Button(load_img('buttons/back.png',alpha=True),load_img('buttons/back1.png',alpha=True),(0,0),None)


book1_img = pygame.transform.scale(load_img('buttons/book1.png',alpha=True), (120,140))
book1_rect = book1_img.get_rect(topleft = (100,200))

book2_img = pygame.transform.scale(load_img('buttons/book2.png',alpha=True), (120,140))
book2_rect = book1_img.get_rect(topleft = (300,200))

book3_img = pygame.transform.scale(load_img('buttons/book3.png',alpha=True), (120,140))
book3_rect = book1_img.get_rect(topleft = (500,200))

book4_img = pygame.transform.scale(load_img('buttons/book4.png',alpha=True), (120,140))
book4_rect = book1_img.get_rect(topleft = (700,200))


fading_effect = pygame.Surface((200,600))
fading_effect.set_alpha(0)
fading_effect.fill((0,0,0))
alp = 0

font = pygame.font.Font('data/font.ttf',25)
font2 = pygame.font.Font('data/font2.ttf',24)

# POSS
# DS
# 1: (197,130) 2: (357,130)
# 3: (197,190) 4: (357,190)
# 5: (197,250) 6: (357,250)
# 7: (197,310) 8: (357,310)
# HH
# 1: (197,400) 2: (357,400)
# 3: (197,460) 4: (357,460)
#

D1 = T_Button(load_img('buttons/khung.png'),load_img('buttons/khung1.png'),(197,130),lambda: move_to(6,'c1'),font2, 'CHƯƠNG I', (255,106,0),(255,255,255))
D2 = T_Button(load_img('buttons/khung.png'),load_img('buttons/khung1.png'),(357,130),lambda: move_to(6,'c2'),font2, 'CHƯƠNG II', (255,106,0),(255,255,255))
D3 = T_Button(load_img('buttons/khung.png'),load_img('buttons/khung1.png'),(197,190),None,font2, 'CHƯƠNG III', (255,106,0),(255,255,255))
D4 = T_Button(load_img('buttons/khung.png'),load_img('buttons/khung1.png'),(197,400),None,font2, 'CHƯƠNG IV', (255,106,0),(255,255,255))
D5 = T_Button(load_img('buttons/khung.png'),load_img('buttons/khung1.png'),(357,400),None,font2, 'CHƯƠNG V', (255,106,0),(255,255,255))
D6 = T_Button(load_img('buttons/khung.png'),load_img('buttons/khung1.png'),(357,190),None,font2, 'CHƯƠNG VI', (255,106,0),(255,255,255))
D7 = T_Button(load_img('buttons/khung.png'),load_img('buttons/khung1.png'),(197,250),None,font2, 'CHƯƠNG VII', (255,106,0),(255,255,255))
D8 = T_Button(load_img('buttons/khung.png'),load_img('buttons/khung1.png'),(197,460),None,font2, 'CHƯƠNG VIII', (255,106,0),(255,255,255))
D9 = T_Button(load_img('buttons/khung.png'),load_img('buttons/khung1.png'),(357,250),None,font2, 'CHƯƠNG IX', (255,106,0),(255,255,255))
D10 = T_Button(load_img('buttons/khung.png'),load_img('buttons/khung1.png'),(357,370),None,font2, 'CHƯƠNG X', (255,106,0),(255,255,255))







l6_bg = load_img('backgrounds/l6_bg.png')
l7_bg = load_img('backgrounds/l7_bg.png')
l8_bg = load_img('backgrounds/l8_bg.png')
l9_bg = load_img('backgrounds/l9_bg.png')

def move_to(lop,c):
	if lop == 6:
		if c == 'c1':
			show_scroll_image(load_img('tomtat/l6_c1.png'))
		elif c == 'c2':
			show_scroll_image(load_img('tomtat/l6_c2.png'))
		elif c == 'c3':
			pass
		elif c == 'c4':
			pass
		elif c == 'c5':
			pass
		elif c == 'c6':
			pass
		elif c == 'c7':
			pass
		elif c == 'c8':
			pass
		elif c == 'c9':
			pass
	elif lop == 7:
		if c == 'c1':
			pass
		elif c == 'c2':
			pass
		elif c == 'c3':
			pass
		elif c == 'c4':
			pass
		elif c == 'c5':
			pass
		elif c == 'c6':
			pass
		elif c == 'c7':
			pass
		elif c == 'c8':
			pass
		elif c == 'c9':
			pass
		elif c == 'c10':
			pass
	elif lop == 8:
		pass
	elif lop == 9:
		pass

def show_scroll_image(img):
	y = 0
	run = True
	h = img.get_height()
	while run:
		if y>0:
			y = 0
		elif y+h<600:
			y = 600 - h


		screen.fill((255,255,255))
		screen.blit(img,(0,y))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 4:
					y += 40
				elif event.button == 5:
					y -= 40
			if event.type == KEYDOWN:
				if event.key == K_q:
					run = False
					break

		pygame.display.update()
		mainClock.tick(60)

# IDK :) == == == == == == == == == == == == == == ==
click = False
can_c = True
def smof():
    global click
    click = False

init = False
# Main =============================================
while True:
	if pygame.mouse.get_pressed()[0] and can_c:
		click = True
		can_c = False


	if start_page:
		screen.blit(_background.get_img(),(0,0))
		start_button.run(screen,click,smof)
		settings_button.run(screen,click,smof)
		info_button.run(screen,click,smof)


	elif choose_class_page:
		screen.fill((255,255,255))
		back_button.change_cmd(_startcmd)
		back_button.run(screen,click,smof)

		if book1_rect.collidepoint(pygame.mouse.get_pos()):
			alp += 10
			if alp > 120:
				alp = 120
			fading_effect.set_alpha(alp)
			screen.blit(fading_effect,(60,0))
			if click:
				smof()
				l6_page = True
				choose_class_page = False
				init = True
		elif book2_rect.collidepoint(pygame.mouse.get_pos()):
			alp += 10
			if alp > 120:
				alp = 120
			fading_effect.set_alpha(alp)
			screen.blit(fading_effect,(260,0))
			if click:
				smof()
				l7_page = True
				choose_class_page = False
				init = True
		elif book3_rect.collidepoint(pygame.mouse.get_pos()):
			alp += 10
			if alp > 120:
				alp = 120
			fading_effect.set_alpha(alp)
			screen.blit(fading_effect,(460,0))
			if click:
				smof()
				l8_page = True
				choose_class_page = False
				init = True
		elif book4_rect.collidepoint(pygame.mouse.get_pos()):
			alp += 10
			if alp > 120:
				alp = 120
			fading_effect.set_alpha(alp)
			screen.blit(fading_effect,(660,0))
			if click:
				smof()
				l9_page = True
				choose_class_page = False
				init = True
		else:
			alp = 0

		screen.blit(book1_img,book1_rect)
		screen.blit(book2_img,book2_rect)
		screen.blit(book3_img,book3_rect)
		screen.blit(book4_img,book4_rect)

		show_label(screen,'Lớp 6',font,(0,0,0),(170,400))
		show_label(screen,'Lớp 7',font,(0,0,0),(370,400))
		show_label(screen,'Lớp 8',font,(0,0,0),(570,400))
		show_label(screen,'Lớp 9',font,(0,0,0),(770,400))
		show_label(screen,'Chọn khối lớp của bạn',font,(0,0,0),(450,100))
	elif settings_page:
		screen.fill((255,255,255))
		back_button.change_cmd(_settingscmd)
		back_button.run(screen,click,smof)
		show_label(screen,'Ở đây không có cài đặt nào cả :(',font,(0,0,0),(450,300))

	elif info_page:
		screen.fill((255,255,255))
		back_button.change_cmd(_infocmd)
		back_button.run(screen,click,smof)

	# MAIN HOC ===============================================================
	elif l6_page:
		if init:
			back_button.change_cmd(l6cmd)
			D1.set_pos((197,130))
			D2.set_pos((357,130))
			D3.set_pos((197,190))
			D6.set_pos((357,190))
			D7.set_pos((197,250))
			D9.set_pos((357,250))

			D4.set_pos((197,400))
			D5.set_pos((357,400))
			D8.set_pos((197,460))

			init = False

		screen.blit(l6_bg,(0,0))
		back_button.run(screen,click,smof)

		D1.run(screen,click,smof)
		D2.run(screen,click,smof)
		D3.run(screen,click,smof)
		D4.run(screen,click,smof)
		D5.run(screen,click,smof)
		D6.run(screen,click,smof)
		D7.run(screen,click,smof)
		D8.run(screen,click,smof)
		D9.run(screen,click,smof)


	elif l7_page:
		if init:
			back_button.change_cmd(l7cmd)
			D1.set_pos((197,130))
			D2.set_pos((357,130))
			D5.set_pos((197,190))
			D6.set_pos((357,190))
			D7.set_pos((197,250))
			D8.set_pos((357,250))

			D3.set_pos((197,400))
			D4.set_pos((357,400))
			D9.set_pos((197,460))
			D10.set_pos((357,460))

			init = False
		screen.blit(l7_bg,(0,0))
		back_button.run(screen,click,smof)

		D1.run(screen,click,smof)
		D2.run(screen,click,smof)
		D3.run(screen,click,smof)
		D4.run(screen,click,smof)
		D5.run(screen,click,smof)
		D6.run(screen,click,smof)
		D7.run(screen,click,smof)
		D8.run(screen,click,smof)
		D9.run(screen,click,smof)
		D10.run(screen,click,smof)

	elif l8_page:
		screen.blit(l8_bg,(0,0))
		back_button.change_cmd(l8cmd)
		back_button.run(screen,click,smof)

	elif l9_page:
		screen.blit(l9_bg,(0,0))
		back_button.change_cmd(l9cmd)
		back_button.run(screen,click,smof)


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	show_label(screen,'by HN',font,(0,0,0),(50,580))
	if (pygame.mouse.get_pressed()[0] == False) and (can_c == False):
		can_c = True
	pygame.display.update()
	mainClock.tick(60)
