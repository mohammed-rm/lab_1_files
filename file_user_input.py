import os
from typing import Generator


def hello() -> None:
    print("Bonjour le monde !")


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


def clear_file(file_name: str) -> None:
    open(f"files_input/{file_name}.txt", 'w').close()


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
    is_file_created: bool = False

    while not quit:
        if choice not in ["0", "1", "2", "3", "4", "5"]:
            choice = input("Choix invalide. Veuillez réessayer: ")

        if choice in ['0', '1', '2', '3', '4', '5']:

            if choice == '0':
                is_file_created = False
                print_choices()
                choice = input("\nChoisissez une option: ")

            if choice == '1':
                file_name: str = input("Entrer le nom du fichier: ")
                create_file(file_name)
                is_file_created = True
                print(f"\nLe fichier {file_name}.txt a été créé dans le répertoire files_input\n")
                new_choice: str = input(
                    "0. Revenir au menu principal\n2. Ajouter du contenu à votre fichier\n5. ou quitter le programme ?\nVotre choix: \n")
                choice = new_choice

            if choice == '2' and is_file_created:
                text: str = input("Entrer le texte à ajouter: ")
                add_text_to_file(file_name, text)
                print(f"\nLe texte {text} a été ajouté au fichier {file_name}.txt\n")
                new_choice: str = input(
                    "0. Revenir au menu principal\n3. Afficher le contenu de votre fichier\n4. Vider le fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                choice = new_choice

            if choice == '3' and is_file_created:
                print(f"\nContenu du fichier {file_name}.txt\n")
                for line in read_file(file_name):
                    print(line)
                new_choice: str = input(
                    "0. Revenir au menu principal\n4. Vider le fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                choice = new_choice

            if choice == '4' and is_file_created:
                clear_file(file_name)
                print(f"\nLe fichier {file_name}.txt a été vidé\n")
                new_choice: str = input(
                    "0. Revenir au menu principal\n2. Ajouter du contenu à votre fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                choice = new_choice

            if choice == '2':
                file_name: str = input("Entrer le nom du fichier dans lequel vous souhaitez écrire: ")
                texte: str = input("Ajouter votre texte: ")
                add_text_to_file(file_name, texte)
                print(f"\nVos texte a bien été écrit dans {file_name}.txt\n")
                new_choice: str = input(
                    "0. Revenir au menu principal\n5. Ou quitter le programme ?\nVotre choix: ")
                choice = new_choice

            if choice == '3':
                file_name: str = input("Entrer le nom du fichier que vous souhaitez afficher: ")
                if is_valid_file(file_name):
                    print(f"\nContenu du fichier {file_name}.txt:\n")
                    for line in read_file(file_name):
                        print(line)
                    new_choice: str = input(
                        "0. Revenir au menu principal\n5. Ou quitter le programme ?\nVotre choix: ")
                    choice = new_choice
                else:
                    print(f"\nLe fichier {file_name}.txt n'existe pas\n")
                    new_choice: str = input(
                        "0. Revenir au menu principal\n3. Afficher le contenu d'un fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                    choice = new_choice

            if choice == '4':
                file_name: str = input("Entrer le nom du fichier que vous souhaitez vider: ")
                if is_valid_file(file_name):
                    clear_file(file_name)
                    print(f"\nLe fichier {file_name}.txt a été vidé\n")
                    new_choice: str = input(
                        "2. Ajouter du contenu à votre fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                    choice = new_choice
                else:
                    print(f"\nLe fichier {file_name}.txt n'existe pas\n")
                    new_choice: str = input(
                        "0. Revenir au menu principal\n4. Vider le fichier\n5. Ou quitter le programme ?\nVotre choix: ")
                    choice = new_choice

            if choice == '5':
                print("Au revoir !")
                quit = True


if __name__ == '__main__':
    # hello()
    main()
