tasks = ['clean', 'mop', 'run']
while True:
    
    i = 0
    print(tasks)
    n = input("Input: ")
    for task in tasks:
        #print(tasks[i])
        i+=1
        if n == task:
            tasks.pop(i-1)
            tasks.insert(i-1, n + " (Complete)")
            print(i)
       
    