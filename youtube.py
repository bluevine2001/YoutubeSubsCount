from googleapiclient.discovery import build
import time

api_key = '' #entrer votre clé api

youtube = build('youtube','v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername=''#entrer l'username de la chaine youtube
)
response = request.execute()
while 1 : # boucle la requête à l'infinni
    for item in response['items'] :
        sub_num = item['statistics']['subscriberCount']
        print(sub_num, " abonnés") #affiche le nombre d'abonnés
        time.sleep(30) # ajoute un délai de 30 secondes entre chaque requêtes
