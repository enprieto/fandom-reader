import xml.etree.ElementTree as ET

tree = ET.parse('output.xml')
root = tree.getroot()

pages_list = root.findall(".//page")

search = input("Enter a search:")

print("Results for \"" + search + "\":\n")

for page in pages_list:
    page_title = page.find("./title")
    if search in page_title.text:
        print(page_title.text)
        
page_to_read = input("\nView which page?")

for page in pages_list:
    page_title = page.find("./title")
    if page_to_read == page_title.text:
        print("\n")
        print(page.find(".//revision/text").text)
