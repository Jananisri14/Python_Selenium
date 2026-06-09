import pytest_check as check
def test_soft_assert():
    name = "Janani"
    age = 20
    city = "Chennai"
    check.equal(name, "Janani")
    check.equal(age, 25, "Age is incorrect")
    check.equal(city, "Coimbatore", "City is incorrect")
    print("Test execution continues")


