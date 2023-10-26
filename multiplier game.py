import random
#best scoroe: 46805
def math():
    x = 0
    score = 0
    while (x < 5):
        y = random.randint(0,100000)
        z = 11
        a = 3
        pick = random.randint(0,1)
        
        print(y," x ", z)
        question_time = time.time()
        answer = input()
        if int(answer) == y*z:
            print("\n⭐  Correct  ⭐")
            print("--- %.4s seconds ---" % (time.time() - question_time))
            points = 10000-(time.time()-question_time)*100
            print("+ %.4s points" % points)
            score += points
        else:
            print ("\nIncorrect, answer was: ", str(11*y))
            print("--- %.4s seconds ---" % (time.time() - question_time))
            print("- ", score/2, " points")
            score /= 2
        x += 1
    print("\nFinal Score: %d" % score)
    return 0
import time
start_time = time.time()
math()
timed = time.time()-start_time
print("--- %.5s seconds --- average: " % (time.time() - start_time))
print("Average: ", round((timed/5),2))
