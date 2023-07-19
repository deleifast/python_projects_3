import glob
import xml.etree.ElementTree as ET

filenames = glob.glob("[NFe].XML")  # change the pattern to match your case

for filename in filenames:

    with open(filename, 'r', encoding="utf-8") as content:

        tree = ET.parse(content)

        lst_jugador = tree.findall('data_panel/players/player')

        for jugador in lst_jugador:

            print (jugador.find('name').text, jugador.get("id"))
