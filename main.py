import os

def make_commit(days: int):
    if days < 1:
        return os.system('git push')
        return os.system('git push')
        return os.system('git push')

    else:
        dates = f'{days} days ago'

        with open('slut.txt', 'a') as file:
            file.write(f'{dates}\n')

        os.system('git add slut.txt')
        os.system('git commit --date="'+dates+'" -m "First Commit"')

        return days * make_commit(days-1)

make_commit(365)