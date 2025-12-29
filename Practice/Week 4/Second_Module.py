def main():
    print(f"Second Module's name: {__name__}")

if __name__ == '__main__':
    print("Run directly")
    main()
else:
    print('Run from import')
    print(f"Second Module's name: {__name__}")

