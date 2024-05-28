import csv
from pyDatalog import pyDatalog

# Define the Datalog predicates (facts and rules)
pyDatalog.create_terms('X, Y, Z, W, V, U, father, mother, son, male, female, daughter, brother, sister, aunt, uncle, cousin, niece, nephew, mother_in_law, father_in_law, wife, husband, brother_in_law, sister_in_law, step_siblings, step_father, step_mother, niece_in_law, nephew_in_law, grandparent, great_grandparent, half_sibling, sibling_in_law')


# Open the CSV file
with open('data-set.csv', mode='r') as csv_file:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)

    # Read and print each row
    for row in csv_reader:
        if row[0] == 'female':
            +female(row[1])
        elif row[0]== 'male':
            +male(row[1])
        elif row[0]== 'mother':
            +mother(row[1], row[2])
        elif row[0]== 'father':
            +father(row[1], row[2])
        elif row[0]== 'husband':
            +husband(row[1], row[2])
        
    son(X, Y) <= (male(X) & father(Y, X))
    son(X, Y) <= (male(X) & mother(Y, X))

    daughter(X, Y) <= (female(X) & mother(Y, X))
    daughter(X, Y) <= (female(X) & father(Y, X))

    # print('Son')
    # print(son(X, Y))
    # print('\nDaughter')
    # print(daughter(X, Y))

    sister(X, Y) <= (female(X) & father(Z, X) & father(Z, Y) & mother(W, X) & mother(W, Y) & (X!=Y))
    brother(X, Y) <= (male(X) & father(Z, X) & father(Z, Y) & mother(W, X) & mother(W, Y) & (X!=Y))
    
    # print('Sister')
    # print(sister(X, Y))
    # print('\nBrother')
    # print(brother(X, Y))

    # # Aunt and Uncle
    aunt(X, Y) <= (sister(X, Z) & father(Z, Y))
    aunt(X, Y) <= (sister(X, Z) & mother(Z, Y))

    wife(X, Y) <= husband(Y, X)

    # print(sister(X, 'Bob'))
    # print(aunt('Mari',X))

    uncle(X, Y) <= (brother(X, Z) & mother(Z, Y))
    uncle(X, Y) <= (brother(X, Z) & father(Z, Y))
    
    # print('aunt')
    # print(aunt(X, Y))
    # print('\nuncle')
    # print(uncle(X, Y))

    # print(uncle('Bob',X))

    # # Cousin
    cousin(X, Y) <= (son(X, Z) & uncle(Z, Y))
    cousin(X, Y) <= (son(X, Z) & aunt(Z, Y))
    cousin(X, Y) <= (daughter(X, Z) & uncle(Z, Y))
    cousin(X, Y) <= (daughter(X, Z) & aunt(Z, Y))
    
    # print('cousin')
    # print(cousin(X, Y))

    # print(cousin('Mari',X))

    # # Niece and Nephew
    niece(X, Y) <= (daughter(X, Z) & sister(Z, Y))
    niece(X, Y) <= (daughter(X, Z) & brother(Z, Y))

    nephew(X, Y) <= (son(X, Z) & sister(Z, Y))
    nephew(X, Y) <= (son(X, Z) & brother(Z, Y))

    # print(niece('Jennifer',X))
    # print(nephew('David',X))

    # # Mother-in-law and Brother-in-law
    mother_in_law(X, Y) <= (mother(X, Z) & wife(Z, Y))
    mother_in_law(X, Y) <= (mother(X, Z) & husband(Z, Y))


    father_in_law(X, Y) <= (father(X, Z) & wife(Z, Y))
    father_in_law(X, Y) <= (father(X, Z) & husband(Z, Y))

    # print(mother_in_law(X,'Sophia'))
    # print(father_in_law(X,'Sophia'))

    # print(mother_in_law(X,'Joey'))
    # print(father_in_law(X,'Joey'))


    brother_in_law(X, Y) <= (brother(X, Z) & husband(Z, Y))
    brother_in_law(X, Y) <= (brother(X, Z) & wife(Z, Y))

    # print(brother_in_law('Bob', X))

    sister_in_law(X, Y) <= (sister(X, Z) & husband(Z, Y))
    sister_in_law(X, Y) <= (sister(X, Z) & wife(Z, Y))

    # print(sister_in_law('Jessica', X))

    # # Step-siblings and Step-parents
    step_siblings(X, Y) <= (mother(Z, X) & father(V, X) & mother(W, Y) & father(U, Y) & wife(Z, U) & (V != U) & (Z != W))
    step_siblings(X, Y) <= (mother(Z, X) & father(V, X) & mother(W, Y) & father(U, Y) &  husband(V, W) & (V != U) & (Z != W))

    # print(step_siblings(X, Y))
    step_father(X, Y) <= (mother(Z, Y) & father(W, Y) & husband(X, Z) & (X != W))
    step_mother(X, Y) <= (father(Z, Y) & mother(W, Y) & wife(X, Z) & (X != W))


    # print(step_father(X, Y))
    # print(step_mother(X, Y))

    niece_in_law(X, Y) <= (nephew(Z, X) & wife(Y, Z))
    nephew_in_law(X, Y) <= (niece(Z, X) & husband(Y, Z))

    # # Grandparent and Great-Grandparent
    grandparent(X, Y) <= (mother(X, Z) & daughter(Y, Z))
    grandparent(X, Y) <= (mother(X, Z) & son(Y, Z))
    grandparent(X, Y) <= (father(X, Z) & daughter(Y, Z))
    grandparent(X, Y) <= (father(X, Z) & son(Y, Z))
              
    great_grandparent(X, Y) <= (mother(X, Z) & grandparent(Z, Y))
    great_grandparent(X, Y) <= (father(X, Z) & grandparent(Z, Y))
    
    # Half-sibling
    half_sibling(X, Y) <= (mother(Z, X) & mother(Z, Y) & father(V, X) & father(W, Y) & (V != W) & (X != Y))
    half_sibling(X, Y) <= (father(Z, X) & father(Z, Y) & mother(V, X) & mother(W, Y) & (V != W) & (X != Y))
    
    print('niece in law')
    print(niece_in_law(X, Y))
    print('nephew in law')
    print(nephew_in_law(X, Y))
    print('grand parent')
    print(grandparent(X, Y))
    print('great grandparent')
    print(great_grandparent(X, Y))
    print('half sibling')
    print(half_sibling(X, Y))
    
    # print(half_sibling(X, Y))
    
    # # Sibling-in-law
    sibling_in_law(X, Y) <= (husband(X, Z) & sister(Z, Y))
    sibling_in_law(X, Y) <= (husband(X, Z) & brother(Z, Y))
    sibling_in_law(X, Y) <= (wife(X, Z) & sister(Z, Y))
    sibling_in_law(X, Y) <= (wife(X, Z) & brother(Z, Y))
    
    # print(sibling_in_law(X, Y))

            
    
    
