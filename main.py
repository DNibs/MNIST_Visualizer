"""
Author: David Niblick
Date: 22 SEP 2020

Visualizes MNIST dataset formatted as CSV with first column as label followed by 785 columns of pixel values.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db_fn = input('What is the MNIST filename? (Must be in same folder.)\n')
    db = pd.read_csv(db_fn, header=None)
    mnist_array = db.to_numpy()
    quit_app = False
    while not quit_app:
        record_idx = input('Which record do you want to see? Type in the row number and press "Enter". \n'
                           'Close image to try another record. \n'
                           'If you want to close, press "q" and hit "Enter". \n')
        if record_idx == 'q':
            exit()
        record_idx = int(record_idx)

        digit = mnist_array[record_idx, :].copy()
        label = digit[0]
        data = digit[1:].copy().reshape([28,28])
        fig = plt.figure()
        ax = fig.add_subplot()
        imgplot = plt.imshow(data, cmap='gray')
        ax.set_title('Record: {}  Target Number = {}'.format(record_idx, label))
        plt.show()