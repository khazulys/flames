import os
from time import sleep

def remove(list1, list2):

	for i in range(len(list1)):
		for j in range(len(list2)):
			if list1[i] == list2[j]:
				c = list1[i]
				list1.remove(c)
				list2.remove(c)
				list3 = list1 + ["*"] + list2
				return [list3, True]

	list3 = list1 + ["*"] + list2
	return [list3, False]

if __name__ == "__main__":
	def main():
		os.system('cls' if os.name=="nt" else "clear")
		print ("\033[1;36m	+-+-+-+-+-+-+-+-+-+-+-+ ")
		print ("\033[1;35m	|F|l|a|m|e|s| |G|a|m|e| ")
		print ("\033[1;36m	+-+-+-+-+-+-+-+-+-+-+-+ ")
		print ("\033[1;33m    Yuks cek status hubungan kalian\n\033[1;32m         [+]\033[1;31mCoded by Khazul\033[1;32m[+]")


		try:
			p1 = input("\n\033[1;31m[-]\033[1;32mNama 1:\033[1;33m ")
			if not p1:
				print ("Harus memasukkan nama")
				exit()
			p1 = p1.lower()
			p1.replace(" ", "")
			p1_list = list(p1)

			p2 = input("\033[1;31m[-]\033[1;32mNama 2:\033[1;33m ")
			if not p2:
				print ("Harus memasukkan nama")
				exit()
			p2 = p2.lower()
			p2.replace(" ", "")
			p2_list = list(p2)

			proses = True
			while proses:
				ret_list = remove(p1_list, p2_list)
				con_list = ret_list[0]
				proses = ret_list[1]
				star_index = con_list.index("*")
				p1_list = con_list[ : star_index]
				p2_list = con_list[star_index + 1 : ]

			count = len(p1_list) + len(p2_list)
			result = ["Teman", "Pecinta", "Penuh kasih", "Pernikahan", "Musuh", "Saudara"]
			while len(result) > 1:
				split_index = (count % len(result) - 1)
				if split_index >= 0:
					right = result[split_index + 1 : ]
					left = result[ : split_index]
					result = right + left
				else:
					result = result[ : len(result) - 1]

			print ("\033[1;31m[√]\033[1;32mStatus Hubungan:\033[1;33m", result[0])
			if "Teman" in result:
				print ("\n\033[1;31m[√]\033[1;32mKalian cocoknya berteman saja")
			elif "Musuh" in result:
				print ("\n\033[1;31m[√]\033[1;32mKalian sangat tidak cocok")
			elif "Pecinta" in result:
				print ("\n\033[1;31m[√]\033[1;32mKalian sangat cocok")
			elif "Penuh kasih" in result:
				print ("\n\033[1;31m[√]\033[1;32mKalian sangat cocok sekali")
			elif "Pernikahan" in result:
				print ("\n\033[1;31m[√]\033[1;32mKalian sangat cocok sekalu")
			elif "Saudara":
				print ("\n\033[1;31m[√]\033[1;32mKalian hanya cocok menjadi saudara")

			while True:
				ul = input("\033[1;31m[?]\033[1;32mMau ulang lagi?(y/n):\033[1;33m ")
				if "y" in ul:
					main()
				elif "n" in ul:
					exit("See you")
				break

		except:
			pass
	main()
