"""
In a file called adieu.py, implement a program that prompts the user for names, one per line,
until the user inputs control-d. Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and names with
commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""
import inflect



def adieu():

    engine = inflect.engine()

    try:
        names = []
        while True:
            name = input("Enter name: ")
            names.append(name)

    except EOFError:
        adieu = "\nAdieu, adieu, to "
        i = 0
        while i != (len(names) + 1):
            if names[:i] == []:
                #print("inside if statement")
                #print("names[:i]", names[:i])
                pass

            else:
                #print("inside else statement")
                print(adieu+engine.join(names[:i]))

            #print("i: ", i)
            i+=1

def main():
    adieu()


if __name__ == "__main__":
    main()




