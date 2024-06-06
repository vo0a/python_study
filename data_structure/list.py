""" List(Data structure)
  When to use?
  - Grouping
  - Keep the order
  
  내용
  - list
  - error
  - nested list
  - loops
  
  시간 복잡도
  - index O(1)
  - store O(1)
  - append O(1)
  - pop O(1) | l.pop()
  - clear O(1)
  
  - slice O(N)
  - extend O(N)
  - construction O(N)
  
  - check O(N)
  - insert O(N)
  - delete O(N)
  - copy O(N)
  - remove O(N)
  - pop O(N) | l.pop(i)
  - extreme value O(N) | min(l)/max(l)
  - reverse O(N)
  - iteration O(N)
  
  - sort O(NlogN)
  - multiple O(kN) | k 가 상수면 n, 길이 n인 list 면 O(N^2)
  
  
  ref) https://ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
  ref 2) 구현 및 내부 구조 https://seoyeonhwng.medium.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%82%B4%EB%B6%80-%EA%B5%AC%EC%A1%B0-f04847b58286
"""


def list():
    countries = ["South Korea", "USA", "Japan", "China"]
    # print(countries)

    countries[2] = "Vietnam"
    # print(countries)

    element = "c"
    alphabets = ["b", element, "d"]
    # print(alphabets)
    alphabets.append("e")
    # print(alphabets)

    alphabets += ["f", "g"]
    # print(alphabets)

    alphabets.insert(0, "a")
    # print(alphabets)

    # print(countries[0])
    # print(countries[len(countries) - 1])
    # print(countries[-1])
    # print(countries[-2])

    # 맨 뒤 삭제
    # print(countries.pop())
    # print(countries)

    # 맨 앞 삭제
    # print(countries.pop(0))
    # print(countries)


def error_case():
    alphabets = ['a', 'b', 'c']
    # print(len(alphabets))

    # What happens if we print the one that does not exist
    # ERROR
    # print(alphabets[3])


def nested_list():
    # barely use it.
    alphabets = [['a', 'b'], ['c']]
    # print(alphabets)


def loops():
    alphabets = ['a', 'b', 'c', 'd']

    # for alphabet in alphabets:
    #     print(alphabet)
    #     print(f"{alphabet} is char")

    # for char in "South Korea":
    #     print(char)

    # average value
    # numbers = [1, 2, 3, 4]
    # sum = 0
    # for number in numbers:
    #     sum += number
    # print(sum / len(numbers))

    # max value
    numbers = [1, 2, 3, 4]
    # max_num = 0
    # for number in numbers:
    #     if number > max_num:
    #         max_num = number
    # print(max_num)

    # print(max(numbers))
    # print(max(1, 5))

    # range 는 마지막 한 값을 제외하여 1~10 까지의 합
    # sum = 0
    # for i in range(1, 11):
    #     sum += i
    # print(sum)  # 55

    # odd number
    # range(start, stop, step)
    for i in range(1, 11, 2):
        print(i)


if __name__ == '__main__':
    list()
    error_case()
    nested_list()
    loops()
