import os
import pickle
import PySimpleGUI as sg
from typing import Dict
import gui
import searchEngine
sg.ChangeLookAndFeel('Black')





def main():
    ''' The main loop for the program '''

    g = gui.Gui()
    s = searchEngine.SearchEngine()
    s.load_existing_index()  # load if exists, otherwise return empty list

    while True:
        event, values = g.window.read()

        if event is None:
            break
        if event == '_INDEX_':
            s.create_new_index(values)
            print()
            print(">> New index created")
            print()
        if event == '_SEARCH_':
            s.search(values)

            # print the results to output element
            print()
            for result in s.results:
                print(result)

            print()
            print(">> Searched {:,d} records and found {:,d} matches".format(s.records, s.matches))
            print(">> Results saved in working directory as search_results.txt.")


if __name__ == '__main__':
    print('Starting program...')
    main()
