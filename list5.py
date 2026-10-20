contacts = [
    ["Renu", "9876543210"],
    ["Sita", "9876501234"],
    ["Anjali", "9123456780"]
]
search_name = "Sita"
found = False
for contact in contacts:
    if contact[0].lower() == search_name.lower():
        print("Name:", contact[0])
        print("Phone:", contact[1])
        found = True
        break
if not found:
    print("Contact Not Found")
