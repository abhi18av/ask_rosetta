import os
import shutil

location = "../_resources/u_acmeism_r_rosettacodedata/Task"
all_tasks = os.listdir(location)

# List of all tasks done in scheme
all_scheme_tasks = []

# Collect all tasks done in Scheme
for a_task in all_tasks:
    new_location = location + "/" + a_task
    if os.path.isdir(new_location):
        if "Scheme" in os.listdir(new_location):
            all_scheme_tasks.append(new_location)

# print(all_scheme_tasks[0])
# print(os.listdir(all_scheme_tasks[0]))


# TODO copy over python, java, mathematica and javascript folders

for a_scheme_task in all_scheme_tasks:
    folder_name = a_scheme_task.split("/")[-1:][0]
    new_location = "../scheme_tasks/" + folder_name + "/Scheme"
    shutil.copytree(a_scheme_task + "/Scheme", new_location)
    shutil.copy(a_scheme_task + "/00DESCRIPTION", new_location + "/00DESCRIPTION.md")
    shutil.copy(a_scheme_task + "/README", new_location + "/URL.md")
