gas_milage   = float(input())
cost_per_gas = float(input())

#calculate for 20 miles
gallons = 20 / gas_milage
cost_20 = gallons * cost_per_gas

#calculate for 75 miles
gallons = 75 / gas_milage
cost_75 = gallons * cost_per_gas

#calculate for 500 miles
gallons = 500 / gas_milage
cost_500 = gallons * cost_per_gas

print(f'{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}')