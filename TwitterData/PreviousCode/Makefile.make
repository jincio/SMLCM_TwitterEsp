#! bin/ make

Datafinal:  
	 bash step05.sh
Dataspaises: step04_1.sh step04.sh CountryList.txt 
	#bash step04_1.sh CountryList.txt;
	bash step04.sh CountryList.txt;
CandidateTweets: step03.sh CountryList.txt CleanFiles
	#python step03.py CountryList.txt
	bash step03.sh CountryList.txt
CleanFiles: step02.sh CountryList.txt
	bash step02.sh CountryList.txt
CountryList.txt: step01.py datacandidatos.xlsx
	#python3 country.py ../../Data/Raw/datacandidatos.xlsx | >> CountryList.txt
	python3 step01.py datacandidatos.xlsx
Clean:
	bash clean.sh CountryList.txt