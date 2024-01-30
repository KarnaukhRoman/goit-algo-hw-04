
def total_salary(path):
    total_sum = 0
    try:
        with open(path, 'r') as salary_file:
            lines = [el.strip().split(',') for el in salary_file.readlines()]
            for i in lines:
                total_sum+=int(i[1])
            return (total_sum, total_sum/len(lines))
    except Exception as e:
            print (f'ERROR: {e}')
            return (0,0)
    
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

#**********************************************************************************
def get_cats_info(path):
     keys_list = ["id", "name", "age"]
     list_cats = []
     try:
          with open(path, 'r') as file_cats:
               lines = [el.strip().split(',') for el in file_cats.readlines()]
               for i in lines:
                  list_cats.append(dict(zip(keys_list, i)))  
     except Exception as e:
        print(f'ERROR: {e}')
    
     return list_cats

cats_info = get_cats_info("home/cats.txt")
print(cats_info)

#********************************************************************
