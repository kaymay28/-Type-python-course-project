raw_names = ["  john smith ", "MARY JONES", "", "  alice brown", "bob wilson  ", "sarah lee"]

clean = []

for name in raw_names:
    name = name.strip()
    if name != "":
        clean.append(name.title())

print(clean)
