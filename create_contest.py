import os


nps = 3 # change
contest_ = "round_853_div2" # change
platform = "Codeforces" # Change (maybe)

###
global_p = f"{platform}/{contest_}"

os.system(f'mkdir {platform}/{contest_}')

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tmp = "./templates/template.py"

for i in range(nps):
    os.system(f'cp {tmp} {global_p}/{abc[i]}.py')


rmd = "templates/readme.md"
os.system(f"cp {rmd} {global_p}")
