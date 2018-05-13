import translate

tr = translate.Translator("ro","en")

x = "Observe the first usage where we use {0} and this corresponds to the variable name which is the first argument to the format method. Similarly, the second specification is {1} corresponding to age which is the second argument to the format method. Note that Python starts counting from 0 which means that first position is at index 0, second position is at index 1, and so on."
s = tr.translate(x)
print(s)