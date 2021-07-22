from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Undersea Adventure!"
    
    text = """You are on a scuba diving adventure with your best friend in the entire world, Larry! 
    As you explore the ocean bottom close to Catalina Island off the coast of Los Angeles, you happen upon a mysterious, ominous looking shipwreck. 
    Your friend Larry says, 'Oh my goodness, this is so cool!' and speeds off to explore the wreck."""

    choices = [
        ('enter_wreck',"Shrug your shoulders and take off after Larry"),
        ('wait_here',"Check your oxygen level and decide it is better to wait where you are for Larry to return!!!")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/inside")
def enter_wreck():
    title = "You go take off after Larry and enter the shipwreck..."
    
    text = """... as soon as you enter the wreck, you get a bad feeling as if you are being watched. 
    The back of your neck tickles and you peer around expecting to see a set of eyes watching you. 
    As you look around the interior of the decaying ship, you notice Larry peering at a skeleton sitting in an old arm chair."""

    choices = [
        ('move_closer',"Move closer to get a better view at what Larry is looking at"),
        ('swim_away',"Turn around and swim out of the wreck as fast as you can without looking back")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)


@app.route("/closer")
def move_closer():
    title = "You inch your way closer alongside Larry and peer at the old skeleton..."
    
    text = """... the skeleton turns its head towards you and begins to cackle. The sound gives you chills like nails on a chalkboard. 
    As you think, sound doesn't travel like that underwater, skeletons surround you and Larry, grabbing you with their talon like fingers and dragging you down into the hull of the ship."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/escape")
def swim_away():
    title = "You swim away!"
    
    text = """You bolt away from the shipweck to safety, leaving Larry behind. You hear the sound of a sinister voice cackling madly behind you. 
    In your terror, you skip your decompresion stops swimming madly towards the dive boat. As you break the surface, you spit out your regulator and begin sobbing.
    A few minutes later, Larry surfaces and says 'Gee, thanks for leaving me behind!'"""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/wait")
def wait_here():
    title = "You stay right where Larry left you"
    
    text = """The minutes pass slowly as you watch the dark hole Larry disappeared into. 
    You check your oxygen level as it begins to wane, letting it pass your typical safety level.
    After an eternally long ten minutes, you decide you need to make your way to the surface NOW whether Larry has returned or not. 
    Once you surface, you tell everyone about Larry's disappearance. Your team organizes dives to look around the shipwreck for Larry, but nobody wants to enter.
    As the sun sets, you realize you may never see Larry again."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
