import requests
import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response

url = 'https://api.github.com/search/repositories?q=language:python#sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

#Store API response in variable

response_dict = r.json()

#Process Results
print(response_dict.keys())
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))



print("\nSelected information about each repository: ")
names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('python_repos.svg')
