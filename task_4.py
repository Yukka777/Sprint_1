new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

#Перенос task_005 в completed_tasks
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))

# Удаление task_007
new_tasks.remove('task_007')

# Вывод последней задачи
print(new_tasks[-1])
