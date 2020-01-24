Algoritmo Tablademultiplicar
	Mientras num<=0 O num>12 Hacer
		num <- 1
		Escribir 'Inserte un numero del 1 al 12 que desee'
		Leer num
		Si num<=0 Entonces
			Escribir 'Error el valor debe ser mayor que 0 y menor que 12'
		SiNo
			Si num>12 Entonces
				Escribir 'Error el valor debe ser mayor que 12'
			FinSi
		FinSi
	FinMientras
	Inferior <- 1
	Maximo <- 12
	Mientras Inferior<=Maximo Hacer
		Escribir num,'*',Inferior,'=',num*Inferior
		Inferior <- Inferior+1
	FinMientras
	Escribir num * 78
FinAlgoritmo
