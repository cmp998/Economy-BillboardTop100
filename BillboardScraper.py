from lxml import html
import requests

def get_song_data(first_year, last_year):
    f = open("song.tsv","w+")
    f.write("ID" + "\t" + "Year" + "\t" + "Title" + "\t" + "Valence")

    for year in range(first_year,last_year + 1):

        page = requests.get('https://www.billboard.com/charts/year-end/' + str(year) + '/hot-100-songs')
        tree = html.fromstring(page.content)
        incoming_song_titles = tree.xpath('//div[@class="ye-chart-item__title"]/text()')
        
        for i in range(len(incoming_song_titles)):   
            incoming_song_titles[i] = incoming_song_titles[i].strip('\n')

            if incoming_song_titles[i][0] == " ":
                incoming_song_titles[i] = incoming_song_titles[i][1:]

            #print(str(year)+"_"+str(i+1),year,incoming_song_titles[i], year)
            f.write("\n" + str(year)+"_"+str(i+1) + "\t" + str(year) + "\t" + incoming_song_titles[i] + "\t" + "valence-score")

    #print("Imported: ",len(incoming_song_titles), "songs from ", year)

    f.close()
    
get_song_data(2006,2019)

