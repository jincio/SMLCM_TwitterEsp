#cleaning the file:
while read -r line;
do p="$line"/candidatos_$line;
cut -d ',' -f 4 $p | awk 'NF' | tail -n +2 | sed 's/ //g' > "$p"_Clean; 
done < $1
 
#cut -d ',' -f 4 Chile/candidatos_chile | awk 'NF' | tail -n +2 > Chile/candidatesclean;
#Reading each line and apply twint

