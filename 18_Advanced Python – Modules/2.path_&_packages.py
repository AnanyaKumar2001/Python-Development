# ------------------------------------------------------------
# -----------------**## Paths & Packages ##**-----------------


# ----------************------ The Path Object
# import sys
# print(sys.path)

# ----------************------ Packages


# ----------************------ Importing Ways

# Approach 1

# import social_media.user_imgs

# social_media.user_imgs.img()


# Approach 2
# from social_media.user_imgs import img, media

# img()
# media()


# Approach 3

from social_media import user_imgs

user_imgs.img()
user_imgs.media()
