import xml.etree.ElementTree as ET


def parseCandidates():
    tree = ET.parse('candidates_all.xml')
    root = tree.getroot()

    outputfile = open("candidateTable.csv", "w")
    outputfile.write(
        "Candidate_ID,First_Name,Mid_Name,Last_Name,Street,Zipcode,Party,Local_PosID,State_PosID,National_PosID\n")

    canID = 0
    line = [0, 0, 0, 0, 0, 0, 0]

    for pos in root:
        if pos.tag == "MAYOR":
            stateID = 0
            natID = 0
            for city in pos:
                # print(city.attrib['VALUE'])
                if city.attrib['VALUE'] == "State College":
                    for can in city:
                        line = [0, 0, 0, 0, 0, 0, 0]
                        canID += 1
                        outputfile.write(str(canID) + ',')
                        # outputfile.write("\n")
                        for attrib in can:
                            if attrib.tag == "PARTY":
                                line[5] = attrib.text
                            if attrib.tag == "FNAME":
                                line[0] = attrib.text
                            if attrib.tag == "MNAME":
                                line[1] = attrib.text
                            if attrib.tag == "LNAME":
                                line[2] = attrib.text
                            if attrib.tag == "ADDRESS":
                                line[3] = attrib.text
                            if attrib.tag == "ZIP":
                                line[4] = attrib.text
                            line[6] = 1
                        outputfile.write(
                            line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                                5] + ',' + str(line[6]) + ',' + str(stateID) + ',' + str(natID))
                        outputfile.write("\n")
                if city.attrib['VALUE'] == "Pine Grove Mills":
                    for can in city:
                        line = [0, 0, 0, 0, 0, 0, 0]
                        canID += 1
                        outputfile.write(str(canID) + ',')
                        # outputfile.write("\n")
                        for attrib in can:
                            if attrib.tag == "PARTY":
                                line[5] = attrib.text
                            if attrib.tag == "FNAME":
                                line[0] = attrib.text
                            if attrib.tag == "MNAME":
                                line[1] = attrib.text
                            if attrib.tag == "LNAME":
                                line[2] = attrib.text
                            if attrib.tag == "ADDRESS":
                                line[3] = attrib.text
                            if attrib.tag == "ZIP":
                                line[4] = attrib.text
                            line[6] = 2
                        outputfile.write(
                            line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                                5] + ',' + str(line[6]) + ',' + str(stateID) + ',' + str(natID))
                        outputfile.write("\n")
                if city.attrib['VALUE'] == "Boalsburg":
                    for can in city:
                        line = [0, 0, 0, 0, 0, 0, 0]
                        canID += 1
                        outputfile.write(str(canID) + ',')
                        # outputfile.write("\n")
                        for attrib in can:
                            if attrib.tag == "PARTY":
                                line[5] = attrib.text
                            if attrib.tag == "FNAME":
                                line[0] = attrib.text
                            if attrib.tag == "MNAME":
                                line[1] = attrib.text
                            if attrib.tag == "LNAME":
                                line[2] = attrib.text
                            if attrib.tag == "ADDRESS":
                                line[3] = attrib.text
                            if attrib.tag == "ZIP":
                                line[4] = attrib.text
                            line[6] = 4
                        outputfile.write(
                            line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                                5] + ',' + str(line[6]) + ',' + str(stateID) + ',' + str(natID))
                        outputfile.write("\n")
                if city.attrib['VALUE'] == "Port Matilda":
                    for can in city:
                        line = [0, 0, 0, 0, 0, 0, 0]
                        canID += 1
                        outputfile.write(str(canID) + ',')
                        # outputfile.write("\n")
                        for attrib in can:
                            if attrib.tag == "PARTY":
                                line[5] = attrib.text
                            if attrib.tag == "FNAME":
                                line[0] = attrib.text
                            if attrib.tag == "MNAME":
                                line[1] = attrib.text
                            if attrib.tag == "LNAME":
                                line[2] = attrib.text
                            if attrib.tag == "ADDRESS":
                                line[3] = attrib.text
                            if attrib.tag == "ZIP":
                                line[4] = attrib.text
                            line[6] = 3
                        outputfile.write(
                            line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                                5] + ',' + str(line[6]) + ',' + str(stateID) + ',' + str(natID))
                        outputfile.write("\n")
                if city.attrib['VALUE'] == "Tyrone":
                    for can in city:
                        line = [0, 0, 0, 0, 0, 0, 0]
                        canID += 1
                        outputfile.write(str(canID) + ',')
                        # outputfile.write("\n")
                        for attrib in can:
                            if attrib.tag == "PARTY":
                                line[5] = attrib.text
                            if attrib.tag == "FNAME":
                                line[0] = attrib.text
                            if attrib.tag == "MNAME":
                                line[1] = attrib.text
                            if attrib.tag == "LNAME":
                                line[2] = attrib.text
                            if attrib.tag == "ADDRESS":
                                line[3] = attrib.text
                            if attrib.tag == "ZIP":
                                line[4] = attrib.text
                            line[6] = 5
                        outputfile.write(
                            line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                                5] + ',' + str(line[6]) + ',' + str(stateID) + ',' + str(natID))
                        outputfile.write("\n")
                if city.attrib['VALUE'] == "Altoona":
                    for can in city:
                        line = [0, 0, 0, 0, 0, 0, 0]
                        canID += 1
                        outputfile.write(str(canID) + ',')
                        # outputfile.write("\n")
                        for attrib in can:
                            if attrib.tag == "PARTY":
                                line[5] = attrib.text
                            if attrib.tag == "FNAME":
                                line[0] = attrib.text
                            if attrib.tag == "MNAME":
                                line[1] = attrib.text
                            if attrib.tag == "LNAME":
                                line[2] = attrib.text
                            if attrib.tag == "ADDRESS":
                                line[3] = attrib.text
                            if attrib.tag == "ZIP":
                                line[4] = attrib.text
                            line[6] = 6
                        outputfile.write(
                            line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                                5] + ',' + str(line[6]) + ',' + str(stateID) + ',' + str(natID))
                        outputfile.write("\n")
                if city.attrib['VALUE'] == "Bellwood":
                    for can in city:
                        line = [0, 0, 0, 0, 0, 0, 0]
                        canID += 1
                        outputfile.write(str(canID) + ',')
                        # outputfile.write("\n")
                        for attrib in can:
                            if attrib.tag == "PARTY":
                                line[5] = attrib.text
                            if attrib.tag == "FNAME":
                                line[0] = attrib.text
                            if attrib.tag == "MNAME":
                                line[1] = attrib.text
                            if attrib.tag == "LNAME":
                                line[2] = attrib.text
                            if attrib.tag == "ADDRESS":
                                line[3] = attrib.text
                            if attrib.tag == "ZIP":
                                line[4] = attrib.text
                            line[6] = 7
                        outputfile.write(
                            line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                                5] + ',' + str(line[6]) + ',' + str(stateID) + ',' + str(natID))
                        outputfile.write("\n")
        if pos.tag == "PRESIDENT":
            localID = 0
            stateID = 0
            for can in pos:
                canID += 1
                line = [0, 0, 0, 0, 0, 0, 0]
                outputfile.write(str(canID) + ',')
                for attrib in can:
                    if attrib.tag == "PARTY":
                        line[5] = attrib.text
                    if attrib.tag == "FNAME":
                        line[0] = attrib.text
                    if attrib.tag == "MNAME":
                        line[1] = attrib.text
                    if attrib.tag == "LNAME":
                        line[2] = attrib.text
                    if attrib.tag == "ADDRESS":
                        line[3] = attrib.text
                    if attrib.tag == "ZIP":
                        line[4] = attrib.text
                    line[6] = 1
                outputfile.write(
                    line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                        5] + ',' + str(localID) + ',' + str(stateID) + ',' + str(line[6]))
                outputfile.write("\n")
        if pos.tag == "GOVERNOR":
            localID = 0
            natID = 0
            for can in pos:
                canID += 1
                line = [0, 0, 0, 0, 0, 0, 0]
                outputfile.write(str(canID) + ',')
                for attrib in can:
                    if attrib.tag == "PARTY":
                        line[5] = attrib.text
                    if attrib.tag == "FNAME":
                        line[0] = attrib.text
                    if attrib.tag == "MNAME":
                        line[1] = attrib.text
                    if attrib.tag == "LNAME":
                        line[2] = attrib.text
                    if attrib.tag == "ADDRESS":
                        line[3] = attrib.text
                    if attrib.tag == "ZIP":
                        line[4] = attrib.text
                    line[6] = 1
                outputfile.write(
                    line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                        5] + ',' + str(localID) + ',' + str(line[6]) + ',' + str(natID))
                outputfile.write("\n")
        if pos.tag == "SENATE":
            localID = 0
            stateID = 0
            for can in pos:
                canID += 1
                line = [0, 0, 0, 0, 0, 0, 0]
                outputfile.write(str(canID) + ',')
                for attrib in can:
                    if attrib.tag == "PARTY":
                        line[5] = attrib.text
                    if attrib.tag == "FNAME":
                        line[0] = attrib.text
                    if attrib.tag == "MNAME":
                        line[1] = attrib.text
                    if attrib.tag == "LNAME":
                        line[2] = attrib.text
                    if attrib.tag == "ADDRESS":
                        line[3] = attrib.text
                    if attrib.tag == "ZIP":
                        line[4] = attrib.text
                    line[6] = 2
                outputfile.write(
                    line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                        5] + ',' + str(localID) + ',' + str(stateID) + ',' + str(line[6]))
                outputfile.write("\n")
        if pos.tag == "STATEHOUSE":
            localID = 0
            natID = 0
            for dis in pos:
                if dis.attrib['district'] == '77':
                    for can in dis:
                        canID += 1
                        line = [0, 0, 0, 0, 0, 0, 0]
                        outputfile.write(str(canID) + ',')
                        for attrib in can:
                            if attrib.tag == "PARTY":
                                line[5] = attrib.text
                            if attrib.tag == "FNAME":
                                line[0] = attrib.text
                            if attrib.tag == "MNAME":
                                line[1] = attrib.text
                            if attrib.tag == "LNAME":
                                line[2] = attrib.text
                            if attrib.tag == "ADDRESS":
                                line[3] = attrib.text
                            if attrib.tag == "ZIP":
                                line[4] = attrib.text
                            line[6] = 2
                        outputfile.write(
                            line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                                5] + ',' + str(localID) + ',' + str(line[6]) + ',' + str(natID))
                        outputfile.write("\n")
                if dis.attrib['district'] == '81':
                    for can in dis:
                        canID += 1
                        line = [0, 0, 0, 0, 0, 0, 0]
                        outputfile.write(str(canID) + ',')
                        for attrib in can:
                            if attrib.tag == "PARTY":
                                line[5] = attrib.text
                            if attrib.tag == "FNAME":
                                line[0] = attrib.text
                            if attrib.tag == "MNAME":
                                line[1] = attrib.text
                            if attrib.tag == "LNAME":
                                line[2] = attrib.text
                            if attrib.tag == "ADDRESS":
                                line[3] = attrib.text
                            if attrib.tag == "ZIP":
                                line[4] = attrib.text
                            line[6] = 3
                        outputfile.write(
                            line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                                5] + ',' + str(localID) + ',' + str(line[6]) + ',' + str(natID))
                        outputfile.write("\n")
                if dis.attrib['district'] == '79':
                    for can in dis:
                        canID += 1
                        line = [0, 0, 0, 0, 0, 0, 0]
                        outputfile.write(str(canID) + ',')
                        for attrib in can:
                            if attrib.tag == "PARTY":
                                line[5] = attrib.text
                            if attrib.tag == "FNAME":
                                line[0] = attrib.text
                            if attrib.tag == "MNAME":
                                line[1] = attrib.text
                            if attrib.tag == "LNAME":
                                line[2] = attrib.text
                            if attrib.tag == "ADDRESS":
                                line[3] = attrib.text
                            if attrib.tag == "ZIP":
                                line[4] = attrib.text
                            line[6] = 4
                        outputfile.write(
                            line[0] + ',' + line[1] + ',' + line[2] + ',' + line[3] + ',' + line[4] + ',' + line[
                                5] + ',' + str(localID) + ',' + str(line[6]) + ',' + str(natID))
                        outputfile.write("\n")

    outputfile.close()


def parseVoters():
    tree = ET.parse("registeredvoters.xml")
    root = tree.getroot()

    outputfile = open("voterTable.csv", "w")
    outputfile.write("Voter_ID,First_Name,Mid_Name,Last_Name,Street,Zipcode,Party,Registered")
    outputfile.write('\n')

    voterID = 0

    for child in root:
        voterID += 1
        outputfile.write(str(voterID) + ',')
        for info in child:
            outputfile.write(str(info.text) + ',')
        outputfile.write("TRUE")
        outputfile.write('\n')

    outputfile.close()


def parseZipcodes():
    inputfile = open("districts_by_zip.csv", "r")
    outputfile = open("zipcodeTable.csv", "w")

    line1 = inputfile.readline()
    line2 = inputfile.readline()
    line3 = inputfile.readline()
    line4 = inputfile.readline()

    line1_list = line1.split(',')
    line2_list = line2.split(',')
    line3_list = line3.split(',')
    line4_list = line4.split(',')

    outputfile.write("Zipcode,City,State_Name,Congressional_Districts\n")
    for elem in range(len(line1_list)):
        if elem == len(line1_list) - 1:
            line1_list[elem] = line1_list[elem][:-1]
            line2_list[elem] = line2_list[elem][:-1]
            line3_list[elem] = line3_list[elem][:-1]
            line4_list[elem] = line4_list[elem][:-1]
        outputfile.write(line1_list[elem] + ',')
        outputfile.write(line2_list[elem] + ',')
        outputfile.write(line3_list[elem] + ',')
        outputfile.write(line4_list[elem])
        outputfile.write('\n')

    inputfile.close()
    outputfile.close()


def parseVotes():
    tree = ET.parse("votes.xml")
    root = tree.getroot()

    voterTable = open("voterTable.csv", "r")
    candTable = open("candidateTable.csv", "r")
    outputfile = open("voteTable.csv", "w")
    outputfile.write("Vote_ID,Voter_ID,Candidate_ID,Title\n")

    line = []
    count = 1
    voteID = 0
    voterID = 0

    for voter in root:
        for elem in voter:
            line.append(elem.text)
        voterTable.seek(0)
        voterTable.readline()
        for voterLine in voterTable:
            voterline = voterLine.split(',')
            if line[0] == voterline[1] and line[1] == voterline[2] and line[2] == voterline[3] and line[3] == voterline[
                4] and line[4] == voterline[5] and line[5] == voterline[6]:
                for elem in voter:
                    if elem.tag == 'VOTES':
                        for vote in elem:
                            x = vote.text.split('~')
                            candTable.seek(0)
                            candTable.readline()
                            for cand in candTable:
                                candline = cand.split(',')
                                if x[0] == candline[1] and x[1] == candline[2] and x[2] == candline[3] and x[3] == \
                                        candline[
                                            4] and x[4] == candline[5]:
                                    voteID += 1
                                    outputfile.write(
                                        str(voteID) + ',' + str(voterline[0]) + ',' + candline[0] + ',' + str(
                                            vote.tag) + '\n')
        line = []

    voterTable.close()
    candTable.close()
    outputfile.close()


def findUnregVoters():
    tree = ET.parse("votes.xml")
    root = tree.getroot()

    readfile = open("voterTable.csv", "r")
    outputfile = open("voterTable.csv", "a")

    voterID = 6690

    line = []

    for child in root:
        reg = False
        for info in child:
            line.append(info.text)
        readfile.seek(0)
        readfile.readline()
        for voter in readfile:
            voterline = voter.split(',')
            if line[0] == voterline[1] and line[1] == voterline[2] and line[2] == voterline[3] and line[3] == \
                    voterline[4] and line[4] == voterline[5] and line[5] == voterline[6]:
                reg = True
                break
        if not reg:
            voterID += 1
            outputfile.write(str(voterID)+','+line[0]+','+line[1]+','+line[2]+','+line[3]+','+line[4]+','+line[5]+','+"FALSE")
            outputfile.write("\n")


        line = []


def stateTable():
    outputfile = open("stateTable.csv", "w")
    outputfile.write("State_Name,Electoral_Votes")
    outputfile.write("\n")
    outputfile.write("PA,20")
    outputfile.write("\n")



#parseVoters()
# parseZipcodes()
# parseCandidates()
# parseVotes()
#findUnregVoters()
stateTable()
