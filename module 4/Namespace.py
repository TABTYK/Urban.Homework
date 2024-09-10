def test_function(a):
    def inner_function():
        return "Я в области видимости функции test_function"

    if a == True:
        print(inner_function())

#test_function(True)
inner_function()

