#ввод точки а

xa = int(input())
ya = int(input())

#ввод точки b

xb = int(input())
yb = int(input())

#ввод точки c

xc = int(input())
yc = int(input())

#первичная проверка на прямоугольность
if xa == xb and yb == yc or xb == xc and yc == ya or xc == xa or ya == yb or xb == xa and ya == yc or xa == xc and yc == yb or xc == xb or yb == ya:
	print("yes") 

else:
	xxa = xa
	yya = ya                        
	xxb = xb - (xb - xa) 
	yyb = yb 
	xxc = xc 
	yyc = yc - (xb - xa)

	if xxa == xxb and yyb == yyc or xxb == xxc and yyc == yya or xxc == xxa or yya == yyb or xxb == xxa and yya == yyc or xxa == xxc and yyc == yyb or xxc == xb or yyb == yya:
		print("yes") 
	else:
		print("no")



