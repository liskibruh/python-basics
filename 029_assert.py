def main():
    
    def print_list(some_list):
        assert type(some_list)==list, ['pass type:list to the function']
        print([elem for elem in some_list])
        
    print_list(2)

if __name__ == "__main__":
    main()