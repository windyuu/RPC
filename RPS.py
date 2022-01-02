import random

weapons = ["R", "P", "S"]

def main():
	pdf = input("どれか選んでね (R: グー, P: パー, S: チョキ) 終了するときは(e): ").upper()
	if pdf == "E":
		print("終了します")
		exit()
	if pdf in weapons:
		tsp = random.choice(weapons)
		if pdf == tsp:
			print ("あいこ")
		elif (pdf == "R" and tsp == "P") or (pdf == "P" and tsp == "S") or (pdf == "S" and tsp == "R"):
			print("負け")
		elif (pdf == "P" and tsp == "R") or (pdf == "R" and tsp == "S") or (pdf == "S" and tsp == "P"):
			print("勝ち")

while True:
	main()
