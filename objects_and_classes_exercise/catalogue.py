class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        filtered = []

        for product_name in self.products:
            if product_name[0] == first_letter:
                filtered.append(product_name)

        return filtered

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:"
        for products in sorted(self.products):
            result += "\n" + products
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
