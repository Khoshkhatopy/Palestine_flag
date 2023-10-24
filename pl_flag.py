
from colorama import Fore,init
init()

cols=90
rows=31
among=rows/2
color=None

for row in range(1,rows+1):
    flag=''
    for col in range(1,cols+1):

        if (row<=among and  col<=row) or (row>=among and col<=among- ( row -among )):
            color=Fore.RED
            flag+=color+'#'

        elif row>=1 and row<=10:
            color=Fore.BLACK
            flag+=color+'#'
        elif row>=11 and row<=20:
            color=Fore.WHITE
            flag+=color+'#'
        elif row>=21 and row<=30:
            color=Fore.GREEN
            flag+=color+'#'

    print(flag)                