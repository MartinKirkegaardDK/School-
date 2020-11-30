import math

def calculate_balance(transactions):
	x = 0
	for elm in transactions:
		x = x + elm
	return x

def calculate_compound(account_balance, rate, years):
	return str(round(account_balance * (1+rate) ** years,2))

def filter_withdrawals(transactions):
	li = []
	x = 0
	for elm in transactions:
		if transactions[x] < 0:
			li.append(transactions[x])
			x = x +1
		else:
			x = x +1
	return li


def risk_analysis(transactions):
	li = []
	for elm in transactions:
		li.append(filter_withdrawals(transactions))

	val_max = 0
	for i in li[0]:
		for k in li[0]:
			if val_max > i:
				val_max = k
			else:
				None
	return val_max


def join_records(names, transactions):
	li = []
	for i in range(0,len(names)):
		li.append((names[i], transactions[i]))	
	return li

def unique_deposit_names(joined_transactions):
	li = []
	for elm in joined_transactions:
		if (str(elm[0][0]).isupper()) == True:
			None
		else:
			li.append(elm)
	new = []
	for elm in li:
		if elm[1] < 0:
			None
		else:
			new.append(elm[0])
	return new


def main():
	#calculate balance example
	transactions = [100 , 5000 , -30, -1200]
	balance = calculate_balance(transactions)
	print(balance) #Expected output: 3870

	#calculate compound example
	compound_balance = calculate_compound(500 , 0.05 , 25)
	print(compound_balance) #Expected outuput: 1693.17[...]

	#filter withdrawals example
	withdrawals = filter_withdrawals(transactions)
	print(withdrawals) #Expected outuput: [-30, -1200]

	#risk analysis example 
	transactions = [-5000, 200, 120, -99999] 
	risk = risk_analysis(transactions)
	print(risk)#Expected outuput: -99999

	#join records example
	names = ['Muhammed', 'emma', 'Emma', 'julie']
	joined_transactions = join_records(names, transactions)
	print(joined_transactions)#Expected outuput: [( ’Muhammed’ , −5000), ( ’emma’ , 200), ( ’Emma’ , 120), ( ’ julie ’ , −99999)]

	#unique deposit names example
	unique_names = unique_deposit_names(joined_transactions)
	print(unique_names) #Expected outuput: ['emma']


if __name__ == "__main__":
	# execute only if run as a script
	main()
	#Expected output:
	#3870
	#1693.17[...]
	#-99999
	#[( ’Muhammed’ , −5000), ( ’emma’ , 200), ( ’Emma’ , 120), ( ’ julie ’ , −99999)]
	#['emma']

