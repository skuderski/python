def calculate_taxes(percentage):
	def taxes(sum_of_money):
		return sum_of_money * percentage / 100
	return taxes

taxes5 = calculate_taxes(5)
taxes10 = calculate_taxes(10)

print(taxes5(1000))
print(taxes10(1000))