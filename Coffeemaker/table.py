from prettytable import PrettyTable

table = PrettyTable()


table.field_names =["Pokemon name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

table.align = "l"

print(table)

table2 = PrettyTable()

table2.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table2.add_column("Type", ["Electric", "Water", "Fire"])

table2.align = "r"
print(table2) 