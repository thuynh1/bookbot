def read_file(file_path):
	"""
	Reads and returns the contents of a file as a list of lines.
	"""
	try:
		with open(file_path, 'r') as file: # 'r' is READ-only permission
			return file.readlines()  # Return a list of lines
	except FileNotFoundError:
		print(f"Error: The file at '{file_path}' was not found.")
		return []
	except IOError as e:
		print(f"Error: Unable to read the file. {e}")
		return []

def count_words(file_content):
	"""
	Counts the total number of words in a list of lines.
	"""
	total_words = 0
	for line in file_content:
		# Split the line into words and count
		total_words += len(line.split())
	return total_words

def count_characters(file_content):
	"""
	Counts the number of times each character appears in a list of lines.
	"""
	character_count = {}
	for line in file_content:
		for char in line.lower():
			if char.isalpha():
				character_count[char] = character_count.get(char, 0) + 1
	return character_count

def report(file_path, word_count, character_count):
	"""
	Print a report of word and character data for a file.
	"""
	print(f"--- Begin report of {file_path} ---")
	print(f"{word_count} words found in the document\n")

	# return the character count from the map in alphetic order 'a'..'z'
	a_to_z_ascii = list(range(ord('a'), ord('z') + 1))
	for ascii in a_to_z_ascii:
		char = (chr(ascii))
		print(f"The \'{char}\' character was found {character_count[char]} times")

	print(f"--- End report ---")

def main():
	path_to_file = "books/frankenstein.txt"
	# Read and print the file contents
	file_content = read_file(path_to_file)
	word_count = count_words(file_content)
	character_count = count_characters(file_content)
	report(path_to_file, word_count, character_count)

# Ensures the script runs only if executed directly
if __name__ == "__main__":
	main()