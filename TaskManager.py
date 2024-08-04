# Task Manager Class
##### By: Arav Raghunathan

# 1. Class Definition
class TaskManager:
    # 2. Constructor that Instantiates a New List
    def __init__(self):
        self.task_list = []

    # 3. Getter: Return the Contents of Task List
    def get_task_list(self):
        return self.task_list

    def return_list_item (self, task_name):
        for i in range(len(self.task_list)):
            if self.task_list[i] == task_name:
                return i

    @staticmethod
    # 4. add: Static_Method that adds a Task with a Priority Rating (Level Between 1 and 10)
    def add(self, task, priority):
        new_task = (task, priority)
        self.task_list.append(new_task)

    @staticmethod
    # 5. remove: Static_Method that will remove the Task with a Given Name
    def remove(self, task_name):
        for value in self.task_list:
            if value[0] == task_name:
                self.task_list.remove(value)

    @staticmethod
    # 6. prioritize: change the priority level for a Specific Task Name
    def prioritize(self, task_name, new_priority):
        new_task = (task_name, new_priority)
        for i in range(len(self.task_list)):
            if self.task_list[i][0] == task_name:
                self.task_list[i] = new_task

    # 7. print: Return The Desired Output For the Task in the List
    @staticmethod
    def to_string (self, i):
        new_string = (self.task_list[i][0] + ", Priority: " + str(self.task_list[i][1]) + "\n")
        return new_string
    # 8. reorder: Return the Order on the Task Lists that goes from a high_value to a low_value
    @staticmethod
    def reorder(self, high_val=100, low_val=0):
        # 9. Create a new_array to store the reorder list
        reordered = []
        while high_val >= low_val:
            for i in range(len(self.task_list)):
                if self.task_list[i][1] == high_val:
                    reordered.append(self.task_list[i])
            high_val -= 1
        self.task_list = reordered

    @staticmethod
    def replace (self, new_task_name, old_task_name, new_priority):
        for i in range(len(self.task_list)):
            if self.task_list[i][0] == old_task_name:
                self.task_list[i] = (new_task_name, new_priority)
