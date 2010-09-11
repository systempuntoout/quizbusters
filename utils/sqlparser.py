scan=open('quizbusters.tsv','r')
season=open('quizbusters.sql','w')
for line in scan:
    line_list= line.split('\t')
    season.write("insert into questions ('description','answer','id_special_question') values ('"+line_list[0].strip().replace("'","''") +"','"+line_list[1].strip().replace('Busted','B').replace('Plausible','P').replace('Confirmed','C')+"'")
    try:
        id_special=line_list[2].strip()
    except:
        id_special=''
    if id_special!='':
        season.write(","+ id_special+");\n")
    else:
        season.write(",null);\n")
scan.close()
season.close()

scan=open('special.tsv','r')
season=open('special.sql','w')
for line in scan:
    line_list= line.split('\t')
    season.write("insert into special_questions (id_special_question,description) values ("+line_list[0].strip() +",'"+line_list[1].strip().replace("'","''")+"');\n")
scan.close()
season.close()

