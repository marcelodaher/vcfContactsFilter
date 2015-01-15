#!/usr/bin/python

import sys

contactsFileName = sys.argv[1]
contactsOut = contactsFileName.split(".vcf")[0] + "_telephone.vcf"
f = open(contactsFileName, "r") 
body = f.read()
contacts = body.split("BEGIN:VCARD")
telContacts = []
for contact in contacts:
    if contact.count("\nTEL;"):
        telContacts.append(contact)
outBody = "BEGIN:VCARD" + "BEGIN:VCARD".join(telContacts)
f.close()
g = open(contactsOut, "w")
g.write(outBody)
g.close()
