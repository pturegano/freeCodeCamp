

from distutils.log import error
import re


def splitExpression(expression):
    expression = expression.split(" ")
    #check operator
    if expression[1] != "+" and expression[1] != "-":
        expression[0] = "Error: Operator must be '+' or '-'."
    else:
        operator = expression[1]
        number1 = int(expression[0])
        number2 = int(expression[2])
        if number1 > 9999 or number2 > 9999:
            expression[0] = "Error: Numbers cannot be more than four digits."

    return expression

def fillMinChars(num, minChars):
    num = str(num)
    i = 0
    while i < minChars:
        num = " " + num
        i += 1
    return num

def FormatResult(exprRaw, printResult = False):
    line1,line2,line3,line4 = "","","",""
    mySpace = "    "
  
    for i in range(len(exprRaw)):
        lenTerm1 = len(str(exprRaw[i][0]))
        lenTerm2 = len(str(exprRaw[i][2]))
        if lenTerm1 > lenTerm2:
            lenTotal = lenTerm1
        else:
            lenTotal = lenTerm2
        lenTotal += 2
        line1 += fillMinChars(exprRaw[i][0],(lenTotal-lenTerm1)) + mySpace    
        line3 += exprRaw[i][1] + fillMinChars(exprRaw[i][2],(lenTotal-lenTerm2-1)) + mySpace
      
        for j in range(0,lenTotal):
            line2 += "-"
        line2 += "    "
        if exprRaw[i][1] == "+":
            total = int(exprRaw[i][0]) + int(exprRaw[i][2])
        else:
            total = int(exprRaw[i][0]) - int(exprRaw[i][2])
        lenLine4 = lenTotal -len(str(total))
        line4 += fillMinChars(total,lenLine4) + mySpace
    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()
    line4 = line4.rstrip()
    line1 += "\n"
    line2 += "\n"
    line3 += "\n"
    line4 += "\n"
    result = line1 + line3 + line2
    if printResult:
        result = line1 + line3 + line2 + line4
    result = result.rstrip()
    return result

def arithmetic_arranger(problemSpec, printResult = False):
    errorCount = 0
    returnTxt = ""
    returnEq = []
    if len(problemSpec) > 5:
        returnTxt = "Error: Too many problems."
    else:
        for spec in problemSpec:
            try:
                specSplit = splitExpression(spec)
                if specSplit[0].find("Error:") != -1:
                    returnTxt = specSplit[0]
                    errorCount += 1     
                    break 
                else:
                    returnEq.append(specSplit)
            except ValueError:  
                errorCount += 1
                returnTxt = "Error: Numbers must only contain digits."
            
    if returnTxt.find("Error") != -1:
        returnTxt = returnTxt
    else:
        returnTxt = FormatResult(returnEq, printResult)
        
    return returnTxt