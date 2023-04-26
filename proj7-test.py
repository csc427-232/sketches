import os
import re
from proj7 import * 

assert_honor_code()


### extended

from simple_finite_automata import *
from turing_machine_sim import *

def extended_test(ms):
    correct, incorrect = 0, 0 
    for (name,empty,m) in ms:
        print(f'testing {name}:')
        de = DecideEmptiness(m)
        d_empty = de.decide_empty()
        if empty:
            if d_empty:
                correct += 1
                print(f'\tcorrect: is empty')
            else:
                incorrect += 1
                print(f'\tincorrect: should be empty')
        else:
            if not d_empty:
                correct += 1
                print(f'\tcorrect: is non-empty')
                p = de.prove_not_empty()
                m1 = SimpleFiniteAutomata(m)
                if m1.compute(p):
                    correct += 1
                    print(f'\tcorrect: {p}')
                else:
                    incorrect += 1
                    print(f'\tincorrect: {p} is not proof')
            else:
                incorrect += 1
                print(f'\tincorrect: hould be non-empty')
    return (correct,incorrect)
    

m1 = {
    'states':{'q1','q2','q3'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','0'):'q1',
        ('q1','1'):'q2',
        ('q2','1'):'q2',
        ('q2','0'):'q3',
        ('q3','0'):'q2',
        ('q3','1'):'q2'
    },
    'start':'q1',
    'accept':{'q2'}
}


m1_e = {
    'states':{'q1','q2','q3'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','0'):'q1',
        ('q1','1'):'q2',
        ('q2','1'):'q2',
        ('q2','0'):'q1',
        ('q3','0'):'q2',
        ('q3','1'):'q2'
    },
    'start':'q1',
    'accept':{'q3'}
}

ring = {
    'states':{'q1','q2','q3','q4','q5'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','0'):'q1',
        ('q1','1'):'q2',
        ('q2','1'):'q2',
        ('q2','0'):'q3',
        ('q3','0'):'q3',
        ('q3','1'):'q4',
        ('q4','0'):'q4',
        ('q4','1'):'q5',
        ('q5','1'):'q5',
        ('q5','0'):'q1',
    },
    'start':'q1',
    'accept':{'q5'}
}


ring_e = {
    'states':{'q1','q2','q3','q4','q5'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','0'):'q1',
        ('q1','1'):'q2',
        ('q2','1'):'q2',
        ('q2','0'):'q3',
        ('q3','0'):'q3',
        ('q3','1'):'q4',
        ('q4','0'):'q4',
        ('q4','1'):'q1',
        ('q5','1'):'q5',
        ('q5','0'):'q1',
    },
    'start':'q1',
    'accept':{'q5'}
}


square = {
    'states':{'q1','q2','q3','q4','q5'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','0'):'q2',
        ('q1','1'):'q3',
        ('q2','1'):'q4',
        ('q2','0'):'q4',
        ('q3','0'):'q4',
        ('q3','1'):'q4',
        ('q4','0'):'q4',
        ('q4','1'):'q4',
        ('q5','1'):'q4',
        ('q5','0'):'q4',
    },
    'start':'q1',
    'accept':{'q4'}
}


square_e = {
    'states':{'q1','q2','q3','q4','q5'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','0'):'q2',
        ('q1','1'):'q3',
        ('q2','1'):'q4',
        ('q2','0'):'q4',
        ('q3','0'):'q4',
        ('q3','1'):'q4',
        ('q4','0'):'q4',
        ('q4','1'):'q4',
        ('q5','1'):'q4',
        ('q5','0'):'q4',
    },
    'start':'q1',
    'accept':{'q5'}
}

exA_tests = [
    ('m1',False,m1),
    ('m1_e',True,m1_e),
    ('ring',False,ring),
    ('ring_e',True,ring_e),
    ('square',False,square),
    ('square_e',True,square_e),
]

exA = extended_test(exA_tests)

# B

# string has at least one 1 and ends in an even number of zeros
m1 = {
    'states':{'q1','q2','q3'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','0'):'q1',
        ('q1','1'):'q2',
        ('q2','1'):'q2',
        ('q2','0'):'q3',
        ('q3','0'):'q2',
        ('q3','1'):'q2'
    },
    'start':'q1',
    'accept':{'q2'}
}

# string ends in a 1
m2 = {
    'states':{"q1","q2"},
    'alphabet':{'0','1'},
    'transitions':{('q1','0'):'q1',('q1','1'):'q2',('q2','0'):'q1',('q2','1'):'q2'},
    'start':'q1',
    'accept':{'q2'}
}

# the machine m accepts strings with at least 1 and end in even number of zeros, and end in a zero
dl_test = (['100','00100','010000','101100','101001000000'],['0','1','000','010','01000'])

star = {
    'states':{'a'},
    'alphabet':{'0','1'},
    'transitions':{
        ('a','0'):'a',
        ('a','1'):'a',
    },
    'start':'a',
    'accept':{'a'}
}


sx01x = {
    'states':{'a','b','c','d','r'},
    'alphabet':{'0','1'},
    'transitions':{
        ('a','0'):'b',
        ('a','1'):'b',
        ('b','0'):'c',
        ('b','1'):'r',
        ('c','1'):'d',
        ('c','0'):'r',
        ('d','0'):'d',
        ('d','1'):'d',
        ('r','1'):'r',
        ('r','0'):'r'
    },
    'start':'a',
    'accept':{'d'}
}


def extended_test(ms):
    
    def alpha_star(sigma,n):
        if n==0:
            return [""]
        tail = alpha_star(sigma,n-1)
        out = []
        for c in sigma:
            for t in tail:
                out.append(c+t)
        return out
 
    correct, incorrect = 0,0
    for (m1_d,m2_d) in ms:
        dl = DifferenceMachine(m1_d,m2_d)
        md_d = dl.make_machine()
        # _d are all descriptions
        m1 = SimpleFiniteAutomata(m1_d)
        m2 = SimpleFiniteAutomata(m2_d)
        md = SimpleFiniteAutomata(md_d)
        
        tests = alpha_star(['0','1'],6)
        for t in tests:
            m1_a = m1.compute(t)
            m2_a = m2.compute(t)
            md_a = md.compute(t)
            # score
            if (m1_a and (not m2_a)) == md_a:
                correct += 1
            else:
                incorrect += 1

    return (correct,incorrect)

exB_tests = [
    (m1,m2),
    (star,sx01x),
    (m2,m1),
    (sx01x,star)
]
exB = extended_test(exB_tests)

# C

pair0_1 = {
    'states':{'q1','q2','r'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','1'):'q1',
        ('q1','0'):'q2',
        ('q2','0'):'q1',
        ('q2','1'):'r',
        ('r','0'):'r',
        ('r','1'):'r'
    },
    'start':'q1',
    'accept':{'q1'}   
}

pair0_2 = {
    'states':{'q1','q2','q3','r'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','1'):'q1',
        ('q1','0'):'q2',
        ('q2','0'):'q3',
        ('q2','1'):'r',
        ('r','0'):'r',
        ('r','1'):'r',
        ('q3','1'):'q1',
        ('q3','0'):'q2'
    },
    'start':'q1',
    'accept':{'q1','q3'}   
}


pair0_2 = {
    'states':{'q1','q2','q3','r'},
    'alphabet':{'0','1'},
    'transitions':{
        ('q1','1'):'q1',
        ('q1','0'):'q2',
        ('q2','0'):'q3',
        ('q2','1'):'r',
        ('r','0'):'r',
        ('r','1'):'r',
        ('q3','1'):'q1',
        ('q3','0'):'q2'
    },
    'start':'q1',
    'accept':{'q1','q3'}   
}

no_zero = {
    'states':{'s','r'},
    'alphabet':{'0','1'},
    'transitions':{
        ('s','1'):'s',
        ('s','0'):'r',
        ('q2','1'):'r',
        ('r','0'):'r',
        ('r','1'):'r',
    },
    'start':'s',
    'accept':{'s'}   
}

zerostaronestar = {
    'states':{'s','z','r'},
    'alphabet':{'0','1'},
    'transitions':{
        ('s','1'):'z',
        ('s','0'):'s',
        ('z','1'):'z',
        ('z','0'):'r',
        ('r','0'):'r',
        ('r','1'):'r',
    },
    'start':'s',
    'accept':{'s','z'}        
}

zerostaroneonestar = {
    'states':{'s','z1','z2','r'},
    'alphabet':{'0','1'},
    'transitions':{
        ('s','1'):'z1',
        ('s','0'):'s',
        ('z1','1'):'z2',
        ('z1','0'):'r',
        ('z2','1'):'z1',
        ('z2','0'):'r',
        ('r','0'):'r',
        ('r','1'):'r',
    },
    'start':'s',
    'accept':{'s','z1'}        
}


test_vector =[ 
    ('A',pair0_1,pair0_2,True),
    ('B',pair0_1,no_zero,False),
    ('C',zerostaronestar,zerostaronestar,True),
    ('D',zerostaronestar,zerostaroneonestar,False),
    ('E',zerostaroneonestar,zerostaronestar,False)
]

def basic_test(test_vector):
    correct, incorrect = 0, 0
    for (example, m1,m2,outcome) in test_vector:
        de = DecideEquality(m1,m2)
        r = de.decide_equality()
        if r==outcome:
            correct += 1
            print(f'OK: {example} is correct.')
        else:
            incorrect += 1
            print(f'ERR: {example} is incorrect. Should be {outcome}')
    print(f'*** {correct} correct out of {len(test_vector)} tests')
    return (correct,incorrect)
            
        
exC = basic_test(test_vector)

# D extra credit


def create_and_test_turing_machine(label, tm_description, test_cases,verbose='none'):
    """
    label: a string nameing the test or Turing Machine
    tm_decription: a string with the TM description
    test_cases: a pair of lists, the first being strings in the language, the second being strings not in the language
    """

    print(f'\nTesting {label}')
    tm = MachineParser.create_from_description(tm_description)
    correct = 0
    incorrect = 0
    exception = 0
    acc, rej = 0,0
    side = True
    for test_side in test_cases:
        for s in test_side:
            # assume complexity is some quadratic
            res = tm.compute_tm(s,step_limit=10*(len(s)+5)**2,verbose=verbose)
            if tm.is_exception():
                print(f'exception:\t|{s}|')
                exception += 1
                continue
            if res==True:
                acc += 1
                print(f'accept:\t|{s}|')
            else:
                rej += 1
                print(f'reject:\t|{s}|')
            if res==side:
                correct += 1
            else:
                incorrect += 1
        side = not side
    print(f'correct: {correct}, incorrect: {incorrect}, exceptions: {exception}, accepts {acc}, rejects {rej}')
    if acc==0 or rej == 0:
        incorrect += correct
        correct = 0
    return (correct,incorrect+exception)

exD_tests = (['&0&1','&00&01&10','&1&111&11','&000&00&0',
              '&100&000&001&010&011&111&110&101', '&00&000&10&100&11&111'],
        ['&0&0','&10&01&10','&1&111&1','&0&00&0',
             '&100&000&001&110&011&111&110&101','&00&000&10&100&10&111'])

exD = create_and_test_turing_machine('Extra Credit', tm_uniq, exD_tests)
                               

print(f'A: {exA}\nB: {exB}\nC: {exC}\nD: {exD}')
score = exA[0]+exB[0]//32+exC[0]*2+exD[0]
print(score,'out of 39')
total = 39

with open("run_summary.out","w",encoding="utf-8") as f:
	f.write(f'Signature: {sign_the_honor_code_with_your_name_in_the_following_string}\n')
	f.write(f'Ex A: {exA}\n')
	f.write(f'Ex B: {exB}\n')
	f.write(f'Ex C: {exC}\n')
	f.write(f'Ex D: {exD}\n')
	f.write(f'Late: 0 days\n\n')
	f.write(f'(correct A) + (correct B)/32 + (correct C)*2 + (correct D)\n')
	f.write(f'Total: {score} out of {total}\n\n')

with open("grade.csv","w",encoding="utf-8") as f:
	u = os.path.basename(os.getcwd())
	f.write(f'{u},{score}\n')



