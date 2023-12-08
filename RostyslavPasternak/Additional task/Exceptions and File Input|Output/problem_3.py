class ContentFilter:
    def __init__(self, file_name):
        while True:
            try:
                with open(file_name, 'r') as file:
                    self.name = file_name
                    self.contents = file.read()
                break
            except (FileNotFoundError, TypeError, OSError):
                file_name = input("Please enter a valid file name: ")



if __name__ =="__main__":
    cf1 = ContentFilter("hello_world.txt")
    print("Name:", cf1.name)
    print("Contents:", cf1.contents)


    cf2 = ContentFilter("not-a-file.txt")
    print("Name:", cf2.name)
    print("Contents:", cf2.contents)

    cf3 = ContentFilter([1, 2, 3])
    print("Name:", cf3.name)
    print("Contents:", cf3.contents)