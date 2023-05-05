dias = input()
dias = dias.split(' ')
dia1 = int(dias[0])
dia2 = int(dias[1])
dia3 = int(dias[2])

if (dia1 > dia2 and dia2 <= dia3):
    print(':)')
elif (dia1 < dia2 and dia2 >= dia3):
    print(':(')
elif (dia1 < dia2 and dia2 < dia3 and (dia3 - dia2) < (dia2 - dia1)):
    print(':(')
elif (dia1 < dia2 and dia2 < dia3 and (dia3 - dia2) >= (dia2 - dia1)):
    print(':)')
elif (dia1 > dia2 and dia2 > dia3 and (dia3 - dia2) > (dia2 - dia1)):
    print(":)")
elif (dia1 > dia2 and dia2 > dia3 and (dia2 - dia3) >= (dia1 - dia2)):
    print(":(")
elif (dia1 == dia2):
    if (dia2 < dia3):
        print(":)")
    else:
        print(":(")