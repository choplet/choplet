tar = int(input()) 
moy = int(input()) 

for i in range(moy*2):
    tar-=1
    moy-=0.5

if tar < 0:
    print("Все тарелки вымыты. Осталось " + str(tar/(-2))+ " ед. моющего средства")
elif tar > 0:
    print("Моющее средство закончилось. Осталось " + str(tar) + " тарелок")
else:
    print ("Все тарелки вымыты, моющее средство закончилось")