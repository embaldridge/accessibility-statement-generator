"""Script to generate a disability/chronic illness statement."""

print("Please enter True or False for the following statements.")
# Asks questions regarding accomodations to provide inputs to generate accessibility statement.
mobility = input("Physical access is available for mobility impaired. ")
if mobility == True:
    mobility = 'is'
else:
    mobility = 'is not'
    print("Please consider making your events more accessible to mobility impaired colleagues in future.")

hearing = input("Accomodations are available for hearing impaired. ")
if hearing == True:
    hearing = 'are'
else:
    hearing = 'are not'
    print("Please consider making your events more accessible for your hearing impaired colleagues in future.")

vision = input("Accomodations are available for visually impaired. ")
if vision == True:
    vision = 'are'
else:
    vision = 'are not'
    print("Please consider making your events more accessible for your vision impaired colleagues in future.")

remote = input("Remote participation is available for those who cannot otherwise attend. ")
if remote == True:
    remote = 'is'
else:
    remote = 'is not'
    print("Please consider making your events more accessible for your colleagues who cannot otherwise attend in future.")

# Generate accessibility statement.
print("Accessibility Statement")
print("We have made an effort to make our event as accessible to chronic ill or disabled colleagues as possible.  For this event, physical access " + mobility + " available, accomodations for hearing impairments " + hearing + " available, accommodations for visually impaired colleagues " + vision + " available. Additionally, for this event, remote participation " + remote + " possible.  If you need one of the accomodations listed, please contact an organizer, who will make sure that the accomodation(s) you require are fully in place and provide you with complete details about the arrangements.")
    
    
