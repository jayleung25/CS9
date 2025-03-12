from Apartment import Apartment
from lab06 import mergesort, ensureSortedAscending, getBestApartment, getWorstApartment, getAffordableApartments

def testApartmentClass():
    a = Apartment(3000, 50, "bad")
    b = Apartment(1500, 70, "excellent")
    c = Apartment(1000, 20, "bad")
    e = Apartment(1000, 30, "average")
    f = Apartment(1000, 30, "bad")
    g = Apartment(1000, 30, "bad")
    assert a.getRent() == 3000
    assert b.getMetersFromUCSB() == 70
    assert c.getCondition() == "bad"
    assert e.getApartmentDetails() == "(Apartment) Rent: $1000, Distance From UCSB: 30m, Condition: average"

def testlab06():
    a = Apartment(3000, 50, "bad")
    b = Apartment(1500, 70, "excellent")
    c = Apartment(1000, 20, "bad")
    e = Apartment(1000, 30, "average")
    f = Apartment(1000, 30, "bad")
    g = Apartment(1000, 30, "bad")
    t = Apartment(1000, 20, "excellent")
    theList = []
    theList.append(a)
    theList.append(b)
    theList.append(c)
    theList.append(e)
    theList.append(f)
    theList.append(g)
    theList.append(t)
    assert ensureSortedAscending(theList) == False
    mergesort(theList)
    assert theList == [t, c, e, f, g, b, a]
    assert ensureSortedAscending(theList) == True
    assert getWorstApartment(theList) == "(Apartment) Rent: $3000, Distance From UCSB: 50m, Condition: bad"
    assert getBestApartment(theList) == "(Apartment) Rent: $1000, Distance From UCSB: 20m, Condition: excellent"
    assert getAffordableApartments(theList, 2000) == "(Apartment) Rent: $1000, Distance From UCSB: 20m, Condition: excellent\n(Apartment) Rent: $1000, Distance From UCSB: 20m, Condition: bad\n(Apartment) Rent: $1000, Distance From UCSB: 30m, Condition: average\n(Apartment) Rent: $1000, Distance From UCSB: 30m, Condition: bad\n(Apartment) Rent: $1000, Distance From UCSB: 30m, Condition: bad\n(Apartment) Rent: $1500, Distance From UCSB: 70m, Condition: excellent"
    

testApartmentClass()
testlab06()
