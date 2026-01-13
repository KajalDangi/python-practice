
"""
Task 2: Write and Append Data to a File
"""

file_name = "output.txt"

try:
    # Write user input to file
    content = input("Enter text to write to the file: ")
    with open(file_name, "w") as fh:
        fh.write(content + "\n")
    print("Data written successfully.")

    # Append additional data
    additional_data = input("Enter additional text to append: ")
    with open(file_name, "a") as fh:
        fh.write(additional_data + "\n")
    print("Data appended successfully.")

    # Read and display final content
    print("\nFinal content of the file:")
    with open(file_name, "r") as fh:
        for line in fh:
            print(line.rstrip("\n"))

except Exception as e:
    print("An error occurred:", e)



