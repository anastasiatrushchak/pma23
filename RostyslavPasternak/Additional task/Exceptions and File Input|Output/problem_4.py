
class ContentFilter:

    def __init__(self, file_name):
        while True:
            try:
                with open(file_name, 'r') as file:
                    self.name = file_name
                    self.contents = file.read()
                    self.stats = self.calculate_stats()
                break
            except (FileNotFoundError, TypeError, OSError):
                file_name = input("Please enter a valid file name: ")

    def calculate_stats(self):
        total_chars = len(self.contents)
        alphabetic_chars = sum(c.isalpha() for c in self.contents)
        numerical_chars = sum(c.isdigit() for c in self.contents)
        whitespace_chars = sum(c.isspace() for c in self.contents)
        num_lines = self.contents.count('\n') + 1

        return {
            'Total characters': total_chars,
            'Alphabetic characters': alphabetic_chars,
            'Numerical characters': numerical_chars,
            'Whitespace characters': whitespace_chars,
            'Number of lines': num_lines
        }

    def uniform(self, outfile, mode='w', case="upper"):
        if mode not in ['w', 'x', 'a']:
            raise ValueError("Invalid mode. Mode must be 'w', 'x', or 'a'.")

        if case not in ['upper', 'lower']:
            raise ValueError("Invalid case. Case must be 'upper' or 'lower'.")

        with open(outfile, mode) as file:
            if case == 'upper':
                file.write(self.contents.upper())
            else:
                file.write(self.contents.lower())

    def reverse(self, outfile, mode='w', unit="line"):
        if mode not in ['w', 'x', 'a']:
            raise ValueError("Invalid mode. Mode must be 'w', 'x', or 'a'.")

        if unit not in ['word', 'line']:
            raise ValueError("Invalid unit. Unit must be 'word' or 'line'.")

        lines = self.contents.split('\n')

        with open(outfile, mode) as file:
            if unit == 'word':
                reversed_words_lines = [' '.join(line.split()[::-1]) for line in lines]
                file.write('\n'.join(reversed_words_lines))
            else:
                file.write('\n'.join(lines[::-1]))

    def transpose(self, outfile, mode='w'):
        if mode not in ['w', 'x', 'a']:
            raise ValueError("Invalid mode. Mode must be 'w', 'x', or 'a'.")
        result_list = [element.split(' ') for element in self.contents.split('\n')]
        transposed_matrix = [list(row) for row in zip(*result_list)]

        with open(outfile, mode) as file:
            for row in transposed_matrix:
                file.write(' '.join(map(str, row)) + '\n')

    def __str__(self):
        stats_str = "\n".join([f"{key}: {value}" for key, value in self.stats.items()])
        return f"Source file:\n{stats_str}\n{self.name}\n{self.contents}"


if __name__ == "__main__":
    cf = ContentFilter("cf_example1.txt")
    print(cf)

    cf.uniform("file/uniform.txt", mode='w', case="upper")
    cf.uniform("file/uniform1.txt", mode='a', case="lower")

    cf.reverse("file/reverse.txt", mode='w', unit="word")
    cf.reverse("file/reverse1.txt", mode='a', unit="line")

    cf.transpose("file/transpose.txt", mode='w')
