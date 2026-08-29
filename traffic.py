traffic = input("Enter traffic level (low/medium/high): ")
emergency = input("Is there an emergency vehicle? (yes/no): ")

if emergency.lower() == "yes":
    print("Priority given to emergency vehicle.")
    print("Signal changed to GREEN.")

elif traffic.lower() == "high":
    print("High traffic detected.")
    print("Green signal time increased.")

elif traffic.lower() == "medium":
    print("Medium traffic detected.")
    print("Normal signal timing applied.")

else:
    print("Low traffic detected.")
    print("Normal signal timing applied.")