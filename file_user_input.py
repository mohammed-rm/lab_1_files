import os
from typing import Generator


def create_file(file_name: str) -> None:
    with open(f"files_input/{file_name}.txt", 'w') as f:
        f.write("")


def add_text_to_file(file_name: str, text: str) -> None:
    with open(f"files_input/{file_name}.txt", 'a') as f:
        f.write(text)


def read_file(file_name: str) -> Generator:
    with open(f"files_input/{file_name}.txt", 'r') as f:
        for line in f:
            yield line


def empty_file(file_name: str) -> None:
    open(f"files_input/{file_name}.txt", "w").close()


def is_valid_file(file_name: str) -> bool:
    return os.path.exists(f"files_input/{file_name}.txt")


def print_choices() -> None:
    print("1. Choisir un nom de fichier")
    print("2. Ajouter un texte")
    print("3. Afficher le contenu du fichier")
    print("4. Vider le fichier")
    print("5. Quitter le programme")


def main():
    print_choices()

    choice: str = input("\nChoisissez une option: ")
    quit: bool = False

    # check if the input is valid
    while not quit:
        if choice not in ["1", "2", "3", "4", "5"]:
            choice = input("Choix invalide. Veuillez réessayer: ")

        if choice in ['1', '2', '3', '4', '5']:

            if choice == '1':
                file_name: str = input("Entrer le nom du fichier: ")
                create_file(file_name)
                print(f"\nLe fichier {file_name}.txt a été créé dans le répertoire files_input\n")
                new_choice: str = input(
                    "2. Ajouter du contenu à votre fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                choice = new_choice

            if choice == '2':
                file_name: str = input("Entrer le nom du fichier dans lequel vous souhaitez écrire: ")
                texte: str = input("Ajouter votre texte: ")
                add_text_to_file(file_name, texte)
                print(f"\nVos texte a bien été écrit dans {file_name}.txt\n")
                new_choice: str = input(
                    "3. Afficher le contenu de votre fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                choice = new_choice

            if choice == '3':
                file_name: str = input("Entrer le nom du fichier que vous souhaitez afficher: ")
                if is_valid_file(file_name):
                    print(f"\nContenu du fichier {file_name}.txt:\n")
                    for line in read_file(file_name):
                        print(line)
                    new_choice: str = input(
                        "2. Ajouter du contenu à votre fichier\n4. Vider le fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                    choice = new_choice
                else:
                    print(f"\nLe fichier {file_name}.txt n'existe pas\n")
                    new_choice: str = input("1. Choisir un nom de fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                    choice = new_choice

            if choice == '4':
                file_name: str = input("Entrer le nom du fichier que vous souhaitez vider: ")
                if is_valid_file(file_name):
                    empty_file(file_name)
                    print(f"\nLe fichier {file_name}.txt a été vidé\n")
                    new_choice: str = input(
                        "2. Ajouter du contenu à votre fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                    choice = new_choice
                else:
                    print(f"\nLe fichier {file_name}.txt n'existe pas\n")
                    new_choice: str = input("1. Choisir un nom de fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                    choice = new_choice
            if choice == '5':
                print("Au revoir !")
                quit = True


if __name__ == '__main__':
    main()
