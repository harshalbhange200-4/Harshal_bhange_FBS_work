def emp(id , name , sal = 15000 , dept = 'back office'):
    print('ID:',id)
    print('Name:',name)
    print('Salary :',sal)
    print('Department:',dept)
emp(101, 'ABC',30000,'IT')#passing values can use 
# if we can't pass value of salary and deprtment its add default value
emp(102,'DEF')# its take def value at the place of salary and departmet 