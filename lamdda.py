g = lambda x: 5*x**3+3*x -4
print(g(8))

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
user = full_name('Leonhard', 'Euler')
print(user)


sci_prof = ['Yussif Abdul Salam', 'Ridwan Shaiba', 'Osei Nimako Daniel',
'Opoku Mathew', 'Otoo Eunice', 'Mohammed Saani', 'Zakaria Hamza']

sci_prof = sci_prof.sort (key=lambda name:name.split(' ')[-1].lower())
print(sci_prof)

def build_quadratic_function(a, b, c):
    return lambda x: a*x**2+b*x+c

f = build_quadratic_function(2, 0, -5)

print(f(0))
print(f(1))
print(f(2))

print(build_quadratic_function(2, 0, 3)(2))