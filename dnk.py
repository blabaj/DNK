# -*- coding: utf-8 -*-
import urllib2
url = 'https://dl.dropboxusercontent.com/u/29645703/SmartNinja/DNK/dna.txt'
odgovor = urllib2.urlopen(url)
zapis = odgovor.read()

#barva las
crna = "CCAGCAATCGC"
rjava = "GCCAGTGCCG"
korencek = "TTAGCTATCGC"
#oblika obraza
kvadraten =  "GCCACGG"
okrogel =  "ACCACAA"
ovalen = "AGGCCTCA"
#barva oci
modraOci = "TTGTGGTGGC"
zelenaOci = "GGGAGGTGGC"
rjavaOci = "AAGTAGTGAC"
#spol
moski = "TGCAGGAACTTC"
zenska = "TGAAGGACCTTC"
#rasa
belec = "AAAACCTCA"
crnec = "CGACTACAG"
azijec = "CGCGGGCCG"

osumljenecNajden = False
print "Osuljenec ima: "
while osumljenecNajden != True:
        preveriBarvoLas = False
        while preveriBarvoLas != True :
                    if zapis.find(crna) != -1:
                        print "Črno barvo las";
                        preveriBarvoLas = True
                        break;
                    elif zapis.find(rjava) != -1:
                        print "Rjavo barvo las";
                        preveriBarvoLas = True
                        break;
                    elif zapis.find(korencek) != -1:
                        print "Korenckasto barvo las";
                        preveriBarvoLas = True
                        break;

        preveriOblikoObraza = False
        while preveriOblikoObraza != True :
                    if zapis.find(kvadraten) != -1:
                        print "Kvadratast obraz";
                        preveriOblikoObraza = True
                        break;
                    elif zapis.find(okrogel) != -1:
                        print "Okrogel obraz";
                        preveriOblikoObraza = True
                        break;
                    elif zapis.find(ovalen) != -1:
                        print "Ovalen obbraz";
                        preveriOblikoObraza = True
                        break;

        preveriBarvoOci = False
        while preveriBarvoOci != True :
                    if zapis.find(modraOci) != -1:
                        print "Modre oci";
                        preveriBarvoOci = True
                        break;
                    elif zapis.find(zelenaOci) != -1:
                        print "Zelene oci";
                        preveriBarvoOci = True
                        break;
                    elif zapis.find(rjavaOci) != -1:
                        print "Rjave oci";
                        preveriBarvoOci = True
                        break;

        preveriSpol = False
        while preveriSpol != True :
                    if zapis.find(moski) != -1:
                        print "Je moški";
                        preveriSpol = True
                        break;
                    elif zapis.find(zenska) != -1:
                        print "Je ženska";
                        preveriSpol = True
                        break;

        preveriRaso = False
        while preveriRaso != True :
                    if zapis.find(belec) != -1:
                        print "Je belec";
                        preveriRaso = True
                        break;
                    elif zapis.find(crnec) != -1:
                        print "Je črnc";
                        preveriRaso = True
                        break;
                    elif zapis.find(azijec) != -1:
                        print "Je azijec";
                        preveriRaso = True
                        break;

        if preveriBarvoLas == True and preveriOblikoObraza == True and preveriBarvoOci == True and preveriSpol == True and preveriRaso == True:
            osumljenecNajden = True
            print "Osuljenec najden!"
        else:
            print "Nekaj se je zalomilo!"
            break