while read -r line;
do fileall="$line"/_all.txt;
cat "$line"/*.txt > "$line"/_all.txt;
awk '{print $0,FILENAME}' "$fileall" > $line/_2all.txt;
done < $1;

