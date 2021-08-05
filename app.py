from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "Scenario 1"
    
    text = """You are at home, watching TV in the bedroom. Alone. The power goes out. What do you do? """

    choices = [
        ('use_phone',"Panic. You freak out. Your phone battery is low."),
        ('just_chill',"Wait and See. This is just temporary. You checked the street lights, they're out. Nothing you can do. Let's wait and see."),
        ('candles', "Look for candles. There are candles somewhere in the basement...")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/use_phone")
def use_phone():
    title = "Don't panic!"
    
    text = """... But you did. Now the battery is dead. You hear some noise downstairs. Did you lock the door? Really?"""

    choices = [
        ('announce',"Announce that you're coming down! And you have a black belt."),
        ('alarm',"Imitate an Alarm. You have no alarm system. But they might not know it. You imitate it.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/use_phone/announce")
def announce():
    title = "The power comes back. Just in time!"

    text = "Happy end"
    choices = []

    
    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/use_phone/alarm")
def alarm():
    title = "Power goes back. But the noise is still there..."

    text = "You go downstairs to check. And you can't believe what you see. It's a freakin'... "
    choices = [
        ('fly', "Fly"),
        ('dragon', "Dragon"),
        ('dog', "Dog")
    ]

    
    return render_template('adventure.html', title=title, text=text, choices=choices)
@app.route("/use_phone/alarm/fly")
def fly():
    title = "A fly? "

    text = "So you grab the fly killing thing and finished it off. Too much fuzz over nothing."
    choices = []

    
    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/use_phone/alarm/dragon")
def dragon():
    title = "A dragon? "

    text = "For real? Yeah, no way. Just wake up already. I'm getting tired of this."
    choices = []

    
    return render_template('adventure.html', title=title, text=text, choices=choices)


@app.route("/use_phone/alarm/dog")
def dog():
    title = "A dog? "

    text = "Well, daahh. You have one, remember? Does the name Lucky ring any bells? Gosh, what kind of person gets paranoid about their own pet. Take him for a walk. "
    choices = []

    
    return render_template('adventure.html', title=title, text=text, choices=choices)


@app.route("/just_chill")
def just_chill():
    title = "Your wait and see approach is getting boring."
    
    text = """When you're bored, you get hungry. You are now starving. Now what?"""

    choices = [
        ('run', "RUN! To the kitchen to get something to eat. If you die, you don't want to die starved."),
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)
@app.route("/just_chill/run")
def run():
    title = "So you open the fridge..."
    
    text = """And it's all green and healthy. Grassy looking. Too bad you're doing the SummerBody Challenge. Without even noticing, you're apetite is gone. Drink some water."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/candles")
def candles():
    title = "As you're trying to make your way down the steps, you hear some noise downstairs. "
    
    text = """The candles are in the kitchen. Downstairs. Where the noise comes from..."""

    choices = [
        ('sing', "Your voice is scary. To show bravery you decide to sing. You try to remember a song with candles. But all you can remember is Hello from the other side!"),
        ('shut_the_door', "Shut the door and lock yourself in the bathroom. In case there's also a tornado coming.")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)

@app.route("/candles/sing")
def sing():
    title = "So you're singing Adele. But you can't really sing."
    
    text = """The robber's goes nuts. Adele + your voice?!! Too much torture. Not worthed. So he escapes."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)
@app.route("/candles/shut_the_door")
def shut_the_door():
    title = "So you spent the night sleeping on the bathroom floor."
    
    text = """In the morning there's nothing, besides backpain. You should really stop watching horror movies before bedtime."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices)



