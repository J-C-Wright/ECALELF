import json
from math import sqrt

def get_inital_commands_and_title(info_dict=None):

    people_dict = info_dict['people']
    validation_name = info_dict['title']
    meeting_date = info_dict['date']
    
    
    code = '\n'
    code += '\\documentclass{beamer}\n'
    code += '\\usepackage{graphicx}\n'
    code += '\\usepackage[font={small}]{caption}'

    #Title and subtitle
    code += '\\title{Monitoring and Validation with Z$\\rightarrow$e$^{+}$e$^{-}$}\n'
    code += '\\subtitle{'+validation_name+'}\n'

    #Date
    code += '\\date{'+meeting_date+'}\n'

    names = people_dict.keys()
    #Institutes
    code += '\\institute{\n'

    institutes = []
    for key,info in people_dict.iteritems():
        if people_dict[key]['institute'] not in institutes:
            institutes.append(people_dict[key]['institute'])

    for i,institute in enumerate(institutes):
        code += '\t\\inst{'+str(i+1)+'}\n'
        code += '\t'+institute+'\n'
        if i+1 != len(institutes):
            code += ' \t\\and\n'
        else:
            code += '\n}\n'

    #Authors
    code += '\\author{ '
    for i,name in enumerate(names):
        code += people_dict[name]['name']
        
        code += '\\inst{'
        for j,institute in enumerate(institutes):
            if people_dict[name]['institute'] == institute:
                code += str(j+1)+'}'

        if i+1 != len(names):
            code += ' \\and '
        else:
            code += '}\n'
    #Subject
    code += '\\subject{CMS ECAL Monitoring and Calibration}\n'
    code += '\n'
    code += '\\begin{document}\n'
    code += '\\frame{\\titlepage}\n'

    return code

def make_introduction_frame(info_dict=None):

    code = '\n'
    code += '\\begin{frame}\n'
    code += '\\frametitle{Introduction}\n'
    code += '\\begin{itemize}\n'

    code += '\\item Dataset: {'+info_dict['dataset']+'}\n'
    code += '\\item Global Tag: {'+info_dict['globaltag'].replace('_','\\_')+'}\n'
    code += '\\item Rereco Tag: {'+info_dict['rerecotag'].replace('_','\\_')+'}\n'
    code += '\\item MC name: {'+info_dict['mcname'].replace('_','\\_')+'}\n'
    code += '\\item Invariant mass: {'+info_dict['invmass'].replace('_','\\_')+'}\n'
    code += '\\item Selection: {'+info_dict['selection'].replace('_','\\_')+'}\n'
    code += '\\item Fit: {'+info_dict['fit']+'}\n'
    
    code += '\\end{itemize}\n'
    
    code += '\\end{frame}\n'
    code += '\n'

    return code

def make_scale_slide(info_dict=None):

    code = '\n'
    code += '\\begin{frame}\n'
    code += '\\frametitle{Z Peak Scale}\n'

    code += 'Fit with '+info_dict['fit']+'\n\n\n'

    code += '\\dualslide{\n'

    code += '\\begin{center}\n'
    code += '\\scalebox{0.8}{\n'
    code += '\\begin{equation*}\n'
    code += '   \\Delta P = \\frac{\\Delta m_{data} - \\Delta m_{MC}}{m_{Z}}\n'
    code += '\\end{equation*}\n'
    code += '}\n'
    code += '\\end{center}\n'

    code += '}{\n'

    code += '\\begin{description}\n'
    code += '\\item [golden:] $R9 > 0.94$\n'
    code += '\\item [showering:] $R9 < 0.94$\n'
    code += '\\end{description}\n'

    code += '}\n'

    code += '\\begin{table}\n'
    code += '\\begin{center}\n'
    code += '\\scalebox{0.8}{\n'

    column_labels = ['Events','$\\Delta m_{data}$','$\\Delta m_{MC}$','$\\Delta$P (\%)']
    column_indices = [1,2,3,4]
    code += make_table(table_path=info_dict['summary_table'],column_labels=column_labels,column_indices=column_indices)

    code += '}\n'
    code += '\\end{center}\n'
    code += '\\end{table}\n'

    code += '\\end{frame}\n'
    code += '\n'

    return code

def make_width_slide(info_dict=None):

    code = '\n'
    code += '\\begin{frame}\n'
    code += '\\frametitle{Z Width}\n'

    code += 'Fit with '+info_dict['fit']+'\n\n\n'

    code += '\\dualslide{\n'

    code += '\\begin{center}\n'
    code += '\\scalebox{0.8}{\n'
    code += '\\begin{equation*}\n'
    code += '\\text{add. smear.}  = \\sqrt{2 \\cdot \\left( \\left(\\frac{\\sigma_{CB}}{peak_{CB}}^{data}\\right)^2 - \\left({\\frac{\\sigma_{CB}}{peak_{CB}}}^{MC}\\right)^2 \\right)} \n'
    code += '\\end{equation*}\n'
    code += '}\n'
    code += '\\end{center}\n'

    code += '}{\n'
    code += '\\begin{description}\n'
    code += '\\item [golden:] $R9 > 0.94$\n'
    code += '\\item [showering:] $R9 < 0.94$\n'
    code += '\\end{description}\n'
    code += '}\n'

    code += '\\begin{table}\n'
    code += '\\begin{center}\n'
    code += '\\scalebox{0.8}{\n'

    column_labels = ['Events','$\\frac{\\sigma}{m_{data}}$','$\\frac{\\sigma}{m_{data}}$','add. smear']
    column_indices = [1,7,8,9]
    code += make_table(table_path=info_dict['summary_table'],column_labels=column_labels,column_indices=column_indices)
    
    code += '}\n'
    code += '\\end{center}\n'
    code += '\\end{table}\n'

    code += '\\end{frame}\n'
    code += '\n'

    return code

def make_effsigma_slide(info_dict=None):

    code = '\n'
    code += '\\begin{frame}\n'
    code += '\\frametitle{Z Width $\\sigma_{eff}$}\n'

    code += 'Fit with '+info_dict['fit']+'\n\n\n'

    code += '\\dualslide{\n'
    code += '\\begin{equation*}\n'
    code += '$ placeholder $\n'
    code += '\\end{equation*}\n'
    code += '}{\n'
    code += '\\begin{description}\n'
    code += '\\item [golden:] $R9 > 0.94$\n'
    code += '\\item [showering:] $R9 < 0.94$\n'
    code += '\\end{description}\n'
    code += '}\n'

    code += '\\begin{table}\n'
    code += '\\begin{center}\n'
    code += '\\scalebox{0.8}{\n'

    column_labels = ['Events','$\\sigma_{eff30}$(data)','$\\sigma_{eff30}$(MC)','$\\sigma_{eff50}$(data)','$\\sigma_{eff50}$(MC)']
    column_indices = [1,16,17,18,19]
    code += make_table(table_path=info_dict['summary_table'],column_labels=column_labels,column_indices=column_indices)

    code += '}\n'
    code += '\\end{center}\n'
    code += '\\end{table}\n'

    code += '\\end{frame}\n'
    code += '\n'

    return code




def make_table_comparison_slide(info_dict=None,table_path1=None,table_path2=None,column_labels=None,column_indices=None,expression=None,title=None):

    code = '\n'
    code += '\\begin{frame}\n'
    code += '\\frametitle{%s}\n'%title

    code += 'Fit with '+info_dict['fit']+'\n\n\n'

    code += '\\dualslide{\n'
    code += '\\begin{equation*}\n'
    code += '%s\n'%expression
    code += '\\end{equation*}\n'
    code += '}{\n'
    code += '\\begin{description}\n'
    code += '\\item [golden:] $R9 > 0.94$\n'
    code += '\\item [showering:] $R9 < 0.94$\n'
    code += '\\end{description}\n'
    code += '}\n'

    code += '\\begin{table}\n'
    code += '\\begin{center}\n'
    code += '\\scalebox{0.8}{\n'

    code += make_comparison_table(table_path1=table_path1,table_path2=table_path2,column_labels=column_labels,column_indices=column_indices)

    code += '}\n'
    code += '\\end{center}\n'
    code += '\\end{table}\n'

    code += '\\end{frame}\n'
    code += '\n'

    return code






def make_comparison_table(table_path1=None,table_path2=None,column_labels=None,column_indices=None):
    
    with open(table_path1,'r') as tab:
        lines1 = tab.read().split('\n')
    with open(table_path2,'r') as tab:
        lines2 = tab.read().split('\n')

    table = '\\begin{tablular}{|l|c|*{%d}{c|}} \\hline\n'%len(column_labels)
    table += 'Region & '+' & '.join(column_labels)+'\\\\ \n'

    table += '\\hline\n'
    table += '\\hline\n'

    for line1,line2 in zip(lines1,lines2):

        if line1 == '': continue
        if line1[0] == '#': continue
        if line2 == '': continue
        if line2[0] == '#': continue

        values1 = line1.split('&')
        values2 = line2.split('&')

        table += label_parser(values1[0])
        for i in column_indices:
            table += ' & ' + number_comparison_parser(string1=values1[i],string2=values2[i])
        table += '\\\\ \n'

    table += '\\hline\n'
    table += '\\end{tabular}\n'

    return table
    
    


def make_table(table_path=None,column_labels=None,column_indices=None):

    with open(table_path,'r') as tab:
        lines = tab.read().split('\n')

    table = '\\begin{tabular}{|l|c|*{%d}{c|}} \\hline\n'%len(column_labels)
    table += 'Region & '+' & '.join(column_labels) + '\\\\ \n'

    table += '\\hline\n'
    table += '\\hline\n'

    for line in lines:

        if line == '': continue
        if line[0] == '#': continue

        values = line.split('&')
        table += label_parser(values[0])
        for i in column_indices:
            table += ' & ' + number_parser(string=values[i])
        table += '\\\\ \n'
    table += '\\hline\n'
    table += '\\end{tabular}\n'

    return table

def number_comparison_parser(string1=None,string2=None,places=2):

    num1 = float(string1.split('\\pm')[0].replace('$',''))
    num2 = float(string2.split('\\pm')[0].replace('$',''))
    err1 = 0
    err2 = 0

    if len(string1.split('\\pm')) == 2:
        err1 = float(string1.split('\\pm')[1].replace('$',''))
    if len(string2.split('\\pm')) == 2:
        err2 = float(string2.split('\\pm')[1].replace('$',''))

    value = num1 - num2
    if err1 != 0 and err2 != 0:
        err = sqrt(err1**2 + err2**2)
        format_str = '$ %4.'+str(places)+'f \\pm %4.'+str(places)+'f $'
        return format_str%(value,err)
    else:
        format_str = '$ %4.'+str(places)+'f $'
        return format_str%(value)




def number_parser(string=None,places=2):

    parts = string.replace('$','').split('\\pm')
    
    if len(parts) > 1:
        value = float(parts[0])
        error = float(parts[1])
        format_str = '$ %4.'+str(places)+'f \\pm %4.'+str(places)+'f $'
        return format_str%(value,error)
    elif len(parts) == 1 and '.' in string:
        value = float(parts[0])
        format_str = '$ %4.'+str(places)+'f $'
        return format_str%(value)
    elif len(parts) == 1 and '.' not in string:
        return parts[0]



def label_parser(string=None):

    label = ''

    parts = string.replace(' ','').split('-')
    
    for part in parts:
        if part == 'EB':
            label += part
        elif part == 'EE':
            label += part
        elif part == 'absEta_0_1':
            label += ' $|\\eta| < 1$'
        elif part == 'absEta_1_1.4442':
            label += ' $|\\eta| > 1$'
        elif part == 'absEta_1.566_2':
            label += ' $|\\eta| < 2$'
        elif part == 'absEta_2_2.5':
            label += ' $|\\eta| > 2$'
        elif part == 'gold':
            label += ' R$_{9} > 0.94$'
        elif part == 'bad':
            label += ' R$_{9} < 0.94$'

    return label
    





def make_barrel_mc_data_plots_slide(info_dict=None):

    code = '\n'
    code += '\\begin{frame}\n'
    code += '\\frametitle{EB Fits}\n'

    code += make_mc_data_six_plots(info_dict=info_dict,regions=['EB','EB-absEta_0_1','EB-absEta_1_1.4442']) 

    code += '\\end{frame}\n'
    code += '\n'

    return code

def make_endcap_mc_data_plots_slide(info_dict=None):

    code = '\n'
    code += '\\begin{frame}\n'
    code += '\\frametitle{EE Fits}\n'

    code += make_mc_data_six_plots(info_dict=info_dict,regions=['EE','EE-absEta_1.566_2','EE-absEta_2_2.5'])

    code += '\\end{frame}\n'
    code += '\n'

    return code

def make_duo_history_slide(info_dict=None,variable=None,xvar='run_min_even',regions=['EB','EE'],title=None):

    code = '\n'
    code += '\\begin{frame}\n'
    code += '\\frametitle{%s}\n'%title
    path = info_dict['historyplots']+'/'+xvar+'/'

    code += '\\begin{figure}\n'
    code += '\\includegraphics[width=0.98\\linewidth,natwidth=610,natheight=642]{{%s%s_%s}.pdf}\n'%(path,regions[0],variable)
    code += '\\end{figure}\n'

    code += '\\begin{figure}\n'
    code += '\\includegraphics[width=0.98\\linewidth,natwidth=610,natheight=642]{{%s%s_%s}.pdf}\n'%(path,regions[1],variable)
    code += '\\end{figure}\n'

    code += '\\end{frame}\n'
    code += '\n'

    return code


def make_mc_data_six_plots(info_dict=None,regions=None):

    code = ''
    code += '\\begin{columns}\n'

    code += '\\column{0.333\\textwidth}\n'
    code += '\\begin{minipage}[c][0.4\\textheight][c]{\\linewidth}\n'

    code += '\\begin{figure}\n'
    code += '\\caption{'+label_parser(regions[0])+'}\n'
    code += '\\centering\n'
    code += '\\includegraphics[width=0.98\\linewidth,natwidth=610,natheight=642]{{%s-Et_25}.pdf}\n'%(info_dict['data_fit_plots']+regions[0])
    code += '\\end{figure}\n'
    code += '\\end{minipage}\n'

    code += '\\begin{minipage}[c][0.4\\textheight][c]{\\linewidth}\n'
    code += '\\begin{figure}\n'
    code += '\\centering\n'
    code += '\\includegraphics[width=0.98\\linewidth,natwidth=610,natheight=642]{{%s-Et_25}.pdf}\n'%(info_dict['mc_fit_plots']+regions[0])
    code += '\\caption{'+label_parser(regions[0])+'}\n'
    code += '\\end{figure}\n'
    code += '\\end{minipage}\n'

    code += '\\column{0.333\\textwidth}\n'
    code += '\\begin{minipage}[c][0.4\\textheight][c]{\\linewidth}\n'
    code += '\\begin{figure}\n'
    code += '\\caption{'+label_parser(regions[1])+'}\n'
    code += '\\centering\n'
    code += '\\includegraphics[width=0.98\\linewidth,natwidth=610,natheight=642]{{%s-Et_25}.pdf}\n'%(info_dict['data_fit_plots']+regions[1])
    code += '\\end{figure}\n'
    code += '\\end{minipage}\n'

    code += '\\begin{minipage}[c][0.4\\textheight][c]{\\linewidth}\n'
    code += '\\begin{figure}\n'
    code += '\\centering\n'
    code += '\\includegraphics[width=0.98\\linewidth,natwidth=610,natheight=642]{{%s-Et_25}.pdf}\n'%(info_dict['mc_fit_plots']+regions[1])
    code += '\\caption{'+label_parser(regions[1])+'}\n'
    code += '\\end{figure}\n'
    code += '\\end{minipage}\n'

    code += '\\column{0.333\\textwidth}\n'
    code += '\\begin{minipage}[c][0.4\\textheight][c]{\\linewidth}\n'
    code += '\\begin{figure}\n'
    code += '\\centering\n'
    code += '\\caption{'+label_parser(regions[2])+'}\n'
    code += '\\includegraphics[width=0.98\\linewidth,natwidth=610,natheight=642]{{%s-Et_25}.pdf}\n'%(info_dict['data_fit_plots']+regions[2]  )
    code += '\\end{figure}\n'
    code += '\\end{minipage}\n'

    code += '\\begin{minipage}[c][0.4\\textheight][c]{\\linewidth}\n'
    code += '\\begin{figure}\n'
    code += '\\centering\n'
    code += '\\includegraphics[width=0.98\\linewidth,natwidth=610,natheight=642]{{%s-Et_25}.pdf}\n'%(info_dict['mc_fit_plots']+regions[2])
    code += '\\caption{'+label_parser(regions[2])+'}\n'
    code += '\\end{figure}\n'
    code += '\\end{minipage}\n'

    code += '\\end{columns}\n'

    return code



