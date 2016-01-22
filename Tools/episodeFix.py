import os

#
# Fixing the wrong Epsisode Numbers of Transformers ripped from the RhenoDVD Set
#

season2_rhinoEpisodeList = [1,6,14,15,5,10,2,11,8,4,18,16,13,9,19,20,17,03,21,22,23,24,26,12,27,7,25,29,30,28,31,37,36,35,38,34,33,39,40,41,48,44,43,45,32,46,47,42,49]

def constructFilename(base,ext,season,episode):
    return base + "\ S%02dE%02d." % (season,episode) + ext

def cleanUpTempFiles():
    # rename all the files leading with ~ removing to ~
    print "Cleaning Up ..."
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if (f.startswith('~')):
            print f, " --> ", f[1:]
#            os.rename(f,f[1:])

def renameFiles(showName,ext,season,episodeList):
    print "start fixing episode numbering ..."
    for i in range(0,len(episodeList)):
        f1 = constructFilename(showName.strip(),ext.strip(),season,episodeList[i])
        f2 = constructFilename("~"+showName.strip(),ext.strip(),season,i+1)
        print f1, " --> ", f2
#       os.rename(f1,f2)
    cleanUpTempFiles()
    return None


renameFiles("Transformers","mkv",2,season2_rhinoEpisodeList)

