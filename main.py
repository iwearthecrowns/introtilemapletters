# Sets tile map to teal, yellow, lime, and blue pixels
scene.set_tile_map(img("""
    . . . . . . . . . . 
        . . . . . . . . . . 
        . . . . . . . . . . 
        . . 6 5 7 8 . . . . 
        . . . . . . . . . . 
        . . . . . . . . . . 
        . . . . . . . . . . 
        . . . . . . . . . .
"""))
# Sets any red tiles to an image of the letter H
scene.set_tile(2,
    img("""
        f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 1 1 1 1 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f
    """),
    False)
# Sets any pink tiles to an image of the letter E
scene.set_tile(3,
    img("""
        f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f 1 1 1 1 1 1 1 f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 1 1 1 f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 1 1 1 1 1 1 f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f
    """),
    False)
# Sets any teal tiles to an image of the letter W
scene.set_tile(6,
    img("""
        f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f 1 f f f f f f 1 f f f f 
            f f f f 1 f f f f f f 1 f f f f 
            f f f f 1 f f f f f f 1 f f f f 
            f f f f 1 f f f f f f 1 f f f f 
            f f f f 1 f f f f f f 1 f f f f 
            f f f f 1 f f f f f f 1 f f f f 
            f f f f 1 f f 1 1 f f 1 f f f f 
            f f f f 1 f 1 f f 1 f 1 f f f f 
            f f f f 1 1 f f f f 1 1 f f f f 
            f f f f 1 f f f f f f 1 f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f
    """),
    False)
# Sets any yellow tiles to an image of the letter O
scene.set_tile(5,
    img("""
        f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f 1 1 1 1 1 1 1 f f f f f 
            f f f f 1 f f f f f 1 f f f f f 
            f f f f 1 f f f f f 1 f f f f f 
            f f f f 1 f f f f f 1 f f f f f 
            f f f f 1 f f f f f 1 f f f f f 
            f f f f 1 f f f f f 1 f f f f f 
            f f f f 1 f f f f f 1 f f f f f 
            f f f f 1 f f f f f 1 f f f f f 
            f f f f 1 f f f f f 1 f f f f f 
            f f f f 1 f f f f f 1 f f f f f 
            f f f f 1 1 1 1 1 1 1 f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f
    """),
    False)
# Sets any orange tiles to an image of the letter L
scene.set_tile(4,
    img("""
        f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 f f f f f f f f f f f 
            f f f f 1 1 1 1 1 1 1 f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f
    """),
    False)
# Sets any lime tiles to an image of the letter R
scene.set_tile(7,
    img("""
        f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f 1 1 1 1 f f f f f f f 
            f f f f f 1 f f f 1 f f f f f f 
            f f f f f 1 f f f 1 f f f f f f 
            f f f f f 1 f f f 1 f f f f f f 
            f f f f f 1 f f f 1 f f f f f f 
            f f f f f 1 1 1 1 1 f f f f f f 
            f f f f f 1 f f 1 f f f f f f f 
            f f f f f 1 f f f 1 f f f f f f 
            f f f f f 1 f f f 1 f f f f f f 
            f f f f f 1 f f f 1 f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f
    """),
    False)
# Sets any blue tiles to an image of the letter D
scene.set_tile(8,
    img("""
        f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f 1 1 1 1 1 f f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 f f f f 1 f f f f f f 
            f f f f 1 1 1 1 1 f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f 
            f f f f f f f f f f f f f f f f
    """),
    False)