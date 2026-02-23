def my_function():
    greet = "Hello"
    return greet

RUN_INDENTED = True

message = "running unindented"

if RUN_INDENTED:
    print(my_function())
    message = "running indented"
    #my_function()

print(message)




