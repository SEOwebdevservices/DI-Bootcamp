import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Invalid page number")
        self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        visible = self.get_visible_items()
        return '\n'.join(str(item) for item in visible)

# === Test the Pagination class ===

if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print("Initial Page:")
    print(p.get_visible_items())

    print("\nNext Page:")
    p.next_page()
    print(p.get_visible_items())

    print("\nLast Page:")
    p.last_page()
    print(p.get_visible_items())

    print("\nGo to Page 3:")
    p.go_to_page(3)
    print(p.get_visible_items())

    print("\nPrint Current Page with __str__:")
    print(str(p))

    print("\nCurrent page index (1-based):")
    print(p.current_idx + 1)

    print("\nTry to go to invalid page:")
    try:
        p.go_to_page(0)
    except ValueError as e:
        print(f"Error: {e}")
