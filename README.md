# iTunes purchase to CSV tool
Parses the text copied from the list of purchases from iTunes online and dumps them to a tab separated file.

# Requirements
* Plain Text editor
* Python Interpreter

# Instructions on use
1. Go to reportaproblem.apple.com.
2. Sign in with your Apple Account and password to see a list of your purchases.
3. Use the mouse to select the text containing the purchases.
4. Right click and select copy or select copy from the edit menu
5. Open your favorite plain text editor like Notepad, BBEdit, VSCode or similar
6. Paste the text in and save the file
7. From the command line type the following:
```shell
python itunes_to_csv.py [input file] [output file ending in csv or tsv]
```
8. Open the file in excel to import it.
