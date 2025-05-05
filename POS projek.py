#Hierdie definisie laat die verbruiker toe om hulle eie produkte by te voeg asook die produk se prys
def get_product_details():
    #Die verbruiker gee hier die produk n naam
    product_name = input("Gee die produk naam: ")
    try:
       #Hier kan die prys van die produk in gesleutel word as desimale ook
        product_price = float(input("Gee die produk prys: "))
    #As die verbruiker die letters in plaas van syfers in sleutel verskyn die woorde
    except ValueError:
        print("Ongeldige prys")
        return None, None
    return product_name, product_price

#Wanneer die verbruiker klaar hul produkte op gelaai het, verskyn dit in die definisie wat as menu gemaak is
def display_menu(menu):
    print("\n--- Menu---")
    #Dit verskyn as n bullet point lys a.g.v die kode
    for i, (name, price) in enumerate(menu.items()):
        print(f"{i + 1}. {name}: R{price:.2f}")
    #Die stukkie kode gee die verbruiker die opsie om klaar te wees
    print("0. Klaar")

#Die definisie gee die verbruiker die opsie om dan die produkte wat hulle opgelaai het te bestel
def take_order(menu):
    order_items = []
    while True:
        display_menu(menu)
        try:
           #Hier is die kode sodat die gebruiker die nommer kan intik van die produk wat hulle wil bestel
            choice = int(input("Voer item nommer in om by bestelling te voeg (of 0 om te voltooi): "))
        #die kode verskyn om die verbruiker te help as hulle letters in plaas van nommers ingesleutel het
        except ValueError:
            print("Ongeldige Keuse")
            continue
        #die kode se funksie is dan om te stop wanneer die gebruiker die opsie 'klaar' kies
        if choice == 0:
            break
        #Hierdie groepie kodes laat die loop aanhou en die persoon kan meer as een produk bestel
        if 1 <= choice <= len(menu):
            item_name = list(menu.keys())[choice - 1]
            order_items.append(item_name)
        #Wanneer enige iets anders ingesleutel word behalwe die opsies wat gegee word sal die boodskap verskyn om die verbruiker in kennis te stel
        else:
            print("Ongeldige Keuse")
    return order_items

#die groepie kodes bereken die totaal van al die produkte se pryse wat die verbruiker gekies het
def calculate_total(order_items, menu):
    total = 0
    #Wanneer nuwe produkte ook op die menu bygevoeg word sal die pryse van die produkte registreer en ook by getel word
    for item_name in order_items:
        total += menu[item_name]
    return total

#die definisie laat toe dat die verbruiker kan insleutel met hoeveel hulle gaan betaal bv R200 noot
def process_payment(total):
    while True:
        try:
            payment_amount = float(input(f"Voer betalingsbedrag in: R"))
        #wanneer enige iets behalwe syfers ingesleutel word sal die boodskap verskyn
        except ValueError:
            print("Ongeldige Betalingsbedrag")
            continue
        #die kode vat dan die verbruiker se bedrag en minus die totaal van die produkte om die kleingeld te vertoon
        if payment_amount >= total:
            change = payment_amount - total
            print(f"Betaling suksesvol. Kleingeld: R{change:.2f}")
            break
        #indien die verbruiker minder in die betalingsbedrag insleutel as wat die totaal is dan sal dit aandui die betaling het misluk
        else:
            print("Betaling het misluk")

#die is die hoof kode om die verbruiker in die begin al die verskillende opsies te wys
def main():
    menu = {}
    while True:
        print("\n--- POS Sisteem ---")
        print("1. Voeg produk by Menu")
        print("2. Vat Bestelling")
        print("3. Klaar")
        try:
            #hier kry die verbruiker die geleentheid om hul eerste keuse te maak van wat hulle wil doen
            choice = int(input("Maak Keuse: "))
        #indien n opsie wat nie bestaan nie gekies word sal die boodskap verskyn
        except ValueError:
            print("Ongeldige Keuse")
            continue
        #hierdie if kode vat die verbruiker na die definisie waar hulle die produk se informasie insleutel
        if choice == 1:
            name, price = get_product_details()
            if name and price:
                menu[name] = price
        #indien daar nog niks in die menu is nie sal die boodskap verskyn om dit aan te dui wanneer die persoon iets wil bestel
        elif choice == 2:
            if not menu:
                print("Menu is leeg. Voeg eers produk by die Menu")
                continue
            #as daar wel iets in die menu is sal dit na die definisie gaan om keuses van produkte te kies vir die bestelling
            order = take_order(menu)
            #hierdie kode kry dan die totaal vanaf die verbruiker se keuses en toon dit aan vir die verbruiker
            if order:
                total = calculate_total(order, menu)
                print(f"Bestellings totaal: R{total:.2f}")
                process_payment(total)
        #wanneer die verbruiker dan kies om klaar te wees sal die loop stop en die definisie waar die kleingeld kode is sal verskyn
        elif choice == 3:
            break
        #die kode sal weereens n boodskap verskyn as n ongeldige keuse deur die verbruiker gemaak is
        else:
            print("Ongeldige Keuse")

#die kode dui aan die die hoof definisie nou moet begin sodat die kode kan begin deur hardloop
if __name__ == "__main__":
    main()
