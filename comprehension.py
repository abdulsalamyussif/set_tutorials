import time

sci_prof = ['Yussif Abdul Salam', 'Ridwan Shaiba', 'Osei Nimako Daniel',
'Opoku Mathew', 'Otoo Eunice', 'Mohammed Saani', 'Zakaria Hamza']
gnames = [name for name in sci_prof if name.startswith('O')]
print(gnames)

movies = [('Hansel and Gretel', 1992),('Jack the Giant Slayer', 1934), ('Ahmad', 2015), 
('Frankeistein', 1889), ('Apocalypto', 2002)]

cmovies = sorted([title for (title, year) in movies if year < 2000],reverse=True)
print(cmovies)

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
C ='abcd'
cartesian_product = [(a, b, c) for a in A for b in B for c in C ]
print(cartesian_product)




    

   