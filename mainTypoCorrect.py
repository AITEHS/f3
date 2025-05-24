import tkinter
#possibly to modify: GoalSettings\goalId = int, change id to goalID or something if it is already reserved for something python related, remove notifications,

class AppSettings():
    def __init__(self, currency:str, dateFormat:str, theme:str, backupEnabled:bool):
        self.currency = currency
        self.dateFormat = dateFormat
        self.theme = theme
        self.backupEnabled = backupEnabled
    def loadSettings():
        pass

    def saveSettings():
        pass

    def resetToDefaults():
        pass

class Database():
    def saveGoal(goal:Goal):
        output:bool
        pass

    def loadGoal(goalId:str):
        output:Goal
        pass

    def loadAllGoals():
        output:list
        pass

    def updateGoal(goal:Goal):
        output:bool
        pass

    def deleteGoal(goalId:str):
        output:bool
        pass

    def saveAppSettings(settings:AppSettings):
        output:bool
        pass

    def loadAppSettings():
        output:AppSettings
        pass

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

class GoalDetailsUI():
    def __init__(self, goal:Goal):
        self.goal = goal

    def displayGoalInfo():
        pass

    def updateProgress(amount:float):
        pass

    def openGoalSettings():
        pass


class GoalSettingsUI():
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

    def calculateProgress():
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

class GoalManager():
    def __init__(self, goals:list, database:Database):
        self.goals = goals
        self.database = database

    def createGoal(goalData:GoalData):
        output:Goal
        pass

    def deleteGoal(goalId:str):
        output:bool
        pass

    def updateGoal(goal:str):
        output:bool
        pass

    def getGoals():
        output:list
        pass

    def getGoal(goalId:str):
        output:Goal
        pass

class AppSettingsUI():
    def __init__(self, appSettings:AppSettings):
        self.appSettings = appSettings


    def displaySettings():
        pass


    def modifySettings(settings:AppSettings):
        pass

    def resetSettings():
        pass

class MainMenuUI():
    def __init__(self, goalManager:GoalManager):
        self.goalManager = goalManager

    def displayGoalsList():
        pass

    def showCreateGoalOption():
        pass

    def showAppSettings():
        pass

    def exitApplication():
        pass


class GoalCreationUI():
    def __init__(self, goalManager:GoalManager):
        self.goalManager = goalManager

    def validateInput(goalData:GoalData):
        output:bool
        pass
    def createGoal(goalData:GoalData):
        pass

    def cancelCreation():
        pass