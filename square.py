# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit



def squarefunc(length):

    square.append(length*'*')
    for i in range(length-2):
        square.append('*'+((length-2)*' ')+'*')
    square.append(length*'*')

def main():
    length = int(input('How long must the side be? '))
    squarefunc(length)
    for item in square:
        print(item)
square = []
main()
