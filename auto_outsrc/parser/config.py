M = 'M'

blindingLoopVar = "y"
blindingSuffix = "-Blinded"
keygenBlindingExponent = "zz"
keygenFuncName = "keygen"
# superset of variables we have used to represent public parameters in
# our crypto schemes
keygenPubVar = ["pk", "mpk", "gpk"]
keygenSecVar = "sk"

# these should be keywords or part of semantics of SDL
inputKeyword = "input"
outputKeyword = "output"

setupFileName = "setupOutsourcing.py"
transformFileName = "transformOutsourcing.py"
decOutFileName = "decOutOutsourcing.cpp"

transformFunctionName = "transform"
partialCT = "partCT"
decOutFunctionName = "decout"

pySuffix = ".py"
cppSuffix = ".cpp"

setupFunctionOrder = ["setup", "keygen", "encrypt"]
argsToFirstSetupFunc = []

groupObjName = "groupObj"
groupArg = "MNT160"

rccaRandomVar = "R"