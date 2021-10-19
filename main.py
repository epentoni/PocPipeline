# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import files_from
import spades_asinc

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(files_from.files_from('/bin/*.sh'))
    spades_asinc.spades_asinc('output_path', 'file1 file2 file3 file4 file5'.split())


