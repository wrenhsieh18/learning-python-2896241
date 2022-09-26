import os


def main():

    byte_count = 0
    str_filenames = ""

    for file in os.listdir():
        if os.path.isfile(file):
            byte_count += os.path.getsize(file)
            str_filenames += file + "\n"

    os.mkdir("results")
    my_file = open("results/results.txt", "w+")

    if my_file.mode == "w+":
        my_file.write("Total bytecount:" + str(byte_count) + "\nFiles list:\n----------------\n" + str_filenames)

    my_file.close()

if __name__ == '__main__':
    print(os.listdir())
    main()