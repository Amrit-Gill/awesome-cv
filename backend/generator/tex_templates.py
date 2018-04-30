LatexContent = '''\\documentclass{scrartcl}
                        \\usepackage{graphicx}
                        \\begin{document}
                            \\includegraphics[width=1cm,height=3cm]{%(Id)s}
                            {\\sffamily %(Fn)s \\textsc{%(Ln)s}}
                                \\newline
                            \\section{Phone}
                            {\\tiny Phone number: %(Ph)s}
                                \\newpage
                            %(Ot)s
                   \\end{document}'''

main_template = '''\\documentclass[11pt, a4paper]{awesome-cv}
\\geometry{left=1.5cm, top=1.5cm, right=1.5cm, bottom=2cm, footskip=.5cm} 
\\fontdir[fonts/]
\\colorlet{awesome}{awesome-darknight} 
\\usepackage{import}
\\usepackage{hyperref}
\\name{}{%(name)s}
\\address{%(address)s}
\\mobile{%(phone_number)s}

\\email{%(email)s}
\\github{%(github)s}
\\linkedin{%(linkedin)s}
\\skype{%(skype)s}

\\position{%(position)s}

\\makecvfooter{\\today}{%(name)s~~~·~~~Résumé}{\\thepage}

\\begin{document}

\\makecvheader 

\\input{cv-sections/education.tex}
\\input{cv-sections/skills.tex}
\\input{cv-sections/experience.tex}

\\end{document}'''

education_cv_entries = '''  \\cventry
    {%(title)s}
    {%(school)s}
    {%(address)s}
    {%(start_date)s - %(end_date)s}{}

    \\vspace{-.5\\baselineskip}'''

education = '''\\cvsection{Education}
\\begin{cventries}
    %(cv_entries)s
\\end{cventries}'''

experience_items = '''\\item {%(item)s}'''
experience_cv_entries = '''\\cventry
{%(title)s}
{%(company)s}
{%(address)s}
{%(start_date)s - %(end_date)s}
{
\\begin{cvitems}
    %(items)s
\\end{cvitems}
}'''
experience = '''\\cvsection{Experience}

\\begin{cventries}

%(cv_entries)s
\\end{cventries}'''

skill_items = '''\\cvskill
{%(title)s}
{%(value)s}'''
skills = '''\\cvsection{Skills}
\\begin{cvskills}

%(skill_items)s

\\end{cvskills}'''
