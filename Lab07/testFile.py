from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue, QueueEmptyException

def test_pizza():
    a = Pizza("S")
    b = Pizza("M")
    c = Pizza("L")
    assert a.getSize() == "S"
    assert b.getSize() == "M"
    assert c.getPrice() == 0.0
    a.setPrice(15.0)
    b.setSize("S")
    assert a.getPrice() == 15.0
    assert b.getSize() == "S"

def test_custompizza():
    a = CustomPizza("S")
    a.addTopping("cheese")
    assert a.getPizzaDetails() == "CUSTOM PIZZA\nSize: S\nToppings:\n\t+ cheese\nPrice: $8.50\n"
    b = CustomPizza("M")
    b.addTopping("extra cheese")
    b.addTopping("pepperoni")
    assert b.getPizzaDetails() == "CUSTOM PIZZA\nSize: M\nToppings:\n\t+ extra cheese\n\t+ pepperoni\nPrice: $11.50\n"
    c = CustomPizza("L")
    assert c.getPizzaDetails() == "CUSTOM PIZZA\nSize: L\nToppings:\nPrice: $12.00\n"

def test_specialtypizza():
    a = SpecialtyPizza("S", "Jay")
    assert a.getPizzaDetails() == "SPECIALTY PIZZA\nSize: S\nName: Jay\nPrice: $12.00\n"
    b = SpecialtyPizza("M", "Derek")
    assert b.getPizzaDetails() == "SPECIALTY PIZZA\nSize: M\nName: Derek\nPrice: $14.00\n"

def test_pizzaorder():
    a = CustomPizza("S")
    a.addTopping("pepperoni")
    a.addTopping("pinneaple")
    b = SpecialtyPizza("L", "John")
    c = PizzaOrder(140000)
    c.addPizza(a)
    c.addPizza(b)
    assert c.getOrderDescription() == "******\nOrder Time: 140000\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ pepperoni\n\t+ pinneaple\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: L\nName: John\nPrice: $16.00\n\n----\nTOTAL ORDER PRICE: $25.00\n******\n"
    d = CustomPizza("M")
    d.addTopping("Fruits")
    c.addPizza(d)
    assert c.getOrderDescription() == "******\nOrder Time: 140000\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ pepperoni\n\t+ pinneaple\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: L\nName: John\nPrice: $16.00\n\n----\nCUSTOM PIZZA\nSize: M\nToppings:\n\t+ Fruits\nPrice: $10.75\n\n----\nTOTAL ORDER PRICE: $35.75\n******\n"

def test_orderqueue():
    x = OrderQueue()
    a = CustomPizza("S")
    b = CustomPizza("L")
    c = SpecialtyPizza("L", "Danny")
    d = CustomPizza("M")
    e = CustomPizza("S")
    e.addTopping("sausage")
    e.addTopping("peppers")
    f = SpecialtyPizza("M", "Jonathan")             
    first = PizzaOrder(111111)
    second = PizzaOrder(111111)
    third = PizzaOrder(134250)
    fourth = PizzaOrder(160000)
    fifth = PizzaOrder(190000)
    first.addPizza(a)
    second.addPizza(b)
    third.addPizza(c)
    fourth.addPizza(d)
    fifth.addPizza(e)
    fifth.addPizza(f)
    x.addOrder(first)
    x.addOrder(second)
    x.addOrder(third)
    x.addOrder(fourth)
    x.addOrder(fifth)
    assert x.processNextOrder() == "******\nOrder Time: 111111\nCUSTOM PIZZA\nSize: S\nToppings:\nPrice: $8.00\n\n----\nTOTAL ORDER PRICE: $8.00\n******\n"
    assert x.processNextOrder() == "******\nOrder Time: 111111\nCUSTOM PIZZA\nSize: L\nToppings:\nPrice: $12.00\n\n----\nTOTAL ORDER PRICE: $12.00\n******\n"
    assert x.processNextOrder() == "******\nOrder Time: 134250\nSPECIALTY PIZZA\nSize: L\nName: Danny\nPrice: $16.00\n\n----\nTOTAL ORDER PRICE: $16.00\n******\n"
    assert x.processNextOrder() == "******\nOrder Time: 160000\nCUSTOM PIZZA\nSize: M\nToppings:\nPrice: $10.00\n\n----\nTOTAL ORDER PRICE: $10.00\n******\n"
    assert x.processNextOrder() == "******\nOrder Time: 190000\nCUSTOM PIZZA\nSize: S\nToppings:\n\t+ sausage\n\t+ peppers\nPrice: $9.00\n\n----\nSPECIALTY PIZZA\nSize: M\nName: Jonathan\nPrice: $14.00\n\n----\nTOTAL ORDER PRICE: $23.00\n******\n"

test_pizza()
test_custompizza()
test_specialtypizza()
test_pizzaorder()
test_orderqueue()
