from FSM_demo_0 import Lock
import random


sample = Lock()


def run_count():
    count = 0
    i = 0
    flag=0
    print('\n')
    print('1 is opened and 0 is closed.')
    print('Progress of key slots:')
    print(sample.lock[0],sample.lock[1],
          sample.lock[2],sample.lock[3],sample.lock[4],sample.lock[5])
    while flag==0:
        print('Unlock by 5-2-5-2-7-1. Lock by 5-2-5-2-7-4.')
        i = input("Enter your value ('s' to stop): ")
        if i=='s':
            flag=1
            print('\n')
            print('Thank you for your time!')
            break
        state_before = sample.state
        sample.entry(i)
        count+=1
        state_after = sample.state
        if state_before==0 and state_after==1:
            print('\n')
            print('Hurray! It took you',count,'entries to unlock!')
            print('The key slots is set back to all 0')
            print('You can try to lock it if you want to?')
            count = 0 
        if state_before==1 and state_after==0:
            print('\n')
            print('It took you',count,'entries to lock it!')
            print('The key slots is set back to all 0')
            print('You can try to unlock it if you want to?')
            count = 0
        print('\n')
        print('1 is opened and 0 is closed.')
        print('Progress of key slots:')
        print(sample.lock[0],sample.lock[1],
              sample.lock[2],sample.lock[3],sample.lock[4],sample.lock[5])
    return count

run_count()

