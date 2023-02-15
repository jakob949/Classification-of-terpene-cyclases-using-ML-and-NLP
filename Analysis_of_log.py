#!/usr/bin/env python3

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Get unique labels for small and large classes
def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

def sort_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines.sort(key=lambda line: line.split()[0])
    with open(f"sorted_{filename}", 'w') as file:
        file.writelines(lines)

def True_Pred_large_small(log_file, class_type):
    # Read the log file
    with open(log_file, "r") as file:
        y_true = list()
        y_pred = list()
    
        # Extract true and predicted values for small and large classes
        for line in file:
            res = line.split('\t')
            # Reading the tab-formatted file
            if res[2] == class_type:
                pred = res[4][5:]
                true = res[3][5:]
                y_pred.append(pred)
                y_true.append(true)

    return y_true, y_pred
    
def confusion_matrix(y_true, y_pred):
    # Display the confusion matrix for the small class
    confusion_matrix_display = ConfusionMatrixDisplay.from_predictions(y_true, y_pred, xticks_rotation='vertical', colorbar=False)
    plt.tick_params(labelsize=8)
    
    # Increase the size of the plot
    fig = confusion_matrix_display.figure_
    dpi = fig.dpi
    fig.set_size_inches(fig.get_size_inches()[0]*3.5, fig.get_size_inches()[1]*5.75)
    
    # Save the plot as an SVG file with high resolution
    fig.savefig("confusion_matrix_small.svg", dpi=dpi*2)
    
    # Show the plot
    plt.show()


def Evalutaion_histogram(y_true_small, y_pred_small, y_true_large, y_pred_large):
    from sklearn.metrics import balanced_accuracy_score
    from sklearn.metrics import precision_score
    from sklearn.metrics import recall_score
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    
    bal_acc_large=round(balanced_accuracy_score(y_true_large, y_pred_large),2)
    bal_acc_small=round(balanced_accuracy_score(y_true_small, y_pred_small),2)
    
    preci_large=round(precision_score(y_true_large, y_pred_large, average='weighted'),2)
    preci_small=round(precision_score(y_true_small, y_pred_small, average='weighted'),2)
    
    recall_large=round(recall_score(y_true_large, y_pred_large, average='weighted'),2)
    recall_small=round(recall_score(y_true_small, y_pred_small, average='weighted'),2)
    
    acc_large=round(accuracy_score(y_true_large, y_pred_large),2)
    acc_small=round(accuracy_score(y_true_small, y_pred_small),2)
    
    f1_large=round(f1_score(y_true_large, y_pred_large, average='weighted'),2)
    f1_small=round(f1_score(y_true_small, y_pred_small, average='weighted'),2)
    
    labels_eval = ['Bal. acc.', 'Precision', 'Recall', 'Accuracy', 'f1']
   
    large_para = [bal_acc_large, preci_large, recall_large, acc_large, f1_large]
    small_para = [bal_acc_small, preci_small, recall_small, acc_small, f1_small]
    
    x = np.arange(len(labels_eval))  # the label locations
    width = 0.4  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, large_para, width, label='Large class')
    rects2 = ax.bar(x + width/2, small_para, width, label='Small class')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Different evaluation parameters - Homology reduced datasets')
    ax.set_xticks(x, labels_eval)
    ax.legend(fontsize=15)
    #
    ax.bar_label(rects1, padding=2)
    ax.bar_label(rects2, padding=2)
    
    fig.tight_layout()
    # Increase the size of the plot
    dpi = fig.dpi
    fig.set_size_inches(fig.get_size_inches()[0]*2, fig.get_size_inches()[1]*2.5)
    
    # Save the plot as an SVG file with high resolution
    fig.savefig("histogram.svg", dpi=dpi*2)
    
    plt.show()


def Evalutaion_histogram_error_bars(y_true_small, y_pred_small, y_true_large, y_pred_large):
    from sklearn.metrics import balanced_accuracy_score
    from sklearn.metrics import precision_score
    from sklearn.metrics import recall_score
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import f1_score
    
    bal_acc_large=round(balanced_accuracy_score(y_true_large, y_pred_large),2)
    bal_acc_small=round(balanced_accuracy_score(y_true_small, y_pred_small),2)
    
    preci_large=round(precision_score(y_true_large, y_pred_large, average='weighted'),2)
    preci_small=round(precision_score(y_true_small, y_pred_small, average='weighted'),2)
    
    recall_large=round(recall_score(y_true_large, y_pred_large, average='weighted'),2)
    recall_small=round(recall_score(y_true_small, y_pred_small, average='weighted'),2)
    
    acc_large=round(accuracy_score(y_true_large, y_pred_large),2)
    acc_small=round(accuracy_score(y_true_small, y_pred_small),2)
    
    f1_large=round(f1_score(y_true_large, y_pred_large, average='weighted'),2)
    f1_small=round(f1_score(y_true_small, y_pred_small, average='weighted'),2)
    
    labels_eval = ['Bal. acc.', 'Precision', 'Recall', 'Accuracy', 'f1']
   
    large_para = [bal_acc_large, preci_large, recall_large, acc_large, f1_large]
    small_para = [bal_acc_small, preci_small, recall_small, acc_small, f1_small]
    
    x = np.arange(len(labels_eval))  # the label locations
    width = 0.4  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, large_para, width, label='Large class', yerr=np.std(large_para)/np.sqrt(len(large_para)))
    rects2 = ax.bar(x + width/2, small_para, width, label='Small class', yerr=np.std(small_para)/np.sqrt(len(small_para)))
    
    # Add some text for labels, title and custom
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title('Different evaluation parameters - Redudant datasets')
    ax.set_xticks(x, labels_eval)
    ax.legend(fontsize=12, loc = 'upper left')
    #
    ax.bar_label(rects1, padding=2)
    ax.bar_label(rects2, padding=2)
    
    fig.tight_layout()
    # Increase the size of the plot
    dpi = fig.dpi
    fig.set_size_inches(fig.get_size_inches()[0]*2, fig.get_size_inches()[1]*2.5)
    
    # Save the plot as an SVG file with high resolution
    fig.savefig("histogram.svg", dpi=dpi*2)
    
    plt.show()

def histogram_class_distribution(reduced_class, non_reduced, labels):
    """
    Parameters
    ----------
    reduced_class : list or set
        Containing a list with number of sequences of each class, reduced.
        following the same order as the labels list
    non_reduced : list or set
        Containing a list with number of sequences of each class, not reduced.
        following the same order as the labels list
    non_reduced : list or set.
    labels : list or set
        list of class labels. 

    Returns
    -------
    Makes a histograms plots of class distribution
    
    
    Vars:
        # #large classes
        labels =['1-6-MTC', '1-6-STC', '1-7-STC', '1-10-DTC', '1-10-STC', '1-11-DTC', '1-11-STC', '1-14-DTC']
        large_NHR =      [4, 184, 8, 4, 246, 2, 81 ,3]
        large_homo_red = [4, 12, 3, 4, 76, 2, 16, 3]
        labels_small =[' (+)-(1(10)E,4E,6S,7R)-Germacradien-6-ol', ' (+)-4-epi-Cubebol_Synthase', ' (+)-Allohedycaryol_Synthase', ' (+)-Caryolan-1-ol_Synthase', ' (+)-Eremophilene_Synthase', ' (+)-Isodauc-8-en-11-ol_Synthase', ' (+)-T-Muurolol_Synthase', ' (+)-epi-Cubenol_Synthase', ' (-)-Germacradien-4-ol_Synthase', ' (-)-Isohirsut-4-ene_Synthase', ' (-)-Neomeranol_B_Synthase', ' (-)-a-Amorphene_Synthase', ' 2-Methylisoborneol_Synthase', ' 7-epi-a-Eudesmol_Synthase', ' Avermitilol_Synthase', ' Cembrene_C_Synthase', ' Geosmin_Synthase', ' Germacrene_A_Synthase', ' Isoafricanol_Synthase', ' Pentalenene_Synthase', ' Pristinol_Synthase', ' Selina-3,7(11)-diene_Synthase', ' Selina-4(15),7(11)-diene_Synthase', ' epi-Isozizaene_Synthase', ' epi-Zizaene_Synthase']
        reduced_class_small = [0, 0, 0, 2, 2, 3, 3, 3, 4, 2, 0,  21, 2, 5, 6,  2,  2,   2, 0, 5, 3, 3, 12, 10, 0] 
        not_reduced_small  = [5, 2, 5, 42, 2, 8, 3, 50, 15, 9, 5, 42, 2, 38, 20,2, 2, 3, 7, 17, 3, 6, 39, 178, 5]
    """
        
    labels_eval = labels

    x = np.arange(len(labels))  # the label locations
    width = 0.4  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, reduced_class, width, label='Reduced')
    rects2 = ax.bar(x + width/2, non_reduced, width, label='Not reduced')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of sequences')
    ax.set_title('Class distribution. Homology reduced VS redundant datasets')
    ax.set_xticks(x, labels_eval)
    ax.legend(fontsize=15)
    #
    ax.bar_label(rects1, padding=2)
    ax.bar_label(rects2, padding=2)
    
    fig.tight_layout()
    # Increase the size of the plot
    dpi = fig.dpi
    fig.set_size_inches(fig.get_size_inches()[0]*2, fig.get_size_inches()[1]*2.5)
    
    # Save the plot as an SVG file with high resolution
    fig.savefig("histogram_class_distribution.svg", dpi=dpi*2)
    
    plt.show()
    

def histogram_class_distribution_jumping_y_axis(reduced_class, non_reduced, labels):
    
    labels_eval = labels

    x = np.arange(len(labels))  # the label locations
    width = 0.4  # the width of the bars

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    
    # plot the same data on both axes
    rects1a = ax1.bar(x - width/2, reduced_class, width, label='Reduced')
    rects2a = ax1.bar(x + width/2, non_reduced, width, label= 'Not reduced')
    rects1b = ax2.bar(x - width/2, reduced_class, width, label='reduced')
    rects2b = ax2.bar(x + width/2, non_reduced, width, label='Not reduced')

    # zoom-in / limit the view to different portions of the data
    ax1.set_ylim(160, 185)  # outliers only
    ax2.set_ylim(0, 65)  # most of the data

    # hide the spines between ax and ax2
    ax1.spines.bottom.set_visible(False)
    ax2.spines.top.set_visible(False)
    ax1.xaxis.tick_top()
    ax1.tick_params(labeltop=False)  # don't put tick labels at the top
    ax2.xaxis.tick_bottom()

    # Now, let's turn towards the cut-out slanted lines.
    # We create line objects in axes coordinates, in which (0,0), (0,1),
    # (1,0), and (1,1) are the four corners of the axes.
    # The slanted lines themselves are markers at those locations, such that the
    # lines keep their angle and position, independent of the axes size or scale
    # Finally, we need to disable clipping.

    d = .5  # proportion of vertical to horizontal extent of the slanted line
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
                  linestyle="none", color='k', mec='k', mew=1, clip_on=False)
    ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
    ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax2.set_ylabel('Number of sequences')
    ax2.set_xticks(x)
    #
    ax2.bar_label(rects1b, padding=2)
    ax2.bar_label(rects2b, padding=2)
    ax1.bar_label(rects1b, padding=2)
    ax1.bar_label(rects2b, padding=2)    
    
    ax1.legend(fontsize=15, loc='upper left')
    ax1.set_title('Class distribution. Homology reduced VS redundant datasets')
    fig.tight_layout()
    # Increase the size of the plot
    dpi = fig.dpi
    fig.set_size_inches(fig.get_size_inches()[0]*2, fig.get_size_inches()[1]*2.5)
    fig.subplots_adjust(hspace=.025)  # adjust space between axes

    # Save the plot as an SVG file with high resolution
    fig.savefig("histogram_class_distribution.svg", dpi=dpi*2)
    
    plt.show()
    
def fasta_in_class_vs_acc_out(fasta_in, acc_vs_class):
    """
    
    Parameters
    ----------
    fasta_in : A fasta-format file from e.g. CD-hit.
    
    acc_vs_class : TYPE
        takes an file with the format class_vs_acc e.g. class_vs_acc_v2.txt

    Returns
    -------
    Creates a matching file for the input fasta file! 

    """
    with open(f"acc_vs_class_{fasta_in}.txt", 'w') as outfile:
        with open(fasta_in, "r") as fasta_in:    
            
            for line in fasta_in:
                if line[0]=='>':
                    acc = line.split('_')[0]
                    accvclass = open(acc_vs_class, 'r')                  
                    for i, line1 in enumerate(accvclass):
                                                  
                        if acc == line1.split('\t')[1].split('_')[0]:
                            print(line1, end='', sep='', file=outfile)
                            accvclass.close()
                            break


# sort_file('acc_vs_class_Homo_red_small.txt')

# fasta_in_class_vs_acc_out('cd_hit_80_large_class.faa', 'class_vs_acc_v2.txt')
log_file = "log_13022023_VAL_small_NHR.txt"
y_true_small, y_pred_small = True_Pred_large_small(log_file, "small")
# log_file = "log_13022023_VAL_small_NHR.txt"
# y_true_large, y_pred_large = True_Pred_large_small(log_file, "large")


# confusion_matrix(y_true_small, y_pred_small)

# Evalutaion_histogram_error_bars(y_true_small, y_pred_small, y_true_large, y_pred_large)

labels_small = unique(y_true_small)
print(labels_small)