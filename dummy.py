from models.base_module import MichiBot


list1 = ["hablamelo michi", "1", "3"]

for i in list1:
    print("here counter is set to: {}".format(MichiBot.counter))
    result = MichiBot()
    response = result.bot_interaction(i)
    print("this is the stored response: {}, and its of type{}".format(response, type(response)))
    if type(response) == str:
        print("it's a string")
    elif type(response) == int:
        print("it's an integer")
    print("counter is set to: {}".format(MichiBot.counter))
    print("code: {}".format(MichiBot.book_code))
    print("{}".format(response))
