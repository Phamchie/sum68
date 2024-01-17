import os
os.system('cls' if os.name == 'nt' else 'clear')
print("Starting App Game")
print("Start XocXoc..")
print("==========================")
import pygame
import random
import time
pygame.init()

screen_x = 750
screen_y = 500
screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption('game bai chien pham - testing game')
banner = pygame.image.load('bg.png').convert_alpha()

mini_game_banner = pygame.image.load('sum.png').convert_alpha()

load_avatar = pygame.image.load('avt1.png').convert_alpha()

# coins 
coin_real = 200000000
# color
WHITE = (255,255,255)
BLACK = (0,0,0,0)
GREY = (150,150,150,150)
YELLOW = (255,255,0)
RED = (255,0,0)

def draw_bg():
	bg_dr = pygame.transform.scale(banner, (screen_x, screen_y))
	screen.blit(bg_dr, (0, 0))
def draw_mini_game():
	mini_game = pygame.transform.scale(mini_game_banner, (740, 470))
	screen.blit(mini_game, (0, 0))

def load_avatars():
	bg_avt = pygame.Rect(0, 0, 165, 55)
	avt = pygame.transform.scale(load_avatar, (50, 50))
	pygame.draw.rect(screen, BLACK, bg_avt)
	screen.blit(avt, (0, 0))

def load_tnv():
	font_tnv = pygame.font.Font(None, 40)
	print_tnv = font_tnv.render("admin", True, WHITE)
	screen.blit(print_tnv, (55, 3))
	def load_coins():
		font_coins = pygame.font.Font(None, 20)
		print_coins = font_coins.render("987,843,000 $", True, YELLOW)
		screen.blit(print_coins, (60, 35))
	load_coins()

# varble font
font_dat_cuoc1 = pygame.font.Font(None, 30)
font_dat_cuoc2 = pygame.font.Font(None, 30)

text_dat_cuoc1 = font_dat_cuoc1.render("dat cuoc", True, BLACK)
text_dat_cuoc2 = font_dat_cuoc2.render("dat cuoc", True, BLACK)

def dat_cuoc():
	font_dat_cuoc3 = pygame.font.Font(None, 36)
	print_dat_cuoc3 = font_dat_cuoc3.render("Dat Cuoc", True, BLACK)
	screen.blit(print_dat_cuoc3, (327, 366))

	def font_all_in():
		font_all_ins = pygame.font.Font(None, 25)
		print_all_in = font_all_ins.render("All In", True, BLACK)
		screen.blit(print_all_in, (200, 380))

	font_all_in()

	def font_huy_cuoc():
		font_huy = pygame.font.Font(None, 25)
		print_huy_cuoc = font_huy.render("Huy", True, BLACK)
		screen.blit(print_huy_cuoc, (525, 380))

	font_huy_cuoc()

def font_tien_cuoc():
	font_1k = pygame.font.Font(None, 25)
	print_1k = font_1k.render("1k", True, BLACK)
	screen.blit(print_1k, (110, 415))

	font_10k = pygame.font.Font(None, 25)
	print_10k = font_10k.render("10k", True, BLACK)
	screen.blit(print_10k, (190, 415))

	font_100k = pygame.font.Font(None, 25)
	print_100k = font_100k.render("100k", True, BLACK)
	screen.blit(print_100k, (275, 415))

	font_1m = pygame.font.Font(None, 25)
	print_1m = font_1m.render("1m", True, BLACK)
	screen.blit(print_1m, (370, 415))

	font_10m = pygame.font.Font(None, 25)
	print_10m = font_10m.render("10m", True, BLACK)
	screen.blit(print_10m, (454, 415))

	font_50m = pygame.font.Font(None, 25)
	print_50m = font_50m.render("50m", True, BLACK)
	screen.blit(print_50m, (543, 415))

	font_100m = pygame.font.Font(None, 25)
	print_100m = font_100m.render("100m", True, BLACK)
	screen.blit(print_100m, (625, 415))

countdown_time = 50
start_time = time.time()
end_time = start_time + countdown_time

so_coins_cuoc = 1
so_coins_cuoc1 = 1

user_list = [
        "hupdiem",
        "thgadngu",
        "netnhusony",
        "aiuxhwbzeu6",
        "eqyntuwuez",
        "uwwynxkwual",
        "_hupdicacem",
        "bunuoclon",
        "hlpnuochau",
        "3consoi",
        "phaidoidoi",
        "nguyenngoc",
        "namden",
        "nguyentien",
        "phonggia",
        "hoangbach",
        "levu01",
        "nguyenbuonhehe",
        "phamgiang2",
        "hoangha06",
        "_nam_con_",
        "hoang_hau",
        "phambao05",
        "huydzdz",
        "abczewi07",
        "allintai",
        "latdonhacai",
        "xiu50m",
        "tai100m",
        "bangkhuang",
        "chenhvenh",
        "cuocsongbonchen",
        "hupcontai",
        "legiahuy2",
        "admindepzaithe",
        "lulzs82",
        "namsicola9",
        "khanhsky",
        "khanhbua01vip",
        "fakerno1",
        "xinnhecaitop",
        "top1vetay",
        "quanp006",
        "xinloca4",
        "TaoLaHuy",
        "haha11",
        "sao22win",
        "done678",
        "ancut123",
        "phchien72",
        "nguyendung4",
        "tranhoanganh",
        "hoangthanh2",
        "tranuquoc08",
        "vip999c",
        "az100c",
        "yb86",
        "thu789",
        "han2003",
        "rlbytinh",
        "huhuhu",
        "ahihi______82729",
        "36pho",
        "vmptd27",
        "393sunwin",
        "sun____winno1",
        "________cu1________",
        "quynhchi1",
        "letai03",
        "leanhtai",
        "xinbinhyen07",
        "luanguku",
        "kunaguero",
        "xin_duoc_nhat",
        "go_lai_tat_ca",
        "golai200m",
        "proooooo22",
        "kkkngao",
        "cuongdieu21",
        "sontran05",
        "____chenh____venh",
        "____bon_____chen_",
        "___cuoc___song31__",
        "__bu_con_tai____",
        "huanrose",
        "khanh_buavip",
        "ditmetaixiu",
        "_lamlaitatca_",
        "lukaku7777",
        "nohukhongtam",
        "ronaldodz38",
        "24quetoi",
        "88quetoi",
        "quenghich555",
        "lucky999999",
        "emba5599",
]

bot_dat_cuoc = [ "TAI", "XIU" ]
bot1 = random.randint(1, 20)
bot2 = random.randint(1, 20)

so_ng_cuoc = []
so_phien = []

times1 = 50

session_game = True
while session_game:

	draw_bg()
	draw_mini_game()
	load_avatars()
	load_tnv()
	dat_cuoc()
	font_tien_cuoc()

	so_phien = f"#23734762"
	font_phien = pygame.font.Font(None, 20)
	text_phien = font_phien.render(str(so_phien), True, BLACK)
	screen.blit(text_phien, (340, 140))

	times1 = times1 - 1
	font_times = pygame.font.Font(None, 120)
	text_times = font_times.render(str(times1), True, YELLOW)
	screen.blit(text_times, (325, 205))

	random_bot1 = random.randint(1, 40)
	bot1 = bot1 + random_bot1
	font_bot1 = pygame.font.Font(None, 15)
	text_bot1 = font_bot1.render(f"{bot1}", True, BLACK)
	screen.blit(text_bot1, (243, 146))

	random_bot2 = random.randint(1, 40)
	bot2 = bot2 + random_bot2
	font_bot2 = pygame.font.Font(None, 15)
	text_bot2 = font_bot2.render(f"{bot2}", True, BLACK)
	screen.blit(text_bot2, (490, 145))
# =====================================================================
# so tien cuoc
	randoms_cuoc = random.randint(1, 35)
	so_coins_cuoc = randoms_cuoc + so_coins_cuoc
	so_xu_tram = random.randint(100, 999)
	duoi_xu = f",{so_xu_tram},000"
	font_fake_cuoc = pygame.font.Font(None, 30)
	print_fake_cuoc = font_fake_cuoc.render(f"{so_coins_cuoc}{duoi_xu}", True, YELLOW)
	screen.blit(print_fake_cuoc, (120, 235))

	randoms_cuoc1 = random.randint(1, 35)
	so_coins_cuoc1 = randoms_cuoc1 + so_coins_cuoc1
	so_xu_tram1 = random.randint(100, 999)
	duoi_xu1 = f",{so_xu_tram1},000"
	font_fake_cuoc1 = pygame.font.Font(None, 30)
	print_fake_cuoc1 = font_fake_cuoc1.render(f"{so_coins_cuoc1}{duoi_xu1}", True, YELLOW)
	screen.blit(print_fake_cuoc1, (505, 235))

	time.sleep(1)

	tnv1 = random.choice(user_list)
	bdc = random.choice(bot_dat_cuoc)
	tien_cuoc = random.randint(1, 20)
	print(f"""
(
	"Username" : "{tnv1}",
	"Cong_dat" : "{bdc}",
	"Tien_Cuoc" : "{tien_cuoc}{duoi_xu}"
)
""")


	screen.blit(text_dat_cuoc1, (135, 265))
	screen.blit(text_dat_cuoc2, (530, 265))

	if times1 == 0:
		times1 = 50
		xn1 = random.randint(1,6)
		xn2 = random.randint(1,6)
		xn3 = random.randint(1,6)
		ket_qua = f"{xn1}-{xn2}-{xn3}"
		tong_diem = int(xn1 + xn2 + xn3)
		tai = [11,12,13,14,15,16,17,18]
		xiu = [3,4,5,6,7,8,9,10]
		font_kq = pygame.font.Font(None, 60)

		if tong_diem in tai:
			print(f"""
	(
		"Ket_QUa": "TAI",
		"Ket_qua_xi_ngau" : "{ket_qua}",
		"Tong_Diem" : "{tong_diem}",
		"So_Nguoi_Cuoc_Tai" : "{bot1}",
		"So_Nguoi_Cuoc_Xiu" : "{bot2}",
		"Tong_Cuoc_Tai" : "{so_coins_cuoc}{duoi_xu}",
		"Tong_Cuoc_Xiu" : "{so_coins_cuoc1}{duoi_xu1}"
	)
	""")
			time.sleep(3)
			text1 = font_kq.render(f"{ket_qua}", True, RED)
			screen.blit(text1, (320, 230))


		if tong_diem in xiu:
			print(f"""
	(
		"Ket_QUa": "XIU",
		"Ket_qua_xi_ngau" : "{ket_qua}",
		"Tong_Diem" : "{tong_diem}",
		"So_Nguoi_Cuoc_Tai" : "{bot1}",
		"So_Nguoi_Cuoc_Xiu" : "{bot2}",
		"Tong_Cuoc_Tai" : "{so_coins_cuoc}{duoi_xu}",
		"Tong_Cuoc_Xiu" : "{so_coins_cuoc1}{duoi_xu1}"
	)
	""")
			time.sleep(3)
			text1 = font_kq.render(f"{ket_qua}", True, RED)
			screen.blit(text1, (320, 230))
			

		bot1 = random.randint(1, 40)
		bot2 = random.randint(1, 40)
		so_coins_cuoc = 1
		so_coins_cuoc1 = 1

		


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			session_game = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if 135 < mouse_pos[0] < 300 and 265 < mouse_pos[1] < 315:
				print("""
{
	"user" : "ADMIN"
	"dat_cuoc" : "TAI"
}
""")

			if 530 < mouse_pos[0] < 605 and 265 < mouse_pos[1] < 315:
				print("""
{
	"user" : "ADMIN"
	"dat_cuoc" : "XIU"
}
""")

	pygame.display.flip()
