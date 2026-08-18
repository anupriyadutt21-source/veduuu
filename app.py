import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(
    page_title="Veduuu ❤️",
    page_icon="❤️",
    layout="centered"
)


# ============================================================
# IMAGE LOADER
# ============================================================

def get_image(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""


wallpaper = get_image("wallpaper.jpg.jpeg")

photos = []

for i in range(1, 9):
    photos.append(
        get_image(f"photos/photo{i}.jpg.jpeg")
    )


photo_js = "["

for photo in photos:
    photo_js += f'"data:image/jpeg;base64,{photo}",'

photo_js += "]"


# ============================================================
# HTML
# ============================================================

html = f"""
<!DOCTYPE html>

<html>

<head>

<meta name="viewport"
content="width=device-width, initial-scale=1">

<style>

/* ============================================================
   GENERAL
============================================================ */

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    background: transparent;
    overflow: hidden;
}}

* {{
    box-sizing: border-box;
}}

body {{
    display: flex;
    justify-content: center;
    align-items: center;

    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Arial,
        sans-serif;
}}


/* ============================================================
   PHONE
============================================================ */

.phone {{
    width: 370px;
    height: 720px;

    max-width: 95vw;
    max-height: 95vh;

    position: relative;
    overflow: hidden;

    border-radius: 42px;

    background-image:
        linear-gradient(
            rgba(0,0,0,.08),
            rgba(0,0,0,.18)
        ),
        url("data:image/jpeg;base64,{wallpaper}");

    background-size: cover;
    background-position: center;

    color: white;

    box-shadow:
        0 0 0 5px #111,
        0 18px 50px rgba(0,0,0,.55);
}}


/* ============================================================
   PAGES
============================================================ */

.page {{
    position: absolute;
    inset: 0;

    padding: 20px;

    overflow-y: auto;

    scrollbar-width: none;
}}

.page::-webkit-scrollbar {{
    display: none;
}}

.hidden {{
    display: none !important;
}}


/* ============================================================
   LOCK SCREEN
============================================================ */

#lock {{
    cursor: pointer;
    text-align: center;
}}

.lock-time {{
    margin-top: 45px;

    font-size: 62px;
    font-weight: 300;

    text-shadow:
        0 3px 12px rgba(0,0,0,.7);
}}

.lock-date {{
    font-size: 15px;

    text-shadow:
        0 2px 8px rgba(0,0,0,.7);
}}

.lock-middle {{
    position: absolute;

    top: 43%;

    left: 0;
    right: 0;
}}

.lock-small {{
    font-size: 13px;
    opacity: .85;
}}

.lock-name {{
    font-size: 30px;
    font-weight: bold;
    margin-top: 6px;
}}

.lock-bottom {{
    position: absolute;

    bottom: 28px;

    left: 0;
    right: 0;

    font-size: 12px;
    opacity: .85;
}}


/* ============================================================
   HOME
============================================================ */

.home-title {{
    margin-top: 25px;

    text-align: center;

    font-size: 27px;
    font-weight: bold;

    text-shadow:
        0 2px 8px rgba(0,0,0,.7);
}}

.home-sub {{
    text-align: center;

    font-size: 11px;

    opacity: .75;
}}

.apps {{
    margin-top: 55px;

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 28px 15px;
}}

.app {{
    text-align: center;
    cursor: pointer;
}}

.app-icon {{
    width: 60px;
    height: 60px;

    margin: auto;

    border-radius: 17px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 28px;

    background:
        rgba(255,255,255,.20);

    backdrop-filter:
        blur(12px);

    box-shadow:
        0 4px 12px rgba(0,0,0,.25);
}}

.app-name {{
    margin-top: 7px;
    font-size: 11px;
}}

.dock {{
    position: absolute;

    bottom: 18px;

    left: 18px;
    right: 18px;

    height: 65px;

    border-radius: 23px;

    background:
        rgba(255,255,255,.18);

    backdrop-filter:
        blur(15px);

    display: flex;

    align-items: center;

    justify-content:
        space-around;

    font-size: 25px;
}}


/* ============================================================
   HEADER
============================================================ */

.header {{
    display: flex;

    align-items: center;

    gap: 10px;

    height: 55px;

    font-size: 21px;
    font-weight: bold;
}}

.back {{
    font-size: 34px;
    cursor: pointer;
}}


/* ============================================================
   MESSAGES
============================================================ */

.message {{
    margin: 10px 0;

    display: flex;
}}

.left {{
    justify-content: flex-start;
}}

.right {{
    justify-content: flex-end;
}}

.bubble {{
    max-width: 265px;

    padding: 10px 14px;

    border-radius: 18px;

    font-size: 13px;

    line-height: 1.45;

    box-shadow:
        0 2px 5px rgba(0,0,0,.16);
}}

.received {{
    background:
        rgba(38,38,38,.95);

    border-bottom-left-radius: 5px;
}}

.sent {{
    background:
        #087cf0;

    border-bottom-right-radius: 5px;
}}

.chat-time {{
    font-size: 8px;

    opacity: .45;

    margin-top: 3px;
}}

.typing {{
    font-size: 10px;

    opacity: .45;

    padding-left: 5px;
}}


/* ============================================================
   GALLERY
============================================================ */

.gallery {{
    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 5px;
}}

.gallery img {{
    width: 100%;

    aspect-ratio: 1;

    object-fit: cover;

    border-radius: 7px;

    cursor: pointer;

    transition:
        transform .2s;
}}

.gallery img:hover {{
    transform: scale(1.03);
}}


/* ============================================================
   PHOTO VIEWER
============================================================ */

.photo-view {{
    position: absolute;

    inset: 0;

    z-index: 50;

    background:
        rgba(0,0,0,.96);

    display: flex;

    align-items: center;

    justify-content: center;
}}

.photo-view img {{
    max-width: 90%;
    max-height: 75%;

    object-fit: contain;

    border-radius: 12px;
}}

.photo-close {{
    position: absolute;

    top: 18px;
    left: 20px;

    font-size: 35px;

    cursor: pointer;
}}


/* ============================================================
   MUSIC
============================================================ */

.music {{
    text-align: center;
}}

.album {{
    width: 210px;
    height: 210px;

    margin: 45px auto 25px;

    border-radius: 25px;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 80px;

    background:
        linear-gradient(
            135deg,
            #7c3aed,
            #ec4899,
            #f97316
        );

    box-shadow:
        0 15px 35px
        rgba(0,0,0,.4);
}}

.song {{
    font-size: 22px;
    font-weight: bold;
}}

.song-sub {{
    margin-top: 5px;

    font-size: 12px;

    opacity: .6;
}}

.play {{
    margin: 28px auto;

    width: 240px;
    height: 55px;

    border-radius: 30px;

    background: white;
    color: black;

    display: flex;

    align-items: center;
    justify-content: center;

    font-weight: bold;

    cursor: pointer;
}}

.youtube {{
    width: 100%;
    margin-top: 15px;
}}

.youtube iframe {{
    width: 100%;
    height: 205px;

    border: none;

    border-radius: 15px;
}}

.note {{
    margin-top: 25px;

    padding: 18px;

    border-radius: 18px;

    background:
        rgba(255,255,255,.10);

    font-size: 13px;

    line-height: 1.7;
}}


/* ============================================================
   MEMORIES
============================================================ */

.timeline {{
    margin-top: 20px;

    padding-left: 15px;

    border-left:
        2px solid
        rgba(255,255,255,.35);
}}

.memory {{
    position: relative;

    margin-bottom: 30px;

    padding-left: 18px;
}}

.memory::before {{
    content: "";

    position: absolute;

    width: 12px;
    height: 12px;

    border-radius: 50%;

    background: white;

    left: -22px;
    top: 5px;

    box-shadow:
        0 0 12px
        rgba(255,255,255,.8);
}}

.memory-date {{
    font-size: 11px;

    opacity: .65;

    text-transform: uppercase;

    letter-spacing: 1px;
}}

.memory-title {{
    font-size: 19px;

    font-weight: bold;

    margin-top: 5px;
}}

.memory-text {{
    font-size: 13px;

    line-height: 1.6;

    opacity: .85;

    margin-top: 7px;
}}

.final-memory {{
    margin-top: 35px;

    padding: 18px;

    border-radius: 20px;

    text-align: center;

    background:
        rgba(255,255,255,.12);

    line-height: 1.7;
}}


/* ============================================================
   NOTES
============================================================ */

.note-paper {{
    margin-top: 10px;

    padding: 22px 18px;

    border-radius: 20px;

    background:
        rgba(255,255,255,.94);

    color: #292929;

    box-shadow:
        0 10px 25px
        rgba(0,0,0,.3);

    font-size: 13px;

    line-height: 1.65;
}}

.note-paper h2 {{
    text-align: center;

    margin-top: 0;
    margin-bottom: 18px;

    font-size: 20px;
}}

.note-paper p {{
    margin: 0 0 14px 0;
}}

.poem {{
    text-align: center;

    font-style: italic;

    margin-top: 20px;

    padding: 15px;

    border-top:
        1px solid
        rgba(0,0,0,.15);
}}

.signature {{
    text-align: right;

    font-weight: bold;

    margin-top: 20px;
}}


/* ============================================================
   PRIVATE
============================================================ */

.passcode {{
    margin-top: 100px;

    text-align: center;
}}

.passcode input {{
    width: 100%;

    padding: 13px;

    border-radius: 25px;

    border:
        1px solid
        rgba(255,255,255,.3);

    background:
        rgba(0,0,0,.4);

    color: white;

    outline: none;

    margin-top: 20px;
}}

.unlock-button {{
    margin-top: 12px;

    padding: 12px 25px;

    border-radius: 25px;

    border: none;

    background: white;

    color: black;

    cursor: pointer;
}}

.secret-message {{
    margin-top: 20px;

    padding: 18px;

    border-radius: 18px;

    background:
        rgba(255,255,255,.10);

    line-height: 1.7;
}}

</style>

</head>


<body>


<div class="phone">


<!-- ============================================================
LOCK SCREEN
============================================================ -->

<div
    id="lock"
    class="page"
    onclick="unlock()"
>

    <div
        id="clock"
        class="lock-time"
    >
        --:--
    </div>

    <div
        id="date"
        class="lock-date"
    >
        Loading...
    </div>

    <div class="lock-middle">

        <div class="lock-small">
            This device belongs to
        </div>

        <div class="lock-name">
            Veduuu 🫠
        </div>

    </div>

    <div class="lock-bottom">

        🔒<br>

        Tap anywhere to unlock

    </div>

</div>


<!-- ============================================================
HOME
============================================================ -->

<div
    id="home"
    class="page hidden"
>

    <div class="home-title">
        Veduuu 📱
    </div>

    <div class="home-sub">
        Private Device
    </div>


    <div class="apps">


        <div
            class="app"
            onclick="openPage('messages')"
        >

            <div class="app-icon">
                💬
            </div>

            <div class="app-name">
                Messages
            </div>

        </div>


        <div
            class="app"
            onclick="openPage('gallery')"
        >

            <div class="app-icon">
                📸
            </div>

            <div class="app-name">
                Gallery
            </div>

        </div>


        <div
            class="app"
            onclick="openPage('music')"
        >

            <div class="app-icon">
                🎵
            </div>

            <div class="app-name">
                Music
            </div>

        </div>


        <div
            class="app"
            onclick="openPage('memories')"
        >

            <div class="app-icon">
                🗓️
            </div>

            <div class="app-name">
                Memories
            </div>

        </div>


        <div
            class="app"
            onclick="openPage('notes')"
        >

            <div class="app-icon">
                📝
            </div>

            <div class="app-name">
                Notes
            </div>

        </div>


        <div
            class="app"
            onclick="openPage('private')"
        >

            <div class="app-icon">
                🔐
            </div>

            <div class="app-name">
                Private
            </div>

        </div>

    </div>


    <div class="dock">

        📞
        💬
        🌐
        📷

    </div>

</div>


<!-- ============================================================
MESSAGES
============================================================ -->

<div
    id="messages"
    class="page hidden"
    style="padding:0;"
>


    <div style="
        height:72px;
        padding:10px 15px;

        display:flex;
        align-items:center;
        gap:10px;

        background:
            rgba(20,20,20,.82);

        border-bottom:
            1px solid
            rgba(255,255,255,.12);

        backdrop-filter:
            blur(15px);
    ">

        <span
            onclick="goHome()"
            style="
                font-size:34px;
                cursor:pointer;
                margin-right:2px;
            "
        >
            ‹
        </span>


        <div style="
            width:43px;
            height:43px;

            border-radius:50%;

            background:
                linear-gradient(
                    135deg,
                    #ff9a9e,
                    #fad0c4
                );

            display:flex;

            align-items:center;
            justify-content:center;

            font-size:22px;
        ">
            ❤️
        </div>


        <div style="line-height:1.25;">

            <div style="
                font-size:16px;
                font-weight:600;
            ">
                Anupriya ❤️
            </div>

            <div style="
                font-size:10px;
                color:#75e28a;
            ">
                ● online
            </div>

        </div>

    </div>


    <div style="
        padding:15px 14px 30px;
    ">


        <div style="
            text-align:center;
            font-size:9px;
            opacity:.5;
            margin:4px 0 18px;
        ">
            TODAY
        </div>


        <div class="message left">
            <div>

                <div class="bubble received">
                    Buba 😭
                </div>

                <div class="chat-time">
                    10:42 PM
                </div>

            </div>
        </div>


        <div class="message left">
            <div>

                <div class="bubble received">

                    I know you're snooping
                    around my phone 👀

                </div>

                <div class="chat-time">
                    10:42 PM
                </div>

            </div>
        </div>


        <div class="message right">
            <div>

                <div class="bubble sent">
                    Kya kar rahe ho 😭
                </div>

                <div class="chat-time">
                    10:43 PM ✓✓
                </div>

            </div>
        </div>


        <div class="message left">
            <div>

                <div class="bubble received">
                    Fad fad nko kru 😂
                </div>

                <div class="chat-time">
                    10:43 PM
                </div>

            </div>
        </div>


        <div class="message right">
            <div>

                <div class="bubble sent">
                    😭😭
                </div>

                <div class="chat-time">
                    10:44 PM ✓✓
                </div>

            </div>
        </div>


        <div class="message left">
            <div>

                <div class="bubble received">
                    Okay wait...
                </div>

                <div class="chat-time">
                    10:44 PM
                </div>

            </div>
        </div>


        <div class="message left">
            <div>

                <div class="bubble received">

                    Do you remember
                    our first kiss? 👀

                </div>

                <div class="chat-time">
                    10:45 PM
                </div>

            </div>
        </div>


        <div class="message right">
            <div>

                <div class="bubble sent">
                    How could I forget? 🥹
                </div>

                <div class="chat-time">
                    10:45 PM ✓✓
                </div>

            </div>
        </div>


        <div class="message left">
            <div>

                <div class="bubble received">
                    Then you remember
                    12/10 too...
                </div>

                <div class="chat-time">
                    10:46 PM
                </div>

            </div>
        </div>


        <div class="message left">
            <div>

                <div class="bubble received">

                    That's the day
                    I fell for you. ❤️

                </div>

                <div class="chat-time">
                    10:46 PM
                </div>

            </div>
        </div>


        <div class="message right">
            <div>

                <div class="bubble sent">
                    🥺❤️
                </div>

                <div class="chat-time">
                    10:47 PM ✓✓
                </div>

            </div>
        </div>


        <div class="message left">
            <div>

                <div class="bubble received">

                    And then...

                    <br><br>

                    16/01/2026 💗

                </div>

                <div class="chat-time">
                    10:47 PM
                </div>

            </div>
        </div>


        <div class="message left">
            <div>

                <div class="bubble received">

                    My birthday.

                    <br>

                    Our beginning.

                </div>

                <div class="chat-time">
                    10:48 PM
                </div>

            </div>
        </div>


        <div class="message left">
            <div>

                <div
                    class="bubble received"
                    style="
                        background:
                        linear-gradient(
                            135deg,
                            #5b3a29,
                            #6d4935
                        );
                    "
                >

                    And somehow...

                    <br><br>

                    you're still my
                    favourite person. 🥹❤️

                </div>

                <div class="chat-time">
                    10:49 PM
                </div>

            </div>
        </div>


        <div class="typing">
            Anupriya is typing...
        </div>


        <div
            class="message left"
            style="margin-top:18px;"
        >

            <div>

                <div
                    class="bubble received"
                    style="
                        background:
                        rgba(255,255,255,.13);

                        border:
                        1px solid
                        rgba(255,255,255,.1);
                    "
                >

                    Don't reply here. 👀

                    <br><br>

                    There's more waiting
                    for you.

                    <br><br>

                    Check <b>Memories</b>. 🗓️

                </div>

            </div>

        </div>


    </div>

</div>


<!-- ============================================================
GALLERY
============================================================ -->

<div
    id="gallery"
    class="page hidden"
>

    <div class="header">

        <span
            class="back"
            onclick="goHome()"
        >
            ‹
        </span>

        📸 Gallery

    </div>


    <div class="gallery">
"""

for i in range(8):

    html += f"""
        <img
            src="data:image/jpeg;base64,{photos[i]}"
            onclick="showPhoto({i})"
        >
    """

html += f"""

    </div>

</div>


<!-- ============================================================
PHOTO VIEWER
============================================================ -->

<div
    id="photoView"
    class="photo-view hidden"
>

    <div
        class="photo-close"
        onclick="closePhoto()"
    >
        ‹
    </div>

    <img
        id="bigPhoto"
        src=""
    >

</div>


<!-- ============================================================
MUSIC
============================================================ -->

<div
    id="music"
    class="page hidden"
>

    <div class="header">

        <span
            class="back"
            onclick="goHome()"
        >
            ‹
        </span>

        🎵 Music

    </div>


    <div class="music">

        <div class="album">
            🎧
        </div>

        <div class="song">
            Our Song ❤️
        </div>

        <div class="song-sub">
            Just for my Veduuu
        </div>


        <div
            class="play"
            onclick="playSong()"
        >
            ▶ &nbsp; PLAY OUR SONG
        </div>


        <div
            id="youtube"
            class="youtube hidden"
        >

            <iframe
                id="youtubeFrame"
                src=""
                allow="autoplay; encrypted-media"
                allowfullscreen>
            </iframe>

        </div>


        <div class="note">

            Put your headphones on... 🎧

            <br><br>

            I could've just sent you a song...

            <br><br>

            But obviously I had to make
            an entire secret phone instead. 😭❤️

        </div>

    </div>

</div>


<!-- ============================================================
MEMORIES
============================================================ -->

<div
    id="memories"
    class="page hidden"
>

    <div class="header">

        <span
            class="back"
            onclick="goHome()"
        >
            ‹
        </span>

        🗓️ Our Timeline

    </div>


    <div class="timeline">


        <div class="memory">

            <div class="memory-date">
                12 October
            </div>

            <div class="memory-title">
                The day everything changed. ❤️
            </div>

            <div class="memory-text">

                Somewhere between all the little
                conversations and moments...

                <br>

                I fell for you.

            </div>

        </div>


        <div class="memory">

            <div class="memory-date">
                16 January 2026
            </div>

            <div class="memory-title">
                Our beginning. 💗
            </div>

            <div class="memory-text">

                My birthday became even more special
                because it became the day
                our story officially began.

            </div>

        </div>


        <div class="memory">

            <div class="memory-date">
                Every day after
            </div>

            <div class="memory-title">
                Us. 🥹
            </div>

            <div class="memory-text">

                The random conversations.
                The stupid jokes.
                The little fights.
                The laughter.
                The memories.

                <br><br>

                All those tiny moments that somehow
                became our story.

            </div>

        </div>


        <div class="memory">

            <div class="memory-date">
                Right now
            </div>

            <div class="memory-title">
                You're still here. ❤️
            </div>

            <div class="memory-text">

                And honestly...

                <br>

                that's one of my favourite parts.

            </div>

        </div>


    </div>


    <div class="final-memory">

        <b>Next memory?</b>

        <br><br>

        We haven't made it yet. 👀

        <br>

        So let's make it good. ❤️

    </div>

</div>


<!-- ============================================================
NOTES
============================================================ -->

<div
    id="notes"
    class="page hidden"
>

    <div class="header">

        <span
            class="back"
            onclick="goHome()"
        >
            ‹
        </span>

        📝 A Note For You

    </div>


    <div class="note-paper">

        <h2>
            To my Veduuu, ❤️
        </h2>


        <p>
        I don't think I'll ever be able to put into
        words exactly how much you mean to me,
        but I still want to try.
        </p>


        <p>
        You came into my life and somehow became
        such a beautiful part of it. You became the
        person I want to tell everything to — the good
        things, the stupid little things, the things
        that make me laugh, and even the things that
        hurt. Somewhere along the way, you became
        more than just my boyfriend. You became my
        comfort, my favourite person, my safe place,
        and one of the biggest reasons behind so many
        of my smiles.
        </p>


        <p>
        I know I'm not perfect. I overthink, I get
        emotional, I can be stubborn, and sometimes
        I probably make things harder than they need
        to be. But behind all of that is a girl who
        loves you with her whole heart. A girl who
        genuinely cares about you, your happiness,
        your dreams, and your future.
        </p>


        <p>
        Thank you for staying through my moods, my
        silly moments, my endless thoughts, and all
        the times I probably made you say,
        <i>"What is wrong with this girl?"</i> 😭❤️
        Thank you for every laugh, every conversation,
        every little memory, and every moment that
        made me feel loved.
        </p>


        <p>
        I don't need some perfect fairytale with you.
        I just want something real. I want us to keep
        growing, learning, laughing, annoying each
        other, forgiving each other, and choosing each
        other even on the difficult days.
        </p>


        <p>
        If I could give you one thing, it would be the
        ability to see yourself through my eyes because
        then you'd understand just how special you are
        to me.
        </p>


        <p>
        You are a chapter of my life that I never want
        to forget, a memory I want to keep making, and
        a person whose happiness will always matter
        to me.
        </p>


        <p>
        And if love is about choosing someone again
        and again, then I hope that no matter how many
        chapters life gives us, we keep finding our way
        back to each other.
        </p>


        <p>
        <b>
        I love you, Veduuu. More than these words can
        ever explain. ❤️
        </b>
        </p>


        <div class="poem">

            “Some people enter your life like a moment,

            <br>

            but you entered mine and became a feeling

            <br>

            a feeling I want to carry with me,

            <br>

            through every season, every distance,

            <br>

            and every tomorrow.”

        </div>


        <div class="signature">

            Always yours,

            <br>

            Your girl ❤️

        </div>

    </div>

</div>


<!-- ============================================================
PRIVATE
============================================================ -->

<div
    id="private"
    class="page hidden"
>

    <div class="header">

        <span
            class="back"
            onclick="goHome()"
        >
            ‹
        </span>

        🔐 Private

    </div>


    <div class="passcode">

        <div style="font-size:65px;">
            🔐
        </div>

        <br>

        <b>SECRET FILE</b>

        <br><br>

        Enter the passcode.


        <input
            id="password"
            type="password"
            placeholder="Passcode"
        >


        <br>


        <button
            class="unlock-button"
            onclick="checkPassword()"
        >

            Unlock ❤️

        </button>


        <div
            id="secret"
            class="secret-message hidden"
        >

            🥹 You found it.

            <br><br>

            jasta fadfad nko kru veduu 😛

            <br><br>

            ❤️

            <br><br>

            You really had to find
            the secret, didn't you? 😭

        </div>

    </div>

</div>


</div>


<script>

/* ============================================================
NAVIGATION
============================================================ */

function hideAll() {{

    const pages = [
        "lock",
        "home",
        "messages",
        "gallery",
        "music",
        "memories",
        "notes",
        "private"
    ];

    pages.forEach(function(id) {{

        document
            .getElementById(id)
            .classList
            .add("hidden");

    }});

}}


function openPage(id) {{

    hideAll();

    document
        .getElementById(id)
        .classList
        .remove("hidden");

}}


function goHome() {{

    openPage("home");

}}


function unlock() {{

    openPage("home");

}}


/* ============================================================
CLOCK - INDIA
============================================================ */

function updateClock() {{

    const now = new Date();


    const time =
        now.toLocaleTimeString(
            "en-IN",
            {{
                timeZone: "Asia/Kolkata",
                hour: "2-digit",
                minute: "2-digit",
                hour12: true
            }}
        );


    const date =
        now.toLocaleDateString(
            "en-IN",
            {{
                timeZone: "Asia/Kolkata",
                weekday: "long",
                month: "long",
                day: "numeric"
            }}
        );


    document
        .getElementById("clock")
        .textContent = time;


    document
        .getElementById("date")
        .textContent = date;

}}


updateClock();

setInterval(
    updateClock,
    1000
);


/* ============================================================
PHOTOS
============================================================ */

const photos = {photo_js};


function showPhoto(index) {{

    document
        .getElementById("bigPhoto")
        .src = photos[index];


    document
        .getElementById("photoView")
        .classList
        .remove("hidden");

}}


function closePhoto() {{

    document
        .getElementById("photoView")
        .classList
        .add("hidden");

}}


/* ============================================================
MUSIC
============================================================ */

function playSong() {{

    const box =
        document.getElementById("youtube");


    const frame =
        document.getElementById("youtubeFrame");


    frame.src =
        "https://www.youtube.com/embed/dSc6ci7TLKE?autoplay=1&rel=0";


    box.classList
        .remove("hidden");

}}


/* ============================================================
SECRET PASSWORD
============================================================ */

function checkPassword() {{

    const input =
        document
            .getElementById("password")
            .value
            .trim();


    const correct = "1612";


    if (input === correct) {{

        document
            .getElementById("secret")
            .classList
            .remove("hidden");

    }}

    else {{

        alert(
            "Wrong passcode 😭"
        );

    }}

}}

</script>

</body>

</html>
"""


# ============================================================
# DISPLAY APP
# ============================================================

components.html(
    html,
    height=750,
    scrolling=False
)