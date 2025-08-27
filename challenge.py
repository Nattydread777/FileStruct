try:
    # Step 1: Read input.txt
    with open("input.txt", "r") as f:
        content = f.read()

    # Step 2: Count words
    word_count = len(content.split())

    # Step 3: Convert to uppercase
    processed_text = content.upper()

    # Step 4: Write to output.txt
    with open("output.txt", "w") as f:
        f.write(processed_text + "\n\n")
        f.write(f"Word count: {word_count}")

    print("Processing complete! Output saved to 'output.txt'")

    # Step 5: Display output.txt content in terminal
    with open("output.txt", "r") as f:
        result = f.read()
        print("\n===== OUTPUT.TXT CONTENT =====")
        print(result)

except FileNotFoundError:
    print("Error: input.txt file not found.")
except Exception as e:
    print("Error:", e)
