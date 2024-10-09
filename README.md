# fandom-reader
Simple command line tool for reading fandom wiki dumps

# Acquiring dumps
Find dumps for any fandom wiki at:  
*.fandom.com/wiki/Special:Statistics  
ex: https://dragonball.fandom.com/wiki/Special:Statistics

Grab the "Current Pages" file from the Database dumps section at the bottom. It is a zip file that contains the dump in the form of an xml file.

# Running the cleaner
Run fandom_cleaner.py on the unzipped xml file to produce a "cleaned" version of the file that only contains the actual pages with contents.  
Essentially this strips out details about users, blogs, etcs.

# Running the reader
Run fandom_reader.py on the cleaned file. Perform a simple search on page titles. Then view a page by typing the exact page title.

Ex.
```console
>>>Enter a search:Goku
Results for "Goku":

Goku
Goku Hangs On
Goku's Trap
Dragon Ball Z: Bardock - The Father of Goku
Goku Jr
Goku Junior
Goku's Unusual Journey
etc...

>>>View which page?Goku

{{Goku}}
{{Featured article}}
{{Seealso|the original character|other uses|Goku (disambiguation)}}
etc...
```

# todo
- improve search, potentially by category
- make page output easier to read
