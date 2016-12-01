import json
from Slides import SlideMaker as sm

table1 = 'Cal_Nov2016_Rereco_plusHPrompt-Batch/dato/Cal_Nov2016_Rereco_plusHPrompt/loose25nsRun2/invMass_SC_corr/table/monitoring_summary-invMass_SC_corr-loose25nsRun2-Et_25.tex'
table2 = 'Cal_Nov2016_Rereco_plusHPrompt-Batch/dato/Cal_Nov2016_Rereco_plusHPrompt/loose25nsRun2/invMass_SC_must_regrCorr_ele/table/monitoring_summary-invMass_SC_must_regrCorr_ele-loose25nsRun2-Et_25.tex'

column_labels = ['Events','$\\Delta m_{data}$','$\\Delta m_{MC}$','$\\Delta$P (\%)']
column_indices = [1,2,3,4]

expression = '\\Delta P = \\frac{\\Delta m_{data} - \\Delta m_{MC}}{m_{Z}}'
title = 'Z Peak Shift (SC_corr - SC_must)'

jf = open('data/metadata/Cal_Nov2016_Rereco_plusHPrompt.json')
info_dict = json.loads(jf.read())
jf.close()

content = sm.get_inital_commands_and_title(info_dict=info_dict)
content += sm.make_table_comparison_slide(table_path1=table1,table_path2=table2,
                                          column_labels=column_labels,column_indices=column_indices,
                                          expression=expression,title=title,info_dict=info_dict)

content += '\\end{document}\n'
content += '\n'*4

print content


with open('comp_slides.tex','w') as sf:
    sf.write(content)
