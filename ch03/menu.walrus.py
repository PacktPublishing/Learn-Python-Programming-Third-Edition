flavors = ["pistachio", "malaga", "vanilla", "chocolate", "strawberry"]
prompt = "Choose your flavor: "

print(flavors)

while (choice := input(prompt)) not in flavors:
    print(f"Sorry, '{choice}' is not a valid option.")

print(f"You chose '{choice}'.")
