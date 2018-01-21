import requests
import re
from bs4 import BeautifulSoup

website_url = 'http://www.espncricinfo.com'
url = website_url + '/story/_/id/18791072/all-cricket-teams-index'

page = requests.get(url)

if page.status_code == 200:

    soup = BeautifulSoup(page.content, 'html.parser')
    
    links = soup.find_all(href=re.compile(r'/team/_/id'))
    urls = []
    
    for link in links:
        if link['href'].startswith('/'):
            urls.append(website_url + link['href'])
        else:
            urls.append(link['href'])
    
    for link in urls:
        
        page = requests.get(link)
        
        if page.status_code == 200:
            soup = BeautifulSoup(page.content, 'html.parser')
            
            links = soup.find_all(href=re.compile(r'/content/player/country'))
        
            if len(links) == 1:
                players_page = requests.get(links[0]['href'])
                
                if players_page.status_code == 200:
                    players_soup = BeautifulSoup(players_page.content, 'html.parser')
                
                    players_links = players_soup.find_all(href=re.compile('alpha='))
                
                    players_links_full = []
                    
                    for players_link in players_links:
                        players_links_full.append(website_url + players_link['href'])
                        
                    for players_link_full in players_links_full:
                        
                        players_alpha_page = requests.get(players_link_full)
                        
                        if players_alpha_page.status_code == 200:
                            players_alpha_soup = BeautifulSoup(players_alpha_page.content, 'html.parser')
                            
                            indv_links = players_alpha_soup.find_all('a', { 'class': 'ColumnistSmry' })
                            
                            indv_urls = []
                            for indv_link in indv_links:
                                indv_urls.append(website_url + indv_link['href'])
                                
                            for indv_url in indv_urls:
                                indv_page = requests.get(indv_url)
                                
                                if indv_page.status_code == 200:
                                    indv_soup = BeautifulSoup(indv_page.content, 'html.parser')
                                    
                                    player_infos = indv_soup.find_all('p', {'class': 'ciPlayerinformationtxt'})
                                    
                                    for player_info in player_infos:
                                        
                                        print(player_info)
                                        
                                        player_info_attr = player_info.b
                                        player_info_val = player_info.span
                                        
                                        f = open('data.txt', 'a')
                                        f.write(player_info_attr.text.replace('\n', '') + '=' + player_info_val.text.replace('\n', '') + '\n')
                                        f.close()
                                        
                                else:
                                    print('Error connecting to ' + indv_url)
                                
                                input()
                        else:
                            print('Error connecting to ' + players_link_full)
                else:
                    print('Error connecting to ' + links[0]['href'])
            else:
                print('Received multiple players links, was expecting just one' + links)
        else:
            print('Error connecting to' + link)
        
else:
    print('Error connecting to ' + url)