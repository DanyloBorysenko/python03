# class Category():
#     """represents category"""
#     def __init__(self, category_name: str):
#         self.category_name = category_name


# class Item_Type():
#     """represents item type"""
#     def __init__(self, item_type_name: str, category: Category):
#         self.item_type_name = item_type_name
#         self.category = category
    
#     def __repr__(self):
#         return f"{self.item_type_name}"


# class Item():
#     """represents item"""
#     def __init__(self, item_name: str, item_type: Item_Type):
#         self.item_name = item_name
#         self.item_type = item_type
    
#     def __repr__(self):
#         return f"{self.item_name}"


# class Inventory():
#     """represents inventory"""
#     def __init__(self):
#         self.storage: dict[Item_Type, list[Item]] = {}


# class Inventory_System_Manager():
#     """represents class for managing inventory tasks"""
#     def display_basic_analysis(self, inventory: Inventory) -> None:
#         print("\n=== Inventory System Analysis ===")
#         total: int = 0
#         for items in inventory.storage.values():
#             total += len(items)
#         print(f"Total items in inventory: {total}")
#         print(f"Unique item types: {len(inventory.storage.keys())}")

#     def display_inventory(self, inventory: Inventory) -> None:
#         print("\n=== Current Inventory ===")
#         total: int = 0
#         for items in inventory.storage.values():
#             total += len(items)
#         for key, value in inventory.storage.items():
#             print(f"{key.item_type_name}: {len(value)} units "
#                   f"({len(value) * 100 / total:.1f})%")

#     def display_statistics(self, inventory: Inventory) -> None:
#         most: list[Item] | None = None
#         key_most: Item_Type | None = None
#         least: list[Item] | None = None
#         key_least: Item_Type | None = None
#         for key, value in inventory.storage.items():
#             if most is None or len(value) > len(most):
#                 most = value
#                 key_most = key
#             if least is None or len(value) < len(least):
#                 least = value
#                 key_least = key
#         print("\n=== Inventory Statistics ===")
#         print(f"Most abundant: {key_most.item_type_name} ({len(most)} unit)")
#         print(f"Least abundant: {key_least.item_type_name} "
#               f"({len(least)} unit)")
        
#     def show_items_by_category(self, inventory: Inventory) -> None:
#         category_inventory: dict[Category, dict[str, int]] = {}
#         for key, value in inventory.storage.items():
#             if key.category not in category_inventory:
#                 category_inventory.update({key.category: {key.item_type_name: len(value)}})
#             else:
#                 category_inventory.get(key.category).update({key.item_type_name: len(value)})
#         print("\n=== Item Categories ===")
#         for key, value in category_inventory.items():
#             print(f"{key.category_name}: {value}")

#     def display_dict_properties(self, inventory: Inventory) -> None:
#         print("\n=== Dictionary Properties Demo ===")
#         print(f"{inventory.storage.keys()}")
#         print(f"{inventory.storage.values()}")
    
#     def simple_look_up(self, item_type: Item_Type, inventory: Inventory) -> None:
#         print(f"Sample lookup - '{item_type.item_type_name}' in inventory: "
#               f"{True if item_type in inventory.storage else False}")

# if __name__ == "__main__":
#     moderate_category = Category("Moderate")
#     scarce_category = Category("Scarce")

#     sword_type = Item_Type("sword", scarce_category)
#     potion_type = Item_Type("potion", moderate_category)
#     shield_type = Item_Type("shield", scarce_category)
#     armor_type = Item_Type("armor", scarce_category)
#     helmet_type = Item_Type("helmet", scarce_category)

#     sword = Item("Long sword", sword_type)
#     helmet = Item("Simple helmet", helmet_type)
#     wood_shield = Item("Wood shield", shield_type)
#     steel_shield = Item("Steel sheild", shield_type)
#     armor = Item("Heavy armor", armor_type)
#     potion = Item("healing potion", potion_type)

#     inventory = Inventory()
#     inventory.storage.update({sword_type: [sword]})
#     inventory.storage.update({
#         potion_type: [potion, potion, potion, potion, potion]})
#     inventory.storage.update({shield_type: [wood_shield, steel_shield]})
#     inventory.storage.update({armor_type: [armor, armor, armor]})
#     inventory.storage.update({helmet_type: [helmet]})

#     manager = Inventory_System_Manager()
#     manager.display_basic_analysis(inventory)
#     manager.display_inventory(inventory)
#     manager.display_statistics(inventory)
#     manager.show_items_by_category(inventory)
#     manager.display_dict_properties(inventory)
#     manager.simple_look_up(sword_type, inventory)

class Inventory_System_Manager():
    """represents class for managing inventory tasks"""
    def display_basic_analysis(self, inventory: dict[str, int]) -> None:
        print("\n=== Inventory System Analysis ===")
        total: int = 0
        for count in inventory.values():
            total += count
        print(f"Total items in inventory: {total}")
        print(f"Unique item types: {len(inventory.keys())}")

    def display_inventory(self, inventory: dict[str, int]) -> None:
        print("\n=== Current Inventory ===")
        total: int = 0
        for count in inventory.values():
            total += count
        for key, value in inventory.items():
            print(f"{key}: {value} units "
                  f"({value * 100 / total:.1f})%")

    def display_statistics(self, inventory: dict[str, int]) -> None:
        key_most: str | None = None
        key_least: str | None = None
        max_value: int | None = None
        min_value: int | None = None
        for key, value in inventory.items():
            if max_value is None or value > max_value:
                max_value = value
                key_most = key
            if min_value is None or value < min_value:
                min_value = value
                key_least = key
        print("\n=== Inventory Statistics ===")
        print(f"Most abundant: {key_most} ({max_value} unit)")
        print(f"Least abundant: {key_least} ({min_value} unit)")
        
    def show_items_by_category(self, inventory: dict[str, dict[str, int]]) -> None:
        print("\n=== Item Categories ===")
        for key, value in inventory.items():
            print(f"{key}: {value}")

    def display_dict_properties(self, inventory: dict[str, int]) -> None:
        print("\n=== Dictionary Properties Demo ===")
        print(f"{inventory.keys()}")
        print(f"{inventory.values()}")
    
    def simple_look_up(self, item_type: str, inventory: dict[str, int]) -> None:
        print(f"Sample lookup - '{item_type}' in inventory: "
              f"{True if item_type in inventory else False}")
        
if __name__ == "__main__":
        manager: Inventory_System_Manager = Inventory_System_Manager()

        inventory: dict[str, int] = {}
        inventory.update({'sword': 1})
        inventory.update({'potion': 5})
        inventory.update({'shield': 2})
        inventory.update({'armor': 3})
        inventory.update({'helmet': 1})
        
        manager.display_basic_analysis(inventory)
        manager.display_inventory(inventory)
        manager.display_statistics(inventory)

        inv_with_categories: dict[str, dict[str, int]] = {}
        inv_with_categories["Moderate"] = {'potion': 5}
        inv_with_categories["Scarce"] = {'sword': 1, 'shield': 2, 'armor': 3, 'helmet': 1}
        
        manager.show_items_by_category(inv_with_categories)
        manager.display_dict_properties(inventory)
        manager.simple_look_up('sword', inventory)