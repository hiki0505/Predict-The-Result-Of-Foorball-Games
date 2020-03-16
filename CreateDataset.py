from UFAZ.IntDiscProject.scrapers import *

DATA_PATH = 'C:/Users/User/Desktop/Datocki'  # Here write path to save your datasets

scraper = LeagueScraper()
scraper.get_league_positions()
scraper.close_driver()

# scraper = LeaguePositionScraper()
# scraper.run()
# scraper.close_driver()
