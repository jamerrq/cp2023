import os


platform = "Codeforces"
contest_ = "round_150_div2"
global_p = f"{platform}/{contest_}"

os.system(f'mkdir {platform}/{contest_}')

nps = 5
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tmp = "template.py"

for i in range(nps):
    os.system(f'cp {tmp} {global_p}/{abc[i]}.py')


rmd = "Codeforces/Unsolved/readme.md"
os.system(f"cp {rmd} {global_p}")