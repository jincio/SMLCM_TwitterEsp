# Notes

- Makefile constructs the finalData.txt. 

## Pendings

- I use "|" as a delimiter. Problem: Tweet has "|" too then it creates a problem when I tried to uplaod the data. Two options; first : eliminate the "|" from tweets or use "$" as a delimiter.
  - I tried both optiosn and didn't work. When I upload the data there are more columns that should be. 
- Try to have two data sets one with the metadata and other with the text.
 - It works. There are two files: finalMetaData.txt and DataTweets.txt. The text need to be clen because it has the info about the likes RT, etc
- The update version set the info together in one table. The problem was that python wasn't reading the /n as endline  
