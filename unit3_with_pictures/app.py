from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    title = "What's your organisational style?"
    
    text = """Your mother emails you another family photo. Do you print and post it to your wall?"""

    choices = [
        ('save_it_to_camera',"Nope, just save it to my phone's camera roll"),
        ('delete',"Read, then delete. I believe in Inbox 0."),
        ('print_and_post', "Absolutely")
    ]

    return render_template('home.html', title=title, text=text, choices=choices)


@app.route("/delete")
def delete():
    title = "YOU DELETED THE PHOTO YOUR MOTHER SENT YOU?"
    
    text = """What kind of son/daughter are you? You better undo it or I'll spill the beans. """

    choices = []

    return render_template('delete.html', title=title, text=text, choices=choices)

@app.route("/print_and_post")
def print_and_post():
    title = "YOU PASSED THE TEST."
    
    text = """Your mother paid me to trick you. This proves you're a good son/daughter. You make 
    her proud. Who cares if you're organized or not? Just keep up with the work and family time. """

    choices = []

    return render_template('print_and_post.html', title=title, text=text, choices=choices)


@app.route("/save_it_to_camera")
def save_it_to_camera():
    title = "Are there any plants on your desk?"
    
    text = """"""

    choices = [
        ('yes_plants',"YES"),
        ('no_plants',"NO")
    ]

    return render_template('save_it_to_camera.html', title=title, text=text, choices=choices)

@app.route("/save_it_to_camera/no_plants")
def no_plants():
    title = "What's your take on a standing desk?"
    
    text = """"""

    choices = [
        ('not_for_me', "It ain't for me. I prefer the good old chair."),
        ('sitting_kills_me', "Sitting kills me.")
    ]

    return render_template('no_plants.html', title=title, text=text, choices=choices)

@app.route("/save_it_to_camera/no_plants/not_for_me")
def not_for_me():
    title = "THE BARE MINIMALIST"
    
    text = """No standing chair, no plants, no nothing. You do the work, then go home. You see no point in all the tacky details. 
    Just more items to clean the dust off. Just leave me be, and I'm good to go."""

    choices = []

    return render_template('no_standing_desk.html', title=title, text=text, choices=choices)


@app.route("/save_it_to_camera/no_plants/sitting_kills_me")
def sitting_kills_me():
    title = "YOU HAVE TO TRY IT FIRST."
    
    text = """You follow the trends. Ergonomic chair? Tried it first. Experimenting with the new printer? You volunteer.
    You have a new sorting method every week based on what's trending. Basically you're the office trendsetter."""

    choices = []

    return render_template('yes_standing_desk.html', title=title, text=text, choices=choices)







@app.route("/save_it_to_camera/yes_plants")
def yes_plants():
    title = "Which plant suits you best?"
    
    text = """"""

    choices = [
        ('cactus', "A cactus in a small pot."),
        ('all_plants', "All of them - it's like a nursery in here.")
    ]

    return render_template('yes_plants.html', title=title, text=text, choices=choices)

@app.route("/save_it_to_camera/yes_plants/cactus")
def cactus():
    title = "THE MINIMALIST"
    
    text = """Only the bearest essentials - your laptop and somewhere discreet to charge it. Everything worth keeping is in the cloud, and the rest can be resources
    if and when hanging files and drawers full of pens and post-its are for suckers. """

    choices = []

    return render_template('cactus.html', title=title, text=text, choices=choices)

@app.route("/save_it_to_camera/yes_plants/all_plants")
def all_plants():
    title = "YOU PACK IT IN."
    
    text = """You know you have notes from that meeting somewhere in here. You manage to keep every pad of paper - and notebook and business card and pile of sticky notes - in case
    you need them down the road. You hit print like there's no tomorrow, and you stuff it all into corresponding
    files in a cabinet that barely closes. The walls of your cubicle are in birthday cards from coworkers and pictures of loved ones -
    pinned 3 or 4 deep. In case of layoff, it would take a day to get you out of your cubicle."""

    choices = []

    return render_template('all_plants.html', title=title, text=text, choices=choices)


