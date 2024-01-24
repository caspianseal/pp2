#Exercises
#1
print(10 > 9)
True
#2
print(10 == 9)
False
#3
print(10 < 9)
False
#4
print(bool("abc"))
True
#5
print(bool(0))
False

#Examples
#1
print(bool("Hello"))
print(bool(15))

#2
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#3
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#4
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#5
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#6
def myFunction() :
  return True

print(myFunction())

#7
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#8
x = 200
print(isinstance(x, int))
