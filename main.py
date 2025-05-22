import tkinter
#possibly to modify: GoalSettings\goalId = int, change id to goalID or something if it is already reserved for something python related, remove notifications,

class GoalSettings():
    def __init__(self, goalId:str,notificationsEnabled:bool, reminderFrequency:int, autoTracking:bool):
        self.goalId = goalId
        self.notificationsEnabled = notificationsEnabled
        self.reminderFrequency = reminderFrequency 
        self.autoTracking = autoTracking

    def validate():
        output:bool
        pass

    def applySettings():
        pass

class Date():
    pass

class GoalData():
    def __init__(self, name:str, description:str, targetAmount:float, deadline:Date, category:str):
        self.name = name
        self.description = description
        self.targetAmount = targetAmount
        self.deadline = deadline
        self.category = category


    def validate():
        output:bool
        pass

class  GoalDetailsUI():
    def __init__(self, goal:Goal):
        self.goal = goal

    def displayGoalInfo():
        pass

    def updateProgress(amount:float):
        pass

    def openGoalSettings():
        pass


class  GoalSettingsUI():
    def __init__(self, goal:Goal):
        self.goal = goal

    def displaySettings():
        pass

    def modifySettings(settings:GoalSettings):
        pass

    def deleteGoalWithConfirmation():
        pass

    def showDeleteConfirmation():
        output:bool
        pass

class Goal():
    def __init__(self, id:str, name:str, description:str, targetAmount:float, currentAmount:float, deadline:Date, createdDate:Date, category:str, isCompleted:bool):
        self.id = id
        self.name = name
        self.description = description
        self.targetAmount = targetAmount
        self.currentAmount = currentAmount
        self.deadline = deadline
        self.createdDate = createdDate
        self.category = category
        self.isCompleted = isCompleted

    def updateProgress(amount:float):
        pass

    def claculateProgress():
        output:float
        pass

    def isGoalAchieved():
        output:bool
        pass

    def getSettings():
        output:GoalSettings
        pass

    def updateSettings(settings:GoalSettings):
        pass

