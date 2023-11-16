import json
from typing import Tuple
from Models.Batiment import Base, Collecteur, Ressource, Storage

def load_json() -> Base:
        f = open('Data/Batiment.json', "r")
        f2 = open('Data/Upgrade.json', "r")
        data = json.loads(f.read())
        upgrade = json.loads(f2.read())

        base = Base()

        chateau = data['chateau']
        chateau_upgrade = upgrade['chateau']
        cost_data = chateau_upgrade["lvls"]["1"]['cost']
        ressource_data = chateau_upgrade["lvls"]["1"]['storage']
        
        cost = Ressource(cost_data['wheat'], cost_data['wood'], cost_data['stone'], cost_data['gold'])
        ressource = Ressource(ressource_data['wheat'], ressource_data['wood'], ressource_data['stone'], ressource_data['gold'])
        base.chateau = Storage(chateau['name'], chateau['lvl'], cost, ressource)

        collecteur_upgrade = upgrade['collecteurs']
        for collecteur in data['collecteurs']:
            type = collecteur["type"]

            cost_data = collecteur_upgrade[type]["lvls"]["1"]['cost']
            ressource_data = collecteur_upgrade[type]["lvls"]["1"]['ressource']
            cost = Ressource(cost_data['wheat'], cost_data['wood'], cost_data['stone'], cost_data['gold'])
            ressource = Ressource(ressource_data['wheat'], ressource_data['wood'], ressource_data['stone'], ressource_data['gold'])


            base.collecteurs.append(Collecteur(
                collecteur['name'],
                type,
                collecteur['lvl'],
                cost,
                ressource,
                collecteur_upgrade[type]["lvls"]["1"]['timing_max']
            ))

        f.close()
        f2.close()

        return base

def load_upgrade_to(str_ressource, type, lvl) -> Tuple[Ressource, Ressource]:
    
    f2 = open('Data/Upgrade.json', "r")
    upgrade = json.loads(f2.read())

    upgrade_data = upgrade[str_ressource]
    if str_ressource == "chateau":
        cost_data = upgrade_data["lvls"][f'{lvl}']['cost']
        ressource_data = upgrade_data["lvls"][f'{lvl}']['storage']
    else:
        cost_data = upgrade_data[type]["lvls"][f'{lvl}']['cost']
        ressource_data = upgrade_data[type]["lvls"][f'{lvl}']['ressource']

    cost = Ressource(cost_data['wheat'], cost_data['wood'], cost_data['stone'], cost_data['gold'])
    ressource = Ressource(ressource_data['wheat'], ressource_data['wood'], ressource_data['stone'], ressource_data['gold'])

    return cost, ressource

def write_in_log_file(str) -> None:
    f = open('Data/Log.txt', "a")

    f.write(str)

    f.close()