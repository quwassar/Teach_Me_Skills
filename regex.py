import re

text = "We arrive on 04/04/2018. So you are welcome after 05/04/2022."
print(re.sub(r'(\d\d)/(\d\d)/(\d{4})', r'\2.\1.\3', text))


def checking_and_censored(validation_text):
    return '>censored<'


text = "Дядя Петя ел на ужин хрен и борщ"
print(re.sub(r'\b[хХxX]\w*', checking_and_censored, text))
