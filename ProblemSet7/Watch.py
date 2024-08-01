import re

def main():
    print(parse(input("HTML: ")), sep="")


def parse(s):
    if match := re.search(r"(?:src=\")?https?://(?:www\.)?youtube\.com/(.+)?\"?", s, re.IGNORECASE):
        substitute = re.sub(r"embed/", "", match.group(1))
        return(f"https://youtu.be/{substitute}")


if __name__ == "__main__":
    main()
