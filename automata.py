#el automata acepta cadenas (ab U abb U aba)*
def automata(z):
	x="q_0"
	c="q_0"
	for i in range(0,len(z)):
		if z[i]=="a" or z[i]=="b" or z[i]==" ":
			if x=="q_0":
				if z[i]=="a":
					x="q_1"
					pass
				elif z[i]=="b":
					x="q_e"
					pass
				pass
			elif x=="q_1":
				if z[i]=="a":
					x="q_e"
					pass
				elif z[i]=="b":
					x="q_2"
					pass
				pass
			elif x=="q_2":
				if z[i]=="a":
					x="q_3"
					pass
				elif z[i]=="b":
					x="q_0"
					pass
				pass
			elif x=="q_3":
				if z[i]=="a":
					x="q_1"
					pass
				elif z[i]=="b":
					x="q_2"
					pass
				pass
			pass
		else:
			print("la cadena no es aceptada")
			return	
			pass		
		c+="-->{}".format(x)
		pass
	if x=="q_0" or x=="q_2" or x=="q_3":
		print (c)
		print("la cadena es aceptada")
		pass
	else:
		print("la cadena no es aceptada")
		pass	
	pass
def AFD():
	z=input("Itroduzca la cadena:")
	automata(z)
	x=input()
	pass

AFD()

