def main():

    names = ['Howard', 'Jamie', 'Jill']

    print('the list before insert or remove')
    print(names)

    name_remove = input('Enter a name to remove: ')

    names.insert(0, 'Joe')
    names.remove(name_remove)

    print('the list after insert and remove')
    print(names)

main()
