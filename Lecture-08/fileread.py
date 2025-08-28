def main():

    infile = open('philosophers.txt','r')
    file_content = infile.read()
    infile.close()

    print(file_content)

main()