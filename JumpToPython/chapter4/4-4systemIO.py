# system 입출력 

# import sys
#  args = sys.argv[1:]
# for i in args:
#     print(i)
    
#python3 ./JumpToPython/chapter4/4-4systemIO.py 1 2 3 4 5



import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
    
#python3 ./JumpToPython/chapter4/4-4systemIO.py aa bb cc dd ee