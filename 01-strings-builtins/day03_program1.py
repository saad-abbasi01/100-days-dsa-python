def compress_string(uncompressed: str) -> str:
    """
    Replaces consecutive duplicate characters with the character and its count.
    Returns original string if compression doesn't save space.
    """
    if not uncompressed:
        return ""

    compressed = []
    current_char = uncompressed[0]
    count = 1

    # Loop through string starting from the second character
    for i in range(1, len(uncompressed)):
        if uncompressed[i] == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = uncompressed[i]
            count = 1

    # Append the final character group
    compressed.append(f"{current_char}{count}")
    result = "".join(compressed)

    # Return original if compressed version is not smaller
    return result if len(result) < len(uncompressed) else uncompressed


# --- Unit Tests ---
if __name__ == "__main__":
    test_strings = ["aabcccccaaa", "abcd", "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWW"]
    for text in test_strings:
        compressed_text = compress_string(text)
        print(f"Original  ({len(text)} chars) : {text}")
        print(f"Compressed ({len(compressed_text)} chars): {compressed_text}\n")
