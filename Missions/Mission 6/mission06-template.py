#
# CS1010S --- Programming Methodology
#
# Mission 6
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from ippt import *
import csv

##########
# Task 1 #
##########

# Function read_csv has been given to help you read the csv file.
# The function returns a tuple of tuples containing rows in the csv
# file and its entries.

# Alternatively, you may use your own method.

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def read_data(filename):
    rows = read_csv(filename)
    age_title = tuple(map(int, (entry[0] for entry in rows[1:])))
    rep_title = tuple(map(int, rows[0][1:]))
    
    data = tuple(tuple(map(int, entry[1:])) for entry in rows[1:])
    
    return create_table(data, age_title, rep_title)

pushup_table = read_data("pushup.csv")
situp_table = read_data("situp.csv")
run_table = read_data("run.csv")

ippt_table = make_ippt_table(pushup_table, situp_table, run_table)

# print("## Q1 ##")
# Sit-up score of a 24-year-old who did 10 sit-ups.
# print(access_cell(situp_table, 24, 10))    # 0

# Push-up score of a 18-year-old who did 30 push-ups.
# print(access_cell(pushup_table, 18, 30))   # 16

# Run score of a 30-year old-who ran 12 minutes (720 seconds)
# print(access_cell(run_table, 30, 720))     # 36

# Since our run.csv file does not have data for 725 seconds, we should
# get None if we try to access that cell.
# print(access_cell(run_table, 30, 725))     # None


##########
# Task 2 #
##########

def pushup_score(pushup_table, age, pushup):
    if pushup > 60:
        pushup = 60
    elif pushup <= 0:
        return 0
    
    return access_cell(pushup_table, age, pushup)

def situp_score(situp_table, age, situp):
    if situp > 60:
        situp = 60
    elif situp <= 0:
        return 0

    return access_cell(situp_table, age, situp)

def run_score(run_table, age, run):
    if run < 510:
        run = 510
    elif run > 1100:
        run = 1100
    
    if run % 10 != 0:
        run += (10 - run % 10)

    return access_cell(run_table, age, run)

# print("## Q2 ##")
# print(pushup_score(pushup_table, 18, 61))   # 25
# print(pushup_score(pushup_table, 18, 70))   # 25
# print(situp_score(situp_table, 24, 0))      # 0

# print(run_score(run_table, 30, 720))        # 36
# print(run_score(run_table, 30, 725))        # 35
# print(run_score(run_table, 30, 735))        # 35
# print(run_score(run_table, 30, 500))        # 50
# print(run_score(run_table, 30, 1300))       # 0


##########
# Task 3 #
##########

def ippt_award(score):
    if score < 51:
        return 'F'
    elif score < 61:
        return 'P'
    elif score < 75:
        return 'P$'
    elif score < 85:
        return 'S'
    else:
        return 'G'

# print("## Q3 ##")
# print(ippt_award(50))     # F
# print(ippt_award(51))     # P
# print(ippt_award(61))     # P$
# print(ippt_award(75))     # S
# print(ippt_award(85))     # G


##########
# Task 4 #
##########

def ippt_results(ippt_table, age, pushup, situp, run):
    pushup_table, situp_table, run_table = ippt_table
    
    pushup_points = pushup_score(pushup_table, age, pushup)
    situp_points = situp_score(situp_table, age, situp)
    run_points = run_score(run_table, age, run)
    
    if pushup_points == None:
        pushup_points = 0
    if situp_points == None:
        situp_points = 0
    if run_points == None:
        run_points = 0
    
    total = pushup_points + situp_points + run_points
    return (total, ippt_award(total))

# print("## Q4 ##")
# print(ippt_results(ippt_table, 25, 30, 25, 820))      # (53, 'P')
# print(ippt_results(ippt_table, 28, 56, 60, 530))      # (99, 'G')
# print(ippt_results(ippt_table, 38, 18, 16, 950))      # (36, 'F')
# print(ippt_results(ippt_table, 25, 34, 35, 817))      # (61, 'P$')
# print(ippt_results(ippt_table, 60, 70, 65, 450))      # (100, 'G')


##########
# Task 5 #
##########

def parse_results(csvfilename):
    rows = []
    data = read_csv(csvfilename)
    rows.append(tuple(list(data[0]) + ['Total-Score', 'Award']))
    
    for entry in data[1:]:
        name, age, pushup, situp, run = entry
        age, pushup, situp, run = int(age), int(pushup), int(situp), int(run)
        rows.append(tuple(list([name, age, pushup, situp, run]) + list(ippt_results(ippt_table, age, pushup, situp, run))))
    
    return rows

# print("## Q5 ##")
ippt_takers_data = parse_results("ippt_takers_data.csv")
# print(ippt_takers_data[0])
# print(ippt_takers_data[1])
# print(ippt_takers_data[2])
# print(ippt_takers_data[3])

# Expected Output:
# ('Name', 'Age', 'Push-Ups', 'Sit-Ups', '2.4-Km-Run', 'Total-Score', 'Award')
# ('Sean Hendricks', 38, 25, 74, 1212, 42, 'F')
# ('Phillip Brown DDS', 59, 15, 15, 852, 61, 'P$')
# ('Ryan Gray MD', 24, 45, 78, 1074, 46, 'F')


##########
# Task 6 #
##########

def num_awards(ippt_takers_data, age):
    data = ippt_takers_data[1:]
    data = list(filter(lambda row: row[1] == age, data))
    d = {}
    for entry in data:
        name, age, pushup, situp, run, score, award = entry
        
        if award not in d:
            d[award] = 0
            
        d[award] += 1
        
    return d

# print("## Q6 ##")
# print(num_awards(ippt_takers_data, 25))
# print(num_awards(ippt_takers_data, 28))

# Expected Output:
# {'F': 56, 'P': 20, 'G': 18, 'P$': 14, 'S': 10}
# {'F': 54, 'S': 13, 'G': 16, 'P': 8, 'P$': 12}


##########
# Task 7 #
##########

def top_k_scores(ippt_takers_data, k, age):
    data = ippt_takers_data[1:]
    data = list(filter(lambda row: row[1] == age, data))
    
    tup = ()
    for entry in data:
        name, age, pushup, situp, run, score, award = entry
        tup += ((name, score),)
    
    tup = sorted(tup, key=lambda x: x[0])
    tup = sorted(tup, key=lambda x: x[1], reverse=True)
    
    if k <= 0:
        return []
    if k >= len(tup):
        return tup
    
    k_value = tup[k-1][1]
    return list(filter(lambda x: x[1] >= k_value, tup))


# print("## Q7 ##")
# print(top_k_scores(ippt_takers_data, 5, 25))
# print(top_k_scores(ippt_takers_data, 1, 28))
# print(top_k_scores(ippt_takers_data, 2, 28))

# Expected Output:
# [('Joseph Burns', 100), ('Mike Williams', 98), ('Rachel Serrano', 98), ('Margaret Jennings', 97), ('Alexandra Day', 95), ('Stephen Boyer', 95)]
# [('Eric Villegas', 100), ('Melissa Evans', 100)]
# [('Eric Villegas', 100), ('Melissa Evans', 100)]