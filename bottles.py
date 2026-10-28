def bottle_song():
	for n in range(99, 0, -1):
		if n == 1:
			current = "1 bottle"
		else:
			current = f"{n} bottles"

		if n - 1 == 0:
			next_up = "no more bottles"
		elif n - 1 == 1:
			next_up = "1 bottle"
		else:
			next_up = f"{n - 1} bottles"

		print(f"{current} of beer on the wall, {current} of beer.")
		print(f"Take one down and pass it around, {next_up} of beer on the wall.")

	print("No more bottles of beer on the wall, no more bottles of beer.")
	print("Go to the store and buy some more, 99 bottles of beer on the wall.")

bottle_song()
####kldjsfalkfdajalskdfjdfls