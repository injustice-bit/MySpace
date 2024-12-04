from flask import Flask, render_template, send_from_directory, redirect, url_for
import os

app = Flask(__name__)

# Path to store uploaded songs and images
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'mp3', 'wav', 'ogg'}

# Predefined lyrics, explanations, and image filenames for songs
SONG_DETAILS = {
    "Ask For Date.mp3": {
        "explanation": "This song was written to express that how much i am desperate for you and also i wanted to ask you out for our 2nd date, and this song explains that how we will spend our day in my delulupur or vayulok. I hope You like this Song Cutiepie. 👉👈",
        "lyrics": """
I see you walking, like a dream in the light,
You turn my days into stars in the night.
I’ve waited long for the courage to say,
Could I steal your time, even just for a day?

Your smile’s a melody, your laugh’s a tune,
With you, the world feels like June.

Would you let me take your hand tonight?
Beneath the sky where the stars shine bright.
We’ll write our story, just me and you,
A night that’s ours, where dreams come true.

We’ll find a place where the world stands still,
Every moment, a memory to fill.
A little café, or a walk in the park,
Where hearts speak louder under the dark.

I don’t need much, just your company,
To turn this night into destiny.

Would you let me take your hand tonight?
Beneath the sky where the stars shine bright.
We’ll write our story, just me and you,
A night that’s ours, where dreams come true.

No grand promises, no perfect plans,
Just me, the stars, and holding hands.
If you say yes, the world will align,
And this moment will forever be mine.

Would you let me take your hand tonight?
Beneath the sky where the stars shine bright.
We’ll write our story, just me and you,
A night that’s ours, where dreams come true.

So what do you say, will you make my day?
Let’s find a forever, starting this way.
One simple date, a spark, a start,
A night for us, straight from the heart.""",
        "image": "date.jpg"
    },
    "In Your Eyes I See Forever.mp3": {
        "explanation": "So, this song explains, chalo ab thodi hindi me batata hoon kaafi english hogya, So yeah song dedicate krta hai, mai kehta hoon naa i see you as my forever, toh ussi be based yeh song hai and isme meri feelings bhi hai waise toh harr gaane me feelings hi hai meri. hahahahaha, suno isko and batao kaisa laga.",
        "lyrics": """
When I see you, the world fades away,
Your smile’s a sunrise, lighting my day.
Every word you speak, a melody so sweet,
You’re the dream where my heart and heaven meet.

I’ve wandered through the shadows and the rain,
But your love has erased every pain.

In your eyes, I see forever,
A love so true, it won't surrender.
Every heartbeat whispers your name,
In this dance of love, we’ll never be the same.

Your laughter’s a song that soothes my soul,
With you by my side, I feel whole.
You’re the stars that guide my restless skies,
The reason I believe, the reason I try.

With every touch, you set me free,
You’re the only one I'll ever need.

In your eyes, I see forever,
A love so true, it won't surrender.
Every heartbeat whispers your name,
In this dance of love, we’ll never be the same.

Take my hand, let’s walk through time,
In every lifetime, I’ll call you mine.
No matter where this life may go,
I’ll hold you close, I’ll never let go.

In your eyes, I see forever,
A love so true, it won't surrender.
Every heartbeat whispers your name,
In this dance of love, we’ll never be the same.

You’re the reason my heart beats strong,
With you, I’ve found where I belong.
Forever in your eyes, I’ll stay,
Loving you more with every day.""",
        "image": "img2.jpg"
    },
    "Not Perfect, Just Yours.mp3": {
        "explanation": "Ahm Ahm! Toh iss gaane se kavi kehna chahte hai ki, shyd wo perfect nahi hai but wo harr ek koshish krenge harr wo dariyaa ko cross krenge jo unhe apke kareeb lekr aae and kavi bss apke hokr rehna chahte hai. Baki ap feelings gaane ki lyrics me hi pdh lena ❤️`",
        "lyrics": """I see you there, like a dream so bright,
You light up the world with your gentle light.
I wonder if I’m enough, if I can be the man,
To hold your heart, to take your hand.

I’m not perfect, I’ve made mistakes,
But for your love, I’ll do what it takes.
I’ll climb every mountain, I’ll face my fears,
Just to have you near, through the years.

For you, I’ll rise, I’ll fight, I’ll grow,
I’ll be the man you deserve to know.
Your love is my reason, my fire, my guide,
I’ll leave all my flaws and fears behind.
I may not be perfect, but I’m yours to find,
I’ll give you my heart, my soul, my time.

I know I stumble, I fall sometimes,
But I’m learning to love in the sweetest rhyme.
I’d rewrite my story, I’d start brand new,
Just to be the one who’s worthy of you.

I see the stars, but you shine brighter,
You give me hope, you’re my fighter.
If you take my hand, I’ll never let go,
With you by my side, I’ll learn to glow.

For you, I’ll rise, I’ll fight, I’ll grow,
I’ll be the man you deserve to know.
Your love is my reason, my fire, my guide,
I’ll leave all my flaws and fears behind.
I may not be perfect, but I’m yours to find,
I’ll give you my heart, my soul, my time.

I’ll love you deeply, I’ll love you true,
Every change I make is all for you.
Just give me a chance to show you I’m real,
My heart is yours, it’s all I feel.
I may not be perfect, but for you, I’ll try,
To be your everything, until the end of time.""",
        "image": "img3.jpg"
    },
    "oYou and I.mp3": {
        "explanation": "Iss gaane me kavi apne dil ki baat kehna chahte hai ki, agar kavi ne dream wali duniya banai hai toh kavi usme apko or khudko kaise image karte hai iss gaane me wahi prastut kiya gya hai, Gaane kaa naam You and I hai, chaliye ap isko suniye and Enjoy kriye!!!",
        "lyrics": """I see you there, in every dream,
A quiet wish, a steady beam.
Your laughter's light, it warms the air,
A moment with you feels so rare.

But how do I tell you what’s in my heart?
The words are tangled, where do I start?

One day, I’ll hold your hand,
We’ll write our story, take a stand.
With every step, I’ll make you see,
You and I, we’re meant to be.

Your every glance, a spark, a flame,
My soul whispers softly, calling your name.
I’d give the stars, the moon, the sky,
Just to be the one you can’t deny.

So here I stand, with hope so true,
Dreaming of a life, one day with you.

One day, I’ll hold your hand,
We’ll write our story, take a stand.
With every step, I’ll make you see,
You and I, we’re meant to be.

I’ll wait a lifetime, if that’s what it takes,
To show you love that never breaks.
I’ll be your strength, your safest place,
And in your heart, I’ll find my space.

One day, I’ll hold your hand,
We’ll write our story, take a stand.
With every step, I’ll make you see,
You and I, we’re meant to be.

So here’s my heart, take it, it’s yours,
Let’s open love’s unopened doors.
One day, I’ll say it, and hope it’s true,
That day, my love, will be with you.""",
        "image": "img4.jpg"
    },
    "Say Yes.mp3": {
        "explanation": "So, finally last wale song pe aagye ap, I hope apka safar boring nhi rha hoga, agar boring hua ho toh maafi chahunga. Ab iss gaane me jo bhi words hai and jo bhi feelings hai usko likha gya hai and iss gaane ki through mai apko propose krna chahta hoon, i know tareeka thoda weird hai but thoda unique hona chahiye, so i did this. I hope you like ❤️",
        "lyrics": """
We've known each other for so long
Laughed through every right and wrong
You light my world like a song
Tonight I wanna ask
Come along

We've danced through moments
Rain or shine
Shared secrets
Dreams
And all things fine
In each other's corner
Always found time
Now I want more
Let's cross this line

Say yes
Let's make a start
We've always been so close at heart
Say yes
Let's never part
From friends to lovers
A perfect chart

Our friendship's gold
It's tried and true
But I'm falling deeper
It's so new
I've waited long
And now I knew
It's time to share these feelings too

Look at the stars
They seem so bright
A mirror of our friendship's light
Take my hand
Hold it tight
Let’s step into this brand new flight

Say yes
Let's make a start
We've always been so close at heart
Say yes
Let's never part
From friends to lovers
A perfect chart""",
        "image": "img5.jpg"
    }
}

@app.route('/')
def toggle():
    return render_template('toggle.html')

@app.route('/index')
def index():
    # Dynamically list all songs in the upload folder
    songs = [
        song for song in os.listdir(UPLOAD_FOLDER)
        if '.' in song and song.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    ]
    return render_template('index.html', songs=songs, song_details=SONG_DETAILS)

@app.route('/play/<filename>')
def play(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

# Redirect all invalid routes to `/`
@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('toggle'))

if __name__ == '__main__':
    app.run(debug=True)
