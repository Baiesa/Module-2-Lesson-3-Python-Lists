submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted the assignment and attended the class.")
else:
    print("Alice did not submit the assignment and/or did not attend the class.")