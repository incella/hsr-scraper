from playwright.sync_api import sync_playwright
import json
import time

print("Démarrage du script...")

class HSRScraperTypeKafka:
    def __init__(self):
        print("Initialisation du scraper Kafka...")
        self.character_url = "https://www.prydwen.gg/star-rail/characters/kafka"
        self.tierlist_url = "https://www.prydwen.gg/star-rail/tier-list"

    def get_character_info(self) -> dict:
        print("Début de la récupération des infos pour Kafka...")
        with sync_playwright() as p:
            print("Lancement du navigateur...")
            browser = p.chromium.launch(
                headless=True,
                args=['--disable-dev-shm-usage']
            )
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
            page = context.new_page()
            character_data = {}
            
            try:
                # Page du personnage
                print("Chargement de la page du personnage...")
                page.goto(self.character_url, wait_until="domcontentloaded", timeout=90000)
                page.wait_for_selector("h1 strong", timeout=10000)
                time.sleep(2)
                
                # Nom du personnage
                name = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[2]/div[1]/h1/strong').inner_text()
                character_data["name"] = name.strip()
                print(f"Nom trouvé : {name}")

                # Set de reliques recommandé
                relic_set = page.locator('//*[@id="build-tabs-tabpane-0"]/div/div[2]/div[2]/div[1]/div[2]/div/h2/button').get_attribute('alt')
                character_data["best_relic_set"] = relic_set.strip()
                print(f"Set de reliques trouvé : {relic_set}")

                # Stats principales des reliques
                body_stat = page.locator('//*[@id="build-tabs-tabpane-0"]/div/div[3]/div[2]/div[1]/div').get_attribute('alt')
                feet_stat = page.locator('//*[@id="build-tabs-tabpane-0"]/div/div[3]/div[2]/div[2]/div').get_attribute('alt')
                character_data["main_stats"] = {
                    "body": body_stat.strip(),
                    "feet": feet_stat.strip()
                    
                }
                print(f"Stats principales des reliques trouvées : {character_data['main_stats']}")

                # Set d'ornements planétaires
                planar_set = page.locator('//*[@id="build-tabs-tabpane-0"]/div/div[2]/div[3]/div[1]/div[2]/div/h2/button').get_attribute('alt')
                character_data["best_planar_set"] = planar_set.strip()
                print(f"Set d'ornements trouvé : {planar_set}")

                # Stats principales des ornements
                sphere_stat = page.locator('//*[@id="build-tabs-tabpane-0"]/div/div[3]/div[2]/div[3]/div').get_attribute('alt')
                rope_stat = page.locator('//*[@id="build-tabs-tabpane-0"]/div/div[3]/div[2]/div[4]/div').get_attribute('alt')
                character_data["planar_stats"] = {
                    "sphere": "Lightning DMG > ATK%",
                    "rope": rope_stat.strip()
                }
                print(f"Stats principales des ornements trouvées : {character_data['planar_stats']}")

                # Substats prioritaires
                substats = page.locator('//*[@id="build-tabs-tabpane-0"]/div/div[3]/div[3]/div/div').inner_text()
                character_data["priority_substats"] = substats.replace("Substats:", "").strip()
                print(f"Substats prioritaires trouvés : {substats}")

                # Tier
                tier = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[9]/div[8]/div[1]/span/div').inner_text()
                character_data["tier"] = tier.strip()
                print(f"Tier trouvé : {tier}")

                # Page de la tier list pour le rôle
                print("\nChargement de la tier list...")
                page.goto(self.tierlist_url, wait_until="domcontentloaded", timeout=90000)
                time.sleep(5)

                role_xpath = '//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[4]/div[9]/div[1]/div[2]/div[2]'
                role = page.locator(f"xpath={role_xpath}").inner_text()
                if role:
                    character_data["role"] = role.strip()
                    print(f"Rôle trouvé : {role}")
                else:
                    print("Rôle non trouvé")

            except Exception as e:
                print(f"Erreur lors du scraping : {e}")
            finally:
                with open('kafka_data.json', 'w', encoding='utf-8') as f:
                    json.dump(character_data, f, ensure_ascii=False, indent=2)
                browser.close()
                
            return character_data

class HSRScraperTypeBronya:
    def __init__(self):
        self.character_url = "https://www.prydwen.gg/star-rail/characters/bronya"
        self.tierlist_url = "https://www.prydwen.gg/star-rail/tier-list"

    def get_character_info(self) -> dict:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(viewport={'width': 1920, 'height': 1080})
            page = context.new_page()
            character_data = {}
            
            try:
                # Page du personnage
                print("Chargement de la page du personnage...")
                page.goto(self.character_url, wait_until="domcontentloaded", timeout=90000)
                page.wait_for_selector("h1 strong", timeout=10000)
                time.sleep(2)
                
                # Nom du personnage
                name = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[2]/div[1]/h1/strong').inner_text()
                character_data["name"] = name.strip()
                print(f"Nom trouvé : {name}")

                # Set de reliques recommandé
                relic_set = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[10]/div[2]/div[2]/div[2]/div[1]/div[2]/div/h2/button').get_attribute('alt')
                character_data["best_relic_set"] = relic_set.strip()
                print(f"Set de reliques trouvé : {relic_set}")

                # Stats principales des reliques
                body_stat = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[10]/div[2]/div[3]/div[2]/div[1]/div').get_attribute('alt')
                feet_stat = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[10]/div[2]/div[3]/div[2]/div[2]/div').get_attribute('alt')
                character_data["main_stats"] = {
                    "body": body_stat.strip(),
                    "feet": feet_stat.strip()
                }
                print(f"Stats principales des reliques trouvées : {character_data['main_stats']}")

                # Set d'ornements planétaires
                planar_set = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[10]/div[2]/div[2]/div[4]/div[1]/div[2]/div/h2/button').get_attribute('alt')
                character_data["best_planar_set"] = planar_set.strip()
                print(f"Set d'ornements trouvé : {planar_set}")

                # Stats principales des ornements
                sphere_stat = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[10]/div[2]/div[3]/div[2]/div[3]/div').get_attribute('alt')
                rope_stat = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[10]/div[2]/div[3]/div[2]/div[4]/div').get_attribute('alt')
                character_data["planar_stats"] = {
                    "sphere": sphere_stat.strip(),
                    "rope": rope_stat.strip()
                }
                print(f"Stats principales des ornements trouvées : {character_data['planar_stats']}")

                # Substats prioritaires
                substats = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[10]/div[2]/div[3]/div[3]/div/div').inner_text()
                character_data["priority_substats"] = substats.replace("Substats:", "").strip()
                print(f"Substats prioritaires trouvés : {substats}")

                # Tier
                tier = page.locator('//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[9]/div[8]/div[1]/span/div').inner_text()
                character_data["tier"] = tier.strip()
                print(f"Tier trouvé : {tier}")

                # Page de la tier list pour le rôle
                print("\nChargement de la tier list...")
                page.goto(self.tierlist_url, wait_until="domcontentloaded", timeout=90000)
                time.sleep(5)

                role_xpath = '//*[@id="gatsby-focus-wrapper"]/div/div[2]/div[2]/div[4]/div[9]/div[1]/div[2]/div[2]'
                role = page.locator(f"xpath={role_xpath}").inner_text()
                if role:
                    character_data["role"] = role.strip()
                    print(f"Rôle trouvé : {role}")
                else:
                    print("Rôle non trouvé")

            except Exception as e:
                print(f"Erreur lors du scraping : {e}")
            finally:
                with open('bronya_data.json', 'w', encoding='utf-8') as f:
                    json.dump(character_data, f, ensure_ascii=False, indent=2)
                browser.close()
                
            return character_data

if __name__ == "__main__":
    # Test avec Kafka
    print("\nTest du scraper type Kafka...")
    scraper_kafka = HSRScraperTypeKafka()
    data_kafka = scraper_kafka.get_character_info()
    print("\nDonnées Kafka :", json.dumps(data_kafka, indent=2, ensure_ascii=False))
    
    # Test avec Bronya
    print("\nTest du scraper type Bronya...")
    scraper_bronya = HSRScraperTypeBronya()
    data_bronya = scraper_bronya.get_character_info()
    print("\nDonnées Bronya :", json.dumps(data_bronya, indent=2, ensure_ascii=False))