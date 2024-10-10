def main() -> None:
    info = input("Enter name of the file: ")
    content = ""
    while True:
        contents = input("Enter new line of content: ")
        if contents == "stop":
            break
        else:
            content += f"{contents}\n"

    with open(f"{info}.txt", "a") as f:
        f.write(content)


if __name__ == "__main__":
    main()
