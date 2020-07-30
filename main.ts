//  Sets tile map to teal, yellow, lime, and blue pixels
scene.setTileMap(img`
    . . . . . . . . . . 
        . . . . . . . . . . 
        . . . . . . . . . . 
        . . 6 5 7 8 . . . . 
        . . . . . . . . . . 
        . . . . . . . . . . 
        . . . . . . . . . . 
        . . . . . . . . . .
`)
//  Sets any red tiles to an image of the letter H
scene.setTile(2, img`
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
    `, false)
//  Sets any pink tiles to an image of the letter E
scene.setTile(3, img`
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
    `, false)
//  Sets any teal tiles to an image of the letter W
scene.setTile(6, img`
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
    `, false)
//  Sets any yellow tiles to an image of the letter O
scene.setTile(5, img`
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
    `, false)
//  Sets any orange tiles to an image of the letter L
scene.setTile(4, img`
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
    `, false)
//  Sets any lime tiles to an image of the letter R
scene.setTile(7, img`
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
    `, false)
//  Sets any blue tiles to an image of the letter D
scene.setTile(8, img`
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
    `, false)
