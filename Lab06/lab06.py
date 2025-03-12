from Apartment import Apartment

def mergesort(apartmentList):
    if len(apartmentList) > 1:
        mid = len(apartmentList) // 2

        lefthalf = apartmentList[:mid]
        righthalf = apartmentList[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                apartmentList[k] = lefthalf[i]
                i  = i + 1
            else:
                apartmentList[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            apartmentList[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            apartmentList[k] = righthalf[j]
            j = j + 1
            k = k + 1

def ensureSortedAscending(apartmentList):
    for i in range(len(apartmentList) - 1):
        if apartmentList[i] > apartmentList[i + 1]:
            return False
    return True

def getBestApartment(apartmentList):
    newList = apartmentList
    mergesort(newList)
    return newList[0].getApartmentDetails()

def getWorstApartment(apartmentList):
    newList = apartmentList
    mergesort(newList)
    return newList[len(newList) - 1].getApartmentDetails()

def getAffordableApartments(apartmentList, budget):
    newList = apartmentList
    mergesort(newList)
    finalList = ""
    for x in newList:
        if x.getRent() <= budget:
            finalList += x.getApartmentDetails() + "\n"
    return finalList[:len(finalList) - 1]