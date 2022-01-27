import pdb 
from models.task import Task
import repositories.task_repository as task_repository  
from models.user import User
import repositories.user_repository as user_repository

user_repository.delete_all()
task_repository.delete_all()
# task_1 = Task("Do the dishes", "Jack Jarvis", 20)
# task_repository.save(task_1)

# returned = task_repository.select(2)

# result = task_repository.select_all()

# for task in result:
#     print(task.__dict__)

# task_1.mark_complete()
# task_repository.update(task_1)

# # task_repository.delete_all()
# # task_repository.delete(4)
# # task_repository.delete(5)
# # task_repository.delete(6)

user_1 = User("John", "Stamos")
user_repository.save(user_1)

user_2 = User("John", "Mellencamp")
user_repository.save(user_2)

task_1 = Task("Crush my enemies", user_1, 10)
task_repository.save(task_1)

task_2 = Task("See them driven before me", user_2, 50)
task_repository.save(task_2)

found_users = user_repository.select_all()

tasks_assigned = user_repository.tasks(user_1)





pdb.set_trace()