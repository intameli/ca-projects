"""test"""
print("comp_cost:")
comp_cost = input()
print("income:")
income = input()
print("expenses:")
expenses = input()

weeks = float(comp_cost) / (float(income) - float(expenses))
print("it will take " + str(weeks) + " weeks")
