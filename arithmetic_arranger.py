import re

def arithmetic_arranger(problems,displayAnswers=False):
    
    def searchError(equations):
        
        if len(equations)>5:
            return 'Error: Too many problems.'
            
        errorTypes=[{'erre': re.compile(r"[%/*x]+"), 'msg':"Error: Operator must be '+' or '-'."},
        {'erre': re.compile(r"[a-z]+",re.IGNORECASE), 'msg':"Error: Numbers must only contain digits."},
        {'erre': re.compile(r"\d{5}"), 'msg':"Error: Numbers cannot be more than four digits."}]
        
        for eq in equations:
            for errorType in errorTypes:
                found= errorType['erre'].search(eq)
                if found:
                    return errorType['msg']
        return False
    
    getErrorMsg= searchError(problems)
    
    if getErrorMsg:
        return getErrorMsg
    
    class Problem:
        
        def __init__(self,first,second,operator):
            self.firstNum=first
            self.secondNum=second
            self.operator=operator
        
        @property
        def firstNum(self):
            return self._firstNum
        @firstNum.setter
        def firstNum(self,value):
            self._firstNum=value
        
        @property
        def secondNum(self):
            return self._secondNum
        @secondNum.setter
        def secondNum(self,value):
            self._secondNum=value
        
        @property
        def operator(self):
            return self._operator
        @operator.setter
        def operator(self,value):
            self._operator=value
        
        def dashLine(self):
            firstLen,secondLen=len(self.firstNum),len(self.secondNum)
            higherLen=firstLen
            if secondLen>firstLen:
                higherLen=secondLen
            return '-'*(2+higherLen)
        
        def answer(self):
            if self.operator == '+':
                return int(self.firstNum)+int(self.secondNum)
            return int(self.firstNum)-int(self.secondNum)
    
    matchEquation=re.compile(r"(\d+)\s+([-+])\s+(\d+)")
    problemObjectsArray=[]
    for problem in problems:
        matched=matchEquation.search(problem)
        problemObjectsArray.append(Problem(matched.group(1),matched.group(3),matched.group(2)))
    
    firstChain=''
    secondChain=''
    dashChain=''
    resultChain=''
    for idx,problemObj in enumerate(problemObjectsArray,1):
        arrangedFirstNum=problemObj.firstNum.rjust(len(problemObj.dashLine()))
        arrangedSecondNum=problemObj.operator+problemObj.secondNum.rjust(len(problemObj.dashLine())-1)
        dash=problemObj.dashLine()
        if idx < len(problemObjectsArray):
            arrangedFirstNum+='    '
            arrangedSecondNum+='    '
            dash+='    '
        else:
            arrangedFirstNum+='\n'
            arrangedSecondNum+='\n'
        firstChain+=arrangedFirstNum
        secondChain+=arrangedSecondNum
        dashChain+=dash
    if displayAnswers:
        dashChain+='\n'
        for idx,problemObj in enumerate(problemObjectsArray,1):
            result=str(problemObj.answer())
            arrangedResult=result.rjust(len(problemObj.dashLine()))
            if idx< len(problemObjectsArray):
                arrangedResult+='    '
            resultChain+=arrangedResult
    
    arranged_problems=firstChain+secondChain+dashChain+resultChain
    return arranged_problems