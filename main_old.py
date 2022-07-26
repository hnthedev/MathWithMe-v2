import pygame,random,time,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption('MathWithMe! v2')
pygame.display.set_icon(pygame.image.load('data/icon.png').convert_alpha())

# Button Classes ==============================================================
class A_Button():
	def __init__(self, button_list,speed,pos,cmd):
		self.button_img = button_list
		self.speed = speed
		self.index = 0
		self.rect = self.button_img[0].get_rect(topleft=pos)
		self.cmd = cmd
		self.collide = False

	def run(self,scr,click,s_m_o_f):
		mouse_pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(mouse_pos):
			self.collide = True
			self.index += self.speed
			if int(self.index) > len(self.button_img)-1:
				self.index = len(self.button_img)-1
			if click and pygame.mouse.get_pressed()[0]:
				self.cmd()
				s_m_o_f()
		elif not self.rect.collidepoint(mouse_pos):
			self.collide = False
			self.index -= self.speed
			if int(self.index) < 0:
				self.index = 0

		scr.blit(self.button_img[int(self.index)],self.rect)

	def set_index(self,index):
		self.index = index

	def get_collide(self):
		return self.collide

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

	def get_collide(self):
		return self.col

	def get_cmd(self):
		return self.cmd

	def get_pressed_now(self):
		return self.get_pressed

	def set_pos(self,pos):
		self.rect = self.button[0].get_rect(topleft=pos)

def show_label(scr,text,font,color,center_pos):
	img = font.render(text, True, color)
	rect = img.get_rect(center = center_pos)
	scr.blit(img,rect)

def show_label_topleft(scr,text,font,color,tl):
	img = font.render(text, True, color)
	rect = img.get_rect(topleft = tl)
	scr.blit(img,rect)

def show_label_tl(scr,texts,font,tl_pos):
	x = tl_pos[0]
	y = tl_pos[1]
	for text in texts:
		if '<!>' in text:
			color = (255,0,0)
		elif '<o>' in text:
			color = (0,255,0)
		elif '<c>' in text:
			color = (255,200,0)
		else:
			color = None
		img = font.render(text, True,(0,0,0),color)
		rect = img.get_rect(topleft = (x,y))
		scr.blit(img,rect)
		y += 25

class T_Button():
	def __init__(self,btn_img,btn_img_hover,pos,varibles_return,font):
		self.button = [btn_img,btn_img_hover]
		self.rect = self.button[0].get_rect(topleft=pos)
		self.index = 0
		self.text = ''
		self.font = font
		self.text_img = font.render(self.text, True ,(0,0,0))
		self.text_rect = self.text_img.get_rect(center = self.rect.center)
		self.varibles_return = varibles_return
		self.can_return = False

	def run(self,scr,click,s_m_o_f):
		mouse_pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(mouse_pos):
			self.index = 1
			self.can_return = False
			if click and pygame.mouse.get_pressed()[0]:
				s_m_o_f()
				self.can_return = True
		else:
			self.index = 0
			self.col = False
			self.can_return = False

		scr.blit(self.button[self.index],self.rect)
		scr.blit(self.text_img,self.text_rect)

	def set_text(self,text):
		self.text = str(text)
		self.text_img = self.font.render(self.text, True ,(0,0,0))
		self.text_rect = self.text_img.get_rect(center = self.rect.center)

	def get_return(self):
		if self.can_return:
			return self.varibles_return
		else:
			return None

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


# Varibles =========================================
_background = bg(load_img('backgrounds/start.png'))
def _startcmd():
    global start_page,choose_class_page
    start_page = not start_page
    choose_class_page = not choose_class_page
start_button = N_Button(load_img('buttons/start.png',alpha=True),load_img('buttons/start1.png',alpha=True),(707,194),_startcmd)

def _settingscmd():
    global start_page,settings_page
    start_page = not start_page
    settings_page = not settings_page
settings_button = N_Button(load_img('buttons/settings.png',alpha=True),load_img('buttons/settings1.png',alpha=True),(689,267),_settingscmd)

def _infocmd():
    global start_page,info_page
    start_page = not start_page
    info_page = not info_page
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

font = pygame.font.Font('data/font.ttf',20)
# IDK :) == == == == == == == == == == == == == == ==
click = False
can_c = True
def smof():
    global click
    click = False
# Main =============================================
while True:
    if pygame.mouse.get_pressed()[0]:
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
        back_button.set_pos((0,0))
        back_button.run(screen,click,smof)

        if book1_rect.collidepoint(pygame.mouse.get_pos()):
            alp += 10
            if alp > 120:
                alp = 120
            fading_effect.set_alpha(alp)
            screen.blit(fading_effect,(60,0))
        elif book2_rect.collidepoint(pygame.mouse.get_pos()):
            alp += 10
            if alp > 120:
                alp = 120
            fading_effect.set_alpha(alp)
            screen.blit(fading_effect,(260,0))
        elif book3_rect.collidepoint(pygame.mouse.get_pos()):
            alp += 10
            if alp > 120:
                alp = 120
            fading_effect.set_alpha(alp)
            screen.blit(fading_effect,(460,0))
        elif book4_rect.collidepoint(pygame.mouse.get_pos()):
            alp += 10
			if alp > 120:
				alp = 120
			fading_effect.set_alpha(alp)
			screen.blit(fading_effect,(660,0))
		else:
			alp = 0

		screen.blit(book1_img,book1_rect)
		screen.blit(book2_img,book2_rect)
		screen.blit(book3_img,book3_rect)
		screen.blit(book4_img,book4_rect)
		print(True)
    elif settings_page:
        screen.fill((255,255,255))
        back_button.change_cmd(_settingscmd)
        back_button.set_pos((0,0))
        back_button.run(screen,click,smof)


    elif info_page:
        screen.fill((255,255,255))
        back_button.change_cmd(_infocmd)
        back_button.set_pos((0,277))
        back_button.run(screen,click,smof)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if (not pygame.mouse.get_pressed()[0]) and (not can_c):
        can_c = True
    pygame.display.update()
    mainClock.tick(60)
