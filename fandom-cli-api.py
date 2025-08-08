import fandom

input_prompt = ">>> "

def chatbot():
    while True:
        try:
            print("Which Fandom do you want to explore? Enter a fandom subdomain")
            print("Examples: 'starwars', 'dragonball', 'gundam', 'pokemon', etc.")
            fandom_input = input(input_prompt)
            if fandom_input == 0:
                break
            fandom.set_wiki(fandom_input)
            print("Fandom set to: " + fandom_input + ".fandom.com")
            while True:
                try:
                    print("Search for a page")
                    search_input = input(input_prompt)
                    if search_input == '0':
                        break
                    search_results = fandom.search(search_input)
                    while True:
                        try:
                            for i, result in enumerate(search_results, 1):
                                print(f"{i}. {result[0]}")
                            print("which page?")
                            page_input = int(input(input_prompt))
                            if page_input == 0:
                                break
                            page = fandom.page(title=search_results[page_input - 1][0])
                            print(page.summary)
                            sections = page.sections
                            while True:
                                try:
                                    for i, section in enumerate(sections, 1):
                                        print(f"{i}. {section}")
                                    print("which section?")
                                    section_input = int(input(input_prompt))
                                    if section_input == 0:
                                        break
                                    print(page.section(sections[section_input - 1]))       
                                except fandom.error.FandomError as e:
                                    print(e)                       
                        except fandom.error.FandomError as e:
                            print(e)
                except fandom.error.FandomError as e:
                    print(e)
        except fandom.error.FandomError as e:
            print(e)


chatbot()