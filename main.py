# check status
git status

# create and switch to a new branch
git checkout -b BRANCH_NAME
# or with newer Git:
# git switch -c BRANCH_NAME

# stage and commit changes (if needed)
git add /Users/nataliaorne/GitAventure/main.py
git commit -m "Add/modify main.py"

# push the new branch to origin
git push -u origin BRANCH_NAME