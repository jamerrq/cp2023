import os


nps = 6  # change
contest_ = "round_886"  # change
platform = "Codeforces"  # Change (maybe)
subfolder = "/div4"  # change
# problems with repeated names such as A1, A2 or B1, B2, etc. (change)
repeated = ""

###
global_p = f"{platform}{subfolder}/{contest_}"

os.system(f'mkdir {platform}{subfolder}/{contest_}')

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tmp = "./templates/template.py"

for i in range(nps):
    os.system(f'cp {tmp} {global_p}/{abc[i]}.py')


rmd = "templates/readme.md"
os.system(f"cp {rmd} {global_p}")
