import os

def translator():
    dictionary_file = "dictionary.txt"

    # თუ ფაილი არ არსებობს, შექმნა ცარიელი ფაილი
    if not os.path.exists(dictionary_file):
        open(dictionary_file, "w", encoding="utf-8").close()

    language_pairs = {
        "1": "Georgian-English",
        "2": "Georgian-Russian",
        "3": "English-Georgian",
        "4": "Russian-Georgian"
    }

    print("Welcome to the Translator!")
    print("Select the language pair:")
    for key, value in language_pairs.items():
        print(f"{key}: {value}")


    choice = input("Enter the number of your choice: ").strip()
    if choice not in language_pairs:
        print("Invalid choice. Exiting program.")
        return

    selected_pair = language_pairs[choice]
    print(f"You selected: {selected_pair}")


    word_to_translate = input("Enter a word or phrase to translate: ").strip()

    translations = {}
    with open(dictionary_file, "r", encoding="utf-8") as file:
        for line in file:

            pair, word, translation = line.strip().split(" | ")
            if pair not in translations:
                translations[pair] = {}
            translations[pair][word] = translation

    # სათარგმნი სიტყვის შემოწმება
    if selected_pair in translations and word_to_translate in translations[selected_pair]:
        print(f"Translation: {translations[selected_pair][word_to_translate]}")
    else:
        print("Word not found in the dictionary.")
        add_translation = input("Would you like to add this word to the dictionary? (yes/no): ").strip().lower()
        if add_translation == "yes":
            translation = input(f"Enter the translation for '{word_to_translate}': ").strip()
            with open(dictionary_file, "a", encoding="utf-8") as file:
                file.write(f"{selected_pair} | {word_to_translate} | {translation}\n")
            print("Word and translation added successfully.")
        else:
            print("Word not added.")


if __name__ == "__main__":
    translator()
