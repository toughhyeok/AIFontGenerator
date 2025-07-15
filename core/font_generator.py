# In a real application, this module would contain complex AI logic
# to generate fonts based on keywords using models like GANs or VAEs.
# For now, we will simulate this process.

import os
import shutil
import random

# The directory where we will store the 'generated' fonts for the user to see.
GENERATED_FONTS_DIR = "static/fonts"
# The directory where we keep our base fonts for the 'AI' to learn from.
BASE_FONTS_DIR = "core/base_fonts"

# Ensure the directories exist.
if not os.path.exists(GENERATED_FONTS_DIR):
    os.makedirs(GENERATED_FONTS_DIR)
if not os.path.exists(BASE_FONTS_DIR):
    os.makedirs(BASE_FONTS_DIR)


def generate_font(keywords: list[str]) -> str | None:
    """
    Simulates the font generation process.

    It looks for a base font matching the provided keywords. If found,
    it copies it to a public directory. This mimics an AI generating a
    font in a specific style.

    Args:
        keywords: A list of keywords describing the desired font style.

    Returns:
        The web-accessible path to the 'generated' font file, or None if no
        base fonts are available to use.
    """
    print(f"Generating font with keywords: {keywords}")

    source_font_path = None
    
    # 1. Try to find a font that matches one of the keywords.
    if keywords:
        # We check all keywords provided by the user.
        for keyword in keywords:
            potential_path = os.path.join(BASE_FONTS_DIR, f"{keyword.lower()}.ttf")
            if os.path.exists(potential_path):
                source_font_path = potential_path
                print(f"Found a base font matching keyword '{keyword}': {source_font_path}")
                break # Use the first match we find

    # 2. If no specific font is found, use a default font.
    if not source_font_path:
        print(f"No font found for keywords {keywords}. Using default font.")
        default_font_path = os.path.join(BASE_FONTS_DIR, "modern.ttf")
        if os.path.exists(default_font_path):
            source_font_path = default_font_path
        else:
            # 3. If even the default is missing, try to use ANY font available.
            available_fonts = [f for f in os.listdir(BASE_FONTS_DIR) if f.endswith('.ttf')]
            if available_fonts:
                source_font_path = os.path.join(BASE_FONTS_DIR, available_fonts[0])
                print(f"Default font not found. Using first available font: {source_font_path}")
            else:
                print("ERROR: No base fonts found in 'core/base_fonts/'. Cannot generate font.")
                return None

    # 4. Create a unique name for the new font and copy it.
    keyword_str = "_".join(keywords) if keywords else "font"
    unique_id = random.randint(1000, 9999)
    generated_font_name = f"generated_{keyword_str}_{unique_id}.ttf"
    generated_font_path = os.path.join(GENERATED_FONTS_DIR, generated_font_name)

    shutil.copy(source_font_path, generated_font_path)

    print(f"Successfully 'generated' font: {generated_font_path}")

    # 5. Return the path that the web browser can use to find the font.
    return f"/{generated_font_path}"
