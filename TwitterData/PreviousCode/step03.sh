# Output: file with the name of the candidate storaged in the Country folder. 
# Imput: Name of the country and each candidate from the clean data. 
while read -r line;
 do folder="$line";
 fileClean="$folder"/candidatos_"$folder"_Clean;
 while read -r line;
 do user="$line";
 twint -u $user --count --stats --o $folder/"$user"_tweets.txt;
 done < $fileClean;
 done < $1 
