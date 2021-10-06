def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


text = """
your string change here to execute the command




        """

lines = (i.strip() for i in text.splitlines())

for line in lines:
    for chunk in chunkstring(line, 65):
        print(chunk)
