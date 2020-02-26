import os
with open('db.txt', 'r') as db:
    content = [line.strip() for line in db]
content.sort()
with open('scanned_saved.txt', 'r+') as sc:
    saved_content = [line.strip() for line in sc]
with open('scanned.txt', 'r+') as reading:
    scanned_content = [line.strip() for line in reading]
list_of_scanned_components = []
summary_list = list_of_scanned_components + saved_content
print('All rights reserved Mateusz Redzynia')
print('Type menu anyware to pop-up menu.')
print('Type exit anyware to exit.')
    
def scanning():
    while True:
        summary_list = list_of_scanned_components + saved_content
        text = input('Scan code: ')
        if text == 'menu':
            menu()
        if text == 'exit':
            exit()
        if text in content:
            
            if text in summary_list or list_of_scanned_components:
                print('Already scanned!') 
                continue       
            else:
                print('Scanned. Remaining scans: {}'.format(len(content)-len(summary_list)))
                with open('scanned.txt', 'w+') as writing:
                    list_of_scanned_components.append(text)
                    writing.writelines('\n'.join(list_of_scanned_components))
                continue
        if text not in content:
            print('Not found, scan again or write it manually.')
            continue
    writing.close
    reading.close
    db.close
    

def raporting():
    summary_list = list_of_scanned_components + saved_content
    print('Total: {}'.format(len(content)))
    print('Scanned components: {}'.format(len(summary_list)))
    print('Records to scans: {}'.format(len(content)-len(summary_list)))
    for x in range(len(content)):
        if content[x] in summary_list:
            print('{} ............ Scanned.'.format(content[x]))
        else:
            print('{} ............ Not scanned.'.format(content[x]))
    menu()
def savefile():
    summary_list = list_of_scanned_components + saved_content
    with open('scanned_saved.txt', 'w+') as sf:
        sf.writelines('\n'.join(summary_list))
    print('Data succesfully saved.')
    sf.close
    menu()
def menu():
    print('1. Start scanning.')
    print('2. Print raport.')
    print('3. Save data to scanned_saved.txt')
    choice = input('Your choice: ')
    if choice == '1':
        scanning()
    elif choice == '2':
        raporting()
    elif choice == '3':
        savefile()

menu()
