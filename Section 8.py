def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalize = phrase.capitalize()
    if phrase.startswith(interrogatives):  #can use ___.startswith(("__" , "____", "____")) yp found out if a string starts with a specific word
        return "{}?".format(capitalize) # just adds ? if the phrase is a question
    else:
        return "{}.".format(capitalize)


results = []
while True:
    user_input = input("Say something: ")
    if user_input =="\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))