emergency = input("Is there an emergency? (yes/no): ")

if emergency.lower() == "yes":
    name = input("Enter patient name: ")

    doctor = input("Is a doctor available? (yes/no): ")
    bed = input("Is a bed available? (yes/no): ")

    print("\nPatient Registered:", name)

    if doctor.lower() == "yes" and bed.lower() == "yes":
        print("Immediate Response: Doctor and bed are available.")
        print("Patient can receive emergency treatment.")
    else:
        print("Immediate Response: Required doctor/bed is not available.")

else:
    print("No emergency detected.")