import random
import os
from colorthief import ColorThief
from PIL import Image, ImageDraw
import webcolors
import colorsys


# Utility Functions
def generate_random_palette(num_colors=5):
    """Generates a random palette of hex colors."""
    palette = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in range(num_colors)]
    return palette


def extract_palette_from_image(image_path, num_colors=5):
    """Extracts dominant colors from an image."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    color_thief = ColorThief(image_path)
    palette = color_thief.get_palette(color_count=num_colors)
    hex_palette = [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in palette]
    return hex_palette


def hex_to_rgb(hex_color):
    """Convert HEX to RGB."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hsl(rgb_color):
    """Convert RGB to HSL."""
    r, g, b = [x / 255.0 for x in rgb_color]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return round(h * 360), round(s * 100), round(l * 100)


def convert_palette(palette, format="hex"):
    """Convert the palette to the specified format."""
    palette = [color.strip() for color in palette]  # Remove leading/trailing whitespace
    if format == "rgb":
        return [hex_to_rgb(color) for color in palette]
    elif format == "hsl":
        return [rgb_to_hsl(hex_to_rgb(color)) for color in palette]
    return palette  # Default is HEX


def name_colors(palette):
    """Assign names to colors in the palette."""
    named_palette = []
    for color in palette:
        try:
            name = webcolors.hex_to_name(color)
        except ValueError:
            name = "Unknown"
        named_palette.append((color, name))
    return named_palette


def save_palette_to_file(palette, filename="palette.txt"):
    """Saves the palette to a file."""
    with open(filename, "w") as f:
        for color in palette:
            f.write(color + "\n")
    print(f"Palette saved to {filename}")


def generate_wallpaper(palette, filename="wallpaper.png", width=1920, height=1080):
    """Create a wallpaper with a gradient using the palette."""
    image = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(image)

    for i, color in enumerate(palette):
        rgb = hex_to_rgb(color)
        x0 = i * (width // len(palette))
        x1 = (i + 1) * (width // len(palette))
        draw.rectangle([x0, 0, x1, height], fill=rgb)

    image.save(filename)
    print(f"Wallpaper saved as {filename}")


# Main Function
def main():
    while True:
        print("\nWelcome to PyColour!")
        print("1. Generate Random Palette")
        print("2. Extract Palette from Image")
        print("3. Convert Palette to RGB or HSL")
        print("4. Name Colors in Palette")
        print("5. Generate Wallpaper")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            num_colors = int(input("Enter the number of colors: "))
            palette = generate_random_palette(num_colors)
            print("Generated Palette (HEX):", palette)
            save_palette_to_file(palette)

        elif choice == "2":
            image_path = input("Enter the image file path: ")
            num_colors = int(input("Enter the number of colors: "))
            try:
                palette = extract_palette_from_image(image_path, num_colors)
                print("Extracted Palette (HEX):", palette)
                save_palette_to_file(palette)
            except FileNotFoundError as e:
                print(e)
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == "3":
            palette = input("Enter your palette (comma-separated HEX values): ").split(",")
            palette = [color.strip() for color in palette]  # Clean input
            format = input("Convert to 'rgb' or 'hsl': ").lower()
            converted_palette = convert_palette(palette, format)
            print(f"Converted Palette ({format.upper()}):", converted_palette)

        elif choice == "4":
            palette = input("Enter your palette (comma-separated HEX values): ").split(",")
            palette = [color.strip() for color in palette]  # Clean input
            named_palette = name_colors(palette)
            for hex_color, name in named_palette:
                print(f"{hex_color} → {name}")

        elif choice == "5":
            palette = input("Enter your palette (comma-separated HEX values): ").split(",")
            palette = [color.strip() for color in palette]  # Clean input
            filename = input("Enter the wallpaper filename (e.g., wallpaper.png): ")
            generate_wallpaper(palette, filename)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Entry Point
if __name__ == "__main__":
    main()