def main() -> None:
    info = input("Enter name of the file: ")
    word = ""
    while True:
        contents = input("Enter new line of content: ")
        if contents == "stop":
            break
        else:
            word += f"{contents}\n"

    with open(f"{info}.txt", "a") as f:
        f.write(content)


if __name__ == "__main__":
    main()
