def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    filename = "day1.txt"
    try:
        data = read_file(filename)
        print("Data from day1.txt:")
        print(data)
    except Exception as e:
        print(f"Error: {e}")
