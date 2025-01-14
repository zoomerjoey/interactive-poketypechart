from cmu_graphics import *

# variable and values defined
pokeTypes = ["NORMAL", "FIRE", "WATER", "ELECTRIC", "GRASS", "ICE", "FIGHTING", "POISON",
             "GROUND", "FLYING", "PSYCHIC", "BUG", "ROCK", "GHOST", "DRAGON", "DARK", "STEEL", "FAIRY"]
typeColors = [rgb(168, 168, 120), rgb(240, 128, 48), rgb(104, 144, 240), rgb(248, 208, 38), rgb(120, 200, 80), rgb(152, 216, 216), rgb(192, 28, 40), rgb(160, 64, 160), rgb(
    224, 192, 104), rgb(168, 144, 240), rgb(248, 88, 136), rgb(168, 184, 32), rgb(184, 160, 56), rgb(112, 88, 152), rgb(112, 56, 248), rgb(112, 88, 72), rgb(184, 184, 208), rgb(238, 153, 172)]
typeIcons = [f"pokemonIcons\\{i.lower()}.png" for i in pokeTypes]
typeChart = [
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],             # normal
    [1, .5, 2, 1, .5, .5, 1, 1, 2, 1, 1, .5, 2, 1, 1, 1, .5, .5],       # fire
    [1, .5, .5, 2, 2, .5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 1],         # water
    [1, 1, 1, .5, 1, 1, 1, 1, 2, .5, 1, 1, 1, 1, 1, 1, .5, 1],          # electric
    [1, 2, .5, .5, .5, 2, 1, 2, .5, 2, 1, 2, 1, 1, 1, 1, 1, 1],         # grass
    [1, 2, 1, 1, 1, .5, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1],            # ice
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, .5, .5, 1, 1, .5, 1, 2],          # fighting
    [1, 1, 1, 1, .5, 1, .5, .5, 2, 1, 2, .5, 1, 1, 1, 1, 1, .5],        # poison
    [1, 1, 2, 0, 2, 2, 1, .5, 1, 1, 1, 1, .5, 1, 1, 1, 1, 1],           # ground
    [1, 1, 1, 2, .5, 2, .5, 1, 0, 1, 1, .5, 2, 1, 1, 1, 1, 1],          # flying
    [1, 1, 1, 1, 1, 1, .5, 1, 1, 1, .5, 2, 1, 2, 1, 2, 1, 1],           # psychic
    [1, 2, 1, 1, .5, 1, .5, 1, .5, 2, 1, 1, 2, 1, 1, 1, 1, 1],          # bug
    [.5, .5, 2, 1, 2, 1, 2, .5, 2, .5, 1, 1, 1, 1, 1, 1, 2, 1],         # rock
    [0, 1, 1, 1, 1, 1, 0, .5, 1, 1, 1, .5, 1, 2, 1, 2, 1, 1],           # ghost
    [1, .5, .5, .5, .5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2],         # dragon
    [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0, 2, 1, .5, 1, .5, 1, 2],           # dark
    [.5, 2, 1, 1, .5, .5, 2, 0, 2, .5, .5, .5, .5, 1, .5, 1, .5, .5],   # steel
    [1, 1, 1, 1, 1, 1, .5, 2, 1, 1, 1, .5, 1, 1, 0, .5, 2, 1]           # fairy
]
typeBack1 = Group()
typeGroup = Group()
pokeTypePos1 = -1
pokeTypePos2 = -1
key = False
back1 = 0
back2 = 0
topLGroup = Group()
topRGroup = Group()
backgroundGroup = Group()
textGroup = Group()
selectedGroup = Group()
attackGroup = Group()
resetGroup = Group()
iconGroup = Group()
attacking = False
# ---------------------------------beginning of functions-------------------------


# selects if calculating for monotype or duotype
def selections(typeP1, typeP2):
    weaknessChecker(typeP1, typeP2) if typeP1 != typeP2 else normalRemover(
        typeChart[typeP1])

# computes the type interactions
def weaknessChecker(typeP1, typeP2):
    calcValues = []
    for i in range(len(pokeTypes)):
        calcValues.append((typeChart[typeP1][i] * typeChart[typeP2][i]))
    normalRemover(calcValues)



# grabs the attacking values instead of defending
def attackingChecker(typePos):
    calcValues = []
    for i in range(len(pokeTypes)):
        calcValues.append(typeChart[i][typePos])
    normalRemover(calcValues)

# removes normal effective types to free screen space since normal effectiveness is implied instead and sorts data into effusiveness
# could refactor to make use index and multiplier only
def normalRemover(list):
    # first layer groups by effectiveness with: weak, resist, nullified. second layer groups parts of each type: text, color, icon
    finalData = [[[], [], []], [[], [], []], [[], [], []]]
    for i in range(len(list)):
        if list[i] > 1:
            finalData[0][0].append(pokeTypes[i] + " X " + str(list[i]))
            finalData[0][1].append(typeColors[i])
            finalData[0][2].append(typeIcons[i])
        elif list[i] < 1 and list[i] != 0:
            finalData[1][0].append(
                pokeTypes[i] + " / " + str(rounded(1/list[i])))
            finalData[1][1].append(typeColors[i])
            finalData[1][2].append(typeIcons[i])
        elif list[i] == 0:
            finalData[2][0].append(pokeTypes[i])
            finalData[2][1].append(typeColors[i])
            finalData[2][2].append(typeIcons[i])
            
    valueDisplay(finalData)


# displays the final values
def valueDisplay(data):
    global pokeTypes
    global pokeType1
    global pokeType2
    global typeColors
    global key
    global typeGroup
    global topLGroup
    global topRGroup
    global attacking
    # size for the interacting types (not the types shown at the top of the screen which are the pokemon's type(s))
    textSize = 20
    typeBorder = .5  # border width of types shown in results
# clears typeGroups to not cause problems
    typeGroup = Group()
    topRGroup = Group()
    topLGroup = Group()

# runs if both types are the same or if attacking, creates a single banner and makes the icon and text a bit bigger
    if pokeTypePos1 == pokeTypePos2 or attacking:
        typeBack = Rect(
            0, 0, 400, 60, fill=typeColors[pokeTypePos1], border='black', borderWidth=4)
        typeText = Label(pokeType1, typeBack.centerX, typeBack.centerY,
                         fill='white', size=55, border='white', borderWidth=1.5)
# used for reselection logic
        if attacking:
            topLGroup.add(typeBack, typeText)
        else:
            topRGroup.add(typeBack, typeText)

# runs if the types are different, creates a split banner
    else:

        typeBack1 = Rect(
            0, 0, 175, 60, fill=typeColors[pokeTypePos1], borderWidth=2)

        typeBack2 = Rect(
            225, 0, 175, 60, fill=typeColors[pokeTypePos2], borderWidth=2)

        typeSplit1 = Polygon(typeBack1.right, typeBack1.top, typeBack2.left, typeBack1.top,
                             typeBack1.right, typeBack1.bottom, fill=typeColors[pokeTypePos1], border=None)
        typeSplit2 = Polygon(typeBack2.left, typeBack2.top, typeBack2.left, typeBack2.bottom,
                             typeBack1.right, typeBack2.bottom, fill=typeColors[pokeTypePos2], border=None)
        typeText1 = Label(pokeType1, typeBack1.centerX+10, typeBack1.centerY,
                          fill='white', border='white', borderWidth=1.5)
        typeText1.size = (20-len(typeText1.value))*2.75
        typeText2 = Label(pokeType2, typeBack2.centerX-10, typeBack2.centerY,
                          fill='white', border='white', borderWidth=1.5)
        typeText2.size = (20-len(typeText2.value))*2.75

        border = Rect(0, 0, 400, 60, fill=None, border='black', borderWidth=4)
        typeGroup.add(border)
        topLGroup.add(typeBack1, typeSplit1, typeText1)
        topRGroup.add(typeBack2, typeSplit2, typeText2)
        topLGroup.toBack()
        topRGroup.toBack()

    # displays super effective types if there are any
    if len(data[0][0]) > 0:
        textLabel = Label("SUPER EFFECTIVE", 100, 75, size=textSize, bold=True)
        typeGroup.add(textLabel)
        for i in range(len(data[0][0])):
            back = Rect(textLabel.centerX-75, (textLabel.centerY +
                        50)+((i-1)*37), 145, 25, fill='black')
            text = Label(data[0][0][i], back.centerX+5, back.centerY, size=textSize,
                         fill='white', border='white', borderWidth=typeBorder, align='left')
            text.left = back.left + 15
            back.width = (text.right - text.left)+15
            backFlair = Polygon(back.right, back.top, back.right+25,
                                back.top, back.right, back.bottom, fill='black')
            iconBack = Polygon(back.left-25, text.centerY, back.left-5, back.top-5, back.left+15,
                               text.centerY, back.left-5, back.bottom+5, fill=data[0][1][i], border='black')
            icon = Image(data[0][2][i], iconBack.left+5,
                         iconBack.top+3, width=30, height=30)
            typeGroup.add(back, backFlair, text, iconBack, icon)

    # displays ineffective types if there are any
    if len(data[1][0]) > 0:
        textLabel = Label("NOT EFFECTIVE", 300, 75, size=textSize, bold=True)
        typeGroup.add(textLabel)
        E = (len(data[1][0])*0.13)
        A = (len(data[1][0]) > 6)
        for i in range(len(data[1][0])):
            back = Rect((textLabel.centerX-75), (textLabel.centerY+15)+(((i)*37)/E)
                        if A else (textLabel.centerY+15)+((i)*35), 145, 25/E if A else 25, fill='black')
            text = Label(data[1][0][i], back.centerX, back.centerY, size=textSize/E if A else textSize,
                         fill='white', border='white', borderWidth=typeBorder, align='left')
            text.left = back.left+15
            back.width = (text.right - text.left)+15
            backFlair = Polygon(back.right, back.top, back.right+(
                25/E) if A else back.right+25, back.top, back.right, back.bottom, fill='black')
            iconBack = Polygon(back.left-(25/E) if A else back.left-25, text.centerY, back.left-(5/E) if A else back.left-5, back.top-(5/E) if A else back.top-5, back.left+(
                15/E) if A else back.left+15, text.centerY, back.left-(5/E) if A else back.left-5, back.bottom+(5/E) if A else back.bottom+5, fill=data[1][1][i], border='black')
            icon = Image(data[1][2][i], iconBack.left+(5/E) if A else iconBack.left+5, iconBack.top+(
                3/E) if A else iconBack.top+3, width=30/E if A else 30, height=30/E if A else 30)
            typeGroup.add(back, backFlair, text, iconBack, icon)

    # displays the no effect types if there are any
    if len(data[2][0]) > 0:
        if (len(data[1][0]) + len(data[2][0])) < 7:
            if len(data[1][0]) > 0:
                textLabel = Label("NO EFFECT", 300, (len(
                    data[1][0])*37) + 95, size=textSize, bold=True)
            else:
                textLabel = Label("NO EFFECT", 300, 75,
                                  size=textSize, bold=True)
        else:
            if len(data[0][0]) > 0:
                textLabel = Label("NO EFFECT", 100, (len(
                    data[0][0])*37) + 95, size=textSize, bold=True)
            else:
                textLabel = Label("NO EFFECT", 100, 75,
                                  size=textSize, bold=True)
        typeGroup.add(textLabel)
        for i in range(len(data[2][0])):
            back = Rect(textLabel.centerX-75, (textLabel.centerY +
                        50)+((i-1)*37), 105, 25, fill='black')
            text = Label(data[2][0][i], back.centerX+5, back.centerY, size=textSize,
                         fill='white', border='white', borderWidth=typeBorder, align='left')
            text.left = back.left + 15
            back.width = (text.right - text.left)+15
            backFlair = Polygon(back.right, back.top, back.right+25,
                                back.top, back.right, back.bottom, fill='black')
            iconBack = Polygon(back.left-25, text.centerY, back.left-5, back.top-5, back.left+15,
                               text.centerY, back.left-5, back.bottom+5, fill=data[2][1][i], border='black')
            icon = Image(data[2][2][i], iconBack.left+5,
                         iconBack.top+3, width=30, height=30)
            typeGroup.add(back, backFlair, text, iconBack, icon)
    key = True

# changes what is selected on the type selection


def selectionActive(back, selection):
    back.border = 'black'
    selection.top = back.top
    selection.left = back.left
    selection.toFront()
    selection.visible = True

# clears screen for the type chart


def clearScreen():
    back1.border = None
    # helpText.visible = False
    backgroundGroup.visible = False
    textGroup.visible = False
    selectedGroup.visible = False
    resetGroup.visible = False
    attackBack.border = None
    attackFlair.fill = 'lightGray'
    iconGroup.visible = False
    if attacking:
        attackGroup.visible = True
    else:
        attackGroup.visible = False

# used to show type selection after first use


def showScreen():
    global iconGroup
    typeGroup.visible = False
    textGroup.visible = True
    backgroundGroup.visible = True
    selectedGroup.visible = True
    topLGroup.visible = False
    topRGroup.visible = False
    iconGroup.visible = True
    if attacking:
        attackGroup.visible = True
        attackFlair.fill = 'black'
        typeBackR.opacity = 0
        typeIconR.opacity = 0
    else:
        attackGroup.visible = False
        resetGroup.visible = True

# ----------------------------start of program-----------------------------------


# creates the type display
for i in range(len(pokeTypes)):
    background = Rect((i % 4)*100, (i//4)*60, 100, 60,
                      fill=typeColors[i], borderWidth=3)
    name = Label(pokeTypes[i], background.centerX,
                 background.centerY, size=20, bold=True, fill='white')

    backgroundGroup.add(background)
    textGroup.add(name)
# helpText = Label("click a type",0,365, size=40, align='left')

# creates selected effect
selected1 = Rect(200, 240, 100, 60, fill='Gray', opacity=50,
                 border='black')  # used for type darkening
selected2 = Rect(0, 0, 100, 60, fill='Gray', opacity=50, border='black')
selectedGroup.add(selected1, selected2)
selected1.visible = False
selected2.visible = False

# reset label
resetBack = Rect(200, 340, 200, 60, fill='Gray', visible=False)
resetText = Label("Reset", resetBack.centerX,
                  resetBack.centerY, visible=False, size=40)
resetGroup.add(resetBack, resetText)
resetGroup.visible = False

# attack label
attackBack = Rect(200, 340, 200, 60, fill='lightGray',
                  borderWidth=3)  # attacking display creation
attackText = Label("ATTACK", attackBack.centerX,
                   attackBack.centerY, size=30, fill='black', bold=True)
attackFlair = Polygon(attackBack.left, attackBack.top, attackBack.left-50,
                      attackBack.bottom, attackBack.left, attackBack.bottom, fill='lightgray')
attackGroup.add(attackBack, attackText, attackFlair)
attackGroup.visible = True

# type Icons
typeBackL = Polygon(0, 375, 25, 350, 50, 375, 25,
                    400, fill='white', border='black')
typeBackR = Polygon(50, 375, 75, 350, 100, 375, 75,
                    400, fill='white', border='black')
typeIconL = Image(typeIcons[0], 0, 350, height=50, width=50, opacity=0)
typeIconR = Image(typeIcons[0], 50, 350, height=50, width=50, opacity=0)
iconGroup.add(typeBackL, typeBackR, typeIconL, typeIconR)


def onMousePress(mouseX, mouseY):
    global pokeTypePos1
    global pokeTypePos2
    global pokeType1
    global pokeType2
    global typeBack1
    global backgroundGroup
    global textGroup
    global topLGroup
    global topRGroup
    global back1
    global back2
    global selectedGroup
    global key
    global resetGroup
    global attackGroup
    global attacking
    global typeIcons
    global iconGroup
    global typeBackR
    global typeBackL

# resets selected types
    if resetGroup.hitTest(mouseX, mouseY) != None and resetGroup.visible:
        pokeTypePos1 = -1
        pokeTypePos2 = -1
        back1.border = None
        if not attacking:
            back2.border = None
        selected1.visible = False
        selected2.visible = False
        resetGroup.visible = False
        attackGroup.visible = True
        typeBackL.fill = 'white'
        typeBackR.fill = 'white'
        typeIconL.opacity = 0
        typeIconR.opacity = 0
# toggle attacking on and off
    elif (attackGroup.hitTest(mouseX, mouseY) != None and attackGroup.visible and not key):
        attacking = not attacking
        if pokeTypePos1 == -1:
            back = attackGroup.hitTest(mouseX, mouseY)
            if attacking:
                attackBack.border = 'black'
                attackFlair.fill = 'black'
                typeBackR.opacity = 0
            else:
                attackBack.border = None
                attackFlair.fill = 'lightGray'
                typeBackR.opacity = 100
# go strait to attacking math if first type is already selected
        else:

            attackingChecker(pokeTypePos1)
            typeBackR.opactiy = 0
            backgroundGroup.add(back1)

            clearScreen()

# checks clicking on a type for type choice
    elif (backgroundGroup.hitTest(mouseX, mouseY) != None or selectedGroup.hitTest(mouseX, mouseY) == selected1) and backgroundGroup.visible == True:
        if pokeTypePos1 == -1:
            back1 = backgroundGroup.hitTest(mouseX, mouseY)
            typeBack1.add(back1)
            selectionActive(back1, selected1)
            typeText1 = textGroup.hitTest(
                (typeBack1.centerX), (typeBack1.centerY))
            pokeType1 = typeText1.value

            pokeTypePos1 = pokeTypes.index(pokeType1)
            typeBackL.fill = typeColors[pokeTypePos1]
            attackGroup.visible = True

    # bypasses the second selection for attack reselection
            if attacking:
                attackingChecker(pokeTypePos1)
                backgroundGroup.add(back1)
                clearScreen()

    # bypasses the second selection for left type reselection
            elif pokeTypePos2 != -1:
                selections(pokeTypePos1, pokeTypePos2)
                backgroundGroup.add(back1)
                clearScreen()

    # selects the same type for both slots
        elif selectedGroup.hitTest(mouseX, mouseY) == selected1:
            back2 = back1
            pokeType2 = pokeType1
            pokeTypePos2 = pokeTypePos1
            backgroundGroup.add(back2)
            selectionActive(back2, selected2)
            normalRemover(typeChart[pokeTypePos1])
            backgroundGroup.add(back1)
            clearScreen()

    # selects second type
        else:
            back2 = backgroundGroup.hitTest(mouseX, mouseY)
            typeText2 = textGroup.hitTest((back2.centerX), (back2.centerY))
            pokeType2 = typeText2.value
            backgroundGroup.add(back2)
            selectionActive(back2, selected2)
            backgroundGroup.add(back1)
            back2.border = None
            pokeTypePos2 = pokeTypes.index(pokeType2)
            typeBackR.fill = typeColors[pokeTypePos2]
            selections(pokeTypePos1, pokeTypePos2)
            clearScreen()

    # reselection of types
    elif key:
        # left type
        if topLGroup.hitTest(mouseX, mouseY) != None:
            key = False
            back1.border = None
            if not attacking:
                back2.border = 'black'
            else:
                attackBack.border = 'black'
            pokeTypePos1 = -1
            typeBackL.fill = 'white'
            typeIconL.opacity = 0
            showScreen()
            selected1.visible = False

    # right type
        elif topRGroup.hitTest(mouseX, mouseY) != None:
            key = False
            back2.border = None
            if not attacking:
                back1.border = 'black'
            pokeTypePos2 = -1
            typeBackR.fill = 'white'
            typeIconR.opacity = 0
            showScreen()
            selected2.visible = False


cmu_graphics.run() # type: ignore
