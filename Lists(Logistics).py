routes = ["Nairobi-Mombasa","Nakuru-Eldoret","Kisumu-Kakamega","Thika-Kiambu",
          "Kitale-Embu","Meru-Nanyuki","Kajiado-Narok","Migori-Homa Bay",
          "Kilifi-Malindi","Lamu-Tana River"]
routes.append("Nanyuki-Meru")
routes.remove("Kisumu-Kakamega")
routes.sort()
routes.reverse()
count_start_N = sum(1 for r in routes if r.startswith("N"))
long_routes = [r for r in routes if len(r) > 10]
