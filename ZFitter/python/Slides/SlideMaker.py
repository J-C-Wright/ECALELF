import json

def make_title_commands(info_dict=None):

    people_dict = info_dict['people']
    validation_name = info_dict['title']
    meeting_date = info_dict['date']
    
    code = '\n'

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

    return code

def make_introduction_frame(info_dict=None):

    code = '\n'
    code += '\\begin{frame}\n'
    code += '\\frametitle{Introduction}\n'
    code += '\\begin{itemize}\n'

    code += '\\item Dataset: '+info_dict['dataset']+'\n'
    code += '\\item Global Tag: '+info_dict['globaltag']+'\n'
    code += '\\item Rereco Tag: '+info_dict['rerecotag']+'\n'
    code += '\\item MC name: '+info_dict['mcname']+'\n'
    code += '\\item Invariant mass: '+info_dict['invmass']+'\n'
    code += '\\item Selection: '+info_dict['selection']+'\n'
    code += '\\item Fit: '+info_dict['fit']+'\n'
    
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
    code += '$ \\Delta P = \\frac{\\Delta m_{data} - \\Delta m_{MC}}{m_{Z}}$\n'
    code += '}{\n'
    code += '\\begin{description}\n'
    code += '\\item [golden:] $R9 > 0.94$\n'
    code += '\\item [showering:] $R9 < 0.94$\n'
    code += '\\end{description}\n'
    code += '}\n'

    code += '\\begin{table}\n'
    code += '\\begin{center}\n'
    code += '\\scalebox{0.7}{\n'
    code += make_scale_table(table_path=info_dict['summary_table'])
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
    code += '$ placeholder $\n'
    code += '}{\n'
    code += '\\begin{description}\n'
    code += '\\item [golden:] $R9 > 0.94$\n'
    code += '\\item [showering:] $R9 < 0.94$\n'
    code += '\\end{description}\n'
    code += '}\n'

    code += '\\begin{table}\n'
    code += '\\begin{center}\n'
    code += '\\scalebox{0.7}{\n'
    code += make_width_table(table_path=info_dict['summary_table'])
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
    code += '$ placeholder $\n'
    code += '}{\n'
    code += '\\begin{description}\n'
    code += '\\item [golden:] $R9 > 0.94$\n'
    code += '\\item [showering:] $R9 < 0.94$\n'
    code += '\\end{description}\n'
    code += '}\n'

    code += '\\begin{table}\n'
    code += '\\begin{center}\n'
    code += '\\scalebox{0.7}{\n'
    code += make_effsigma_table(table_path=info_dict['summary_table'])
    code += '}\n'
    code += '\\end{center}\n'
    code += '\\end{table}\n'

    code += '\\end{frame}\n'
    code += '\n'

    return code



def number_parser(string=None,places=2):

    parts = string.replace('$','').split('\\pm')
    
    if len(parts) > 1:
        value = float(parts[0])
        error = float(parts[1])
        format_str = '$ %4.'+str(places)+'f \\pm %4.'+str(places)+'f $'
        return format_str%(value,error)
    elif len(parts) == 1:
        value = float(parts[0])
        format_str = '$ %4.'+str(places)+'f $'
        return format_str%(value)



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
    


def make_scale_table(table_path=None):

    with open(table_path,'r') as tab:
        lines = tab.read().split('\n')

    table = '\\begin{tabular}{|l|c|*{3}{c|}} \\hline\n'
    table += 'ECAL Region of & selected  & $\\Delta m_{data}$ & $\\Delta m_{MC}$  & $\\Delta$P (\%) \\\\ \n'
    table += 'the two electrons & events & (GeV) & (GeV) & \\\\ \n'
    table += '\\hline\n'
    table += '\\hline\n'
    for line in lines:
        if line == '': continue
        if line[0] == '#': continue
        values = line.split('&')
        table += label_parser(values[0])+'&'+values[1]
        for string in values[2:5]:
            table += ' & ' + number_parser(string=string)
        table += '\\\\ \n'
    table += '\\hline\n'
    table += '\\end{tabular}\n'

    return table


def make_width_table(table_path=None):

    with open(table_path,'r') as tab:
        lines = tab.read().split('\n')

    table = '\\begin{tabular}{|l|c|*{3}{c|}} \\hline\n'
    table += 'ECAL Region of & selected  & $\\frac{\\sigma}{m_{data}}$ & $\\frac{\\sigma}{m_{data}}$  & add. smear  \\\\ \n'
    table += 'the two electrons & events &  &  & \\\\ \n'
    table += '\\hline\n'
    table += '\\hline\n'
    for line in lines:
        if line == '': continue
        if line[0] == '#': continue
        values = line.split('&')
        table += label_parser(values[0])+'&'+values[1]
        for string in values[7:10]:
            table += ' & ' + number_parser(string=string)
        table += '\\\\ \n'
    table += '\\hline\n'
    table += '\\end{tabular}\n'

    return table

def make_effsigma_table(table_path=None):

    with open(table_path,'r') as tab:
        lines = tab.read().split('\n')

    table = '\\begin{tabular}{|l|c|*{4}{c|}} \\hline\n'

    table += 'ECAL Region of & selected  & $\\sigma_{eff30}$(data) & $\\sigma_{eff30}$(MC)  & $\\sigma_{eff50}$(data) & $\\sigma_{eff50}$(MC)  \\\\ \n'
    table += 'the two electrons & events &  &  &  &\\\\ \n'
    table += '\\hline\n'
    table += '\\hline\n'

    for line in lines:
        if line == '': continue
        if line[0] == '#': continue
        values = line.split('&')
        table += label_parser(values[0])+'&'+values[1]
        for string in values[16:20]:
            table += ' & '+number_parser(string=string)
        table += '\\\\ \n'
    table += '\\hline\n'
    table += '\\end{tabular}\n'

    return table
    







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








with open('python/slides_info.json','r') as jf:

    info_dict = json.loads(jf.read())

    title_slide_commands = make_title_commands(info_dict=info_dict)

    intro_frame = make_introduction_frame(info_dict=info_dict)

    scale_frame = make_scale_slide(info_dict=info_dict)

    width_frame = make_width_slide(info_dict=info_dict)
    effsigma_frame = make_effsigma_slide(info_dict=info_dict)
    EB_mc_data_plots =  make_barrel_mc_data_plots_slide(info_dict=info_dict)
    EE_mc_data_plots =  make_endcap_mc_data_plots_slide(info_dict=info_dict)

    EBEE_deltaM_history_plots = make_duo_history_slide(info_dict=info_dict,variable='Delta_m',regions=['EB','EE'],title='EB/EE $\\Delta$m history')
    EB_deltaM_history_plots = make_duo_history_slide(info_dict=info_dict,variable='Delta_m',regions=['EB-absEta_0_1','EB-absEta_1_1.4442'],title='EB regions $\\Delta$m history')
    EE_deltaM_history_plots = make_duo_history_slide(info_dict=info_dict,variable='Delta_m',regions=['EE-absEta_1.566_2','EE-absEta_2_2.5'],title='EE regions $\\Delta$m history')
    EBEE_sigmaCB_history_plots = make_duo_history_slide(info_dict=info_dict,variable='sigma_CB_(Rescaled)',regions=['EB','EE'],title='EB/EB width history')
    EBEE_chi2_history_plots = make_duo_history_slide(info_dict=info_dict,variable='chi2',regions=['EB','EE'],title='EB/EB $\\chi^2$ history')


    content = ''
    content += '\\documentclass{beamer}\n'
    content += '\\usepackage{graphicx}\n'
    content += '\\usepackage[font={small}]{caption}'

    content += title_slide_commands
    content += '\\begin{document}\n'
    content += '\\frame{\\titlepage}\n'
    content += intro_frame
    content += scale_frame
    content += width_frame
    content += effsigma_frame
    content += EB_mc_data_plots
    content += EE_mc_data_plots
    content += EBEE_deltaM_history_plots
    content += EB_deltaM_history_plots
    content += EE_deltaM_history_plots
    content += EBEE_sigmaCB_history_plots
    content += EBEE_chi2_history_plots
    content += '\\end{document}\n'

    print content

    with open('python/tex/test_slide.tex','w') as sf:
        sf.write(content)


