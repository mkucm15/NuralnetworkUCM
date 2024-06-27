def count_words_in_file(input_file, output_file):
    word_count = {}

    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(output_file, 'w') as outfile:
        for line in lines:
            outfile.write(line)
            words = line.split()
            for word in words:
                word = word.strip()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        # Write the word count to the output file
        outfile.write("\nWord_Count:\n")
        for word, count in word_count.sort():
            outfile.write(f"{word}: {count}\n")

def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    count_words_in_file(input_file, output_file)
    print(f"Word count has been written to {output_file}")

if __name__ == "__main__":
    main()
