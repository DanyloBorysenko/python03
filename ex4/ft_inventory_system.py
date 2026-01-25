class Category():
    """represents category"""
    def __init__(self, category_name: str):
        self.category_name = category_name


class Item_Type():
    """represents item type"""
    def __init__(self, item_type_name: str, category: Category):
        self.item_type_name = item_type_name
        self.category = category


class Item():
    """represents item"""
    def __init__(self, item_name: str, item_type: Item_Type):
        self.item_name = item_name
        self.item_type = item_type


class Inventory():
    """represents inventory"""
    def __init__(self):
        self.storage: dict[Item_Type, list[Item]] = {}


class Inventory_System_Manager():
    """represents class for managing inventory tasks"""
    def display_basic_analysis(self, inventory: Inventory) -> None:
        print("\n=== Inventory System Analysis ===")
        total: int = 0
        for items in inventory.storage.values():
            total += len(items)
        print(f"Total items in inventory: {total}")
        print(f"Unique item types: {len(inventory.storage.keys())}")

    def display_inventory(self, inventory: Inventory) -> None:
        print("\n=== Current Inventory ===")
        total: int = 0
        for items in inventory.storage.values():
            total += len(items)
        for key, value in inventory.storage.items():
            print(f"{key.item_type_name}: {len(value)} units "
                  f"({len(value) * 100 / total:.1f})%")

    def display_statistics(self, inventory: Inventory) -> None:
        most: list[Item] | None = None
        key_most: Item_Type | None = None
        least: list[Item] | None = None
        key_least: Item_Type | None = None
        for key, value in inventory.storage.items():
            if most is None or len(value) > len(most):
                most = value
                key_most = key
            if least is None or len(value) < len(least):
                least = value
                key_least = key
        print("\n=== Inventory Statistics ===")
        print(f"Most abundant: {key_most.item_type_name} ({len(most)} unit)")
        print(f"Least abundant: {key_least.item_type_name} "
              f"({len(least)} unit)")


if __name__ == "__main__":
    moderate_category = Category("Moderate")
    scarce_category = Category("Scarce:")

    sword_type = Item_Type("sword", scarce_category)
    potion_type = Item_Type("potion", moderate_category)
    shield_type = Item_Type("shield", scarce_category)
    armor_type = Item_Type("armor", scarce_category)
    helmet_type = Item_Type("helmet", scarce_category)

    sword = Item("Long", sword_type)
    helmet = Item("Simple", helmet_type)
    wood_shield = Item("Wood shield", shield_type)
    steel_shield = Item("Steel sheild", shield_type)
    armor = Item("Heavy", armor_type)
    potion = Item("healing potion", potion_type)

    inventory = Inventory()
    inventory.storage.update({sword_type: [sword]})
    inventory.storage.update({
        potion_type: [potion, potion, potion, potion, potion]})
    inventory.storage.update({shield_type: [wood_shield, steel_shield]})
    inventory.storage.update({armor_type: [armor, armor, armor]})
    inventory.storage.update({helmet_type: [helmet]})

    manager = Inventory_System_Manager()
    manager.display_basic_analysis(inventory)
    manager.display_inventory(inventory)
    manager.display_statistics(inventory)
