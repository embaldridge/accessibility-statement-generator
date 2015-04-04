#"""Script to generate a disability/chronic illness statement."""
#Contact information for organizer
name = raw_input("Please provide the name of the organizer who will be handling accessibility accommodations. ")
email = raw_input("Please provide an email address for the organizer. ")

print("Please enter True or False for the following statements.")
# Asks questions regarding accomodations to provide inputs to generate accessibility statement.
mobility = raw_input("Physical access is available for mobility impaired. ")
if mobility == True:
    mobility = 'is'
elif mobility == 'true':
    mobility = 'is'
elif mobility == 'T':
    mobility = 'is'
elif mobility == 't':
    mobility = 'is'
elif mobility == 'True':
    mobility = 'is'
else:
    mobility = 'is not'
    print("Please consider making your events more accessible to mobility impaired colleagues in future.")

hearing = raw_input("Accomodations are available for hearing impaired. ")
if hearing == True:
    hearing = 'are'
elif hearing == 'true':
    hearing = 'are'
elif hearing == 'T':
    hearing = 'are'
elif hearing == 't':
    hearing = 'are'
elif hearing == 'True':
    hearing = 'are'
else:
    hearing = 'are not'
    print("Please consider making your events more accessible for your hearing impaired colleagues in future.")

vision = raw_input("Accomodations are available for visually impaired. ")
if vision == True:
    vision = 'are'
elif vision == 'true':
    vision = 'are'
elif vision == 'T':
    vision = 'are'
elif vision == 't':
    vision = 'are'
elif vision == 'True':
    vision = 'are'
else:
    vision = 'are not'
    print("Please consider making your events more accessible for your vision impaired colleagues in future.")

remote = raw_input("Remote participation is available for those who cannot otherwise attend. ")
if remote == True:
    remote = 'is'
elif remote == 'true':
    remote = 'is'
elif remote == 'T':
    remote = 'is'
elif remote == 't':
    remote = 'is'
elif remote == 'True':
    remote = 'is'
else:
    remote = 'is not'
    print("Please consider making your events more accessible for your colleagues who cannot otherwise attend in future.")
    
lactation = raw_input("Lactation facilities are available. ")
if lactation == True:
    lactation = 'are'
elif lactation == 'true':
    lactation = 'are'
elif lactation == 'T':
    lactation = 'are'
elif lactation == 't':
    lactation = 'are'
elif lactation == 'True':
    lactation = 'are'
else:
    lactation = 'are not'
    print("Please consider providing lactation facilities for your colleagues who may require such accomodations.")

# Generate accessibility statement.
print("Accessibility Statement")
print("We have made an effort to make our event as accessible to chronic ill or disabled colleagues as possible.  For this event, physical access " + mobility + " available, accomodations for hearing impairments " + hearing + " available, accommodations for visually impaired colleagues " + vision + " available. Additionally, for this event, remote participation " + remote + " possible.  Lactation facilities " + lactation + " available. If you need one of the accomodations listed, please contact " + name + " (" + email + "), who will make sure that the accomodation(s) you require are fully in place and provide you with complete details about the arrangements.")
    
    
