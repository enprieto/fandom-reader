import xml.etree.ElementTree as ET

tree = ET.parse('dragonball_ns0.xml')
root = tree.getroot()
#print(root)
ns = {'ns': "http://www.mediawiki.org/xml/export-0.11/"}

print("Loading wiki for: " + root.find('.//ns:sitename', ns).text)


pages_list = root.findall('.//ns:page', ns)
print(str(len(pages_list)) + " pages found")
search = input("Enter a search:")

print("Results for \"" + search + "\":\n")

for page in pages_list:
    page_title = page.find("./ns:title", ns)
    if search in page_title.text:
        print(page_title.text)
        
page_to_read = input("\nView which page?")

for page in pages_list:
    page_title = page.find("./ns:title", ns)
    if page_to_read == page_title.text:
        print("\n")
        print(page.find("./ns:revision/ns:text", ns).text)
