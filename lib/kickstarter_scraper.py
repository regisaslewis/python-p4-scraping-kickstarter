from bs4 import BeautifulSoup
import ipdb



def create_project_dict():
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()
    kickstarter = BeautifulSoup(html, 'html.parser')
    projects = {}


    # Iterate through the projects
    for n in kickstarter.select("li.project.grid_4"):
        title = n.select("h2.bbcard_name strong a")[0].text
        projects[title] = {
            "image_link": n.select("div.project-thumbnail a img")[0]["src"],
            "description": n.select("p.bbcard_blurb")[0].text,
            "location": n.select("li span.location-name")[0].text,
            "percent_funded": n.select("li.first.funded")[0].text.replace("\n", "").replace("%", "% ")
        }
    # return the projects dictionary

    return projects

projects = create_project_dict()