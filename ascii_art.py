from PIL import Image
import os

ASCII_CHARS = "@%#*+=-:. "
SAVED_ARTS = {}

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def pixels_to_ascii_color(image):
    pixels = list(image.getdata())
    ascii_image = ""
    width = image.width

    for i in range(0, len(pixels), width):
        line = ""
        for j in range(width):
            r, g, b = pixels[i + j][:3]
            brightness = int((r + g + b) / 3)
            char = ASCII_CHARS[brightness * len(ASCII_CHARS) // 256]
            line += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
        ascii_image += line + "\n"
    return ascii_image

def convert_image_to_ascii(image_path, width):
    try:
        image = Image.open(image_path).convert("RGBA")
    except Exception as e:
        return f"이미지를 열 수 없습니다: {e}"

    background = Image.new("RGBA", image.size, (255, 255, 255, 255))
    image = Image.alpha_composite(background, image)

    image = image.convert("RGB")
    image = resize_image(image, width)
    return pixels_to_ascii_color(image)

def save_ascii_to_txt(name, content):
    with open(f"./save/{name}.txt", "w", encoding="utf-8") as f:
        # ANSI escape code 제거 후 저장
        import re
        clean_text = re.sub(r'\033\[[0-9;]*m', '', content)
        f.write(clean_text)

def main():
    print("Welcome to ASCII Art Terminal!")
    print("command: make, list, print, save, exit")

    while True:
        cmd = input("ascii-art > ").strip()
        if cmd == "exit":
            break
        elif cmd.startswith("make"):
            try:
                _, name, path = cmd.split(maxsplit=2)
            except ValueError:
                print("Enable: make <name> <image_path>")
                continue

            abs_path = os.path.abspath(os.path.expanduser(path))
            if not os.path.isfile(abs_path):
                print(f"can`t not found file: {abs_path}")
                continue

            try:
                width = int(input("Output width (default 100): ") or 100)
            except ValueError:
                width = 100

            art = convert_image_to_ascii(abs_path, width)
            SAVED_ARTS[name] = art
            print(f"'{name}' to complete the save.")
        elif cmd == "list":
            if not SAVED_ARTS:
                print("No art was created.")
            else:
                print("List of Saved Art")
                for k in SAVED_ARTS.keys():
                    print(" -", k)
        elif cmd.startswith("print"):
            try:
                _, name = cmd.split(maxsplit=1)
            except ValueError:
                print("Enable: print <name>")
                continue
            art = SAVED_ARTS.get(name)
            if not art:
                print(f"'{name}' can`t not found Art")
            else:
                print(art)
        elif cmd.startswith("save"):
            try:
                _, name = cmd.split(maxsplit=1)
            except ValueError:
                print("Enable: save <name>")
                continue
            art = SAVED_ARTS.get(name)
            if not art:
                print(f"'{name}' can`t not found Art")
            else:
                save_ascii_to_txt(name, art)
                print(f"'{name}.txt' file saved successfully.")
        else:
            print("Unknown commands: make, list, print, save, exit")

if __name__ == "__main__":
    main()
