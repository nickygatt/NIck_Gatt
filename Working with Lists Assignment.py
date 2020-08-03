1
walsh_courses = ["it405", "it407", "it419", "it410"]
print(walsh_courses)

2
walsh_courses = ["it405", "it410", "it419", "it407"]
walsh_courses.sort()
for walsh in walsh_courses:
    print(f"I have taken {walsh.upper()}, at Walsh College!")

3
walsh_courses = ["it405", "it410", "it419", "it407", "it417", "it415"]
walsh_courses.sort()
for walsh in walsh_courses:
    print(f"This is my course of study with upcoming courses added: {walsh.upper()}")

4
walsh_courses = ["it405", "it410", "it419", "it407"]
walsh_courses.sort()
for walsh in walsh_courses:
    print(f"I do not have to take these courses: {walsh.upper()}")

5
walsh_courses = ["it415", "it417"]
walsh_courses.sort()
for walsh in walsh_courses:
    print(f"I plan to take the following courses next term: {walsh.upper()}.\n")

6
digits = [6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114,120,126,132,138,144,150,156,162,168,174,180,186,192,198,204,210,216,222,228,234,240,246,252,258,264,270,276,282,288,294,300]

7
print("Here are twenty numbers divisible by 6:")
for value in range(6,153,6):
    print(value)

8
digits = [6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114,120,126,132,138,144,150,156,162,168,174,180,186,192,198,204,210,216,222,228,234,240,246,252,258,264,270,276,282,288,294,300]

print(max(digits))

maximun_number = 300

9
digit_numbers = [300]
for digit in digit_numbers:
    print(f"The maximum value in the list is: {maximun_number}")

10
digits = [6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114,120,126,132,138,144,150,156,162,168,174,180,186,192,198,204,210,216,222,228,234,240,246,252,258,264,270,276,282,288,294,300]
for value in range(10,50):

    print(sum(digits))
