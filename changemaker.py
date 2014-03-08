#maybe mess with numarrays during optimization to see if that makes the program faster.
#for now just a sequence is fine.

class ChangeMaker:
	def change(self,n,coins):
		ways=0
		i=0
		while len(coins)>0:
			coin=coins[0]
			if (n-coin) >0:
				ways+=self.change(n-coin,coins)
			elif (n-coin)==0:
                #				print "leaf! coin is " + str(coin) + " n is " + str(n)
				ways+=1
			coins=coins[1:]
		return ways

a=int(raw_input("what do you want to break?"))
bob = ChangeMaker()
coins = [50,25,10,5,1]
print bob.change(a,coins)