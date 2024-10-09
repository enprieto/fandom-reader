import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('fandom_dump.xml')  # Replace 'input.xml' with your file path
root = tree.getroot()

# If there is a namespace in your XML, it can be something like this:
ns = {'ns': 'http://www.mediawiki.org/xml/export-0.11/'}  # Adjust based on your XML

# Log the number of <page> tags found before removal
pages = root.findall('.//ns:page', ns)
print(f"Total <page> elements found: {len(pages)}")

# Iterate over <page> elements to find and remove those without <id>0</id>
for page in pages:
    ns_tag = page.find('ns:ns', ns)  # Find the <id> tag within each <page>
    
    # Debug: Check what <id> values are found
    #if ns_tag is not None:
    #    print(f"<id> tag found with value: {ns_tag.text}")
    #else:
    #    print("<id> tag not found in <page>")
    
    # Remove the <page> if the <id> is not '0'
    if ns_tag is None or ns_tag.text != '0':
        #print(f"Removing <page> element with <id>: {ns_tag.text if ns_tag else 'None'}")
        root.remove(page)

# Log the number of <page> tags left after removal
remaining_pages = root.findall('.//ns:page', ns)
print(f"Total <page> elements remaining: {len(remaining_pages)}")

# Save the modified XML back to a file
tree.write('output.xml', encoding='utf-8', xml_declaration=True)
