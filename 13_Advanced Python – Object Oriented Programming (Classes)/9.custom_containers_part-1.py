# ------------------------------------------------------------
# -------------**## Custom Containers Part 1 ##**-------------


# --**--**--**--**--** Example 21 ->>>> creating a custom container

# class BookmarkedPage:
#   def __init__(self):
#     self.bookmarks = {}


#   def add(self, bookmark):
#     self.bookmarks[bookmark] = self.bookmarks.get(bookmark, 0) + 1


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("python")

# print(target_bookmark.bookmarks)


# --**--**--**--**--** Example 22 ->>>> handling corner cases

# class BookmarkedPage:
#     def __init__(self):
#         self.bookmarks = {}

#     def add(self, bookmark):
#         self.bookmarks[bookmark.lower()] = self.bookmarks.get(bookmark.lower(), 0) + 1


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("Python")
# target_bookmark.add("Python")
# target_bookmark.add("Python")

# print(target_bookmark.bookmarks)


# --**--**--**--**--** Example 23 ->>>> getting the count of a key

class BookmarkedPage:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(
            bookmark.lower(), 0) + 1

    def __getitem__(self, bookmark):
        return self.bookmarks.get(bookmark.lower(), 0)


target_bookmark = BookmarkedPage()
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("Python")
target_bookmark.add("Python")
target_bookmark.add("Python")
target_bookmark.add("Python")

# print(target_bookmark.bookmarks)

print(target_bookmark["python"])
