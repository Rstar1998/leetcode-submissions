class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = tasks
        self.pri_queue = []
        self.task_pri = defaultdict(int)
        self.task_user = defaultdict(int)
        
        for task in tasks:
            userId = task[0]
            taskId = task[1]
            priority = task[2]

            self.task_pri[taskId] = priority
            self.task_user[taskId] = userId

            heapq.heappush(self.pri_queue, (-priority,-taskId))

        

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_pri[taskId] = priority
        self.task_user[taskId] = userId
        heapq.heappush(self.pri_queue, (-priority,-taskId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_pri[taskId] = newPriority
        userId = self.task_user[taskId] 
        
        heapq.heappush(self.pri_queue, (-newPriority,-taskId))

        
    def rmv(self, taskId: int) -> None:
        self.task_pri[taskId] = None
        
        

    def execTop(self) -> int:
        

        while self.pri_queue:
            priority,taskId = heapq.heappop(self.pri_queue)
            if self.task_pri[-taskId] is not None and self.task_pri[-taskId] == -priority:
                self.task_pri[-taskId] = None
                return self.task_user[-taskId]
        return -1
        

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()