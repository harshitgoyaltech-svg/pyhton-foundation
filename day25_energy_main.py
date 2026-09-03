import day25_energy as energy
print("Welcome to the energy calculation program!")
print("Let's calculate the energy consumed by an electrical device.")
print("Please enter the power and time details:")
calculated_energy = energy.caculate_energy()
print(f"The energy consumed is: {calculated_energy} watt-hours.")