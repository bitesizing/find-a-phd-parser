# %% 
from PhDParser import PhDParser, DisciplineParser

# %%
""" Fill in variables manually """
discipline = "psychology"           # discipline (subject) to search within
recent_only = True                  # whether to only show recent projects
keywords = "development"              # keywords should be comma separated

save_as_json = True                 # whether to save as .json in this file
json_output_path = "recent.json"    # shouldn't need to change this

# %%
parser = PhDParser("law")
parser = PhDParser("psychology", keywords="development")
parser.saveAllAsJson()

# %%
""" Find matching PhD projects and save to class """
parser = PhDParser(discipline=discipline, recent_only=recent_only, keywords=keywords)


# %%
""" Save as .json file """
if save_as_json: parser.saveCurrentAsJson(output_path=json_output_path)