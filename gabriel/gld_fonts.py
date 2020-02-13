import matplotlib as mpl

def gl_fonts():
    mpl.rc('text', usetex=True)
    mpl.rcParams['text.latex.preamble'] = [
        r'\usepackage{tgheros}', # helvetica font
        r'\usepackage{sansmath}', # math-font matching helvetica
    r'\sansmath' # actually tell tex to use it!
r'\usepackage[scientific-notation=false]{siunitx}', # micro symbols
        r'\sisetup{detect-all}', # force siunitx to use the fonts
    ]
