import pygal

from die import Die

die_num = input("Ile kości ")
die_num = int(die_num)

dielist = []
for num in range(1,die_num+1):
    d_value = input("Ściany kości "+str(num)+" ")
    d_value = int(d_value)
    dice = Die(d_value)
    dielist.append(dice)

print (dielist)
results = []
roll_num = input("Liczba rzutów ")
roll_num = int(roll_num)

result = 0
for r in range(roll_num):
    for i in range(1,die_num+1):
        
        result = result + dielist[i-1].roll()
    
    results.append(result)
    result = 0

frequencies = []
max_result = 0
for i in range(1,die_num+1):
        max_result = max_result + dielist[i-1].num_sides


print(max_result)
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()
hist.force_uri_protocol = 'http'
xlabels = []
for p in range(min(results),(max(results))+1):
    str (p)
    xlabels.append(p)


print(xlabels)

hist.x_labels = xlabels
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
