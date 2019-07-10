import matplotlib.pyplot as plt
from matplotlib import axes
import os
from matplotlib import rc

rc('font', **{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)



def save_fig_gld(ffilename):
    
    # function to save the figures with the good format png and good resolution 
    # date : 10/07/2019
    # author : Gabriel LE DOUDIC
    
    #ffilename : takes a string where the path to the savefolder is and then the name of the fig
    #savefolder = '/home/gld/Documents/PhD_Gabriel/Data_lambda/'
    #filename = savefolder + 'lambda_epaisseur_linlin'
    #save_fig_gld(filename)
    
    if not os.path.isdir(os.path.dirname(ffilename)):
        os.mkdir(os.path.dirname(ffilename))
    plt.savefig(ffilename,bbox_inches='tight',dpi=300)   
