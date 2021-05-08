import random
while True:
	pdf = input("どれか選んでね (R, P, S) 終了するときは(e)")
	tsp = random.choice(["R","P","S"])
	if pdf == tsp:
		print ("あいこ")
	elif (pdf == "R" and tsp == "P") or (pdf == "P" and tsp == "S") or (pdf == "S" and tsp == "R"):
		print("負け")
	elif (pdf == "P" and tsp == "R") or (pdf == "R" and tsp == "S") or (pdf == "S" and tsp == "P"):
		print("勝ち")