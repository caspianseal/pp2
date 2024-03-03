import re

#1
pattern = r'ab*'

test_strings = ['ab', 'aab', 'abb', 'abbb', 'ac', 'a']

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")

#2
pattern = r'ab{2,3}'

test_strings = ['ab', 'aab', 'abb', 'abbb', 'ac', 'a']

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")

#3
pattern = r'[a-z]+_[a-z]+'

test_string = "this_is_a_test_string"

result = re.findall(pattern, test_string)
print(result)

#4
pattern = r'[A-Z][a-z]+'

test_string = "HelloWorld ThisIsATestString"

result = re.findall(pattern, test_string)
print(result)

#5
pattern = r'a.*b$'

test_strings = ['acb', 'a123b', 'ab', 'acbd', 'acb123']

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"'{string}' matches the pattern.")
    else:
        print(f"'{string}' does not match the pattern.")

#6
text = "This is, a test. String"

result = re.sub(r'[ ,.]', ':', text)
print(result)

#7
snake_case = "this_is_snake_case_string"

camel_case = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case)
print(camel_case)

#8
text = "SplitThisStringAtUppercaseLetters"

result = re.findall(r'[A-Z][a-z]*', text)
print(result)

#9
text = "InsertSpacesBetweenWordsStartingWithCapitalLetters"

result = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print(result)

#10
camel_case = "ConvertThisCamelCaseStringToSnakeCase"

snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
print(snake_case)
