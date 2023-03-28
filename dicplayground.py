# word = "user"

# url = f"{word}"

# print(url)


print("\033[1mHello, world!\033[0m")



file_path = os.path.abspath(__file__)
directory_path = os.path.dirname(file_path)

# Change the file permissions to make it executable
os.chmod(file_path, 0o755)

# Get the current value of the PATH environment variable
path = os.environ.get("PATH")

# Add the directory path to the PATH variable
subprocess.run(
    f'echo \'export PATH="$PATH:{directory_path}"\' >> ~/.bashrc', shell=True)

print(os.environ["PATH"])


################
# word_eng = sys.argv[1]
# word_eng = input("what's the word?")