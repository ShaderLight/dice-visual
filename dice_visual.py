import pygal
from generate_die import generate_die
from messages import Msg

language = input("Select your language (EN/PL)\nWybierz język (EN/PL)")
msg = Msg(language)

die_num = input(msg.msg_1)

dielist = generate_die(die_num, msg.msg_3)

roll_num = input(msg.msg_2)
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
hist.x_title = msg.msg_4
hist.y_title = msg.msg_5
hist.add("", frequencies)

hist.render_to_file('dice_visual.svg')
