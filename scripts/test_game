import builtins
import main
import pytest 
from main import Alien
from main import create_alien
from unittest.mock import patch
from main import Mireling

# Unit tests are segments of code written to test other pieces of code, typically a single function or method

def test_alien_is_alive(): # we test alien.is_alive function
    alien = Alien("Testing_alien", "desciption", 10, 5, 3, "run", drops = []) # creates own alien

    # assert statement is a built-in statement in Python used to, as the name says, 
    # assert if a given condition is true or not. 
    assert alien.is_alive() is True #should return True because health is 10

    alien.health = 0 # check is alien alive
    assert alien.is_alive() is False #should be False, cause not alive
    return True


    
def test_drop_item(): # testing drop_item function
    alien = Alien("Test", "desc", 10, 5, 2, "guard", drops=["Item1", "Item2"]) # creates own alien to test

    with patch("random.choice", return_value="Item1"): # Replace random.choice with a fake version
        assert alien.drop_item() == "Item1"

def test_create_unknown_alien(): # now we test create_alien def by unknown name
    try:
        create_alien("unknown")
        assert False #should return False
    except:
        assert True

def test_create_mireling(): #now testing creating Mireling alien
    alien = create_alien("Mireling")
    assert isinstance(alien, Mireling)     

if __name__ == "__main__":
    #the main function that runs all function
    try:
        test_alien_is_alive()
        print("Testing function alien.is_alive() is passed")
    except AssertionError:
        print("Testing function alien.is_alive() is failed")

    try:
        test_drop_item()
        print("Testing function alien.drop_item() is passed")
    except:
        print("Testing function alien.drop_item() is failed")
    
    try:
        test_create_unknown_alien()
        print("Testing function create_alien is passed")
    except:
        print("Testing function create_alien is failed")

    try:
        test_create_mireling()
        print("Testing function creating Mireling alien is passed")
    except:
        print("Testing function creating Mireling alien is failed")




