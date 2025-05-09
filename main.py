import requests
from bs4 import BeautifulSoup

r = requests.get('https://game8.co/games/Honkai-Star-Rail/archives/486305')

print(r)

soup = BeautifulSoup(r.content, 'html.parser')


data = []
tables_info = []
count = 0
s = soup.find(id = 'hl_3')
while "hl_4" not in str(next):
    next = s.find_next()
    if "<th>" in str(next):
        tables_info.append(next.get_text())
        print(next)
        count += 1
    else:
        data.append(next.get_text())
    s = next
print(count)
data[:] = [i for i in data if i != '']
data[:] = [i for i in data if '\n' not in i]

return_table = [
    item.replace('\r', '').replace('\n', '')
    for item in tables_info
]

# The plan will be
# - dont clean the data yet when putting it in the list
# - once everything is in the list, sort via <p> <table> and other important tags to know what i'm dealing with
# - format the printing of that data to be more readable as well as have the table data properly layered

#for i in data:
#    if i == 'Support' or i == 'DPS' or i == 'Healer' or i == 'Sustain' or i == 'Tank' or i == 'Flex' or i == 'Shielder' or i == 'Main DPS' or i == 'Sub-DPS':
#        #?
#        idk
    

#print(data)
print(return_table)

#s = soup.find(id = 'hl_3')
#next = s.find_next()
#print(s.get_text())
#print(next.get_text())
#print(next.find_next())