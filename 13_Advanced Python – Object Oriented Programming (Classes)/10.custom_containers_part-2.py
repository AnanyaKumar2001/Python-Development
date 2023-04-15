# ------------------------------------------------------------
# -------------**## Custom Containers Part 2 ##**-------------


# --**--**--**--**--** Example 24 ->>>> setting the count of a key

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


# target_bookmark = BookmarkedPage()
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("python")
# target_bookmark.add("Python")
# target_bookmark.add("Python")

# target_bookmark["python"] = 110

# print(target_bookmark.bookmarks)
# print(target_bookmark["python"])


# --**--**--**--**--** Example 25 ->>>> getting the number of the bookmark types

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

# print(target_bookmark.bookmarks)
# print(len(target_bookmark))


# --**--**--**--**--** Example 26 ->>>> iterating over the class

class BookmarkedPage:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(
            bookmark.lower(), 0) + 1

    def __getitem__(self, bookmark):
        return self.bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        self.bookmarks[bookmark.lower()] = count

    def __len__(self):
        return len(self.bookmarks)

    def __iter__(self):
        return iter(self.bookmarks)


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

print(target_bookmark.bookmarks)

for bookmark in target_bookmark:
    print(bookmark)
