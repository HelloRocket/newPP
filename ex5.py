name = 'Justin Barrera'
age = 41 #not a lie
height = 63 #inches
weight = 154 #pounds
eyes = 'brown'
teeth = 'white'
hair = 'black'

print ('Let\'s talk about {}'.format (name))
print ("He's {} inches and {} centimeters tall.".format (height, height*2.54))
print ("He's {} pounds and {} kilos heavy.".format (weight, weight*0.453))
print ("actually that's not to heavy.")
print ("He's got {} eyes and {} hair.".format (eyes, hair))
print ("His teeth are usually {} depending on the coffee.".format (teeth))

#This line is tricky
print ("If I add {}, {} and {} I get {}.".format (age, height, weight, age + height + weight))
