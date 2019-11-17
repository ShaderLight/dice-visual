from die import Die

def generate_die(die_num):

    die_num = int(die_num)
    dielist=[]
    
    for num in range(1, die_num+1):
        d_value = input("Ściany kości "+str(num)+" ")
        d_value = int(d_value)
        dice = Die(d_value)
        dielist.append(dice)

    return dielist
