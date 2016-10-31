def apple_and_peanutbutter(apple_count, jars_of_peanutbutter):
    print "You have %d apples!" % apple_count
    print "You have %d jars of peanut butter!" % jars_of_peanutbutter
    print "Man that's enough for a party!"
    print "Get a blanket. \n"


print "We can just give the function numbers directly:"
apple_and_peanutbutter(20, 30)


print "OR, we can use variables from our script:"
amount_of_apples= 10
amount_of_peanuts = 50

apple_and_peanutbutter(amount_of_apples, amount_of_peanuts)


print "We can even do math inside too:"
apple_and_peanutbutter(10 + 20, 5 + 6)

print "And we can combine the two, avriables and math:"
apple_and_peanutbutter(amount_of_apples + 100, amount_of_peanuts + 1000)
