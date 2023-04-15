# ------------------------------------------------------------
# -------------**## Custom Containers Part 3 ##**-------------
# -----------------**## Private Memebers ##**-----------------


# --**--**--**--**--** Example 27 ->>>> accessing a dict from outside

# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark.lower()] = self.bookmarks.get(
#             bookmark.lower(), 0) + 1

#     def __getitem__(self, bookmark):
#         return self.bookmarks.get(bookmark.lower(), 0)

#     def __setitem__(self, bookmark, count):
#         self.bookmarks[bookmark.lower()] = count

#     def __len__(self):
#         return len(self.bookmarks)

#     def __iter__(self):
#         return iter(self.bookmarks)


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("Python")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("Java")
# target_bookmark.add("Java")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("React")
# target_bookmark.add("Vue")
# target_bookmark.add("TypeScript")

# print(target_bookmark["PYTHON"])
# print(target_bookmark.bookmarks["PYTHON"])
# print(target_bookmark.bookmarks["python"])

# --**--**--**--**--** Example 28 ->>>> blocking a dict access from outside

# class BookmarkedPage:
#     def __init__(self):
#         self.__bookmarks = {}

#     def add(self, bookmark):
#         self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(
#             bookmark.lower(), 0) + 1

#     def __getitem__(self, bookmark):
#         return self.__bookmarks.get(bookmark.lower(), 0)

#     def __setitem__(self, bookmark, count):
#         self.__bookmarks[bookmark.lower()] = count

#     def __len__(self):
#         return len(self.__bookmarks)

#     def __iter__(self):
#         return iter(self.__bookmarks)


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("Python")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("JavaScript")
# target_bookmark.add("Java")
# target_bookmark.add("Java")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("GoLang")
# target_bookmark.add("React")
# target_bookmark.add("Vue")
# target_bookmark.add("TypeScript")

# target_bookmark.bookmarks # Not Available
# target_bookmark.__bookmarks # Not Available

# print(target_bookmark.__bookmarks)


# --**--**--**--**--** Example 29 ->>>> accessing a blocked dict from outside


class BookmarkedPage:
    def __init__(self):
        self.__bookmarks = {}

    def add(self, bookmark):
        self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(
            bookmark.lower(), 0) + 1

    def __getitem__(self, bookmark):
        return self.__bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        self.__bookmarks[bookmark.lower()] = count

    def __len__(self):
        return len(self.__bookmarks)

    def __iter__(self):
        return iter(self.__bookmarks)


target_bookmark = BookmarkedPage()
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("Python")
target_bookmark.add("Python")
target_bookmark.add("JavaScript")
target_bookmark.add("JavaScript")
target_bookmark.add("JavaScript")
target_bookmark.add("Java")
target_bookmark.add("Java")
target_bookmark.add("GoLang")
target_bookmark.add("GoLang")
target_bookmark.add("GoLang")
target_bookmark.add("GoLang")
target_bookmark.add("GoLang")
target_bookmark.add("GoLang")
target_bookmark.add("React")
target_bookmark.add("Vue")
target_bookmark.add("TypeScript")

# print(target_bookmark.__dict__)

# print(target_bookmark._BookmarkedPage__bookmarks)
