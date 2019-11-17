import pygal
from generate_die import generate_die

die_num = input("Ile kości ")

dielist = generate_die(die_num)

roll_num = input("Liczba rzutów ")
roll_num = int(roll_num)

result = 0
results = []
for r in range(roll_num):
    for i in range(1,int(die_num)+1):
        
        result = result + dielist[i-1].roll()
    
    results.append(result)
    result = 0

frequencies = []
max_result = 0
for i in range(1,int(die_num)+1):
        max_result = max_result + dielist[i-1].num_sides


for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()
hist.force_uri_protocol = 'http'
xlabels = []

for p in range(min(results),(max(results))+1):
    str (p)
    xlabels.append(p)

hist.x_labels = xlabels
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"
hist.add('D6 + D6', frequencies)

hist.render_to_file('dice_visual.svg')
