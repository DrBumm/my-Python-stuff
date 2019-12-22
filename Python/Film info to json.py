import json
import time

class movie:
    def __init__(self, title, release_year, actors, age_ratint, duration):
        self.info = {
                     'title': title,
                     'duration': duration,
                     'age_rating': age_rating,
                     'release_year': release_year,
                     'actors': actors
                     }
        json.dump(self.info, open(str(title) + ".JSON",
                                  'w', encoding='UTF-8'), ensure_ascii=False)

# Information input
title = input('Titel: ')
duration = input('Dauer: ')
age_rating = input('Altersfreigabe: ')
release_year = input('Erscheinungsjahr: ')
regie = input('Regie: ')
drehbuch = input('Drehbuch: ')
production = input('Produktion: ')
music = input('Musik: ')
camera = input('Kamera: ')
cut = input('Schnitt: ')

# Put the actors information together
actors = {
          'regie': regie,
          'drehbuch': drehbuch,
          'produktion': production,
          'musik': music,
          'kamera': camera,
          'schnitt': cut
          }

# Create JSON
movie(title, release_year, actors, age_rating, duration)

print('Finished')
print('exiting...')
time.sleep(2)
exit()
