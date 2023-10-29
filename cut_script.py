from PIL import Image

def split_image(image_path):
    original_image = Image.open(image_path)
    width, height = original_image.size
    fragments = []
    for y in range(0, height, 42):
        for x in range(0, width, 42):
            box = (x, y, x + 42, y + 42)
            fragment = original_image.crop(box)
            fragment_data = {
                'fragment': fragment,
                'position': (x, y)
            }
            fragments.append(fragment_data)
    return fragments

# Пример использования
fragments = split_image('GuQn_g6aPlo.jpg')
for i, fragment_data in enumerate(fragments):
    fragment_data['fragment'].save(f'fragment_{i}.png')
