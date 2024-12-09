# PyColour: Colour Palette Generator 🎨
PyColour is a CLI tool wrriten in Python to generate and manage beautiful colour palettes.
---
## Features
1 - Generate Random Palettes: Create stunning random colour palettes.

2 - Extract Colours from Images: Extract dominant colours from any image.

3 - Convert Formats: Transform palettes into HEX, RGB, or HSL.

4 - Name Your Colours: Get human-friendly names for your colours.

5 - Create Wallpapers: Generate gradient wallpapers using your palette.
---
### Installation
1. Install dependencies:
   ```bash
   pip install colorthief pillow webcolors
   ```
2. Run the script:
   ```bash
   python pycolour.py
   ```

---

### Usage

#### Generate a Palette
```text
Welcome to PyColour!
1. Generate Random Palette
Enter the number of colours: 5
Generated Palette (HEX): ['#FF5733', '#33FF57', '#3357FF', '#FFFF33', '#FF33FF']
```

#### Extract Colours from an Image
```text
Welcome to PyColour!
2. Extract Palette from Image
Enter the image file path: image.jpg
Enter the number of colours: 5
Extracted Palette (HEX): ['#112233', '#445566', '#778899', '#AABBCC', '#DDEEFF']
```

#### Convert Formats
```text
Welcome to PyColour!
3. Convert Palette to RGB or HSL
Enter your palette (comma-separated HEX values): #FF5733, #33FF57
Convert to 'rgb' or 'hsl': rgb
Converted Palette (RGB): [(255, 87, 51), (51, 255, 87)]
```

#### Generate a Wallpaper
```text
Welcome to PyColour!
5. Generate Wallpaper
Enter your palette (comma-separated HEX values): #FF5733, #33FF57, #3357FF
Enter the wallpaper filename (e.g., wallpaper.png): my_wallpaper.png
Wallpaper saved as my_wallpaper.png
```

---
