import bullet, libpng, ogg, sdl, sdl_image, vorbis, zlib, freetype

# If port A depends on port B, then A should be _after_ B
ports = [zlib, libpng, sdl, sdl_image, ogg, vorbis, bullet, freetype]
