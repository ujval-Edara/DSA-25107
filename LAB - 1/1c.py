def search_employee(emp_list, emp_id, index=0):
    # av.sc.u4cse25107
    if index == len(emp_list):
        return False
    if emp_list[index] == emp_id:
        return True
    return search_employee(emp_list, emp_id, index + 1)

employees = [101, 105, 108, 112]
print(search_employee(employees, 108))