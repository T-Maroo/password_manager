import json
import sys
import os
import pathlib
import random 

dir = ".\password.json"
if not os.path.exists(dir):
    new_file = pathlib.Path(dir)
    new_file.touch()
    with open(dir, "w", encoding="UTF-8") as f:
        f.write('{"Unknown":{"user_name":"none", "password":"none", "mail":"none", "phone_number":"none", "url":"none"}}')


def Hello():
    words = ["LIFE IS GOOD \nurl:https://www.youtube.com/watch?v=l0U7SxXHkPY", "I wanna go back W.Academy.", "If you have the problem about this program, call T.Maroo", "I praise the lord then break the law!", "I'm becomming tired of thinking these messages.", "Who is T.Maroo?", "Praise T.Maroo!!!", "T.Maroo on the your PC, that's crazy", "This is not bad, right?", "Put your trust on this program.", "How are you, my bro?", "Hello World", "2020,03,31,22:45", "These are the messages from T.Maroo!!!", "If you want more tool, call T.Maroo"]
    words_num = random.randint(0, 15)
    print(f"Hello! \nThis was made by T.Maroo \n\n\n\n\nWARNING!!!! \nDON'T DELETE 'password.json'!!!\nTHERE IS THE MEMORY OF YOUR PASSWORD!!!\n\n\n{words[words_num]} \n\n\n\n")


def key_all():
    try:
        with open(dir, "r", encoding="UTF-8") as f:
            file = json.load(f)
        for i in file.keys():
            print(i)
    except Exception as e:
        print(f"{e}")
#----------------------------------------------
def key_append_change():
    key = input("key:")
    user_name = input("user_name: ")
    password = input("password: ")
    mail = input("mail address: ")
    phone = input("phone_number: ")
    url = input("url: ")

    with open(dir, "r", encoding="UTF-8") as f:
        data = json.load(f)

    data[key] = {"user_name": user_name, "password": password, "mail":mail, "phone_number":phone, "url":url}
    str = json.dumps(data,indent=0)

    with open(dir, "w", encoding="UTF-8") as f:
        f.write(str)
#----------------------------------------------
def key_search():

    with open(dir, "r", encoding="UTF-8") as f:
        file = json.load(f)
    query_word = input("query word: ")
    answer = file.get(query_word)
    if answer is not None:
        print("user_name: " + file[query_word]['user_name'])
        print("password: " + file[query_word]["password"])
        print("mail: " + file[query_word]["mail"])
        print("phone_number: " + file[query_word]["phone_number"])
        print("url: " + file[query_word]["url"])

#----------------------------------------------
def key_delete():
    del_key = input("key: ")
    question = input("Do you really want to delete ? [Y/N]: ").lower()
    if question == "y":
        with open(dir, "r", encoding="UTF-8") as f:
            file = json.load(f)
        del file[del_key]
        str = json.dumps(file, indent=0)
        with open(dir, "w", encoding="UTF-8") as f:
            f.write(str)

#----------------------------------------------
def main():
    Hello()
    if len(sys.argv) == 2:
        choice = sys.argv[1]
    else:
        choice = input("\nWatch the all your key[-a], Search the key[-s], Change and add key[-c], Delete key[-d], Quit[-q]: ")
    while True:
        if choice == "-a":
            print("\n")
            key_all()
        elif choice == "-s":
            print("\n")
            key_search()
        elif choice == "-c":
            print("\n")
            key_append_change()
        elif choice == "-d":
            print("\n")
            key_delete()
        else:
            break
        choice = input("\nWatch the all your key[-a], Search the key[-s], Change and add key[-c], Delete key[-d], Quit[-q]: ")
main()
