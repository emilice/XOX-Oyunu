
#düşünmeden haraket eden ezbere dayalı bir xox oyunu
#makine öğrenmesi kısmında yapay zekalı kodlanacak (yenilemeyen)
oyuntahtasi=['' for x in range(10)]

def ekrandagoster():
    print(' ', oyuntahtasi[1], ' ', '|', ' ', oyuntahtasi[2], ' ', '|', ' ',oyuntahtasi[3])
    print('--------------------')
    print(' ', oyuntahtasi[4], ' ', '|', ' ', oyuntahtasi[5], ' ', '|', ' ',oyuntahtasi[6])
    print('--------------------')
    print(' ', oyuntahtasi[7], ' ', '|', ' ', oyuntahtasi[8], ' ', '|', ' ',oyuntahtasi[9])
    print('--------------------')

def konumaharfkoy(harf, konum):
    oyuntahtasi[konum]=harf
1

def konumbosmu(konum):
    return oyuntahtasi[konum]==' '

def tahtadolu():
    if oyuntahtasi.count(' ')>1:
        return False
    else:
        return True

def kazanan(harf):
    return (oyuntahtasi[1]==harf and oyuntahtasi[2]==harf and oyuntahtasi[3]==harf) or (oyuntahtasi[4]==harf and oyuntahtasi[5]==harf and oyuntahtasi[6]==harf) or (oyuntahtasi[7]==harf and oyuntahtasi[8]==harf and oyuntahtasi[9]==harf) or (oyuntahtasi[1]==harf and oyuntahtasi[4]==harf and oyuntahtasi[7]==harf) or (oyuntahtasi[2]==harf and oyuntahtasi[5]==harf and oyuntahtasi[8]==harf) or (oyuntahtasi[3]==harf and oyuntahtasi[6]==harf and oyuntahtasi[9]==harf) or (oyuntahtasi[1]==harf and oyuntahtasi[5]==harf and oyuntahtasi[9]==harf) or (oyuntahtasi[3]==harf and oyuntahtasi[5]==harf and oyuntahtasi[7]==harf)

while not kazanan('X'): #eğer kazanan yok ise
    konum=int(input('1-9 arasında bir konum giriniz:'))
    konumaharfkoy('X',konum)
    ekrandagoster()

#harfkoy('X',5)
