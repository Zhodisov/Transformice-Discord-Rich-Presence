import re

def mi_sa_find_ton_momon(fbr_tonzob: str):
    out_mareine = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    
    with open(fbr_tonzob, 'r', encoding='utf-8') as file:
        lamoukate = file.readlines()
        
        for bour_tonser, tser in enumerate(lamoukate, start=1):
            out_papa = out_mareine.search(tser)
            if out_papa:
                print(f"Ligne {bour_tonser}: {tser.strip()} (IP: {out_papa.group(0)})")

if __name__ == "__main__":
    fbr_tonzob = 'tfd.txt'
    mi_sa_find_ton_momon(fbr_tonzob)