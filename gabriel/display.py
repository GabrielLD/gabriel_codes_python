

import matplotlib.pyplot as plt
from matplotlib import axes
import os
from matplotlib import rc

rc('font', **{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def graphestyle_gld(axs, x,y,ftitle,xmin=0,xmax=1,ymin=0,ymax=1,loglin=False):
    
    # function to normalize the display of graphs with python
    # date : 10/07/2019
    # author : Gabriel LE DOUDIC
    
    # x takes in account a string for the abscisse axis
    # y takes in account a string for the ordinate axis
    # ftitle takes in account a string for the title of the graphs
    # tick_params donne la taille des labels des axes
    if loglin == False:
        size_labels_absciss_ordinate_title = 36
        size_ticks = 22 
    
        plt.xlabel(x, fontsize = size_labels_absciss_ordinate_title)
        plt.ylabel(y, fontsize = size_labels_absciss_ordinate_title)
        plt.title(ftitle, fontsize = size_labels_absciss_ordinate_title)
        plt.legend(fontsize = 22)
    
        axs.tick_params(labelsize = 22)
        axs.set_xlim([xmin, xmax])
        axs.set_ylim([ymin, ymax])
    
    if loglin == True:
        plt.xscale('log')
        plt.yscale('log')
        
        size_labels_absciss_ordinate_title = 36
        size_ticks = 22 

        plt.title(ftitle, fontsize = size_labels_absciss_ordinate_title)
        plt.legend(fontsize = 22)
        axs.tick_params(length = 10, width = 2, labelsize = 22)
        axs.set_xlim([xmin, xmax])
        axs.set_ylim([ymin, ymax])
        plt.xlabel(x, fontsize = size_labels_absciss_ordinate_title)
        plt.ylabel(y, fontsize = size_labels_absciss_ordinate_title)
        
        
