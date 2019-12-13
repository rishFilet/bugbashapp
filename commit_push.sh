#!/bin/bash

python $PWD/manage.py test
echo Continue with commit? [y/n]
read answer 
if [ "$answer" == "y" ]
then
    echo What is your commit message?
    read m
    git commit -m "$m"
    git fetch origin
    git rebase origin/master
    git push
    echo "Damn you are lit..thanks for pushing"
elif [ "$answer" == "n" ]
then
    echo "Commitment can be hard sometimes. Goodbye"
else
    echo Invalid Answer, try again
fi
