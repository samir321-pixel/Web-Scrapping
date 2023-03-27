import csv


class Product:
    def __init__(self, title, brand, mrp, old_price, listing_position):
        self.title = title
        self.brand = brand
        self.mrp = mrp
        self.old_price = old_price
        self.listing_position = int(listing_position)

    def __repr__(self):
        return f"{self.brand} {self.title}"


def load_products():
    with open("croma_products.csv") as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        return [Product(*row) for row in reader]


def search_products(products, search_terms):
    matching_products = [p for p in products if all(term.lower() in p.title.lower() for term in search_terms)]

    by_position = sorted(matching_products, key=lambda p: p.listing_position)[:3]
    by_price_low = sorted(matching_products, key=lambda p: p.old_price)[:3]
    # by_rating_high = sorted(matching_products, key=lambda p: p.rating, reverse=True)[:3]

    return by_position, by_price_low


def exex():
    products = load_products()
    while True:
        search_terms = input("Enter search terms: ").split()
        if not search_terms:
            break
        by_position, by_price_low = search_products(products, search_terms)
        print("Top 3 by position:")
        for p in by_position:
            print(p)

        print("Top 3 by price (low to high):")
        for p in by_price_low:
            print(p)

        # print("Top 3 by rating (high to low):")
        # for p in by_rating_high:
        #     print(p)

        print()


exex()
