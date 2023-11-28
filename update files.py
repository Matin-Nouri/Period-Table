from models.Atom import Atom as AtomObject
import requests,pdfkit
from os import system,name
import pandas as pd
import csv

def get_number(x):
    return x[0]

if name=="posix":
    system("cd downloads ; rm -rf *")
else:
    system('Del downloads\\*')
    
path_out = ''

if name=='posix':
    path_out = './downloads/'
else:
    path_out = '.\\downloads\\'

for ui in range(118):
    user_input = ui+1
    try:
        user_input = int(user_input)
    except ValueError:
        user_input = str(user_input[0]).upper() + str(user_input[1:]).lower()



    if user_input is str and user_input.len() > 2:
        print("Symbol should be write correctly!")
        exit()

    if user_input is int and user_input > 118:
        print("Number should be write correctly!")
        exit()

    atom = AtomObject(user_input)
    atom.Get_Data()
    data = atom.Get_Data()
    system(f'mkdir {data["name"]} {data["number"]}')
    system(f'cd {data["name"]} {data["number"]}')
    path_out = f'./downloads/{data["name"]}_{data["number"]}'
    for i in data:
        if i == 'bohr_model_image':
            url = data[i]
            r = requests.get(url, allow_redirects=True)
            path = f'{path_out}{data["name"]}_{data["number"]}.png'
            open(path, 'wb').write(r.content)
            continue
        if i== 'bohr_model_3d':
            continue
        if i == 'image':
            continue

        print(f"{str(i[0]).upper()}{str(i[1:])} : {data[i]}")

    with open(f'{path_out}{data["name"]}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(["Subject", "Value"])
        for i in data:
            if i == 'image':
                continue
            if i == 'electron_configuration':
                sort = data['electron_configuration']
                newsort = sort.split()
                newsort.sort(key=get_number)
                writer.writerow(["Sorted electron configuration", " ".join(newsort)])
            if i == 'source' or i == 'bohr_model_image' or i == 'bohr_model_3d' or i=='spectral_img':
                continue
            writer.writerow([ f"{str(i[0]).upper()}{str(i[1:]).replace('_',' ')}" , data[i]])
        
        file.close()

    df1 = pd.read_csv(f'{path_out}{data["name"]}_{data["number"]}.csv')
    html_string = df1.to_html()
    pdfkit.from_string(html_string, f'{path_out}{data["name"]}_{data["number"]}.pdf')

    url = data['source']
    pdfkit.from_url(url, f'{path_out}{data["name"]}_{data["number"]}_wiki.pdf')

    ul = f'https://images-of-elements.com/{str(data["name"]).lower()}.php'
    pdfkit.from_url(ul, f'{path_out}{data["name"]}_{data["number"]}_element.pdf')
    
    system("cd ..")
